# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_cms20190101 import models as main_models
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
        if not DaraCore.is_null(endpoint):
            return endpoint
        if not DaraCore.is_null(endpoint_map) and not DaraCore.is_null(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return Utils.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_tags_with_options(
        self,
        request: main_models.AddTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTags',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_tags_with_options_async(
        self,
        request: main_models.AddTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddTags',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_tags(
        self,
        request: main_models.AddTagsRequest,
    ) -> main_models.AddTagsResponse:
        runtime = RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    async def add_tags_async(
        self,
        request: main_models.AddTagsRequest,
    ) -> main_models.AddTagsResponse:
        runtime = RuntimeOptions()
        return await self.add_tags_with_options_async(request, runtime)

    def apply_metric_rule_template_with_options(
        self,
        request: main_models.ApplyMetricRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyMetricRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.append_mode):
            query['AppendMode'] = request.append_mode
        if not DaraCore.is_null(request.apply_mode):
            query['ApplyMode'] = request.apply_mode
        if not DaraCore.is_null(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not DaraCore.is_null(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.notify_level):
            query['NotifyLevel'] = request.notify_level
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyMetricRuleTemplate',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def apply_metric_rule_template_with_options_async(
        self,
        request: main_models.ApplyMetricRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApplyMetricRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.append_mode):
            query['AppendMode'] = request.append_mode
        if not DaraCore.is_null(request.apply_mode):
            query['ApplyMode'] = request.apply_mode
        if not DaraCore.is_null(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not DaraCore.is_null(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.notify_level):
            query['NotifyLevel'] = request.notify_level
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.template_ids):
            query['TemplateIds'] = request.template_ids
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApplyMetricRuleTemplate',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApplyMetricRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def apply_metric_rule_template(
        self,
        request: main_models.ApplyMetricRuleTemplateRequest,
    ) -> main_models.ApplyMetricRuleTemplateResponse:
        runtime = RuntimeOptions()
        return self.apply_metric_rule_template_with_options(request, runtime)

    async def apply_metric_rule_template_async(
        self,
        request: main_models.ApplyMetricRuleTemplateRequest,
    ) -> main_models.ApplyMetricRuleTemplateResponse:
        runtime = RuntimeOptions()
        return await self.apply_metric_rule_template_with_options_async(request, runtime)

    def batch_create_instant_site_monitor_with_options(
        self,
        request: main_models.BatchCreateInstantSiteMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateInstantSiteMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_list):
            query['TaskList'] = request.task_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateInstantSiteMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateInstantSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_create_instant_site_monitor_with_options_async(
        self,
        request: main_models.BatchCreateInstantSiteMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchCreateInstantSiteMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_list):
            query['TaskList'] = request.task_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchCreateInstantSiteMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchCreateInstantSiteMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_create_instant_site_monitor(
        self,
        request: main_models.BatchCreateInstantSiteMonitorRequest,
    ) -> main_models.BatchCreateInstantSiteMonitorResponse:
        runtime = RuntimeOptions()
        return self.batch_create_instant_site_monitor_with_options(request, runtime)

    async def batch_create_instant_site_monitor_async(
        self,
        request: main_models.BatchCreateInstantSiteMonitorRequest,
    ) -> main_models.BatchCreateInstantSiteMonitorResponse:
        runtime = RuntimeOptions()
        return await self.batch_create_instant_site_monitor_with_options_async(request, runtime)

    def batch_export_with_options(
        self,
        tmp_req: main_models.BatchExportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchExportResponse:
        tmp_req.validate()
        request = main_models.BatchExportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.measurements):
            request.measurements_shrink = Utils.array_to_string_with_specified_style(tmp_req.measurements, 'Measurements', 'json')
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['Cursor'] = request.cursor
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.measurements_shrink):
            body['Measurements'] = request.measurements_shrink
        if not DaraCore.is_null(request.metric):
            body['Metric'] = request.metric
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchExport',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchExportResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_export_with_options_async(
        self,
        tmp_req: main_models.BatchExportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchExportResponse:
        tmp_req.validate()
        request = main_models.BatchExportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.measurements):
            request.measurements_shrink = Utils.array_to_string_with_specified_style(tmp_req.measurements, 'Measurements', 'json')
        body = {}
        if not DaraCore.is_null(request.cursor):
            body['Cursor'] = request.cursor
        if not DaraCore.is_null(request.length):
            body['Length'] = request.length
        if not DaraCore.is_null(request.measurements_shrink):
            body['Measurements'] = request.measurements_shrink
        if not DaraCore.is_null(request.metric):
            body['Metric'] = request.metric
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchExport',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchExportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_export(
        self,
        request: main_models.BatchExportRequest,
    ) -> main_models.BatchExportResponse:
        runtime = RuntimeOptions()
        return self.batch_export_with_options(request, runtime)

    async def batch_export_async(
        self,
        request: main_models.BatchExportRequest,
    ) -> main_models.BatchExportResponse:
        runtime = RuntimeOptions()
        return await self.batch_export_with_options_async(request, runtime)

    def create_dynamic_tag_group_with_options(
        self,
        request: main_models.CreateDynamicTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDynamicTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not DaraCore.is_null(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not DaraCore.is_null(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not DaraCore.is_null(request.match_express):
            query['MatchExpress'] = request.match_express
        if not DaraCore.is_null(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not DaraCore.is_null(request.template_id_list):
            query['TemplateIdList'] = request.template_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDynamicTagGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDynamicTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_dynamic_tag_group_with_options_async(
        self,
        request: main_models.CreateDynamicTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDynamicTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not DaraCore.is_null(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not DaraCore.is_null(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not DaraCore.is_null(request.match_express):
            query['MatchExpress'] = request.match_express
        if not DaraCore.is_null(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not DaraCore.is_null(request.template_id_list):
            query['TemplateIdList'] = request.template_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDynamicTagGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDynamicTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_dynamic_tag_group(
        self,
        request: main_models.CreateDynamicTagGroupRequest,
    ) -> main_models.CreateDynamicTagGroupResponse:
        runtime = RuntimeOptions()
        return self.create_dynamic_tag_group_with_options(request, runtime)

    async def create_dynamic_tag_group_async(
        self,
        request: main_models.CreateDynamicTagGroupRequest,
    ) -> main_models.CreateDynamicTagGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_dynamic_tag_group_with_options_async(request, runtime)

    def create_group_metric_rules_with_options(
        self,
        request: main_models.CreateGroupMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_metric_rules):
            query['GroupMetricRules'] = request.group_metric_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroupMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_metric_rules_with_options_async(
        self,
        request: main_models.CreateGroupMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_metric_rules):
            query['GroupMetricRules'] = request.group_metric_rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroupMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_metric_rules(
        self,
        request: main_models.CreateGroupMetricRulesRequest,
    ) -> main_models.CreateGroupMetricRulesResponse:
        runtime = RuntimeOptions()
        return self.create_group_metric_rules_with_options(request, runtime)

    async def create_group_metric_rules_async(
        self,
        request: main_models.CreateGroupMetricRulesRequest,
    ) -> main_models.CreateGroupMetricRulesResponse:
        runtime = RuntimeOptions()
        return await self.create_group_metric_rules_with_options_async(request, runtime)

    def create_group_monitoring_agent_process_with_options(
        self,
        request: main_models.CreateGroupMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.match_express):
            query['MatchExpress'] = request.match_express
        if not DaraCore.is_null(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroupMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_group_monitoring_agent_process_with_options_async(
        self,
        request: main_models.CreateGroupMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateGroupMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.match_express):
            query['MatchExpress'] = request.match_express
        if not DaraCore.is_null(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateGroupMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGroupMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_group_monitoring_agent_process(
        self,
        request: main_models.CreateGroupMonitoringAgentProcessRequest,
    ) -> main_models.CreateGroupMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return self.create_group_monitoring_agent_process_with_options(request, runtime)

    async def create_group_monitoring_agent_process_async(
        self,
        request: main_models.CreateGroupMonitoringAgentProcessRequest,
    ) -> main_models.CreateGroupMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return await self.create_group_monitoring_agent_process_with_options_async(request, runtime)

    def create_host_availability_with_options(
        self,
        request: main_models.CreateHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not DaraCore.is_null(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_host_availability_with_options_async(
        self,
        request: main_models.CreateHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not DaraCore.is_null(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_host_availability(
        self,
        request: main_models.CreateHostAvailabilityRequest,
    ) -> main_models.CreateHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return self.create_host_availability_with_options(request, runtime)

    async def create_host_availability_async(
        self,
        request: main_models.CreateHostAvailabilityRequest,
    ) -> main_models.CreateHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return await self.create_host_availability_with_options_async(request, runtime)

    def create_hybrid_monitor_namespace_with_options(
        self,
        request: main_models.CreateHybridMonitorNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridMonitorNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_region):
            query['NamespaceRegion'] = request.namespace_region
        if not DaraCore.is_null(request.namespace_type):
            query['NamespaceType'] = request.namespace_type
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridMonitorNamespace',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridMonitorNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_monitor_namespace_with_options_async(
        self,
        request: main_models.CreateHybridMonitorNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridMonitorNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.namespace_region):
            query['NamespaceRegion'] = request.namespace_region
        if not DaraCore.is_null(request.namespace_type):
            query['NamespaceType'] = request.namespace_type
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridMonitorNamespace',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridMonitorNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_monitor_namespace(
        self,
        request: main_models.CreateHybridMonitorNamespaceRequest,
    ) -> main_models.CreateHybridMonitorNamespaceResponse:
        runtime = RuntimeOptions()
        return self.create_hybrid_monitor_namespace_with_options(request, runtime)

    async def create_hybrid_monitor_namespace_async(
        self,
        request: main_models.CreateHybridMonitorNamespaceRequest,
    ) -> main_models.CreateHybridMonitorNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.create_hybrid_monitor_namespace_with_options_async(request, runtime)

    def create_hybrid_monitor_slsgroup_with_options(
        self,
        request: main_models.CreateHybridMonitorSLSGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridMonitorSLSGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not DaraCore.is_null(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not DaraCore.is_null(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridMonitorSLSGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_monitor_slsgroup_with_options_async(
        self,
        request: main_models.CreateHybridMonitorSLSGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridMonitorSLSGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not DaraCore.is_null(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not DaraCore.is_null(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridMonitorSLSGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridMonitorSLSGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_monitor_slsgroup(
        self,
        request: main_models.CreateHybridMonitorSLSGroupRequest,
    ) -> main_models.CreateHybridMonitorSLSGroupResponse:
        runtime = RuntimeOptions()
        return self.create_hybrid_monitor_slsgroup_with_options(request, runtime)

    async def create_hybrid_monitor_slsgroup_async(
        self,
        request: main_models.CreateHybridMonitorSLSGroupRequest,
    ) -> main_models.CreateHybridMonitorSLSGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_hybrid_monitor_slsgroup_with_options_async(request, runtime)

    def create_hybrid_monitor_task_with_options(
        self,
        request: main_models.CreateHybridMonitorTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridMonitorTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not DaraCore.is_null(request.cloud_access_id):
            query['CloudAccessId'] = request.cloud_access_id
        if not DaraCore.is_null(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not DaraCore.is_null(request.collect_target_type):
            query['CollectTargetType'] = request.collect_target_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not DaraCore.is_null(request.target_user_id_list):
            query['TargetUserIdList'] = request.target_user_id_list
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.yarmconfig):
            query['YARMConfig'] = request.yarmconfig
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridMonitorTask',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_hybrid_monitor_task_with_options_async(
        self,
        request: main_models.CreateHybridMonitorTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateHybridMonitorTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not DaraCore.is_null(request.cloud_access_id):
            query['CloudAccessId'] = request.cloud_access_id
        if not DaraCore.is_null(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not DaraCore.is_null(request.collect_target_type):
            query['CollectTargetType'] = request.collect_target_type
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not DaraCore.is_null(request.target_user_id_list):
            query['TargetUserIdList'] = request.target_user_id_list
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.yarmconfig):
            query['YARMConfig'] = request.yarmconfig
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateHybridMonitorTask',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateHybridMonitorTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_hybrid_monitor_task(
        self,
        request: main_models.CreateHybridMonitorTaskRequest,
    ) -> main_models.CreateHybridMonitorTaskResponse:
        runtime = RuntimeOptions()
        return self.create_hybrid_monitor_task_with_options(request, runtime)

    async def create_hybrid_monitor_task_async(
        self,
        request: main_models.CreateHybridMonitorTaskRequest,
    ) -> main_models.CreateHybridMonitorTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_hybrid_monitor_task_with_options_async(request, runtime)

    def create_instant_site_monitor_with_options(
        self,
        request: main_models.CreateInstantSiteMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstantSiteMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.agent_group):
            query['AgentGroup'] = request.agent_group
        if not DaraCore.is_null(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.random_isp_city):
            query['RandomIspCity'] = request.random_isp_city
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstantSiteMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstantSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_instant_site_monitor_with_options_async(
        self,
        request: main_models.CreateInstantSiteMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateInstantSiteMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.agent_group):
            query['AgentGroup'] = request.agent_group
        if not DaraCore.is_null(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.random_isp_city):
            query['RandomIspCity'] = request.random_isp_city
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateInstantSiteMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateInstantSiteMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_instant_site_monitor(
        self,
        request: main_models.CreateInstantSiteMonitorRequest,
    ) -> main_models.CreateInstantSiteMonitorResponse:
        runtime = RuntimeOptions()
        return self.create_instant_site_monitor_with_options(request, runtime)

    async def create_instant_site_monitor_async(
        self,
        request: main_models.CreateInstantSiteMonitorRequest,
    ) -> main_models.CreateInstantSiteMonitorResponse:
        runtime = RuntimeOptions()
        return await self.create_instant_site_monitor_with_options_async(request, runtime)

    def create_metric_rule_black_list_with_options(
        self,
        request: main_models.CreateMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not DaraCore.is_null(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_metric_rule_black_list_with_options_async(
        self,
        request: main_models.CreateMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not DaraCore.is_null(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_metric_rule_black_list(
        self,
        request: main_models.CreateMetricRuleBlackListRequest,
    ) -> main_models.CreateMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return self.create_metric_rule_black_list_with_options(request, runtime)

    async def create_metric_rule_black_list_async(
        self,
        request: main_models.CreateMetricRuleBlackListRequest,
    ) -> main_models.CreateMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return await self.create_metric_rule_black_list_with_options_async(request, runtime)

    def create_metric_rule_resources_with_options(
        self,
        request: main_models.CreateMetricRuleResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetricRuleResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetricRuleResources',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMetricRuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_metric_rule_resources_with_options_async(
        self,
        request: main_models.CreateMetricRuleResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetricRuleResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.overwrite):
            query['Overwrite'] = request.overwrite
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetricRuleResources',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMetricRuleResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_metric_rule_resources(
        self,
        request: main_models.CreateMetricRuleResourcesRequest,
    ) -> main_models.CreateMetricRuleResourcesResponse:
        runtime = RuntimeOptions()
        return self.create_metric_rule_resources_with_options(request, runtime)

    async def create_metric_rule_resources_async(
        self,
        request: main_models.CreateMetricRuleResourcesRequest,
    ) -> main_models.CreateMetricRuleResourcesResponse:
        runtime = RuntimeOptions()
        return await self.create_metric_rule_resources_with_options_async(request, runtime)

    def create_metric_rule_template_with_options(
        self,
        request: main_models.CreateMetricRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetricRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetricRuleTemplate',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_metric_rule_template_with_options_async(
        self,
        request: main_models.CreateMetricRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMetricRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMetricRuleTemplate',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMetricRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_metric_rule_template(
        self,
        request: main_models.CreateMetricRuleTemplateRequest,
    ) -> main_models.CreateMetricRuleTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_metric_rule_template_with_options(request, runtime)

    async def create_metric_rule_template_async(
        self,
        request: main_models.CreateMetricRuleTemplateRequest,
    ) -> main_models.CreateMetricRuleTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_metric_rule_template_with_options_async(request, runtime)

    def create_monitor_agent_process_with_options(
        self,
        request: main_models.CreateMonitorAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        if not DaraCore.is_null(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_agent_process_with_options_async(
        self,
        request: main_models.CreateMonitorAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        if not DaraCore.is_null(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_agent_process(
        self,
        request: main_models.CreateMonitorAgentProcessRequest,
    ) -> main_models.CreateMonitorAgentProcessResponse:
        runtime = RuntimeOptions()
        return self.create_monitor_agent_process_with_options(request, runtime)

    async def create_monitor_agent_process_async(
        self,
        request: main_models.CreateMonitorAgentProcessRequest,
    ) -> main_models.CreateMonitorAgentProcessResponse:
        runtime = RuntimeOptions()
        return await self.create_monitor_agent_process_with_options_async(request, runtime)

    def create_monitor_group_with_options(
        self,
        request: main_models.CreateMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_with_options_async(
        self,
        request: main_models.CreateMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group(
        self,
        request: main_models.CreateMonitorGroupRequest,
    ) -> main_models.CreateMonitorGroupResponse:
        runtime = RuntimeOptions()
        return self.create_monitor_group_with_options(request, runtime)

    async def create_monitor_group_async(
        self,
        request: main_models.CreateMonitorGroupRequest,
    ) -> main_models.CreateMonitorGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_monitor_group_with_options_async(request, runtime)

    def create_monitor_group_by_resource_group_id_with_options(
        self,
        request: main_models.CreateMonitorGroupByResourceGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupByResourceGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not DaraCore.is_null(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not DaraCore.is_null(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroupByResourceGroupId',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupByResourceGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_by_resource_group_id_with_options_async(
        self,
        request: main_models.CreateMonitorGroupByResourceGroupIdRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupByResourceGroupIdResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_list):
            query['ContactGroupList'] = request.contact_group_list
        if not DaraCore.is_null(request.enable_install_agent):
            query['EnableInstallAgent'] = request.enable_install_agent
        if not DaraCore.is_null(request.enable_subscribe_event):
            query['EnableSubscribeEvent'] = request.enable_subscribe_event
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resource_group_name):
            query['ResourceGroupName'] = request.resource_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroupByResourceGroupId',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupByResourceGroupIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group_by_resource_group_id(
        self,
        request: main_models.CreateMonitorGroupByResourceGroupIdRequest,
    ) -> main_models.CreateMonitorGroupByResourceGroupIdResponse:
        runtime = RuntimeOptions()
        return self.create_monitor_group_by_resource_group_id_with_options(request, runtime)

    async def create_monitor_group_by_resource_group_id_async(
        self,
        request: main_models.CreateMonitorGroupByResourceGroupIdRequest,
    ) -> main_models.CreateMonitorGroupByResourceGroupIdResponse:
        runtime = RuntimeOptions()
        return await self.create_monitor_group_by_resource_group_id_with_options_async(request, runtime)

    def create_monitor_group_instances_with_options(
        self,
        request: main_models.CreateMonitorGroupInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroupInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_instances_with_options_async(
        self,
        request: main_models.CreateMonitorGroupInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroupInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group_instances(
        self,
        request: main_models.CreateMonitorGroupInstancesRequest,
    ) -> main_models.CreateMonitorGroupInstancesResponse:
        runtime = RuntimeOptions()
        return self.create_monitor_group_instances_with_options(request, runtime)

    async def create_monitor_group_instances_async(
        self,
        request: main_models.CreateMonitorGroupInstancesRequest,
    ) -> main_models.CreateMonitorGroupInstancesResponse:
        runtime = RuntimeOptions()
        return await self.create_monitor_group_instances_with_options_async(request, runtime)

    def create_monitor_group_notify_policy_with_options(
        self,
        request: main_models.CreateMonitorGroupNotifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupNotifyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroupNotifyPolicy',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupNotifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_notify_policy_with_options_async(
        self,
        request: main_models.CreateMonitorGroupNotifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupNotifyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroupNotifyPolicy',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupNotifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group_notify_policy(
        self,
        request: main_models.CreateMonitorGroupNotifyPolicyRequest,
    ) -> main_models.CreateMonitorGroupNotifyPolicyResponse:
        runtime = RuntimeOptions()
        return self.create_monitor_group_notify_policy_with_options(request, runtime)

    async def create_monitor_group_notify_policy_async(
        self,
        request: main_models.CreateMonitorGroupNotifyPolicyRequest,
    ) -> main_models.CreateMonitorGroupNotifyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.create_monitor_group_notify_policy_with_options_async(request, runtime)

    def create_monitoring_agent_process_with_options(
        self,
        request: main_models.CreateMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        if not DaraCore.is_null(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitoring_agent_process_with_options_async(
        self,
        request: main_models.CreateMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        if not DaraCore.is_null(request.process_user):
            query['ProcessUser'] = request.process_user
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitoring_agent_process(
        self,
        request: main_models.CreateMonitoringAgentProcessRequest,
    ) -> main_models.CreateMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return self.create_monitoring_agent_process_with_options(request, runtime)

    async def create_monitoring_agent_process_async(
        self,
        request: main_models.CreateMonitoringAgentProcessRequest,
    ) -> main_models.CreateMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return await self.create_monitoring_agent_process_with_options_async(request, runtime)

    def create_site_monitor_with_options(
        self,
        request: main_models.CreateSiteMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSiteMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.agent_group):
            query['AgentGroup'] = request.agent_group
        if not DaraCore.is_null(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not DaraCore.is_null(request.custom_schedule):
            query['CustomSchedule'] = request.custom_schedule
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.vpc_config):
            query['VpcConfig'] = request.vpc_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSiteMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_site_monitor_with_options_async(
        self,
        request: main_models.CreateSiteMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSiteMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.agent_group):
            query['AgentGroup'] = request.agent_group
        if not DaraCore.is_null(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not DaraCore.is_null(request.custom_schedule):
            query['CustomSchedule'] = request.custom_schedule
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.vpc_config):
            query['VpcConfig'] = request.vpc_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSiteMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSiteMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_site_monitor(
        self,
        request: main_models.CreateSiteMonitorRequest,
    ) -> main_models.CreateSiteMonitorResponse:
        runtime = RuntimeOptions()
        return self.create_site_monitor_with_options(request, runtime)

    async def create_site_monitor_async(
        self,
        request: main_models.CreateSiteMonitorRequest,
    ) -> main_models.CreateSiteMonitorResponse:
        runtime = RuntimeOptions()
        return await self.create_site_monitor_with_options_async(request, runtime)

    def cursor_with_options(
        self,
        tmp_req: main_models.CursorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CursorResponse:
        tmp_req.validate()
        request = main_models.CursorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.matchers):
            request.matchers_shrink = Utils.array_to_string_with_specified_style(tmp_req.matchers, 'Matchers', 'json')
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.matchers_shrink):
            body['Matchers'] = request.matchers_shrink
        if not DaraCore.is_null(request.metric):
            body['Metric'] = request.metric
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Cursor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CursorResponse(),
            self.call_api(params, req, runtime)
        )

    async def cursor_with_options_async(
        self,
        tmp_req: main_models.CursorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CursorResponse:
        tmp_req.validate()
        request = main_models.CursorShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.matchers):
            request.matchers_shrink = Utils.array_to_string_with_specified_style(tmp_req.matchers, 'Matchers', 'json')
        body = {}
        if not DaraCore.is_null(request.end_time):
            body['EndTime'] = request.end_time
        if not DaraCore.is_null(request.matchers_shrink):
            body['Matchers'] = request.matchers_shrink
        if not DaraCore.is_null(request.metric):
            body['Metric'] = request.metric
        if not DaraCore.is_null(request.namespace):
            body['Namespace'] = request.namespace
        if not DaraCore.is_null(request.period):
            body['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'Cursor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CursorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cursor(
        self,
        request: main_models.CursorRequest,
    ) -> main_models.CursorResponse:
        runtime = RuntimeOptions()
        return self.cursor_with_options(request, runtime)

    async def cursor_async(
        self,
        request: main_models.CursorRequest,
    ) -> main_models.CursorResponse:
        runtime = RuntimeOptions()
        return await self.cursor_with_options_async(request, runtime)

    def delete_contact_with_options(
        self,
        request: main_models.DeleteContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContact',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_with_options_async(
        self,
        request: main_models.DeleteContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContact',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact(
        self,
        request: main_models.DeleteContactRequest,
    ) -> main_models.DeleteContactResponse:
        runtime = RuntimeOptions()
        return self.delete_contact_with_options(request, runtime)

    async def delete_contact_async(
        self,
        request: main_models.DeleteContactRequest,
    ) -> main_models.DeleteContactResponse:
        runtime = RuntimeOptions()
        return await self.delete_contact_with_options_async(request, runtime)

    def delete_contact_group_with_options(
        self,
        request: main_models.DeleteContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_contact_group_with_options_async(
        self,
        request: main_models.DeleteContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteContactGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_contact_group(
        self,
        request: main_models.DeleteContactGroupRequest,
    ) -> main_models.DeleteContactGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_contact_group_with_options(request, runtime)

    async def delete_contact_group_async(
        self,
        request: main_models.DeleteContactGroupRequest,
    ) -> main_models.DeleteContactGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_contact_group_with_options_async(request, runtime)

    def delete_custom_metric_with_options(
        self,
        request: main_models.DeleteCustomMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.uuid):
            query['UUID'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomMetric',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_custom_metric_with_options_async(
        self,
        request: main_models.DeleteCustomMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.uuid):
            query['UUID'] = request.uuid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomMetric',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_custom_metric(
        self,
        request: main_models.DeleteCustomMetricRequest,
    ) -> main_models.DeleteCustomMetricResponse:
        runtime = RuntimeOptions()
        return self.delete_custom_metric_with_options(request, runtime)

    async def delete_custom_metric_async(
        self,
        request: main_models.DeleteCustomMetricRequest,
    ) -> main_models.DeleteCustomMetricResponse:
        runtime = RuntimeOptions()
        return await self.delete_custom_metric_with_options_async(request, runtime)

    def delete_dynamic_tag_group_with_options(
        self,
        request: main_models.DeleteDynamicTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDynamicTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDynamicTagGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDynamicTagGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_dynamic_tag_group_with_options_async(
        self,
        request: main_models.DeleteDynamicTagGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDynamicTagGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDynamicTagGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDynamicTagGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_dynamic_tag_group(
        self,
        request: main_models.DeleteDynamicTagGroupRequest,
    ) -> main_models.DeleteDynamicTagGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_dynamic_tag_group_with_options(request, runtime)

    async def delete_dynamic_tag_group_async(
        self,
        request: main_models.DeleteDynamicTagGroupRequest,
    ) -> main_models.DeleteDynamicTagGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_dynamic_tag_group_with_options_async(request, runtime)

    def delete_event_rule_targets_with_options(
        self,
        request: main_models.DeleteEventRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_rule_targets_with_options_async(
        self,
        request: main_models.DeleteEventRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_rule_targets(
        self,
        request: main_models.DeleteEventRuleTargetsRequest,
    ) -> main_models.DeleteEventRuleTargetsResponse:
        runtime = RuntimeOptions()
        return self.delete_event_rule_targets_with_options(request, runtime)

    async def delete_event_rule_targets_async(
        self,
        request: main_models.DeleteEventRuleTargetsRequest,
    ) -> main_models.DeleteEventRuleTargetsResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_rule_targets_with_options_async(request, runtime)

    def delete_event_rules_with_options(
        self,
        request: main_models.DeleteEventRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_event_rules_with_options_async(
        self,
        request: main_models.DeleteEventRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEventRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteEventRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteEventRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_event_rules(
        self,
        request: main_models.DeleteEventRulesRequest,
    ) -> main_models.DeleteEventRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_event_rules_with_options(request, runtime)

    async def delete_event_rules_async(
        self,
        request: main_models.DeleteEventRulesRequest,
    ) -> main_models.DeleteEventRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_event_rules_with_options_async(request, runtime)

    def delete_exporter_output_with_options(
        self,
        request: main_models.DeleteExporterOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExporterOutputResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_name):
            query['DestName'] = request.dest_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExporterOutput',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExporterOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_exporter_output_with_options_async(
        self,
        request: main_models.DeleteExporterOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExporterOutputResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dest_name):
            query['DestName'] = request.dest_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExporterOutput',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExporterOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_exporter_output(
        self,
        request: main_models.DeleteExporterOutputRequest,
    ) -> main_models.DeleteExporterOutputResponse:
        runtime = RuntimeOptions()
        return self.delete_exporter_output_with_options(request, runtime)

    async def delete_exporter_output_async(
        self,
        request: main_models.DeleteExporterOutputRequest,
    ) -> main_models.DeleteExporterOutputResponse:
        runtime = RuntimeOptions()
        return await self.delete_exporter_output_with_options_async(request, runtime)

    def delete_exporter_rule_with_options(
        self,
        request: main_models.DeleteExporterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExporterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExporterRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExporterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_exporter_rule_with_options_async(
        self,
        request: main_models.DeleteExporterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteExporterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteExporterRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteExporterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_exporter_rule(
        self,
        request: main_models.DeleteExporterRuleRequest,
    ) -> main_models.DeleteExporterRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_exporter_rule_with_options(request, runtime)

    async def delete_exporter_rule_async(
        self,
        request: main_models.DeleteExporterRuleRequest,
    ) -> main_models.DeleteExporterRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_exporter_rule_with_options_async(request, runtime)

    def delete_group_monitoring_agent_process_with_options(
        self,
        request: main_models.DeleteGroupMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroupMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_group_monitoring_agent_process_with_options_async(
        self,
        request: main_models.DeleteGroupMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteGroupMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteGroupMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteGroupMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_group_monitoring_agent_process(
        self,
        request: main_models.DeleteGroupMonitoringAgentProcessRequest,
    ) -> main_models.DeleteGroupMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return self.delete_group_monitoring_agent_process_with_options(request, runtime)

    async def delete_group_monitoring_agent_process_async(
        self,
        request: main_models.DeleteGroupMonitoringAgentProcessRequest,
    ) -> main_models.DeleteGroupMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return await self.delete_group_monitoring_agent_process_with_options_async(request, runtime)

    def delete_host_availability_with_options(
        self,
        request: main_models.DeleteHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_host_availability_with_options_async(
        self,
        request: main_models.DeleteHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_host_availability(
        self,
        request: main_models.DeleteHostAvailabilityRequest,
    ) -> main_models.DeleteHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return self.delete_host_availability_with_options(request, runtime)

    async def delete_host_availability_async(
        self,
        request: main_models.DeleteHostAvailabilityRequest,
    ) -> main_models.DeleteHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return await self.delete_host_availability_with_options_async(request, runtime)

    def delete_hybrid_monitor_namespace_with_options(
        self,
        request: main_models.DeleteHybridMonitorNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridMonitorNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridMonitorNamespace',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridMonitorNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hybrid_monitor_namespace_with_options_async(
        self,
        request: main_models.DeleteHybridMonitorNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridMonitorNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridMonitorNamespace',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridMonitorNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hybrid_monitor_namespace(
        self,
        request: main_models.DeleteHybridMonitorNamespaceRequest,
    ) -> main_models.DeleteHybridMonitorNamespaceResponse:
        runtime = RuntimeOptions()
        return self.delete_hybrid_monitor_namespace_with_options(request, runtime)

    async def delete_hybrid_monitor_namespace_async(
        self,
        request: main_models.DeleteHybridMonitorNamespaceRequest,
    ) -> main_models.DeleteHybridMonitorNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.delete_hybrid_monitor_namespace_with_options_async(request, runtime)

    def delete_hybrid_monitor_slsgroup_with_options(
        self,
        request: main_models.DeleteHybridMonitorSLSGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridMonitorSLSGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridMonitorSLSGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hybrid_monitor_slsgroup_with_options_async(
        self,
        request: main_models.DeleteHybridMonitorSLSGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridMonitorSLSGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridMonitorSLSGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridMonitorSLSGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hybrid_monitor_slsgroup(
        self,
        request: main_models.DeleteHybridMonitorSLSGroupRequest,
    ) -> main_models.DeleteHybridMonitorSLSGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_hybrid_monitor_slsgroup_with_options(request, runtime)

    async def delete_hybrid_monitor_slsgroup_async(
        self,
        request: main_models.DeleteHybridMonitorSLSGroupRequest,
    ) -> main_models.DeleteHybridMonitorSLSGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_hybrid_monitor_slsgroup_with_options_async(request, runtime)

    def delete_hybrid_monitor_task_with_options(
        self,
        request: main_models.DeleteHybridMonitorTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridMonitorTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridMonitorTask',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_hybrid_monitor_task_with_options_async(
        self,
        request: main_models.DeleteHybridMonitorTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteHybridMonitorTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteHybridMonitorTask',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteHybridMonitorTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_hybrid_monitor_task(
        self,
        request: main_models.DeleteHybridMonitorTaskRequest,
    ) -> main_models.DeleteHybridMonitorTaskResponse:
        runtime = RuntimeOptions()
        return self.delete_hybrid_monitor_task_with_options(request, runtime)

    async def delete_hybrid_monitor_task_async(
        self,
        request: main_models.DeleteHybridMonitorTaskRequest,
    ) -> main_models.DeleteHybridMonitorTaskResponse:
        runtime = RuntimeOptions()
        return await self.delete_hybrid_monitor_task_with_options_async(request, runtime)

    def delete_log_monitor_with_options(
        self,
        request: main_models.DeleteLogMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_id):
            query['LogId'] = request.log_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_log_monitor_with_options_async(
        self,
        request: main_models.DeleteLogMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLogMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.log_id):
            query['LogId'] = request.log_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteLogMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteLogMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_log_monitor(
        self,
        request: main_models.DeleteLogMonitorRequest,
    ) -> main_models.DeleteLogMonitorResponse:
        runtime = RuntimeOptions()
        return self.delete_log_monitor_with_options(request, runtime)

    async def delete_log_monitor_async(
        self,
        request: main_models.DeleteLogMonitorRequest,
    ) -> main_models.DeleteLogMonitorResponse:
        runtime = RuntimeOptions()
        return await self.delete_log_monitor_with_options_async(request, runtime)

    def delete_metric_rule_black_list_with_options(
        self,
        request: main_models.DeleteMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rule_black_list_with_options_async(
        self,
        request: main_models.DeleteMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rule_black_list(
        self,
        request: main_models.DeleteMetricRuleBlackListRequest,
    ) -> main_models.DeleteMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return self.delete_metric_rule_black_list_with_options(request, runtime)

    async def delete_metric_rule_black_list_async(
        self,
        request: main_models.DeleteMetricRuleBlackListRequest,
    ) -> main_models.DeleteMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return await self.delete_metric_rule_black_list_with_options_async(request, runtime)

    def delete_metric_rule_resources_with_options(
        self,
        request: main_models.DeleteMetricRuleResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRuleResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRuleResources',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rule_resources_with_options_async(
        self,
        request: main_models.DeleteMetricRuleResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRuleResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRuleResources',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRuleResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rule_resources(
        self,
        request: main_models.DeleteMetricRuleResourcesRequest,
    ) -> main_models.DeleteMetricRuleResourcesResponse:
        runtime = RuntimeOptions()
        return self.delete_metric_rule_resources_with_options(request, runtime)

    async def delete_metric_rule_resources_async(
        self,
        request: main_models.DeleteMetricRuleResourcesRequest,
    ) -> main_models.DeleteMetricRuleResourcesResponse:
        runtime = RuntimeOptions()
        return await self.delete_metric_rule_resources_with_options_async(request, runtime)

    def delete_metric_rule_targets_with_options(
        self,
        request: main_models.DeleteMetricRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.target_ids):
            query['TargetIds'] = request.target_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rule_targets_with_options_async(
        self,
        request: main_models.DeleteMetricRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.target_ids):
            query['TargetIds'] = request.target_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rule_targets(
        self,
        request: main_models.DeleteMetricRuleTargetsRequest,
    ) -> main_models.DeleteMetricRuleTargetsResponse:
        runtime = RuntimeOptions()
        return self.delete_metric_rule_targets_with_options(request, runtime)

    async def delete_metric_rule_targets_async(
        self,
        request: main_models.DeleteMetricRuleTargetsRequest,
    ) -> main_models.DeleteMetricRuleTargetsResponse:
        runtime = RuntimeOptions()
        return await self.delete_metric_rule_targets_with_options_async(request, runtime)

    def delete_metric_rule_template_with_options(
        self,
        request: main_models.DeleteMetricRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRuleTemplate',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rule_template_with_options_async(
        self,
        request: main_models.DeleteMetricRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRuleTemplate',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rule_template(
        self,
        request: main_models.DeleteMetricRuleTemplateRequest,
    ) -> main_models.DeleteMetricRuleTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_metric_rule_template_with_options(request, runtime)

    async def delete_metric_rule_template_async(
        self,
        request: main_models.DeleteMetricRuleTemplateRequest,
    ) -> main_models.DeleteMetricRuleTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_metric_rule_template_with_options_async(request, runtime)

    def delete_metric_rules_with_options(
        self,
        request: main_models.DeleteMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_metric_rules_with_options_async(
        self,
        request: main_models.DeleteMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_metric_rules(
        self,
        request: main_models.DeleteMetricRulesRequest,
    ) -> main_models.DeleteMetricRulesResponse:
        runtime = RuntimeOptions()
        return self.delete_metric_rules_with_options(request, runtime)

    async def delete_metric_rules_async(
        self,
        request: main_models.DeleteMetricRulesRequest,
    ) -> main_models.DeleteMetricRulesResponse:
        runtime = RuntimeOptions()
        return await self.delete_metric_rules_with_options_async(request, runtime)

    def delete_monitor_group_with_options(
        self,
        request: main_models.DeleteMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_with_options_async(
        self,
        request: main_models.DeleteMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group(
        self,
        request: main_models.DeleteMonitorGroupRequest,
    ) -> main_models.DeleteMonitorGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_monitor_group_with_options(request, runtime)

    async def delete_monitor_group_async(
        self,
        request: main_models.DeleteMonitorGroupRequest,
    ) -> main_models.DeleteMonitorGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_monitor_group_with_options_async(request, runtime)

    def delete_monitor_group_dynamic_rule_with_options(
        self,
        request: main_models.DeleteMonitorGroupDynamicRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupDynamicRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroupDynamicRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupDynamicRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_dynamic_rule_with_options_async(
        self,
        request: main_models.DeleteMonitorGroupDynamicRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupDynamicRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroupDynamicRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupDynamicRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group_dynamic_rule(
        self,
        request: main_models.DeleteMonitorGroupDynamicRuleRequest,
    ) -> main_models.DeleteMonitorGroupDynamicRuleResponse:
        runtime = RuntimeOptions()
        return self.delete_monitor_group_dynamic_rule_with_options(request, runtime)

    async def delete_monitor_group_dynamic_rule_async(
        self,
        request: main_models.DeleteMonitorGroupDynamicRuleRequest,
    ) -> main_models.DeleteMonitorGroupDynamicRuleResponse:
        runtime = RuntimeOptions()
        return await self.delete_monitor_group_dynamic_rule_with_options_async(request, runtime)

    def delete_monitor_group_instances_with_options(
        self,
        request: main_models.DeleteMonitorGroupInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroupInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_instances_with_options_async(
        self,
        request: main_models.DeleteMonitorGroupInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_id_list):
            query['InstanceIdList'] = request.instance_id_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroupInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group_instances(
        self,
        request: main_models.DeleteMonitorGroupInstancesRequest,
    ) -> main_models.DeleteMonitorGroupInstancesResponse:
        runtime = RuntimeOptions()
        return self.delete_monitor_group_instances_with_options(request, runtime)

    async def delete_monitor_group_instances_async(
        self,
        request: main_models.DeleteMonitorGroupInstancesRequest,
    ) -> main_models.DeleteMonitorGroupInstancesResponse:
        runtime = RuntimeOptions()
        return await self.delete_monitor_group_instances_with_options_async(request, runtime)

    def delete_monitor_group_notify_policy_with_options(
        self,
        request: main_models.DeleteMonitorGroupNotifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupNotifyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroupNotifyPolicy',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupNotifyPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_notify_policy_with_options_async(
        self,
        request: main_models.DeleteMonitorGroupNotifyPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupNotifyPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroupNotifyPolicy',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupNotifyPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group_notify_policy(
        self,
        request: main_models.DeleteMonitorGroupNotifyPolicyRequest,
    ) -> main_models.DeleteMonitorGroupNotifyPolicyResponse:
        runtime = RuntimeOptions()
        return self.delete_monitor_group_notify_policy_with_options(request, runtime)

    async def delete_monitor_group_notify_policy_async(
        self,
        request: main_models.DeleteMonitorGroupNotifyPolicyRequest,
    ) -> main_models.DeleteMonitorGroupNotifyPolicyResponse:
        runtime = RuntimeOptions()
        return await self.delete_monitor_group_notify_policy_with_options_async(request, runtime)

    def delete_monitoring_agent_process_with_options(
        self,
        request: main_models.DeleteMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitoring_agent_process_with_options_async(
        self,
        request: main_models.DeleteMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.process_id):
            query['ProcessId'] = request.process_id
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitoring_agent_process(
        self,
        request: main_models.DeleteMonitoringAgentProcessRequest,
    ) -> main_models.DeleteMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return self.delete_monitoring_agent_process_with_options(request, runtime)

    async def delete_monitoring_agent_process_async(
        self,
        request: main_models.DeleteMonitoringAgentProcessRequest,
    ) -> main_models.DeleteMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return await self.delete_monitoring_agent_process_with_options_async(request, runtime)

    def delete_site_monitors_with_options(
        self,
        request: main_models.DeleteSiteMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSiteMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_delete_alarms):
            query['IsDeleteAlarms'] = request.is_delete_alarms
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSiteMonitors',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSiteMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_site_monitors_with_options_async(
        self,
        request: main_models.DeleteSiteMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSiteMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_delete_alarms):
            query['IsDeleteAlarms'] = request.is_delete_alarms
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSiteMonitors',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSiteMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_site_monitors(
        self,
        request: main_models.DeleteSiteMonitorsRequest,
    ) -> main_models.DeleteSiteMonitorsResponse:
        runtime = RuntimeOptions()
        return self.delete_site_monitors_with_options(request, runtime)

    async def delete_site_monitors_async(
        self,
        request: main_models.DeleteSiteMonitorsRequest,
    ) -> main_models.DeleteSiteMonitorsResponse:
        runtime = RuntimeOptions()
        return await self.delete_site_monitors_with_options_async(request, runtime)

    def describe_active_metric_rule_list_with_options(
        self,
        request: main_models.DescribeActiveMetricRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveMetricRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveMetricRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveMetricRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_active_metric_rule_list_with_options_async(
        self,
        request: main_models.DescribeActiveMetricRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeActiveMetricRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeActiveMetricRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeActiveMetricRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_active_metric_rule_list(
        self,
        request: main_models.DescribeActiveMetricRuleListRequest,
    ) -> main_models.DescribeActiveMetricRuleListResponse:
        runtime = RuntimeOptions()
        return self.describe_active_metric_rule_list_with_options(request, runtime)

    async def describe_active_metric_rule_list_async(
        self,
        request: main_models.DescribeActiveMetricRuleListRequest,
    ) -> main_models.DescribeActiveMetricRuleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_active_metric_rule_list_with_options_async(request, runtime)

    def describe_alert_history_list_with_options(
        self,
        request: main_models.DescribeAlertHistoryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertHistoryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascending):
            query['Ascending'] = request.ascending
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertHistoryList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertHistoryListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_history_list_with_options_async(
        self,
        request: main_models.DescribeAlertHistoryListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertHistoryListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ascending):
            query['Ascending'] = request.ascending
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertHistoryList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertHistoryListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_history_list(
        self,
        request: main_models.DescribeAlertHistoryListRequest,
    ) -> main_models.DescribeAlertHistoryListResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_history_list_with_options(request, runtime)

    async def describe_alert_history_list_async(
        self,
        request: main_models.DescribeAlertHistoryListRequest,
    ) -> main_models.DescribeAlertHistoryListResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_history_list_with_options_async(request, runtime)

    def describe_alert_log_count_with_options(
        self,
        request: main_models.DescribeAlertLogCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertLogCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.last_min):
            query['LastMin'] = request.last_min
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.send_status):
            query['SendStatus'] = request.send_status
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertLogCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertLogCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_log_count_with_options_async(
        self,
        request: main_models.DescribeAlertLogCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertLogCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.last_min):
            query['LastMin'] = request.last_min
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.send_status):
            query['SendStatus'] = request.send_status
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertLogCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertLogCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_log_count(
        self,
        request: main_models.DescribeAlertLogCountRequest,
    ) -> main_models.DescribeAlertLogCountResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_log_count_with_options(request, runtime)

    async def describe_alert_log_count_async(
        self,
        request: main_models.DescribeAlertLogCountRequest,
    ) -> main_models.DescribeAlertLogCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_log_count_with_options_async(request, runtime)

    def describe_alert_log_histogram_with_options(
        self,
        request: main_models.DescribeAlertLogHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertLogHistogramResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.last_min):
            query['LastMin'] = request.last_min
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.send_status):
            query['SendStatus'] = request.send_status
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertLogHistogram',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertLogHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_log_histogram_with_options_async(
        self,
        request: main_models.DescribeAlertLogHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertLogHistogramResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.last_min):
            query['LastMin'] = request.last_min
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.send_status):
            query['SendStatus'] = request.send_status
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertLogHistogram',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertLogHistogramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_log_histogram(
        self,
        request: main_models.DescribeAlertLogHistogramRequest,
    ) -> main_models.DescribeAlertLogHistogramResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_log_histogram_with_options(request, runtime)

    async def describe_alert_log_histogram_async(
        self,
        request: main_models.DescribeAlertLogHistogramRequest,
    ) -> main_models.DescribeAlertLogHistogramResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_log_histogram_with_options_async(request, runtime)

    def describe_alert_log_list_with_options(
        self,
        request: main_models.DescribeAlertLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.last_min):
            query['LastMin'] = request.last_min
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.send_status):
            query['SendStatus'] = request.send_status
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertLogList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertLogListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alert_log_list_with_options_async(
        self,
        request: main_models.DescribeAlertLogListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertLogListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_by):
            query['GroupBy'] = request.group_by
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.last_min):
            query['LastMin'] = request.last_min
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.search_key):
            query['SearchKey'] = request.search_key
        if not DaraCore.is_null(request.send_status):
            query['SendStatus'] = request.send_status
        if not DaraCore.is_null(request.source_type):
            query['SourceType'] = request.source_type
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertLogList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertLogListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alert_log_list(
        self,
        request: main_models.DescribeAlertLogListRequest,
    ) -> main_models.DescribeAlertLogListResponse:
        runtime = RuntimeOptions()
        return self.describe_alert_log_list_with_options(request, runtime)

    async def describe_alert_log_list_async(
        self,
        request: main_models.DescribeAlertLogListRequest,
    ) -> main_models.DescribeAlertLogListResponse:
        runtime = RuntimeOptions()
        return await self.describe_alert_log_list_with_options_async(request, runtime)

    def describe_alerting_metric_rule_resources_with_options(
        self,
        request: main_models.DescribeAlertingMetricRuleResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertingMetricRuleResourcesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertingMetricRuleResources',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertingMetricRuleResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_alerting_metric_rule_resources_with_options_async(
        self,
        request: main_models.DescribeAlertingMetricRuleResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeAlertingMetricRuleResourcesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeAlertingMetricRuleResources',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeAlertingMetricRuleResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_alerting_metric_rule_resources(
        self,
        request: main_models.DescribeAlertingMetricRuleResourcesRequest,
    ) -> main_models.DescribeAlertingMetricRuleResourcesResponse:
        runtime = RuntimeOptions()
        return self.describe_alerting_metric_rule_resources_with_options(request, runtime)

    async def describe_alerting_metric_rule_resources_async(
        self,
        request: main_models.DescribeAlertingMetricRuleResourcesRequest,
    ) -> main_models.DescribeAlertingMetricRuleResourcesResponse:
        runtime = RuntimeOptions()
        return await self.describe_alerting_metric_rule_resources_with_options_async(request, runtime)

    def describe_contact_group_list_with_options(
        self,
        request: main_models.DescribeContactGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContactGroupList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contact_group_list_with_options_async(
        self,
        request: main_models.DescribeContactGroupListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactGroupListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContactGroupList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactGroupListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contact_group_list(
        self,
        request: main_models.DescribeContactGroupListRequest,
    ) -> main_models.DescribeContactGroupListResponse:
        runtime = RuntimeOptions()
        return self.describe_contact_group_list_with_options(request, runtime)

    async def describe_contact_group_list_async(
        self,
        request: main_models.DescribeContactGroupListRequest,
    ) -> main_models.DescribeContactGroupListResponse:
        runtime = RuntimeOptions()
        return await self.describe_contact_group_list_with_options_async(request, runtime)

    def describe_contact_list_with_options(
        self,
        request: main_models.DescribeContactListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chanel_type):
            query['ChanelType'] = request.chanel_type
        if not DaraCore.is_null(request.chanel_value):
            query['ChanelValue'] = request.chanel_value
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContactList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contact_list_with_options_async(
        self,
        request: main_models.DescribeContactListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.chanel_type):
            query['ChanelType'] = request.chanel_type
        if not DaraCore.is_null(request.chanel_value):
            query['ChanelValue'] = request.chanel_value
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContactList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contact_list(
        self,
        request: main_models.DescribeContactListRequest,
    ) -> main_models.DescribeContactListResponse:
        runtime = RuntimeOptions()
        return self.describe_contact_list_with_options(request, runtime)

    async def describe_contact_list_async(
        self,
        request: main_models.DescribeContactListRequest,
    ) -> main_models.DescribeContactListResponse:
        runtime = RuntimeOptions()
        return await self.describe_contact_list_with_options_async(request, runtime)

    def describe_contact_list_by_contact_group_with_options(
        self,
        request: main_models.DescribeContactListByContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactListByContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContactListByContactGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactListByContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_contact_list_by_contact_group_with_options_async(
        self,
        request: main_models.DescribeContactListByContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeContactListByContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeContactListByContactGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeContactListByContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_contact_list_by_contact_group(
        self,
        request: main_models.DescribeContactListByContactGroupRequest,
    ) -> main_models.DescribeContactListByContactGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_contact_list_by_contact_group_with_options(request, runtime)

    async def describe_contact_list_by_contact_group_async(
        self,
        request: main_models.DescribeContactListByContactGroupRequest,
    ) -> main_models.DescribeContactListByContactGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_contact_list_by_contact_group_with_options_async(request, runtime)

    def describe_custom_event_attribute_with_options(
        self,
        request: main_models.DescribeCustomEventAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomEventAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomEventAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomEventAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_event_attribute_with_options_async(
        self,
        request: main_models.DescribeCustomEventAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomEventAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomEventAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomEventAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_event_attribute(
        self,
        request: main_models.DescribeCustomEventAttributeRequest,
    ) -> main_models.DescribeCustomEventAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_event_attribute_with_options(request, runtime)

    async def describe_custom_event_attribute_async(
        self,
        request: main_models.DescribeCustomEventAttributeRequest,
    ) -> main_models.DescribeCustomEventAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_event_attribute_with_options_async(request, runtime)

    def describe_custom_event_count_with_options(
        self,
        request: main_models.DescribeCustomEventCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomEventCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomEventCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_event_count_with_options_async(
        self,
        request: main_models.DescribeCustomEventCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomEventCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomEventCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomEventCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_event_count(
        self,
        request: main_models.DescribeCustomEventCountRequest,
    ) -> main_models.DescribeCustomEventCountResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_event_count_with_options(request, runtime)

    async def describe_custom_event_count_async(
        self,
        request: main_models.DescribeCustomEventCountRequest,
    ) -> main_models.DescribeCustomEventCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_event_count_with_options_async(request, runtime)

    def describe_custom_event_histogram_with_options(
        self,
        request: main_models.DescribeCustomEventHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomEventHistogramResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomEventHistogram',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomEventHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_event_histogram_with_options_async(
        self,
        request: main_models.DescribeCustomEventHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomEventHistogramResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_id):
            query['EventId'] = request.event_id
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomEventHistogram',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomEventHistogramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_event_histogram(
        self,
        request: main_models.DescribeCustomEventHistogramRequest,
    ) -> main_models.DescribeCustomEventHistogramResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_event_histogram_with_options(request, runtime)

    async def describe_custom_event_histogram_async(
        self,
        request: main_models.DescribeCustomEventHistogramRequest,
    ) -> main_models.DescribeCustomEventHistogramResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_event_histogram_with_options_async(request, runtime)

    def describe_custom_metric_list_with_options(
        self,
        request: main_models.DescribeCustomMetricListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomMetricListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomMetricList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_custom_metric_list_with_options_async(
        self,
        request: main_models.DescribeCustomMetricListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeCustomMetricListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.md_5):
            query['Md5'] = request.md_5
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeCustomMetricList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeCustomMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_custom_metric_list(
        self,
        request: main_models.DescribeCustomMetricListRequest,
    ) -> main_models.DescribeCustomMetricListResponse:
        runtime = RuntimeOptions()
        return self.describe_custom_metric_list_with_options(request, runtime)

    async def describe_custom_metric_list_async(
        self,
        request: main_models.DescribeCustomMetricListRequest,
    ) -> main_models.DescribeCustomMetricListResponse:
        runtime = RuntimeOptions()
        return await self.describe_custom_metric_list_with_options_async(request, runtime)

    def describe_dynamic_tag_rule_list_with_options(
        self,
        request: main_models.DescribeDynamicTagRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDynamicTagRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not DaraCore.is_null(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDynamicTagRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDynamicTagRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_dynamic_tag_rule_list_with_options_async(
        self,
        request: main_models.DescribeDynamicTagRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeDynamicTagRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tag_region_id):
            query['TagRegionId'] = request.tag_region_id
        if not DaraCore.is_null(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeDynamicTagRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeDynamicTagRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_dynamic_tag_rule_list(
        self,
        request: main_models.DescribeDynamicTagRuleListRequest,
    ) -> main_models.DescribeDynamicTagRuleListResponse:
        runtime = RuntimeOptions()
        return self.describe_dynamic_tag_rule_list_with_options(request, runtime)

    async def describe_dynamic_tag_rule_list_async(
        self,
        request: main_models.DescribeDynamicTagRuleListRequest,
    ) -> main_models.DescribeDynamicTagRuleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_dynamic_tag_rule_list_with_options_async(request, runtime)

    def describe_event_rule_attribute_with_options(
        self,
        request: main_models.DescribeEventRuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventRuleAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventRuleAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_rule_attribute_with_options_async(
        self,
        request: main_models.DescribeEventRuleAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventRuleAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventRuleAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventRuleAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_rule_attribute(
        self,
        request: main_models.DescribeEventRuleAttributeRequest,
    ) -> main_models.DescribeEventRuleAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_event_rule_attribute_with_options(request, runtime)

    async def describe_event_rule_attribute_async(
        self,
        request: main_models.DescribeEventRuleAttributeRequest,
    ) -> main_models.DescribeEventRuleAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_rule_attribute_with_options_async(request, runtime)

    def describe_event_rule_list_with_options(
        self,
        request: main_models.DescribeEventRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not DaraCore.is_null(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_rule_list_with_options_async(
        self,
        request: main_models.DescribeEventRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not DaraCore.is_null(request.name_prefix):
            query['NamePrefix'] = request.name_prefix
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_rule_list(
        self,
        request: main_models.DescribeEventRuleListRequest,
    ) -> main_models.DescribeEventRuleListResponse:
        runtime = RuntimeOptions()
        return self.describe_event_rule_list_with_options(request, runtime)

    async def describe_event_rule_list_async(
        self,
        request: main_models.DescribeEventRuleListRequest,
    ) -> main_models.DescribeEventRuleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_rule_list_with_options_async(request, runtime)

    def describe_event_rule_target_list_with_options(
        self,
        request: main_models.DescribeEventRuleTargetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventRuleTargetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventRuleTargetList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventRuleTargetListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_event_rule_target_list_with_options_async(
        self,
        request: main_models.DescribeEventRuleTargetListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeEventRuleTargetListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeEventRuleTargetList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeEventRuleTargetListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_event_rule_target_list(
        self,
        request: main_models.DescribeEventRuleTargetListRequest,
    ) -> main_models.DescribeEventRuleTargetListResponse:
        runtime = RuntimeOptions()
        return self.describe_event_rule_target_list_with_options(request, runtime)

    async def describe_event_rule_target_list_async(
        self,
        request: main_models.DescribeEventRuleTargetListRequest,
    ) -> main_models.DescribeEventRuleTargetListResponse:
        runtime = RuntimeOptions()
        return await self.describe_event_rule_target_list_with_options_async(request, runtime)

    def describe_exporter_output_list_with_options(
        self,
        request: main_models.DescribeExporterOutputListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExporterOutputListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExporterOutputList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExporterOutputListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exporter_output_list_with_options_async(
        self,
        request: main_models.DescribeExporterOutputListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExporterOutputListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExporterOutputList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExporterOutputListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exporter_output_list(
        self,
        request: main_models.DescribeExporterOutputListRequest,
    ) -> main_models.DescribeExporterOutputListResponse:
        runtime = RuntimeOptions()
        return self.describe_exporter_output_list_with_options(request, runtime)

    async def describe_exporter_output_list_async(
        self,
        request: main_models.DescribeExporterOutputListRequest,
    ) -> main_models.DescribeExporterOutputListResponse:
        runtime = RuntimeOptions()
        return await self.describe_exporter_output_list_with_options_async(request, runtime)

    def describe_exporter_rule_list_with_options(
        self,
        request: main_models.DescribeExporterRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExporterRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExporterRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExporterRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_exporter_rule_list_with_options_async(
        self,
        request: main_models.DescribeExporterRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeExporterRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeExporterRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeExporterRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_exporter_rule_list(
        self,
        request: main_models.DescribeExporterRuleListRequest,
    ) -> main_models.DescribeExporterRuleListResponse:
        runtime = RuntimeOptions()
        return self.describe_exporter_rule_list_with_options(request, runtime)

    async def describe_exporter_rule_list_async(
        self,
        request: main_models.DescribeExporterRuleListRequest,
    ) -> main_models.DescribeExporterRuleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_exporter_rule_list_with_options_async(request, runtime)

    def describe_group_monitoring_agent_process_with_options(
        self,
        request: main_models.DescribeGroupMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_group_monitoring_agent_process_with_options_async(
        self,
        request: main_models.DescribeGroupMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeGroupMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.process_name):
            query['ProcessName'] = request.process_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeGroupMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeGroupMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_group_monitoring_agent_process(
        self,
        request: main_models.DescribeGroupMonitoringAgentProcessRequest,
    ) -> main_models.DescribeGroupMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return self.describe_group_monitoring_agent_process_with_options(request, runtime)

    async def describe_group_monitoring_agent_process_async(
        self,
        request: main_models.DescribeGroupMonitoringAgentProcessRequest,
    ) -> main_models.DescribeGroupMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return await self.describe_group_monitoring_agent_process_with_options_async(request, runtime)

    def describe_host_availability_list_with_options(
        self,
        request: main_models.DescribeHostAvailabilityListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHostAvailabilityListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHostAvailabilityList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHostAvailabilityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_host_availability_list_with_options_async(
        self,
        request: main_models.DescribeHostAvailabilityListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHostAvailabilityListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHostAvailabilityList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHostAvailabilityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_host_availability_list(
        self,
        request: main_models.DescribeHostAvailabilityListRequest,
    ) -> main_models.DescribeHostAvailabilityListResponse:
        runtime = RuntimeOptions()
        return self.describe_host_availability_list_with_options(request, runtime)

    async def describe_host_availability_list_async(
        self,
        request: main_models.DescribeHostAvailabilityListRequest,
    ) -> main_models.DescribeHostAvailabilityListResponse:
        runtime = RuntimeOptions()
        return await self.describe_host_availability_list_with_options_async(request, runtime)

    def describe_hybrid_monitor_data_list_with_options(
        self,
        request: main_models.DescribeHybridMonitorDataListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridMonitorDataListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.prom_sql):
            query['PromSQL'] = request.prom_sql
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridMonitorDataList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridMonitorDataListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_monitor_data_list_with_options_async(
        self,
        request: main_models.DescribeHybridMonitorDataListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridMonitorDataListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end):
            query['End'] = request.end
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.prom_sql):
            query['PromSQL'] = request.prom_sql
        if not DaraCore.is_null(request.start):
            query['Start'] = request.start
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridMonitorDataList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridMonitorDataListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_monitor_data_list(
        self,
        request: main_models.DescribeHybridMonitorDataListRequest,
    ) -> main_models.DescribeHybridMonitorDataListResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_monitor_data_list_with_options(request, runtime)

    async def describe_hybrid_monitor_data_list_async(
        self,
        request: main_models.DescribeHybridMonitorDataListRequest,
    ) -> main_models.DescribeHybridMonitorDataListResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_monitor_data_list_with_options_async(request, runtime)

    def describe_hybrid_monitor_namespace_list_with_options(
        self,
        request: main_models.DescribeHybridMonitorNamespaceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridMonitorNamespaceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_task_statistic):
            query['ShowTaskStatistic'] = request.show_task_statistic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridMonitorNamespaceList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridMonitorNamespaceListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_monitor_namespace_list_with_options_async(
        self,
        request: main_models.DescribeHybridMonitorNamespaceListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridMonitorNamespaceListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.show_task_statistic):
            query['ShowTaskStatistic'] = request.show_task_statistic
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridMonitorNamespaceList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridMonitorNamespaceListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_monitor_namespace_list(
        self,
        request: main_models.DescribeHybridMonitorNamespaceListRequest,
    ) -> main_models.DescribeHybridMonitorNamespaceListResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_monitor_namespace_list_with_options(request, runtime)

    async def describe_hybrid_monitor_namespace_list_async(
        self,
        request: main_models.DescribeHybridMonitorNamespaceListRequest,
    ) -> main_models.DescribeHybridMonitorNamespaceListResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_monitor_namespace_list_with_options_async(request, runtime)

    def describe_hybrid_monitor_slsgroup_with_options(
        self,
        request: main_models.DescribeHybridMonitorSLSGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridMonitorSLSGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridMonitorSLSGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_monitor_slsgroup_with_options_async(
        self,
        request: main_models.DescribeHybridMonitorSLSGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridMonitorSLSGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridMonitorSLSGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridMonitorSLSGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_monitor_slsgroup(
        self,
        request: main_models.DescribeHybridMonitorSLSGroupRequest,
    ) -> main_models.DescribeHybridMonitorSLSGroupResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_monitor_slsgroup_with_options(request, runtime)

    async def describe_hybrid_monitor_slsgroup_async(
        self,
        request: main_models.DescribeHybridMonitorSLSGroupRequest,
    ) -> main_models.DescribeHybridMonitorSLSGroupResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_monitor_slsgroup_with_options_async(request, runtime)

    def describe_hybrid_monitor_task_list_with_options(
        self,
        request: main_models.DescribeHybridMonitorTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridMonitorTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.include_aliyun_task):
            query['IncludeAliyunTask'] = request.include_aliyun_task
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridMonitorTaskList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridMonitorTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_hybrid_monitor_task_list_with_options_async(
        self,
        request: main_models.DescribeHybridMonitorTaskListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeHybridMonitorTaskListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.include_aliyun_task):
            query['IncludeAliyunTask'] = request.include_aliyun_task
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.target_user_id):
            query['TargetUserId'] = request.target_user_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeHybridMonitorTaskList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeHybridMonitorTaskListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_hybrid_monitor_task_list(
        self,
        request: main_models.DescribeHybridMonitorTaskListRequest,
    ) -> main_models.DescribeHybridMonitorTaskListResponse:
        runtime = RuntimeOptions()
        return self.describe_hybrid_monitor_task_list_with_options(request, runtime)

    async def describe_hybrid_monitor_task_list_async(
        self,
        request: main_models.DescribeHybridMonitorTaskListRequest,
    ) -> main_models.DescribeHybridMonitorTaskListResponse:
        runtime = RuntimeOptions()
        return await self.describe_hybrid_monitor_task_list_with_options_async(request, runtime)

    def describe_log_monitor_attribute_with_options(
        self,
        request: main_models.DescribeLogMonitorAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogMonitorAttributeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogMonitorAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogMonitorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_monitor_attribute_with_options_async(
        self,
        request: main_models.DescribeLogMonitorAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogMonitorAttributeResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogMonitorAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogMonitorAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_monitor_attribute(
        self,
        request: main_models.DescribeLogMonitorAttributeRequest,
    ) -> main_models.DescribeLogMonitorAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_log_monitor_attribute_with_options(request, runtime)

    async def describe_log_monitor_attribute_async(
        self,
        request: main_models.DescribeLogMonitorAttributeRequest,
    ) -> main_models.DescribeLogMonitorAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_monitor_attribute_with_options_async(request, runtime)

    def describe_log_monitor_list_with_options(
        self,
        request: main_models.DescribeLogMonitorListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogMonitorListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogMonitorList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_log_monitor_list_with_options_async(
        self,
        request: main_models.DescribeLogMonitorListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeLogMonitorListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.search_value):
            query['SearchValue'] = request.search_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeLogMonitorList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeLogMonitorListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_log_monitor_list(
        self,
        request: main_models.DescribeLogMonitorListRequest,
    ) -> main_models.DescribeLogMonitorListResponse:
        runtime = RuntimeOptions()
        return self.describe_log_monitor_list_with_options(request, runtime)

    async def describe_log_monitor_list_async(
        self,
        request: main_models.DescribeLogMonitorListRequest,
    ) -> main_models.DescribeLogMonitorListResponse:
        runtime = RuntimeOptions()
        return await self.describe_log_monitor_list_with_options_async(request, runtime)

    def describe_metric_data_with_options(
        self,
        request: main_models.DescribeMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.express):
            query['Express'] = request.express
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricData',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_data_with_options_async(
        self,
        request: main_models.DescribeMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.express):
            query['Express'] = request.express
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricData',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_data(
        self,
        request: main_models.DescribeMetricDataRequest,
    ) -> main_models.DescribeMetricDataResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_data_with_options(request, runtime)

    async def describe_metric_data_async(
        self,
        request: main_models.DescribeMetricDataRequest,
    ) -> main_models.DescribeMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_data_with_options_async(request, runtime)

    def describe_metric_last_with_options(
        self,
        request: main_models.DescribeMetricLastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricLastResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.express):
            query['Express'] = request.express
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricLast',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricLastResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_last_with_options_async(
        self,
        request: main_models.DescribeMetricLastRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricLastResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.express):
            query['Express'] = request.express
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricLast',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricLastResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_last(
        self,
        request: main_models.DescribeMetricLastRequest,
    ) -> main_models.DescribeMetricLastResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_last_with_options(request, runtime)

    async def describe_metric_last_async(
        self,
        request: main_models.DescribeMetricLastRequest,
    ) -> main_models.DescribeMetricLastResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_last_with_options_async(request, runtime)

    def describe_metric_list_with_options(
        self,
        request: main_models.DescribeMetricListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.express):
            query['Express'] = request.express
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_list_with_options_async(
        self,
        request: main_models.DescribeMetricListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.express):
            query['Express'] = request.express
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_list(
        self,
        request: main_models.DescribeMetricListRequest,
    ) -> main_models.DescribeMetricListResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_list_with_options(request, runtime)

    async def describe_metric_list_async(
        self,
        request: main_models.DescribeMetricListRequest,
    ) -> main_models.DescribeMetricListResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_list_with_options_async(request, runtime)

    def describe_metric_meta_list_with_options(
        self,
        request: main_models.DescribeMetricMetaListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricMetaListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricMetaList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_meta_list_with_options_async(
        self,
        request: main_models.DescribeMetricMetaListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricMetaListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricMetaList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_meta_list(
        self,
        request: main_models.DescribeMetricMetaListRequest,
    ) -> main_models.DescribeMetricMetaListResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_meta_list_with_options(request, runtime)

    async def describe_metric_meta_list_async(
        self,
        request: main_models.DescribeMetricMetaListRequest,
    ) -> main_models.DescribeMetricMetaListResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_meta_list_with_options_async(request, runtime)

    def describe_metric_rule_black_list_with_options(
        self,
        request: main_models.DescribeMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_black_list_with_options_async(
        self,
        request: main_models.DescribeMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.ids):
            query['Ids'] = request.ids
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_black_list(
        self,
        request: main_models.DescribeMetricRuleBlackListRequest,
    ) -> main_models.DescribeMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_rule_black_list_with_options(request, runtime)

    async def describe_metric_rule_black_list_async(
        self,
        request: main_models.DescribeMetricRuleBlackListRequest,
    ) -> main_models.DescribeMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_rule_black_list_with_options_async(request, runtime)

    def describe_metric_rule_count_with_options(
        self,
        request: main_models.DescribeMetricRuleCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleCountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_count_with_options_async(
        self,
        request: main_models.DescribeMetricRuleCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleCountResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_count(
        self,
        request: main_models.DescribeMetricRuleCountRequest,
    ) -> main_models.DescribeMetricRuleCountResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_rule_count_with_options(request, runtime)

    async def describe_metric_rule_count_async(
        self,
        request: main_models.DescribeMetricRuleCountRequest,
    ) -> main_models.DescribeMetricRuleCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_rule_count_with_options_async(request, runtime)

    def describe_metric_rule_list_with_options(
        self,
        request: main_models.DescribeMetricRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_state):
            query['AlertState'] = request.alert_state
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.enable_state):
            query['EnableState'] = request.enable_state
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_list_with_options_async(
        self,
        request: main_models.DescribeMetricRuleListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_state):
            query['AlertState'] = request.alert_state
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.enable_state):
            query['EnableState'] = request.enable_state
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_list(
        self,
        request: main_models.DescribeMetricRuleListRequest,
    ) -> main_models.DescribeMetricRuleListResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_rule_list_with_options(request, runtime)

    async def describe_metric_rule_list_async(
        self,
        request: main_models.DescribeMetricRuleListRequest,
    ) -> main_models.DescribeMetricRuleListResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_rule_list_with_options_async(request, runtime)

    def describe_metric_rule_targets_with_options(
        self,
        request: main_models.DescribeMetricRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_targets_with_options_async(
        self,
        request: main_models.DescribeMetricRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_targets(
        self,
        request: main_models.DescribeMetricRuleTargetsRequest,
    ) -> main_models.DescribeMetricRuleTargetsResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_rule_targets_with_options(request, runtime)

    async def describe_metric_rule_targets_async(
        self,
        request: main_models.DescribeMetricRuleTargetsRequest,
    ) -> main_models.DescribeMetricRuleTargetsResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_rule_targets_with_options_async(request, runtime)

    def describe_metric_rule_template_attribute_with_options(
        self,
        request: main_models.DescribeMetricRuleTemplateAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleTemplateAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleTemplateAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleTemplateAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_template_attribute_with_options_async(
        self,
        request: main_models.DescribeMetricRuleTemplateAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleTemplateAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleTemplateAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleTemplateAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_template_attribute(
        self,
        request: main_models.DescribeMetricRuleTemplateAttributeRequest,
    ) -> main_models.DescribeMetricRuleTemplateAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_rule_template_attribute_with_options(request, runtime)

    async def describe_metric_rule_template_attribute_async(
        self,
        request: main_models.DescribeMetricRuleTemplateAttributeRequest,
    ) -> main_models.DescribeMetricRuleTemplateAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_rule_template_attribute_with_options_async(request, runtime)

    def describe_metric_rule_template_list_with_options(
        self,
        request: main_models.DescribeMetricRuleTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.history):
            query['History'] = request.history
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleTemplateList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleTemplateListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_rule_template_list_with_options_async(
        self,
        request: main_models.DescribeMetricRuleTemplateListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricRuleTemplateListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.history):
            query['History'] = request.history
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.order_by):
            query['OrderBy'] = request.order_by
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricRuleTemplateList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricRuleTemplateListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_rule_template_list(
        self,
        request: main_models.DescribeMetricRuleTemplateListRequest,
    ) -> main_models.DescribeMetricRuleTemplateListResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_rule_template_list_with_options(request, runtime)

    async def describe_metric_rule_template_list_async(
        self,
        request: main_models.DescribeMetricRuleTemplateListRequest,
    ) -> main_models.DescribeMetricRuleTemplateListResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_rule_template_list_with_options_async(request, runtime)

    def describe_metric_top_with_options(
        self,
        request: main_models.DescribeMetricTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricTopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.express):
            query['Express'] = request.express
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.order_desc):
            query['OrderDesc'] = request.order_desc
        if not DaraCore.is_null(request.orderby):
            query['Orderby'] = request.orderby
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricTop',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricTopResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_metric_top_with_options_async(
        self,
        request: main_models.DescribeMetricTopRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMetricTopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.express):
            query['Express'] = request.express
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.order_desc):
            query['OrderDesc'] = request.order_desc
        if not DaraCore.is_null(request.orderby):
            query['Orderby'] = request.orderby
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMetricTop',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMetricTopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_metric_top(
        self,
        request: main_models.DescribeMetricTopRequest,
    ) -> main_models.DescribeMetricTopResponse:
        runtime = RuntimeOptions()
        return self.describe_metric_top_with_options(request, runtime)

    async def describe_metric_top_async(
        self,
        request: main_models.DescribeMetricTopRequest,
    ) -> main_models.DescribeMetricTopResponse:
        runtime = RuntimeOptions()
        return await self.describe_metric_top_with_options_async(request, runtime)

    def describe_monitor_group_categories_with_options(
        self,
        request: main_models.DescribeMonitorGroupCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupCategories',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_categories_with_options_async(
        self,
        request: main_models.DescribeMonitorGroupCategoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupCategoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupCategories',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_categories(
        self,
        request: main_models.DescribeMonitorGroupCategoriesRequest,
    ) -> main_models.DescribeMonitorGroupCategoriesResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_group_categories_with_options(request, runtime)

    async def describe_monitor_group_categories_async(
        self,
        request: main_models.DescribeMonitorGroupCategoriesRequest,
    ) -> main_models.DescribeMonitorGroupCategoriesResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_group_categories_with_options_async(request, runtime)

    def describe_monitor_group_dynamic_rules_with_options(
        self,
        request: main_models.DescribeMonitorGroupDynamicRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupDynamicRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupDynamicRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupDynamicRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_dynamic_rules_with_options_async(
        self,
        request: main_models.DescribeMonitorGroupDynamicRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupDynamicRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupDynamicRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupDynamicRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_dynamic_rules(
        self,
        request: main_models.DescribeMonitorGroupDynamicRulesRequest,
    ) -> main_models.DescribeMonitorGroupDynamicRulesResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_group_dynamic_rules_with_options(request, runtime)

    async def describe_monitor_group_dynamic_rules_async(
        self,
        request: main_models.DescribeMonitorGroupDynamicRulesRequest,
    ) -> main_models.DescribeMonitorGroupDynamicRulesResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_group_dynamic_rules_with_options_async(request, runtime)

    def describe_monitor_group_instance_attribute_with_options(
        self,
        request: main_models.DescribeMonitorGroupInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.total):
            query['Total'] = request.total
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupInstanceAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_instance_attribute_with_options_async(
        self,
        request: main_models.DescribeMonitorGroupInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupInstanceAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.total):
            query['Total'] = request.total
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupInstanceAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_instance_attribute(
        self,
        request: main_models.DescribeMonitorGroupInstanceAttributeRequest,
    ) -> main_models.DescribeMonitorGroupInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_group_instance_attribute_with_options(request, runtime)

    async def describe_monitor_group_instance_attribute_async(
        self,
        request: main_models.DescribeMonitorGroupInstanceAttributeRequest,
    ) -> main_models.DescribeMonitorGroupInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_group_instance_attribute_with_options_async(request, runtime)

    def describe_monitor_group_instances_with_options(
        self,
        request: main_models.DescribeMonitorGroupInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_instances_with_options_async(
        self,
        request: main_models.DescribeMonitorGroupInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_instances(
        self,
        request: main_models.DescribeMonitorGroupInstancesRequest,
    ) -> main_models.DescribeMonitorGroupInstancesResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_group_instances_with_options(request, runtime)

    async def describe_monitor_group_instances_async(
        self,
        request: main_models.DescribeMonitorGroupInstancesRequest,
    ) -> main_models.DescribeMonitorGroupInstancesResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_group_instances_with_options_async(request, runtime)

    def describe_monitor_group_notify_policy_list_with_options(
        self,
        request: main_models.DescribeMonitorGroupNotifyPolicyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupNotifyPolicyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupNotifyPolicyList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupNotifyPolicyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_group_notify_policy_list_with_options_async(
        self,
        request: main_models.DescribeMonitorGroupNotifyPolicyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupNotifyPolicyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroupNotifyPolicyList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupNotifyPolicyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_group_notify_policy_list(
        self,
        request: main_models.DescribeMonitorGroupNotifyPolicyListRequest,
    ) -> main_models.DescribeMonitorGroupNotifyPolicyListResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_group_notify_policy_list_with_options(request, runtime)

    async def describe_monitor_group_notify_policy_list_async(
        self,
        request: main_models.DescribeMonitorGroupNotifyPolicyListRequest,
    ) -> main_models.DescribeMonitorGroupNotifyPolicyListResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_group_notify_policy_list_with_options_async(request, runtime)

    def describe_monitor_groups_with_options(
        self,
        request: main_models.DescribeMonitorGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not DaraCore.is_null(request.group_founder_tag_key):
            query['GroupFounderTagKey'] = request.group_founder_tag_key
        if not DaraCore.is_null(request.group_founder_tag_value):
            query['GroupFounderTagValue'] = request.group_founder_tag_value
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.include_template_history):
            query['IncludeTemplateHistory'] = request.include_template_history
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.select_contact_groups):
            query['SelectContactGroups'] = request.select_contact_groups
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroups',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_groups_with_options_async(
        self,
        request: main_models.DescribeMonitorGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dynamic_tag_rule_id):
            query['DynamicTagRuleId'] = request.dynamic_tag_rule_id
        if not DaraCore.is_null(request.group_founder_tag_key):
            query['GroupFounderTagKey'] = request.group_founder_tag_key
        if not DaraCore.is_null(request.group_founder_tag_value):
            query['GroupFounderTagValue'] = request.group_founder_tag_value
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        if not DaraCore.is_null(request.include_template_history):
            query['IncludeTemplateHistory'] = request.include_template_history
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.select_contact_groups):
            query['SelectContactGroups'] = request.select_contact_groups
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.types):
            query['Types'] = request.types
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorGroups',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_groups(
        self,
        request: main_models.DescribeMonitorGroupsRequest,
    ) -> main_models.DescribeMonitorGroupsResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_groups_with_options(request, runtime)

    async def describe_monitor_groups_async(
        self,
        request: main_models.DescribeMonitorGroupsRequest,
    ) -> main_models.DescribeMonitorGroupsResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_groups_with_options_async(request, runtime)

    def describe_monitor_resource_quota_attribute_with_options(
        self,
        request: main_models.DescribeMonitorResourceQuotaAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorResourceQuotaAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.show_used):
            query['ShowUsed'] = request.show_used
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorResourceQuotaAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorResourceQuotaAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitor_resource_quota_attribute_with_options_async(
        self,
        request: main_models.DescribeMonitorResourceQuotaAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitorResourceQuotaAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.show_used):
            query['ShowUsed'] = request.show_used
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitorResourceQuotaAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitorResourceQuotaAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitor_resource_quota_attribute(
        self,
        request: main_models.DescribeMonitorResourceQuotaAttributeRequest,
    ) -> main_models.DescribeMonitorResourceQuotaAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_monitor_resource_quota_attribute_with_options(request, runtime)

    async def describe_monitor_resource_quota_attribute_async(
        self,
        request: main_models.DescribeMonitorResourceQuotaAttributeRequest,
    ) -> main_models.DescribeMonitorResourceQuotaAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitor_resource_quota_attribute_with_options_async(request, runtime)

    def describe_monitoring_agent_access_key_with_options(
        self,
        request: main_models.DescribeMonitoringAgentAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentAccessKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentAccessKey',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentAccessKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_access_key_with_options_async(
        self,
        request: main_models.DescribeMonitoringAgentAccessKeyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentAccessKeyResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentAccessKey',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentAccessKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_access_key(
        self,
        request: main_models.DescribeMonitoringAgentAccessKeyRequest,
    ) -> main_models.DescribeMonitoringAgentAccessKeyResponse:
        runtime = RuntimeOptions()
        return self.describe_monitoring_agent_access_key_with_options(request, runtime)

    async def describe_monitoring_agent_access_key_async(
        self,
        request: main_models.DescribeMonitoringAgentAccessKeyRequest,
    ) -> main_models.DescribeMonitoringAgentAccessKeyResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitoring_agent_access_key_with_options_async(request, runtime)

    def describe_monitoring_agent_config_with_options(
        self,
        request: main_models.DescribeMonitoringAgentConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_config_with_options_async(
        self,
        request: main_models.DescribeMonitoringAgentConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_config(
        self,
        request: main_models.DescribeMonitoringAgentConfigRequest,
    ) -> main_models.DescribeMonitoringAgentConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_monitoring_agent_config_with_options(request, runtime)

    async def describe_monitoring_agent_config_async(
        self,
        request: main_models.DescribeMonitoringAgentConfigRequest,
    ) -> main_models.DescribeMonitoringAgentConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitoring_agent_config_with_options_async(request, runtime)

    def describe_monitoring_agent_hosts_with_options(
        self,
        request: main_models.DescribeMonitoringAgentHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentHostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_host):
            query['AliyunHost'] = request.aliyun_host
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sysom_status):
            query['SysomStatus'] = request.sysom_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentHosts',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentHostsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_hosts_with_options_async(
        self,
        request: main_models.DescribeMonitoringAgentHostsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentHostsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aliyun_host):
            query['AliyunHost'] = request.aliyun_host
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not DaraCore.is_null(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not DaraCore.is_null(request.key_word):
            query['KeyWord'] = request.key_word
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.sysom_status):
            query['SysomStatus'] = request.sysom_status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentHosts',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentHostsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_hosts(
        self,
        request: main_models.DescribeMonitoringAgentHostsRequest,
    ) -> main_models.DescribeMonitoringAgentHostsResponse:
        runtime = RuntimeOptions()
        return self.describe_monitoring_agent_hosts_with_options(request, runtime)

    async def describe_monitoring_agent_hosts_async(
        self,
        request: main_models.DescribeMonitoringAgentHostsRequest,
    ) -> main_models.DescribeMonitoringAgentHostsResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitoring_agent_hosts_with_options_async(request, runtime)

    def describe_monitoring_agent_processes_with_options(
        self,
        request: main_models.DescribeMonitoringAgentProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentProcessesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentProcesses',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentProcessesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_processes_with_options_async(
        self,
        request: main_models.DescribeMonitoringAgentProcessesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentProcessesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentProcesses',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentProcessesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_processes(
        self,
        request: main_models.DescribeMonitoringAgentProcessesRequest,
    ) -> main_models.DescribeMonitoringAgentProcessesResponse:
        runtime = RuntimeOptions()
        return self.describe_monitoring_agent_processes_with_options(request, runtime)

    async def describe_monitoring_agent_processes_async(
        self,
        request: main_models.DescribeMonitoringAgentProcessesRequest,
    ) -> main_models.DescribeMonitoringAgentProcessesResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitoring_agent_processes_with_options_async(request, runtime)

    def describe_monitoring_agent_statuses_with_options(
        self,
        request: main_models.DescribeMonitoringAgentStatusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentStatusesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_availability_task_id):
            query['HostAvailabilityTaskId'] = request.host_availability_task_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentStatuses',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentStatusesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_agent_statuses_with_options_async(
        self,
        request: main_models.DescribeMonitoringAgentStatusesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringAgentStatusesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_availability_task_id):
            query['HostAvailabilityTaskId'] = request.host_availability_task_id
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringAgentStatuses',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringAgentStatusesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_agent_statuses(
        self,
        request: main_models.DescribeMonitoringAgentStatusesRequest,
    ) -> main_models.DescribeMonitoringAgentStatusesResponse:
        runtime = RuntimeOptions()
        return self.describe_monitoring_agent_statuses_with_options(request, runtime)

    async def describe_monitoring_agent_statuses_async(
        self,
        request: main_models.DescribeMonitoringAgentStatusesRequest,
    ) -> main_models.DescribeMonitoringAgentStatusesResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitoring_agent_statuses_with_options_async(request, runtime)

    def describe_monitoring_config_with_options(
        self,
        request: main_models.DescribeMonitoringConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_monitoring_config_with_options_async(
        self,
        request: main_models.DescribeMonitoringConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeMonitoringConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeMonitoringConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeMonitoringConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_monitoring_config(
        self,
        request: main_models.DescribeMonitoringConfigRequest,
    ) -> main_models.DescribeMonitoringConfigResponse:
        runtime = RuntimeOptions()
        return self.describe_monitoring_config_with_options(request, runtime)

    async def describe_monitoring_config_async(
        self,
        request: main_models.DescribeMonitoringConfigRequest,
    ) -> main_models.DescribeMonitoringConfigResponse:
        runtime = RuntimeOptions()
        return await self.describe_monitoring_config_with_options_async(request, runtime)

    def describe_product_resource_tag_key_list_with_options(
        self,
        request: main_models.DescribeProductResourceTagKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductResourceTagKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductResourceTagKeyList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductResourceTagKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_product_resource_tag_key_list_with_options_async(
        self,
        request: main_models.DescribeProductResourceTagKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductResourceTagKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProductResourceTagKeyList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductResourceTagKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_product_resource_tag_key_list(
        self,
        request: main_models.DescribeProductResourceTagKeyListRequest,
    ) -> main_models.DescribeProductResourceTagKeyListResponse:
        runtime = RuntimeOptions()
        return self.describe_product_resource_tag_key_list_with_options(request, runtime)

    async def describe_product_resource_tag_key_list_async(
        self,
        request: main_models.DescribeProductResourceTagKeyListRequest,
    ) -> main_models.DescribeProductResourceTagKeyListResponse:
        runtime = RuntimeOptions()
        return await self.describe_product_resource_tag_key_list_with_options_async(request, runtime)

    def describe_products_of_active_metric_rule_with_options(
        self,
        request: main_models.DescribeProductsOfActiveMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductsOfActiveMetricRuleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeProductsOfActiveMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductsOfActiveMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_products_of_active_metric_rule_with_options_async(
        self,
        request: main_models.DescribeProductsOfActiveMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProductsOfActiveMetricRuleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeProductsOfActiveMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProductsOfActiveMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_products_of_active_metric_rule(
        self,
        request: main_models.DescribeProductsOfActiveMetricRuleRequest,
    ) -> main_models.DescribeProductsOfActiveMetricRuleResponse:
        runtime = RuntimeOptions()
        return self.describe_products_of_active_metric_rule_with_options(request, runtime)

    async def describe_products_of_active_metric_rule_async(
        self,
        request: main_models.DescribeProductsOfActiveMetricRuleRequest,
    ) -> main_models.DescribeProductsOfActiveMetricRuleResponse:
        runtime = RuntimeOptions()
        return await self.describe_products_of_active_metric_rule_with_options_async(request, runtime)

    def describe_project_meta_with_options(
        self,
        request: main_models.DescribeProjectMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectMeta',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_project_meta_with_options_async(
        self,
        request: main_models.DescribeProjectMetaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeProjectMetaResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeProjectMeta',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeProjectMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_project_meta(
        self,
        request: main_models.DescribeProjectMetaRequest,
    ) -> main_models.DescribeProjectMetaResponse:
        runtime = RuntimeOptions()
        return self.describe_project_meta_with_options(request, runtime)

    async def describe_project_meta_async(
        self,
        request: main_models.DescribeProjectMetaRequest,
    ) -> main_models.DescribeProjectMetaResponse:
        runtime = RuntimeOptions()
        return await self.describe_project_meta_with_options_async(request, runtime)

    def describe_site_monitor_attribute_with_options(
        self,
        request: main_models.DescribeSiteMonitorAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_alert):
            query['IncludeAlert'] = request.include_alert
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_attribute_with_options_async(
        self,
        request: main_models.DescribeSiteMonitorAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.include_alert):
            query['IncludeAlert'] = request.include_alert
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_attribute(
        self,
        request: main_models.DescribeSiteMonitorAttributeRequest,
    ) -> main_models.DescribeSiteMonitorAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_site_monitor_attribute_with_options(request, runtime)

    async def describe_site_monitor_attribute_async(
        self,
        request: main_models.DescribeSiteMonitorAttributeRequest,
    ) -> main_models.DescribeSiteMonitorAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_site_monitor_attribute_with_options_async(request, runtime)

    def describe_site_monitor_data_with_options(
        self,
        request: main_models.DescribeSiteMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorData',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_data_with_options_async(
        self,
        request: main_models.DescribeSiteMonitorDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorData',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_data(
        self,
        request: main_models.DescribeSiteMonitorDataRequest,
    ) -> main_models.DescribeSiteMonitorDataResponse:
        runtime = RuntimeOptions()
        return self.describe_site_monitor_data_with_options(request, runtime)

    async def describe_site_monitor_data_async(
        self,
        request: main_models.DescribeSiteMonitorDataRequest,
    ) -> main_models.DescribeSiteMonitorDataResponse:
        runtime = RuntimeOptions()
        return await self.describe_site_monitor_data_with_options_async(request, runtime)

    def describe_site_monitor_ispcity_list_with_options(
        self,
        request: main_models.DescribeSiteMonitorISPCityListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorISPCityListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.ipv4):
            query['IPV4'] = request.ipv4
        if not DaraCore.is_null(request.ipv6):
            query['IPV6'] = request.ipv6
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.view_all):
            query['ViewAll'] = request.view_all
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorISPCityList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorISPCityListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_ispcity_list_with_options_async(
        self,
        request: main_models.DescribeSiteMonitorISPCityListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorISPCityListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.ipv4):
            query['IPV4'] = request.ipv4
        if not DaraCore.is_null(request.ipv6):
            query['IPV6'] = request.ipv6
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.view_all):
            query['ViewAll'] = request.view_all
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorISPCityList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorISPCityListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_ispcity_list(
        self,
        request: main_models.DescribeSiteMonitorISPCityListRequest,
    ) -> main_models.DescribeSiteMonitorISPCityListResponse:
        runtime = RuntimeOptions()
        return self.describe_site_monitor_ispcity_list_with_options(request, runtime)

    async def describe_site_monitor_ispcity_list_async(
        self,
        request: main_models.DescribeSiteMonitorISPCityListRequest,
    ) -> main_models.DescribeSiteMonitorISPCityListResponse:
        runtime = RuntimeOptions()
        return await self.describe_site_monitor_ispcity_list_with_options_async(request, runtime)

    def describe_site_monitor_list_with_options(
        self,
        request: main_models.DescribeSiteMonitorListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_group):
            query['AgentGroup'] = request.agent_group
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_state):
            query['TaskState'] = request.task_state
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_list_with_options_async(
        self,
        request: main_models.DescribeSiteMonitorListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.agent_group):
            query['AgentGroup'] = request.agent_group
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page):
            query['Page'] = request.page
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_state):
            query['TaskState'] = request.task_state
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_list(
        self,
        request: main_models.DescribeSiteMonitorListRequest,
    ) -> main_models.DescribeSiteMonitorListResponse:
        runtime = RuntimeOptions()
        return self.describe_site_monitor_list_with_options(request, runtime)

    async def describe_site_monitor_list_async(
        self,
        request: main_models.DescribeSiteMonitorListRequest,
    ) -> main_models.DescribeSiteMonitorListResponse:
        runtime = RuntimeOptions()
        return await self.describe_site_monitor_list_with_options_async(request, runtime)

    def describe_site_monitor_log_with_options(
        self,
        request: main_models.DescribeSiteMonitorLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.browser):
            query['Browser'] = request.browser
        if not DaraCore.is_null(request.browser_info):
            query['BrowserInfo'] = request.browser_info
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.device):
            query['Device'] = request.device
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorLog',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_log_with_options_async(
        self,
        request: main_models.DescribeSiteMonitorLogRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorLogResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.browser):
            query['Browser'] = request.browser
        if not DaraCore.is_null(request.browser_info):
            query['BrowserInfo'] = request.browser_info
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.device):
            query['Device'] = request.device
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.length):
            query['Length'] = request.length
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorLog',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_log(
        self,
        request: main_models.DescribeSiteMonitorLogRequest,
    ) -> main_models.DescribeSiteMonitorLogResponse:
        runtime = RuntimeOptions()
        return self.describe_site_monitor_log_with_options(request, runtime)

    async def describe_site_monitor_log_async(
        self,
        request: main_models.DescribeSiteMonitorLogRequest,
    ) -> main_models.DescribeSiteMonitorLogResponse:
        runtime = RuntimeOptions()
        return await self.describe_site_monitor_log_with_options_async(request, runtime)

    def describe_site_monitor_quota_with_options(
        self,
        request: main_models.DescribeSiteMonitorQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorQuotaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorQuota',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorQuotaResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_quota_with_options_async(
        self,
        request: main_models.DescribeSiteMonitorQuotaRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorQuotaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorQuota',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorQuotaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_quota(
        self,
        request: main_models.DescribeSiteMonitorQuotaRequest,
    ) -> main_models.DescribeSiteMonitorQuotaResponse:
        runtime = RuntimeOptions()
        return self.describe_site_monitor_quota_with_options(request, runtime)

    async def describe_site_monitor_quota_async(
        self,
        request: main_models.DescribeSiteMonitorQuotaRequest,
    ) -> main_models.DescribeSiteMonitorQuotaResponse:
        runtime = RuntimeOptions()
        return await self.describe_site_monitor_quota_with_options_async(request, runtime)

    def describe_site_monitor_statistics_with_options(
        self,
        request: main_models.DescribeSiteMonitorStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorStatistics',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_site_monitor_statistics_with_options_async(
        self,
        request: main_models.DescribeSiteMonitorStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSiteMonitorStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.time_range):
            query['TimeRange'] = request.time_range
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSiteMonitorStatistics',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSiteMonitorStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_site_monitor_statistics(
        self,
        request: main_models.DescribeSiteMonitorStatisticsRequest,
    ) -> main_models.DescribeSiteMonitorStatisticsResponse:
        runtime = RuntimeOptions()
        return self.describe_site_monitor_statistics_with_options(request, runtime)

    async def describe_site_monitor_statistics_async(
        self,
        request: main_models.DescribeSiteMonitorStatisticsRequest,
    ) -> main_models.DescribeSiteMonitorStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.describe_site_monitor_statistics_with_options_async(request, runtime)

    def describe_synthetic_probe_list_with_options(
        self,
        request: main_models.DescribeSyntheticProbeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyntheticProbeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.idc_probe):
            query['IdcProbe'] = request.idc_probe
        if not DaraCore.is_null(request.ipv_4):
            query['Ipv4'] = request.ipv_4
        if not DaraCore.is_null(request.ipv_6):
            query['Ipv6'] = request.ipv_6
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lm_probe):
            query['LmProbe'] = request.lm_probe
        if not DaraCore.is_null(request.mb_probe):
            query['MbProbe'] = request.mb_probe
        if not DaraCore.is_null(request.view_all):
            query['ViewAll'] = request.view_all
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyntheticProbeList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyntheticProbeListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_synthetic_probe_list_with_options_async(
        self,
        request: main_models.DescribeSyntheticProbeListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSyntheticProbeListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.city):
            query['City'] = request.city
        if not DaraCore.is_null(request.idc_probe):
            query['IdcProbe'] = request.idc_probe
        if not DaraCore.is_null(request.ipv_4):
            query['Ipv4'] = request.ipv_4
        if not DaraCore.is_null(request.ipv_6):
            query['Ipv6'] = request.ipv_6
        if not DaraCore.is_null(request.isp):
            query['Isp'] = request.isp
        if not DaraCore.is_null(request.lm_probe):
            query['LmProbe'] = request.lm_probe
        if not DaraCore.is_null(request.mb_probe):
            query['MbProbe'] = request.mb_probe
        if not DaraCore.is_null(request.view_all):
            query['ViewAll'] = request.view_all
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSyntheticProbeList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSyntheticProbeListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_synthetic_probe_list(
        self,
        request: main_models.DescribeSyntheticProbeListRequest,
    ) -> main_models.DescribeSyntheticProbeListResponse:
        runtime = RuntimeOptions()
        return self.describe_synthetic_probe_list_with_options(request, runtime)

    async def describe_synthetic_probe_list_async(
        self,
        request: main_models.DescribeSyntheticProbeListRequest,
    ) -> main_models.DescribeSyntheticProbeListResponse:
        runtime = RuntimeOptions()
        return await self.describe_synthetic_probe_list_with_options_async(request, runtime)

    def describe_system_event_attribute_with_options(
        self,
        request: main_models.DescribeSystemEventAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemEventAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemEventAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemEventAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_event_attribute_with_options_async(
        self,
        request: main_models.DescribeSystemEventAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemEventAttributeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemEventAttribute',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemEventAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_event_attribute(
        self,
        request: main_models.DescribeSystemEventAttributeRequest,
    ) -> main_models.DescribeSystemEventAttributeResponse:
        runtime = RuntimeOptions()
        return self.describe_system_event_attribute_with_options(request, runtime)

    async def describe_system_event_attribute_async(
        self,
        request: main_models.DescribeSystemEventAttributeRequest,
    ) -> main_models.DescribeSystemEventAttributeResponse:
        runtime = RuntimeOptions()
        return await self.describe_system_event_attribute_with_options_async(request, runtime)

    def describe_system_event_count_with_options(
        self,
        request: main_models.DescribeSystemEventCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemEventCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemEventCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemEventCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_event_count_with_options_async(
        self,
        request: main_models.DescribeSystemEventCountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemEventCountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemEventCount',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemEventCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_event_count(
        self,
        request: main_models.DescribeSystemEventCountRequest,
    ) -> main_models.DescribeSystemEventCountResponse:
        runtime = RuntimeOptions()
        return self.describe_system_event_count_with_options(request, runtime)

    async def describe_system_event_count_async(
        self,
        request: main_models.DescribeSystemEventCountRequest,
    ) -> main_models.DescribeSystemEventCountResponse:
        runtime = RuntimeOptions()
        return await self.describe_system_event_count_with_options_async(request, runtime)

    def describe_system_event_histogram_with_options(
        self,
        request: main_models.DescribeSystemEventHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemEventHistogramResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemEventHistogram',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemEventHistogramResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_event_histogram_with_options_async(
        self,
        request: main_models.DescribeSystemEventHistogramRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemEventHistogramResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        if not DaraCore.is_null(request.search_keywords):
            query['SearchKeywords'] = request.search_keywords
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeSystemEventHistogram',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemEventHistogramResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_event_histogram(
        self,
        request: main_models.DescribeSystemEventHistogramRequest,
    ) -> main_models.DescribeSystemEventHistogramResponse:
        runtime = RuntimeOptions()
        return self.describe_system_event_histogram_with_options(request, runtime)

    async def describe_system_event_histogram_async(
        self,
        request: main_models.DescribeSystemEventHistogramRequest,
    ) -> main_models.DescribeSystemEventHistogramResponse:
        runtime = RuntimeOptions()
        return await self.describe_system_event_histogram_with_options_async(request, runtime)

    def describe_system_event_meta_list_with_options(
        self,
        request: main_models.DescribeSystemEventMetaListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemEventMetaListResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSystemEventMetaList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemEventMetaListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_system_event_meta_list_with_options_async(
        self,
        request: main_models.DescribeSystemEventMetaListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeSystemEventMetaListResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DescribeSystemEventMetaList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeSystemEventMetaListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_system_event_meta_list(
        self,
        request: main_models.DescribeSystemEventMetaListRequest,
    ) -> main_models.DescribeSystemEventMetaListResponse:
        runtime = RuntimeOptions()
        return self.describe_system_event_meta_list_with_options(request, runtime)

    async def describe_system_event_meta_list_async(
        self,
        request: main_models.DescribeSystemEventMetaListRequest,
    ) -> main_models.DescribeSystemEventMetaListResponse:
        runtime = RuntimeOptions()
        return await self.describe_system_event_meta_list_with_options_async(request, runtime)

    def describe_tag_key_list_with_options(
        self,
        request: main_models.DescribeTagKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagKeyList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagKeyListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_key_list_with_options_async(
        self,
        request: main_models.DescribeTagKeyListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagKeyListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagKeyList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagKeyListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_key_list(
        self,
        request: main_models.DescribeTagKeyListRequest,
    ) -> main_models.DescribeTagKeyListResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_key_list_with_options(request, runtime)

    async def describe_tag_key_list_async(
        self,
        request: main_models.DescribeTagKeyListRequest,
    ) -> main_models.DescribeTagKeyListResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_key_list_with_options_async(request, runtime)

    def describe_tag_value_list_with_options(
        self,
        request: main_models.DescribeTagValueListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagValueListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagValueList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagValueListResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_tag_value_list_with_options_async(
        self,
        request: main_models.DescribeTagValueListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeTagValueListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeTagValueList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeTagValueListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_tag_value_list(
        self,
        request: main_models.DescribeTagValueListRequest,
    ) -> main_models.DescribeTagValueListResponse:
        runtime = RuntimeOptions()
        return self.describe_tag_value_list_with_options(request, runtime)

    async def describe_tag_value_list_async(
        self,
        request: main_models.DescribeTagValueListRequest,
    ) -> main_models.DescribeTagValueListResponse:
        runtime = RuntimeOptions()
        return await self.describe_tag_value_list_with_options_async(request, runtime)

    def describe_unhealthy_host_availability_with_options(
        self,
        request: main_models.DescribeUnhealthyHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnhealthyHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnhealthyHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnhealthyHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_unhealthy_host_availability_with_options_async(
        self,
        request: main_models.DescribeUnhealthyHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeUnhealthyHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeUnhealthyHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeUnhealthyHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_unhealthy_host_availability(
        self,
        request: main_models.DescribeUnhealthyHostAvailabilityRequest,
    ) -> main_models.DescribeUnhealthyHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return self.describe_unhealthy_host_availability_with_options(request, runtime)

    async def describe_unhealthy_host_availability_async(
        self,
        request: main_models.DescribeUnhealthyHostAvailabilityRequest,
    ) -> main_models.DescribeUnhealthyHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return await self.describe_unhealthy_host_availability_with_options_async(request, runtime)

    def disable_active_metric_rule_with_options(
        self,
        request: main_models.DisableActiveMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableActiveMetricRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableActiveMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableActiveMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_active_metric_rule_with_options_async(
        self,
        request: main_models.DisableActiveMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableActiveMetricRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableActiveMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableActiveMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_active_metric_rule(
        self,
        request: main_models.DisableActiveMetricRuleRequest,
    ) -> main_models.DisableActiveMetricRuleResponse:
        runtime = RuntimeOptions()
        return self.disable_active_metric_rule_with_options(request, runtime)

    async def disable_active_metric_rule_async(
        self,
        request: main_models.DisableActiveMetricRuleRequest,
    ) -> main_models.DisableActiveMetricRuleResponse:
        runtime = RuntimeOptions()
        return await self.disable_active_metric_rule_with_options_async(request, runtime)

    def disable_event_rules_with_options(
        self,
        request: main_models.DisableEventRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableEventRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableEventRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_event_rules_with_options_async(
        self,
        request: main_models.DisableEventRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableEventRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableEventRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableEventRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_event_rules(
        self,
        request: main_models.DisableEventRulesRequest,
    ) -> main_models.DisableEventRulesResponse:
        runtime = RuntimeOptions()
        return self.disable_event_rules_with_options(request, runtime)

    async def disable_event_rules_async(
        self,
        request: main_models.DisableEventRulesRequest,
    ) -> main_models.DisableEventRulesResponse:
        runtime = RuntimeOptions()
        return await self.disable_event_rules_with_options_async(request, runtime)

    def disable_host_availability_with_options(
        self,
        request: main_models.DisableHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_host_availability_with_options_async(
        self,
        request: main_models.DisableHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_host_availability(
        self,
        request: main_models.DisableHostAvailabilityRequest,
    ) -> main_models.DisableHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return self.disable_host_availability_with_options(request, runtime)

    async def disable_host_availability_async(
        self,
        request: main_models.DisableHostAvailabilityRequest,
    ) -> main_models.DisableHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return await self.disable_host_availability_with_options_async(request, runtime)

    def disable_metric_rules_with_options(
        self,
        request: main_models.DisableMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_metric_rules_with_options_async(
        self,
        request: main_models.DisableMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_metric_rules(
        self,
        request: main_models.DisableMetricRulesRequest,
    ) -> main_models.DisableMetricRulesResponse:
        runtime = RuntimeOptions()
        return self.disable_metric_rules_with_options(request, runtime)

    async def disable_metric_rules_async(
        self,
        request: main_models.DisableMetricRulesRequest,
    ) -> main_models.DisableMetricRulesResponse:
        runtime = RuntimeOptions()
        return await self.disable_metric_rules_with_options_async(request, runtime)

    def disable_site_monitors_with_options(
        self,
        request: main_models.DisableSiteMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSiteMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSiteMonitors',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSiteMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_site_monitors_with_options_async(
        self,
        request: main_models.DisableSiteMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisableSiteMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DisableSiteMonitors',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableSiteMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_site_monitors(
        self,
        request: main_models.DisableSiteMonitorsRequest,
    ) -> main_models.DisableSiteMonitorsResponse:
        runtime = RuntimeOptions()
        return self.disable_site_monitors_with_options(request, runtime)

    async def disable_site_monitors_async(
        self,
        request: main_models.DisableSiteMonitorsRequest,
    ) -> main_models.DisableSiteMonitorsResponse:
        runtime = RuntimeOptions()
        return await self.disable_site_monitors_with_options_async(request, runtime)

    def enable_active_metric_rule_with_options(
        self,
        request: main_models.EnableActiveMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableActiveMetricRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableActiveMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableActiveMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_active_metric_rule_with_options_async(
        self,
        request: main_models.EnableActiveMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableActiveMetricRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableActiveMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableActiveMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_active_metric_rule(
        self,
        request: main_models.EnableActiveMetricRuleRequest,
    ) -> main_models.EnableActiveMetricRuleResponse:
        runtime = RuntimeOptions()
        return self.enable_active_metric_rule_with_options(request, runtime)

    async def enable_active_metric_rule_async(
        self,
        request: main_models.EnableActiveMetricRuleRequest,
    ) -> main_models.EnableActiveMetricRuleResponse:
        runtime = RuntimeOptions()
        return await self.enable_active_metric_rule_with_options_async(request, runtime)

    def enable_event_rules_with_options(
        self,
        request: main_models.EnableEventRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableEventRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableEventRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableEventRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_event_rules_with_options_async(
        self,
        request: main_models.EnableEventRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableEventRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_names):
            query['RuleNames'] = request.rule_names
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableEventRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableEventRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_event_rules(
        self,
        request: main_models.EnableEventRulesRequest,
    ) -> main_models.EnableEventRulesResponse:
        runtime = RuntimeOptions()
        return self.enable_event_rules_with_options(request, runtime)

    async def enable_event_rules_async(
        self,
        request: main_models.EnableEventRulesRequest,
    ) -> main_models.EnableEventRulesResponse:
        runtime = RuntimeOptions()
        return await self.enable_event_rules_with_options_async(request, runtime)

    def enable_host_availability_with_options(
        self,
        request: main_models.EnableHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_host_availability_with_options_async(
        self,
        request: main_models.EnableHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_host_availability(
        self,
        request: main_models.EnableHostAvailabilityRequest,
    ) -> main_models.EnableHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return self.enable_host_availability_with_options(request, runtime)

    async def enable_host_availability_async(
        self,
        request: main_models.EnableHostAvailabilityRequest,
    ) -> main_models.EnableHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return await self.enable_host_availability_with_options_async(request, runtime)

    def enable_metric_rule_black_list_with_options(
        self,
        request: main_models.EnableMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_metric_rule_black_list_with_options_async(
        self,
        request: main_models.EnableMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.is_enable):
            query['IsEnable'] = request.is_enable
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_metric_rule_black_list(
        self,
        request: main_models.EnableMetricRuleBlackListRequest,
    ) -> main_models.EnableMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return self.enable_metric_rule_black_list_with_options(request, runtime)

    async def enable_metric_rule_black_list_async(
        self,
        request: main_models.EnableMetricRuleBlackListRequest,
    ) -> main_models.EnableMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return await self.enable_metric_rule_black_list_with_options_async(request, runtime)

    def enable_metric_rules_with_options(
        self,
        request: main_models.EnableMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_metric_rules_with_options_async(
        self,
        request: main_models.EnableMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_metric_rules(
        self,
        request: main_models.EnableMetricRulesRequest,
    ) -> main_models.EnableMetricRulesResponse:
        runtime = RuntimeOptions()
        return self.enable_metric_rules_with_options(request, runtime)

    async def enable_metric_rules_async(
        self,
        request: main_models.EnableMetricRulesRequest,
    ) -> main_models.EnableMetricRulesResponse:
        runtime = RuntimeOptions()
        return await self.enable_metric_rules_with_options_async(request, runtime)

    def enable_site_monitors_with_options(
        self,
        request: main_models.EnableSiteMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSiteMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSiteMonitors',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSiteMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_site_monitors_with_options_async(
        self,
        request: main_models.EnableSiteMonitorsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableSiteMonitorsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableSiteMonitors',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableSiteMonitorsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_site_monitors(
        self,
        request: main_models.EnableSiteMonitorsRequest,
    ) -> main_models.EnableSiteMonitorsResponse:
        runtime = RuntimeOptions()
        return self.enable_site_monitors_with_options(request, runtime)

    async def enable_site_monitors_async(
        self,
        request: main_models.EnableSiteMonitorsRequest,
    ) -> main_models.EnableSiteMonitorsResponse:
        runtime = RuntimeOptions()
        return await self.enable_site_monitors_with_options_async(request, runtime)

    def install_monitoring_agent_with_options(
        self,
        request: main_models.InstallMonitoringAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallMonitoringAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.install_command):
            query['InstallCommand'] = request.install_command
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallMonitoringAgent',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallMonitoringAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def install_monitoring_agent_with_options_async(
        self,
        request: main_models.InstallMonitoringAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.InstallMonitoringAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.force):
            query['Force'] = request.force
        if not DaraCore.is_null(request.install_command):
            query['InstallCommand'] = request.install_command
        if not DaraCore.is_null(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'InstallMonitoringAgent',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.InstallMonitoringAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def install_monitoring_agent(
        self,
        request: main_models.InstallMonitoringAgentRequest,
    ) -> main_models.InstallMonitoringAgentResponse:
        runtime = RuntimeOptions()
        return self.install_monitoring_agent_with_options(request, runtime)

    async def install_monitoring_agent_async(
        self,
        request: main_models.InstallMonitoringAgentRequest,
    ) -> main_models.InstallMonitoringAgentResponse:
        runtime = RuntimeOptions()
        return await self.install_monitoring_agent_with_options_async(request, runtime)

    def modify_group_monitoring_agent_process_with_options(
        self,
        request: main_models.ModifyGroupMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGroupMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGroupMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGroupMonitoringAgentProcessResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_group_monitoring_agent_process_with_options_async(
        self,
        request: main_models.ModifyGroupMonitoringAgentProcessRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyGroupMonitoringAgentProcessResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.match_express_filter_relation):
            query['MatchExpressFilterRelation'] = request.match_express_filter_relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyGroupMonitoringAgentProcess',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyGroupMonitoringAgentProcessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_group_monitoring_agent_process(
        self,
        request: main_models.ModifyGroupMonitoringAgentProcessRequest,
    ) -> main_models.ModifyGroupMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return self.modify_group_monitoring_agent_process_with_options(request, runtime)

    async def modify_group_monitoring_agent_process_async(
        self,
        request: main_models.ModifyGroupMonitoringAgentProcessRequest,
    ) -> main_models.ModifyGroupMonitoringAgentProcessResponse:
        runtime = RuntimeOptions()
        return await self.modify_group_monitoring_agent_process_with_options_async(request, runtime)

    def modify_host_availability_with_options(
        self,
        request: main_models.ModifyHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not DaraCore.is_null(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostAvailabilityResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_availability_with_options_async(
        self,
        request: main_models.ModifyHostAvailabilityRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostAvailabilityResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_config_escalation_list):
            query['AlertConfigEscalationList'] = request.alert_config_escalation_list
        if not DaraCore.is_null(request.alert_config_target_list):
            query['AlertConfigTargetList'] = request.alert_config_target_list
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_list):
            query['InstanceList'] = request.instance_list
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_scope):
            query['TaskScope'] = request.task_scope
        if not DaraCore.is_null(request.alert_config):
            query['AlertConfig'] = request.alert_config
        if not DaraCore.is_null(request.task_option):
            query['TaskOption'] = request.task_option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostAvailability',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostAvailabilityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host_availability(
        self,
        request: main_models.ModifyHostAvailabilityRequest,
    ) -> main_models.ModifyHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return self.modify_host_availability_with_options(request, runtime)

    async def modify_host_availability_async(
        self,
        request: main_models.ModifyHostAvailabilityRequest,
    ) -> main_models.ModifyHostAvailabilityResponse:
        runtime = RuntimeOptions()
        return await self.modify_host_availability_with_options_async(request, runtime)

    def modify_host_info_with_options(
        self,
        request: main_models.ModifyHostInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostInfo',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_host_info_with_options_async(
        self,
        request: main_models.ModifyHostInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHostInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.host_name):
            query['HostName'] = request.host_name
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHostInfo',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHostInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_host_info(
        self,
        request: main_models.ModifyHostInfoRequest,
    ) -> main_models.ModifyHostInfoResponse:
        runtime = RuntimeOptions()
        return self.modify_host_info_with_options(request, runtime)

    async def modify_host_info_async(
        self,
        request: main_models.ModifyHostInfoRequest,
    ) -> main_models.ModifyHostInfoResponse:
        runtime = RuntimeOptions()
        return await self.modify_host_info_with_options_async(request, runtime)

    def modify_hybrid_monitor_namespace_with_options(
        self,
        request: main_models.ModifyHybridMonitorNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridMonitorNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridMonitorNamespace',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridMonitorNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_monitor_namespace_with_options_async(
        self,
        request: main_models.ModifyHybridMonitorNamespaceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridMonitorNamespaceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.spec):
            query['Spec'] = request.spec
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridMonitorNamespace',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridMonitorNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_monitor_namespace(
        self,
        request: main_models.ModifyHybridMonitorNamespaceRequest,
    ) -> main_models.ModifyHybridMonitorNamespaceResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_monitor_namespace_with_options(request, runtime)

    async def modify_hybrid_monitor_namespace_async(
        self,
        request: main_models.ModifyHybridMonitorNamespaceRequest,
    ) -> main_models.ModifyHybridMonitorNamespaceResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_monitor_namespace_with_options_async(request, runtime)

    def modify_hybrid_monitor_slsgroup_with_options(
        self,
        request: main_models.ModifyHybridMonitorSLSGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridMonitorSLSGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not DaraCore.is_null(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not DaraCore.is_null(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridMonitorSLSGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridMonitorSLSGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_monitor_slsgroup_with_options_async(
        self,
        request: main_models.ModifyHybridMonitorSLSGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridMonitorSLSGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.slsgroup_config):
            query['SLSGroupConfig'] = request.slsgroup_config
        if not DaraCore.is_null(request.slsgroup_description):
            query['SLSGroupDescription'] = request.slsgroup_description
        if not DaraCore.is_null(request.slsgroup_name):
            query['SLSGroupName'] = request.slsgroup_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridMonitorSLSGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridMonitorSLSGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_monitor_slsgroup(
        self,
        request: main_models.ModifyHybridMonitorSLSGroupRequest,
    ) -> main_models.ModifyHybridMonitorSLSGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_monitor_slsgroup_with_options(request, runtime)

    async def modify_hybrid_monitor_slsgroup_async(
        self,
        request: main_models.ModifyHybridMonitorSLSGroupRequest,
    ) -> main_models.ModifyHybridMonitorSLSGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_monitor_slsgroup_with_options_async(request, runtime)

    def modify_hybrid_monitor_task_with_options(
        self,
        request: main_models.ModifyHybridMonitorTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridMonitorTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not DaraCore.is_null(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridMonitorTask',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridMonitorTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_hybrid_monitor_task_with_options_async(
        self,
        request: main_models.ModifyHybridMonitorTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyHybridMonitorTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.attach_labels):
            query['AttachLabels'] = request.attach_labels
        if not DaraCore.is_null(request.collect_interval):
            query['CollectInterval'] = request.collect_interval
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.slsprocess_config):
            query['SLSProcessConfig'] = request.slsprocess_config
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyHybridMonitorTask',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyHybridMonitorTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_hybrid_monitor_task(
        self,
        request: main_models.ModifyHybridMonitorTaskRequest,
    ) -> main_models.ModifyHybridMonitorTaskResponse:
        runtime = RuntimeOptions()
        return self.modify_hybrid_monitor_task_with_options(request, runtime)

    async def modify_hybrid_monitor_task_async(
        self,
        request: main_models.ModifyHybridMonitorTaskRequest,
    ) -> main_models.ModifyHybridMonitorTaskResponse:
        runtime = RuntimeOptions()
        return await self.modify_hybrid_monitor_task_with_options_async(request, runtime)

    def modify_metric_rule_black_list_with_options(
        self,
        request: main_models.ModifyMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not DaraCore.is_null(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMetricRuleBlackListResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_metric_rule_black_list_with_options_async(
        self,
        request: main_models.ModifyMetricRuleBlackListRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMetricRuleBlackListResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not DaraCore.is_null(request.enable_end_time):
            query['EnableEndTime'] = request.enable_end_time
        if not DaraCore.is_null(request.enable_start_time):
            query['EnableStartTime'] = request.enable_start_time
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        if not DaraCore.is_null(request.metrics):
            query['Metrics'] = request.metrics
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not DaraCore.is_null(request.scope_value):
            query['ScopeValue'] = request.scope_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMetricRuleBlackList',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMetricRuleBlackListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_metric_rule_black_list(
        self,
        request: main_models.ModifyMetricRuleBlackListRequest,
    ) -> main_models.ModifyMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return self.modify_metric_rule_black_list_with_options(request, runtime)

    async def modify_metric_rule_black_list_async(
        self,
        request: main_models.ModifyMetricRuleBlackListRequest,
    ) -> main_models.ModifyMetricRuleBlackListResponse:
        runtime = RuntimeOptions()
        return await self.modify_metric_rule_black_list_with_options_async(request, runtime)

    def modify_metric_rule_template_with_options(
        self,
        request: main_models.ModifyMetricRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMetricRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.rest_version):
            query['RestVersion'] = request.rest_version
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMetricRuleTemplate',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMetricRuleTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_metric_rule_template_with_options_async(
        self,
        request: main_models.ModifyMetricRuleTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMetricRuleTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_templates):
            query['AlertTemplates'] = request.alert_templates
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.rest_version):
            query['RestVersion'] = request.rest_version
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMetricRuleTemplate',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMetricRuleTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_metric_rule_template(
        self,
        request: main_models.ModifyMetricRuleTemplateRequest,
    ) -> main_models.ModifyMetricRuleTemplateResponse:
        runtime = RuntimeOptions()
        return self.modify_metric_rule_template_with_options(request, runtime)

    async def modify_metric_rule_template_async(
        self,
        request: main_models.ModifyMetricRuleTemplateRequest,
    ) -> main_models.ModifyMetricRuleTemplateResponse:
        runtime = RuntimeOptions()
        return await self.modify_metric_rule_template_with_options_async(request, runtime)

    def modify_monitor_group_with_options(
        self,
        request: main_models.ModifyMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMonitorGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMonitorGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_monitor_group_with_options_async(
        self,
        request: main_models.ModifyMonitorGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMonitorGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_name):
            query['GroupName'] = request.group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMonitorGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMonitorGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_monitor_group(
        self,
        request: main_models.ModifyMonitorGroupRequest,
    ) -> main_models.ModifyMonitorGroupResponse:
        runtime = RuntimeOptions()
        return self.modify_monitor_group_with_options(request, runtime)

    async def modify_monitor_group_async(
        self,
        request: main_models.ModifyMonitorGroupRequest,
    ) -> main_models.ModifyMonitorGroupResponse:
        runtime = RuntimeOptions()
        return await self.modify_monitor_group_with_options_async(request, runtime)

    def modify_monitor_group_instances_with_options(
        self,
        request: main_models.ModifyMonitorGroupInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMonitorGroupInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMonitorGroupInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMonitorGroupInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_monitor_group_instances_with_options_async(
        self,
        request: main_models.ModifyMonitorGroupInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyMonitorGroupInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.instances):
            query['Instances'] = request.instances
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyMonitorGroupInstances',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyMonitorGroupInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_monitor_group_instances(
        self,
        request: main_models.ModifyMonitorGroupInstancesRequest,
    ) -> main_models.ModifyMonitorGroupInstancesResponse:
        runtime = RuntimeOptions()
        return self.modify_monitor_group_instances_with_options(request, runtime)

    async def modify_monitor_group_instances_async(
        self,
        request: main_models.ModifyMonitorGroupInstancesRequest,
    ) -> main_models.ModifyMonitorGroupInstancesResponse:
        runtime = RuntimeOptions()
        return await self.modify_monitor_group_instances_with_options_async(request, runtime)

    def modify_site_monitor_with_options(
        self,
        request: main_models.ModifySiteMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySiteMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not DaraCore.is_null(request.custom_schedule):
            query['CustomSchedule'] = request.custom_schedule
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.interval_unit):
            query['IntervalUnit'] = request.interval_unit
        if not DaraCore.is_null(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySiteMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySiteMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_site_monitor_with_options_async(
        self,
        request: main_models.ModifySiteMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifySiteMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.address):
            query['Address'] = request.address
        if not DaraCore.is_null(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not DaraCore.is_null(request.custom_schedule):
            query['CustomSchedule'] = request.custom_schedule
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.interval_unit):
            query['IntervalUnit'] = request.interval_unit
        if not DaraCore.is_null(request.isp_cities):
            query['IspCities'] = request.isp_cities
        if not DaraCore.is_null(request.options_json):
            query['OptionsJson'] = request.options_json
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifySiteMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifySiteMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_site_monitor(
        self,
        request: main_models.ModifySiteMonitorRequest,
    ) -> main_models.ModifySiteMonitorResponse:
        runtime = RuntimeOptions()
        return self.modify_site_monitor_with_options(request, runtime)

    async def modify_site_monitor_async(
        self,
        request: main_models.ModifySiteMonitorRequest,
    ) -> main_models.ModifySiteMonitorResponse:
        runtime = RuntimeOptions()
        return await self.modify_site_monitor_with_options_async(request, runtime)

    def put_contact_with_options(
        self,
        request: main_models.PutContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.describe):
            query['Describe'] = request.describe
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.channels):
            query['Channels'] = request.channels
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutContact',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_contact_with_options_async(
        self,
        request: main_models.PutContactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutContactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_name):
            query['ContactName'] = request.contact_name
        if not DaraCore.is_null(request.describe):
            query['Describe'] = request.describe
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.channels):
            query['Channels'] = request.channels
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutContact',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_contact(
        self,
        request: main_models.PutContactRequest,
    ) -> main_models.PutContactResponse:
        runtime = RuntimeOptions()
        return self.put_contact_with_options(request, runtime)

    async def put_contact_async(
        self,
        request: main_models.PutContactRequest,
    ) -> main_models.PutContactResponse:
        runtime = RuntimeOptions()
        return await self.put_contact_with_options_async(request, runtime)

    def put_contact_group_with_options(
        self,
        request: main_models.PutContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_names):
            query['ContactNames'] = request.contact_names
        if not DaraCore.is_null(request.describe):
            query['Describe'] = request.describe
        if not DaraCore.is_null(request.enable_subscribed):
            query['EnableSubscribed'] = request.enable_subscribed
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutContactGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_contact_group_with_options_async(
        self,
        request: main_models.PutContactGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutContactGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not DaraCore.is_null(request.contact_names):
            query['ContactNames'] = request.contact_names
        if not DaraCore.is_null(request.describe):
            query['Describe'] = request.describe
        if not DaraCore.is_null(request.enable_subscribed):
            query['EnableSubscribed'] = request.enable_subscribed
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutContactGroup',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_contact_group(
        self,
        request: main_models.PutContactGroupRequest,
    ) -> main_models.PutContactGroupResponse:
        runtime = RuntimeOptions()
        return self.put_contact_group_with_options(request, runtime)

    async def put_contact_group_async(
        self,
        request: main_models.PutContactGroupRequest,
    ) -> main_models.PutContactGroupResponse:
        runtime = RuntimeOptions()
        return await self.put_contact_group_with_options_async(request, runtime)

    def put_custom_event_with_options(
        self,
        request: main_models.PutCustomEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCustomEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_info):
            query['EventInfo'] = request.event_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCustomEvent',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCustomEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_custom_event_with_options_async(
        self,
        request: main_models.PutCustomEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCustomEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_info):
            query['EventInfo'] = request.event_info
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCustomEvent',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCustomEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_custom_event(
        self,
        request: main_models.PutCustomEventRequest,
    ) -> main_models.PutCustomEventResponse:
        runtime = RuntimeOptions()
        return self.put_custom_event_with_options(request, runtime)

    async def put_custom_event_async(
        self,
        request: main_models.PutCustomEventRequest,
    ) -> main_models.PutCustomEventResponse:
        runtime = RuntimeOptions()
        return await self.put_custom_event_with_options_async(request, runtime)

    def put_custom_event_rule_with_options(
        self,
        request: main_models.PutCustomEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCustomEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not DaraCore.is_null(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCustomEventRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCustomEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_custom_event_rule_with_options_async(
        self,
        request: main_models.PutCustomEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCustomEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not DaraCore.is_null(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCustomEventRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCustomEventRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_custom_event_rule(
        self,
        request: main_models.PutCustomEventRuleRequest,
    ) -> main_models.PutCustomEventRuleResponse:
        runtime = RuntimeOptions()
        return self.put_custom_event_rule_with_options(request, runtime)

    async def put_custom_event_rule_async(
        self,
        request: main_models.PutCustomEventRuleRequest,
    ) -> main_models.PutCustomEventRuleResponse:
        runtime = RuntimeOptions()
        return await self.put_custom_event_rule_with_options_async(request, runtime)

    def put_custom_metric_with_options(
        self,
        request: main_models.PutCustomMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCustomMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metric_list):
            query['MetricList'] = request.metric_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCustomMetric',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCustomMetricResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_custom_metric_with_options_async(
        self,
        request: main_models.PutCustomMetricRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCustomMetricResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metric_list):
            query['MetricList'] = request.metric_list
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCustomMetric',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCustomMetricResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_custom_metric(
        self,
        request: main_models.PutCustomMetricRequest,
    ) -> main_models.PutCustomMetricResponse:
        runtime = RuntimeOptions()
        return self.put_custom_metric_with_options(request, runtime)

    async def put_custom_metric_async(
        self,
        request: main_models.PutCustomMetricRequest,
    ) -> main_models.PutCustomMetricResponse:
        runtime = RuntimeOptions()
        return await self.put_custom_metric_with_options_async(request, runtime)

    def put_custom_metric_rule_with_options(
        self,
        request: main_models.PutCustomMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCustomMetricRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not DaraCore.is_null(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.statistics):
            query['Statistics'] = request.statistics
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCustomMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCustomMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_custom_metric_rule_with_options_async(
        self,
        request: main_models.PutCustomMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutCustomMetricRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.comparison_operator):
            query['ComparisonOperator'] = request.comparison_operator
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not DaraCore.is_null(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not DaraCore.is_null(request.evaluation_count):
            query['EvaluationCount'] = request.evaluation_count
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.level):
            query['Level'] = request.level
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.statistics):
            query['Statistics'] = request.statistics
        if not DaraCore.is_null(request.threshold):
            query['Threshold'] = request.threshold
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutCustomMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutCustomMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_custom_metric_rule(
        self,
        request: main_models.PutCustomMetricRuleRequest,
    ) -> main_models.PutCustomMetricRuleResponse:
        runtime = RuntimeOptions()
        return self.put_custom_metric_rule_with_options(request, runtime)

    async def put_custom_metric_rule_async(
        self,
        request: main_models.PutCustomMetricRuleRequest,
    ) -> main_models.PutCustomMetricRuleResponse:
        runtime = RuntimeOptions()
        return await self.put_custom_metric_rule_with_options_async(request, runtime)

    def put_event_rule_with_options(
        self,
        request: main_models.PutEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_pattern):
            query['EventPattern'] = request.event_pattern
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutEventRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEventRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_event_rule_with_options_async(
        self,
        request: main_models.PutEventRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEventRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.event_pattern):
            query['EventPattern'] = request.event_pattern
        if not DaraCore.is_null(request.event_type):
            query['EventType'] = request.event_type
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.state):
            query['State'] = request.state
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutEventRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEventRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_event_rule(
        self,
        request: main_models.PutEventRuleRequest,
    ) -> main_models.PutEventRuleResponse:
        runtime = RuntimeOptions()
        return self.put_event_rule_with_options(request, runtime)

    async def put_event_rule_async(
        self,
        request: main_models.PutEventRuleRequest,
    ) -> main_models.PutEventRuleResponse:
        runtime = RuntimeOptions()
        return await self.put_event_rule_with_options_async(request, runtime)

    def put_event_rule_targets_with_options(
        self,
        request: main_models.PutEventRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEventRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_parameters):
            query['ContactParameters'] = request.contact_parameters
        if not DaraCore.is_null(request.fc_parameters):
            query['FcParameters'] = request.fc_parameters
        if not DaraCore.is_null(request.mns_parameters):
            query['MnsParameters'] = request.mns_parameters
        if not DaraCore.is_null(request.open_api_parameters):
            query['OpenApiParameters'] = request.open_api_parameters
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sls_parameters):
            query['SlsParameters'] = request.sls_parameters
        if not DaraCore.is_null(request.webhook_parameters):
            query['WebhookParameters'] = request.webhook_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutEventRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEventRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_event_rule_targets_with_options_async(
        self,
        request: main_models.PutEventRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutEventRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_parameters):
            query['ContactParameters'] = request.contact_parameters
        if not DaraCore.is_null(request.fc_parameters):
            query['FcParameters'] = request.fc_parameters
        if not DaraCore.is_null(request.mns_parameters):
            query['MnsParameters'] = request.mns_parameters
        if not DaraCore.is_null(request.open_api_parameters):
            query['OpenApiParameters'] = request.open_api_parameters
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.sls_parameters):
            query['SlsParameters'] = request.sls_parameters
        if not DaraCore.is_null(request.webhook_parameters):
            query['WebhookParameters'] = request.webhook_parameters
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutEventRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutEventRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_event_rule_targets(
        self,
        request: main_models.PutEventRuleTargetsRequest,
    ) -> main_models.PutEventRuleTargetsResponse:
        runtime = RuntimeOptions()
        return self.put_event_rule_targets_with_options(request, runtime)

    async def put_event_rule_targets_async(
        self,
        request: main_models.PutEventRuleTargetsRequest,
    ) -> main_models.PutEventRuleTargetsResponse:
        runtime = RuntimeOptions()
        return await self.put_event_rule_targets_with_options_async(request, runtime)

    def put_exporter_output_with_options(
        self,
        request: main_models.PutExporterOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutExporterOutputResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_json):
            query['ConfigJson'] = request.config_json
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.dest_name):
            query['DestName'] = request.dest_name
        if not DaraCore.is_null(request.dest_type):
            query['DestType'] = request.dest_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutExporterOutput',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutExporterOutputResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_exporter_output_with_options_async(
        self,
        request: main_models.PutExporterOutputRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutExporterOutputResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_json):
            query['ConfigJson'] = request.config_json
        if not DaraCore.is_null(request.desc):
            query['Desc'] = request.desc
        if not DaraCore.is_null(request.dest_name):
            query['DestName'] = request.dest_name
        if not DaraCore.is_null(request.dest_type):
            query['DestType'] = request.dest_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutExporterOutput',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutExporterOutputResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_exporter_output(
        self,
        request: main_models.PutExporterOutputRequest,
    ) -> main_models.PutExporterOutputResponse:
        runtime = RuntimeOptions()
        return self.put_exporter_output_with_options(request, runtime)

    async def put_exporter_output_async(
        self,
        request: main_models.PutExporterOutputRequest,
    ) -> main_models.PutExporterOutputResponse:
        runtime = RuntimeOptions()
        return await self.put_exporter_output_with_options_async(request, runtime)

    def put_exporter_rule_with_options(
        self,
        request: main_models.PutExporterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutExporterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.describe):
            query['Describe'] = request.describe
        if not DaraCore.is_null(request.dst_names):
            query['DstNames'] = request.dst_names
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.target_windows):
            query['TargetWindows'] = request.target_windows
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutExporterRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutExporterRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_exporter_rule_with_options_async(
        self,
        request: main_models.PutExporterRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutExporterRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.describe):
            query['Describe'] = request.describe
        if not DaraCore.is_null(request.dst_names):
            query['DstNames'] = request.dst_names
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.target_windows):
            query['TargetWindows'] = request.target_windows
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutExporterRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutExporterRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_exporter_rule(
        self,
        request: main_models.PutExporterRuleRequest,
    ) -> main_models.PutExporterRuleResponse:
        runtime = RuntimeOptions()
        return self.put_exporter_rule_with_options(request, runtime)

    async def put_exporter_rule_async(
        self,
        request: main_models.PutExporterRuleRequest,
    ) -> main_models.PutExporterRuleResponse:
        runtime = RuntimeOptions()
        return await self.put_exporter_rule_with_options_async(request, runtime)

    def put_group_metric_rule_with_options(
        self,
        request: main_models.PutGroupMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutGroupMetricRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not DaraCore.is_null(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not DaraCore.is_null(request.extra_dimension_json):
            query['ExtraDimensionJson'] = request.extra_dimension_json
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not DaraCore.is_null(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        if not DaraCore.is_null(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutGroupMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutGroupMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_group_metric_rule_with_options_async(
        self,
        request: main_models.PutGroupMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutGroupMetricRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not DaraCore.is_null(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not DaraCore.is_null(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not DaraCore.is_null(request.extra_dimension_json):
            query['ExtraDimensionJson'] = request.extra_dimension_json
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not DaraCore.is_null(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not DaraCore.is_null(request.options):
            query['Options'] = request.options
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        if not DaraCore.is_null(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutGroupMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutGroupMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_group_metric_rule(
        self,
        request: main_models.PutGroupMetricRuleRequest,
    ) -> main_models.PutGroupMetricRuleResponse:
        runtime = RuntimeOptions()
        return self.put_group_metric_rule_with_options(request, runtime)

    async def put_group_metric_rule_async(
        self,
        request: main_models.PutGroupMetricRuleRequest,
    ) -> main_models.PutGroupMetricRuleResponse:
        runtime = RuntimeOptions()
        return await self.put_group_metric_rule_with_options_async(request, runtime)

    def put_hybrid_monitor_metric_data_with_options(
        self,
        request: main_models.PutHybridMonitorMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutHybridMonitorMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metric_list):
            query['MetricList'] = request.metric_list
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutHybridMonitorMetricData',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutHybridMonitorMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_hybrid_monitor_metric_data_with_options_async(
        self,
        request: main_models.PutHybridMonitorMetricDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutHybridMonitorMetricDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metric_list):
            query['MetricList'] = request.metric_list
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutHybridMonitorMetricData',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutHybridMonitorMetricDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_hybrid_monitor_metric_data(
        self,
        request: main_models.PutHybridMonitorMetricDataRequest,
    ) -> main_models.PutHybridMonitorMetricDataResponse:
        runtime = RuntimeOptions()
        return self.put_hybrid_monitor_metric_data_with_options(request, runtime)

    async def put_hybrid_monitor_metric_data_async(
        self,
        request: main_models.PutHybridMonitorMetricDataRequest,
    ) -> main_models.PutHybridMonitorMetricDataResponse:
        runtime = RuntimeOptions()
        return await self.put_hybrid_monitor_metric_data_with_options_async(request, runtime)

    def put_log_monitor_with_options(
        self,
        request: main_models.PutLogMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutLogMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregates):
            query['Aggregates'] = request.aggregates
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.groupbys):
            query['Groupbys'] = request.groupbys
        if not DaraCore.is_null(request.log_id):
            query['LogId'] = request.log_id
        if not DaraCore.is_null(request.metric_express):
            query['MetricExpress'] = request.metric_express
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.sls_logstore):
            query['SlsLogstore'] = request.sls_logstore
        if not DaraCore.is_null(request.sls_project):
            query['SlsProject'] = request.sls_project
        if not DaraCore.is_null(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        if not DaraCore.is_null(request.tumblingwindows):
            query['Tumblingwindows'] = request.tumblingwindows
        if not DaraCore.is_null(request.unit):
            query['Unit'] = request.unit
        if not DaraCore.is_null(request.value_filter):
            query['ValueFilter'] = request.value_filter
        if not DaraCore.is_null(request.value_filter_relation):
            query['ValueFilterRelation'] = request.value_filter_relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutLogMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutLogMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_log_monitor_with_options_async(
        self,
        request: main_models.PutLogMonitorRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutLogMonitorResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.aggregates):
            query['Aggregates'] = request.aggregates
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.groupbys):
            query['Groupbys'] = request.groupbys
        if not DaraCore.is_null(request.log_id):
            query['LogId'] = request.log_id
        if not DaraCore.is_null(request.metric_express):
            query['MetricExpress'] = request.metric_express
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.sls_logstore):
            query['SlsLogstore'] = request.sls_logstore
        if not DaraCore.is_null(request.sls_project):
            query['SlsProject'] = request.sls_project
        if not DaraCore.is_null(request.sls_region_id):
            query['SlsRegionId'] = request.sls_region_id
        if not DaraCore.is_null(request.tumblingwindows):
            query['Tumblingwindows'] = request.tumblingwindows
        if not DaraCore.is_null(request.unit):
            query['Unit'] = request.unit
        if not DaraCore.is_null(request.value_filter):
            query['ValueFilter'] = request.value_filter
        if not DaraCore.is_null(request.value_filter_relation):
            query['ValueFilterRelation'] = request.value_filter_relation
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutLogMonitor',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutLogMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_log_monitor(
        self,
        request: main_models.PutLogMonitorRequest,
    ) -> main_models.PutLogMonitorResponse:
        runtime = RuntimeOptions()
        return self.put_log_monitor_with_options(request, runtime)

    async def put_log_monitor_async(
        self,
        request: main_models.PutLogMonitorRequest,
    ) -> main_models.PutLogMonitorResponse:
        runtime = RuntimeOptions()
        return await self.put_log_monitor_with_options_async(request, runtime)

    def put_metric_rule_targets_with_options(
        self,
        request: main_models.PutMetricRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMetricRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutMetricRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMetricRuleTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_metric_rule_targets_with_options_async(
        self,
        request: main_models.PutMetricRuleTargetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMetricRuleTargetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.targets):
            query['Targets'] = request.targets
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutMetricRuleTargets',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMetricRuleTargetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_metric_rule_targets(
        self,
        request: main_models.PutMetricRuleTargetsRequest,
    ) -> main_models.PutMetricRuleTargetsResponse:
        runtime = RuntimeOptions()
        return self.put_metric_rule_targets_with_options(request, runtime)

    async def put_metric_rule_targets_async(
        self,
        request: main_models.PutMetricRuleTargetsRequest,
    ) -> main_models.PutMetricRuleTargetsResponse:
        runtime = RuntimeOptions()
        return await self.put_metric_rule_targets_with_options_async(request, runtime)

    def put_monitor_group_dynamic_rule_with_options(
        self,
        request: main_models.PutMonitorGroupDynamicRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMonitorGroupDynamicRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_rules):
            query['GroupRules'] = request.group_rules
        if not DaraCore.is_null(request.is_async):
            query['IsAsync'] = request.is_async
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutMonitorGroupDynamicRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMonitorGroupDynamicRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_monitor_group_dynamic_rule_with_options_async(
        self,
        request: main_models.PutMonitorGroupDynamicRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMonitorGroupDynamicRuleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.group_rules):
            query['GroupRules'] = request.group_rules
        if not DaraCore.is_null(request.is_async):
            query['IsAsync'] = request.is_async
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutMonitorGroupDynamicRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMonitorGroupDynamicRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_monitor_group_dynamic_rule(
        self,
        request: main_models.PutMonitorGroupDynamicRuleRequest,
    ) -> main_models.PutMonitorGroupDynamicRuleResponse:
        runtime = RuntimeOptions()
        return self.put_monitor_group_dynamic_rule_with_options(request, runtime)

    async def put_monitor_group_dynamic_rule_async(
        self,
        request: main_models.PutMonitorGroupDynamicRuleRequest,
    ) -> main_models.PutMonitorGroupDynamicRuleResponse:
        runtime = RuntimeOptions()
        return await self.put_monitor_group_dynamic_rule_with_options_async(request, runtime)

    def put_monitoring_config_with_options(
        self,
        request: main_models.PutMonitoringConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMonitoringConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_install):
            query['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.enable_install_agent_new_ecs):
            query['EnableInstallAgentNewECS'] = request.enable_install_agent_new_ecs
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutMonitoringConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMonitoringConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_monitoring_config_with_options_async(
        self,
        request: main_models.PutMonitoringConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutMonitoringConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auto_install):
            query['AutoInstall'] = request.auto_install
        if not DaraCore.is_null(request.enable_install_agent_new_ecs):
            query['EnableInstallAgentNewECS'] = request.enable_install_agent_new_ecs
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutMonitoringConfig',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutMonitoringConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_monitoring_config(
        self,
        request: main_models.PutMonitoringConfigRequest,
    ) -> main_models.PutMonitoringConfigResponse:
        runtime = RuntimeOptions()
        return self.put_monitoring_config_with_options(request, runtime)

    async def put_monitoring_config_async(
        self,
        request: main_models.PutMonitoringConfigRequest,
    ) -> main_models.PutMonitoringConfigResponse:
        runtime = RuntimeOptions()
        return await self.put_monitoring_config_with_options_async(request, runtime)

    def put_resource_metric_rule_with_options(
        self,
        tmp_req: main_models.PutResourceMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutResourceMetricRuleResponse:
        tmp_req.validate()
        request = main_models.PutResourceMetricRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.composite_expression):
            request.composite_expression_shrink = Utils.array_to_string_with_specified_style(tmp_req.composite_expression, 'CompositeExpression', 'json')
        if not DaraCore.is_null(tmp_req.prometheus):
            request.prometheus_shrink = Utils.array_to_string_with_specified_style(tmp_req.prometheus, 'Prometheus', 'json')
        query = {}
        if not DaraCore.is_null(request.composite_expression_shrink):
            query['CompositeExpression'] = request.composite_expression_shrink
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not DaraCore.is_null(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not DaraCore.is_null(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.prometheus_shrink):
            query['Prometheus'] = request.prometheus_shrink
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        if not DaraCore.is_null(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutResourceMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutResourceMetricRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_resource_metric_rule_with_options_async(
        self,
        tmp_req: main_models.PutResourceMetricRuleRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutResourceMetricRuleResponse:
        tmp_req.validate()
        request = main_models.PutResourceMetricRuleShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.composite_expression):
            request.composite_expression_shrink = Utils.array_to_string_with_specified_style(tmp_req.composite_expression, 'CompositeExpression', 'json')
        if not DaraCore.is_null(tmp_req.prometheus):
            request.prometheus_shrink = Utils.array_to_string_with_specified_style(tmp_req.prometheus, 'Prometheus', 'json')
        query = {}
        if not DaraCore.is_null(request.composite_expression_shrink):
            query['CompositeExpression'] = request.composite_expression_shrink
        if not DaraCore.is_null(request.contact_groups):
            query['ContactGroups'] = request.contact_groups
        if not DaraCore.is_null(request.effective_interval):
            query['EffectiveInterval'] = request.effective_interval
        if not DaraCore.is_null(request.email_subject):
            query['EmailSubject'] = request.email_subject
        if not DaraCore.is_null(request.interval):
            query['Interval'] = request.interval
        if not DaraCore.is_null(request.labels):
            query['Labels'] = request.labels
        if not DaraCore.is_null(request.metric_name):
            query['MetricName'] = request.metric_name
        if not DaraCore.is_null(request.namespace):
            query['Namespace'] = request.namespace
        if not DaraCore.is_null(request.no_data_policy):
            query['NoDataPolicy'] = request.no_data_policy
        if not DaraCore.is_null(request.no_effective_interval):
            query['NoEffectiveInterval'] = request.no_effective_interval
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.prometheus_shrink):
            query['Prometheus'] = request.prometheus_shrink
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.rule_id):
            query['RuleId'] = request.rule_id
        if not DaraCore.is_null(request.rule_name):
            query['RuleName'] = request.rule_name
        if not DaraCore.is_null(request.silence_time):
            query['SilenceTime'] = request.silence_time
        if not DaraCore.is_null(request.webhook):
            query['Webhook'] = request.webhook
        if not DaraCore.is_null(request.escalations):
            query['Escalations'] = request.escalations
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutResourceMetricRule',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutResourceMetricRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_resource_metric_rule(
        self,
        request: main_models.PutResourceMetricRuleRequest,
    ) -> main_models.PutResourceMetricRuleResponse:
        runtime = RuntimeOptions()
        return self.put_resource_metric_rule_with_options(request, runtime)

    async def put_resource_metric_rule_async(
        self,
        request: main_models.PutResourceMetricRuleRequest,
    ) -> main_models.PutResourceMetricRuleResponse:
        runtime = RuntimeOptions()
        return await self.put_resource_metric_rule_with_options_async(request, runtime)

    def put_resource_metric_rules_with_options(
        self,
        request: main_models.PutResourceMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutResourceMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutResourceMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutResourceMetricRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_resource_metric_rules_with_options_async(
        self,
        request: main_models.PutResourceMetricRulesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PutResourceMetricRulesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.rules):
            query['Rules'] = request.rules
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PutResourceMetricRules',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PutResourceMetricRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_resource_metric_rules(
        self,
        request: main_models.PutResourceMetricRulesRequest,
    ) -> main_models.PutResourceMetricRulesResponse:
        runtime = RuntimeOptions()
        return self.put_resource_metric_rules_with_options(request, runtime)

    async def put_resource_metric_rules_async(
        self,
        request: main_models.PutResourceMetricRulesRequest,
    ) -> main_models.PutResourceMetricRulesResponse:
        runtime = RuntimeOptions()
        return await self.put_resource_metric_rules_with_options_async(request, runtime)

    def remove_tags_with_options(
        self,
        request: main_models.RemoveTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTags',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: main_models.RemoveTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveTags',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_tags(
        self,
        request: main_models.RemoveTagsRequest,
    ) -> main_models.RemoveTagsResponse:
        runtime = RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    async def remove_tags_async(
        self,
        request: main_models.RemoveTagsRequest,
    ) -> main_models.RemoveTagsResponse:
        runtime = RuntimeOptions()
        return await self.remove_tags_with_options_async(request, runtime)

    def send_dry_run_system_event_with_options(
        self,
        request: main_models.SendDryRunSystemEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendDryRunSystemEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_content):
            query['EventContent'] = request.event_content
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendDryRunSystemEvent',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendDryRunSystemEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_dry_run_system_event_with_options_async(
        self,
        request: main_models.SendDryRunSystemEventRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SendDryRunSystemEventResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.event_content):
            query['EventContent'] = request.event_content
        if not DaraCore.is_null(request.event_name):
            query['EventName'] = request.event_name
        if not DaraCore.is_null(request.group_id):
            query['GroupId'] = request.group_id
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SendDryRunSystemEvent',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendDryRunSystemEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_dry_run_system_event(
        self,
        request: main_models.SendDryRunSystemEventRequest,
    ) -> main_models.SendDryRunSystemEventResponse:
        runtime = RuntimeOptions()
        return self.send_dry_run_system_event_with_options(request, runtime)

    async def send_dry_run_system_event_async(
        self,
        request: main_models.SendDryRunSystemEventRequest,
    ) -> main_models.SendDryRunSystemEventResponse:
        runtime = RuntimeOptions()
        return await self.send_dry_run_system_event_with_options_async(request, runtime)

    def uninstall_monitoring_agent_with_options(
        self,
        request: main_models.UninstallMonitoringAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallMonitoringAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallMonitoringAgent',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallMonitoringAgentResponse(),
            self.call_api(params, req, runtime)
        )

    async def uninstall_monitoring_agent_with_options_async(
        self,
        request: main_models.UninstallMonitoringAgentRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UninstallMonitoringAgentResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UninstallMonitoringAgent',
            version = '2019-01-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UninstallMonitoringAgentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def uninstall_monitoring_agent(
        self,
        request: main_models.UninstallMonitoringAgentRequest,
    ) -> main_models.UninstallMonitoringAgentResponse:
        runtime = RuntimeOptions()
        return self.uninstall_monitoring_agent_with_options(request, runtime)

    async def uninstall_monitoring_agent_async(
        self,
        request: main_models.UninstallMonitoringAgentRequest,
    ) -> main_models.UninstallMonitoringAgentResponse:
        runtime = RuntimeOptions()
        return await self.uninstall_monitoring_agent_with_options_async(request, runtime)
