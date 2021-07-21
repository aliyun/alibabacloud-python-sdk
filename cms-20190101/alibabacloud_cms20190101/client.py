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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.AddTagsResponse(),
            self.do_rpcrequest('AddTags', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def add_tags_with_options_async(
        self,
        request: cms_20190101_models.AddTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.AddTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.AddTagsResponse(),
            await self.do_rpcrequest_async('AddTags', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_tags(
        self,
        request: cms_20190101_models.AddTagsRequest,
    ) -> cms_20190101_models.AddTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    async def add_tags_async(
        self,
        request: cms_20190101_models.AddTagsRequest,
    ) -> cms_20190101_models.AddTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_tags_with_options_async(request, runtime)

    def apply_metric_rule_template_with_options(
        self,
        request: cms_20190101_models.ApplyMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ApplyMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ApplyMetricRuleTemplateResponse(),
            self.do_rpcrequest('ApplyMetricRuleTemplate', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def apply_metric_rule_template_with_options_async(
        self,
        request: cms_20190101_models.ApplyMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ApplyMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ApplyMetricRuleTemplateResponse(),
            await self.do_rpcrequest_async('ApplyMetricRuleTemplate', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def apply_metric_rule_template(
        self,
        request: cms_20190101_models.ApplyMetricRuleTemplateRequest,
    ) -> cms_20190101_models.ApplyMetricRuleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.apply_metric_rule_template_with_options(request, runtime)

    async def apply_metric_rule_template_async(
        self,
        request: cms_20190101_models.ApplyMetricRuleTemplateRequest,
    ) -> cms_20190101_models.ApplyMetricRuleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.apply_metric_rule_template_with_options_async(request, runtime)

    def create_cms_call_num_order_with_options(
        self,
        request: cms_20190101_models.CreateCmsCallNumOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsCallNumOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsCallNumOrderResponse(),
            self.do_rpcrequest('CreateCmsCallNumOrder', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cms_call_num_order_with_options_async(
        self,
        request: cms_20190101_models.CreateCmsCallNumOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsCallNumOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsCallNumOrderResponse(),
            await self.do_rpcrequest_async('CreateCmsCallNumOrder', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsOrderResponse(),
            self.do_rpcrequest('CreateCmsOrder', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cms_order_with_options_async(
        self,
        request: cms_20190101_models.CreateCmsOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsOrderResponse(),
            await self.do_rpcrequest_async('CreateCmsOrder', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsSmspackageOrderResponse(),
            self.do_rpcrequest('CreateCmsSmspackageOrder', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_cms_smspackage_order_with_options_async(
        self,
        request: cms_20190101_models.CreateCmsSmspackageOrderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateCmsSmspackageOrderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateCmsSmspackageOrderResponse(),
            await self.do_rpcrequest_async('CreateCmsSmspackageOrder', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateDynamicTagGroupResponse(),
            self.do_rpcrequest('CreateDynamicTagGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_dynamic_tag_group_with_options_async(
        self,
        request: cms_20190101_models.CreateDynamicTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateDynamicTagGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateDynamicTagGroupResponse(),
            await self.do_rpcrequest_async('CreateDynamicTagGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dynamic_tag_group(
        self,
        request: cms_20190101_models.CreateDynamicTagGroupRequest,
    ) -> cms_20190101_models.CreateDynamicTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_dynamic_tag_group_with_options(request, runtime)

    async def create_dynamic_tag_group_async(
        self,
        request: cms_20190101_models.CreateDynamicTagGroupRequest,
    ) -> cms_20190101_models.CreateDynamicTagGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_dynamic_tag_group_with_options_async(request, runtime)

    def create_group_metric_rules_with_options(
        self,
        request: cms_20190101_models.CreateGroupMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateGroupMetricRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMetricRulesResponse(),
            self.do_rpcrequest('CreateGroupMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_group_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.CreateGroupMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateGroupMetricRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMetricRulesResponse(),
            await self.do_rpcrequest_async('CreateGroupMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group_metric_rules(
        self,
        request: cms_20190101_models.CreateGroupMetricRulesRequest,
    ) -> cms_20190101_models.CreateGroupMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_group_metric_rules_with_options(request, runtime)

    async def create_group_metric_rules_async(
        self,
        request: cms_20190101_models.CreateGroupMetricRulesRequest,
    ) -> cms_20190101_models.CreateGroupMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_group_metric_rules_with_options_async(request, runtime)

    def create_group_monitoring_agent_process_with_options(
        self,
        request: cms_20190101_models.CreateGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMonitoringAgentProcessResponse(),
            self.do_rpcrequest('CreateGroupMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_group_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.CreateGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateGroupMonitoringAgentProcessResponse(),
            await self.do_rpcrequest_async('CreateGroupMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHostAvailabilityResponse(),
            self.do_rpcrequest('CreateHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_host_availability_with_options_async(
        self,
        request: cms_20190101_models.CreateHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateHostAvailabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateHostAvailabilityResponse(),
            await self.do_rpcrequest_async('CreateHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_host_availability(
        self,
        request: cms_20190101_models.CreateHostAvailabilityRequest,
    ) -> cms_20190101_models.CreateHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_host_availability_with_options(request, runtime)

    async def create_host_availability_async(
        self,
        request: cms_20190101_models.CreateHostAvailabilityRequest,
    ) -> cms_20190101_models.CreateHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_host_availability_with_options_async(request, runtime)

    def create_metric_rule_resources_with_options(
        self,
        request: cms_20190101_models.CreateMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleResourcesResponse(),
            self.do_rpcrequest('CreateMetricRuleResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_metric_rule_resources_with_options_async(
        self,
        request: cms_20190101_models.CreateMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleResourcesResponse(),
            await self.do_rpcrequest_async('CreateMetricRuleResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleTemplateResponse(),
            self.do_rpcrequest('CreateMetricRuleTemplate', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_metric_rule_template_with_options_async(
        self,
        request: cms_20190101_models.CreateMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMetricRuleTemplateResponse(),
            await self.do_rpcrequest_async('CreateMetricRuleTemplate', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorAgentProcessResponse(),
            self.do_rpcrequest('CreateMonitorAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_monitor_agent_process_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorAgentProcessResponse(),
            await self.do_rpcrequest_async('CreateMonitorAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupResponse(),
            self.do_rpcrequest('CreateMonitorGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_monitor_group_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupResponse(),
            await self.do_rpcrequest_async('CreateMonitorGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_monitor_group(
        self,
        request: cms_20190101_models.CreateMonitorGroupRequest,
    ) -> cms_20190101_models.CreateMonitorGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_with_options(request, runtime)

    async def create_monitor_group_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupRequest,
    ) -> cms_20190101_models.CreateMonitorGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_group_with_options_async(request, runtime)

    def create_monitor_group_by_resource_group_id_with_options(
        self,
        request: cms_20190101_models.CreateMonitorGroupByResourceGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse(),
            self.do_rpcrequest('CreateMonitorGroupByResourceGroupId', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_monitor_group_by_resource_group_id_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupByResourceGroupIdRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse(),
            await self.do_rpcrequest_async('CreateMonitorGroupByResourceGroupId', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_monitor_group_by_resource_group_id(
        self,
        request: cms_20190101_models.CreateMonitorGroupByResourceGroupIdRequest,
    ) -> cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_by_resource_group_id_with_options(request, runtime)

    async def create_monitor_group_by_resource_group_id_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupByResourceGroupIdRequest,
    ) -> cms_20190101_models.CreateMonitorGroupByResourceGroupIdResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_group_by_resource_group_id_with_options_async(request, runtime)

    def create_monitor_group_instances_with_options(
        self,
        request: cms_20190101_models.CreateMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupInstancesResponse(),
            self.do_rpcrequest('CreateMonitorGroupInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_monitor_group_instances_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupInstancesResponse(),
            await self.do_rpcrequest_async('CreateMonitorGroupInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_monitor_group_instances(
        self,
        request: cms_20190101_models.CreateMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.CreateMonitorGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_instances_with_options(request, runtime)

    async def create_monitor_group_instances_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupInstancesRequest,
    ) -> cms_20190101_models.CreateMonitorGroupInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_group_instances_with_options_async(request, runtime)

    def create_monitor_group_notify_policy_with_options(
        self,
        request: cms_20190101_models.CreateMonitorGroupNotifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse(),
            self.do_rpcrequest('CreateMonitorGroupNotifyPolicy', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_monitor_group_notify_policy_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupNotifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse(),
            await self.do_rpcrequest_async('CreateMonitorGroupNotifyPolicy', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_monitor_group_notify_policy(
        self,
        request: cms_20190101_models.CreateMonitorGroupNotifyPolicyRequest,
    ) -> cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_monitor_group_notify_policy_with_options(request, runtime)

    async def create_monitor_group_notify_policy_async(
        self,
        request: cms_20190101_models.CreateMonitorGroupNotifyPolicyRequest,
    ) -> cms_20190101_models.CreateMonitorGroupNotifyPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_monitor_group_notify_policy_with_options_async(request, runtime)

    def create_monitoring_agent_process_with_options(
        self,
        request: cms_20190101_models.CreateMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitoringAgentProcessResponse(),
            self.do_rpcrequest('CreateMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.CreateMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateMonitoringAgentProcessResponse(),
            await self.do_rpcrequest_async('CreateMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateSiteMonitorResponse(),
            self.do_rpcrequest('CreateSiteMonitor', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_site_monitor_with_options_async(
        self,
        request: cms_20190101_models.CreateSiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.CreateSiteMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.CreateSiteMonitorResponse(),
            await self.do_rpcrequest_async('CreateSiteMonitor', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_site_monitor(
        self,
        request: cms_20190101_models.CreateSiteMonitorRequest,
    ) -> cms_20190101_models.CreateSiteMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_site_monitor_with_options(request, runtime)

    async def create_site_monitor_async(
        self,
        request: cms_20190101_models.CreateSiteMonitorRequest,
    ) -> cms_20190101_models.CreateSiteMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_site_monitor_with_options_async(request, runtime)

    def delete_contact_with_options(
        self,
        request: cms_20190101_models.DeleteContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactResponse(),
            self.do_rpcrequest('DeleteContact', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_contact_with_options_async(
        self,
        request: cms_20190101_models.DeleteContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactResponse(),
            await self.do_rpcrequest_async('DeleteContact', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactGroupResponse(),
            self.do_rpcrequest('DeleteContactGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_contact_group_with_options_async(
        self,
        request: cms_20190101_models.DeleteContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteContactGroupResponse(),
            await self.do_rpcrequest_async('DeleteContactGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteCustomMetricResponse(),
            self.do_rpcrequest('DeleteCustomMetric', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_custom_metric_with_options_async(
        self,
        request: cms_20190101_models.DeleteCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteCustomMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteCustomMetricResponse(),
            await self.do_rpcrequest_async('DeleteCustomMetric', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteDynamicTagGroupResponse(),
            self.do_rpcrequest('DeleteDynamicTagGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_dynamic_tag_group_with_options_async(
        self,
        request: cms_20190101_models.DeleteDynamicTagGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteDynamicTagGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteDynamicTagGroupResponse(),
            await self.do_rpcrequest_async('DeleteDynamicTagGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_event_rules_with_options(
        self,
        request: cms_20190101_models.DeleteEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteEventRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRulesResponse(),
            self.do_rpcrequest('DeleteEventRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_event_rules_with_options_async(
        self,
        request: cms_20190101_models.DeleteEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteEventRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRulesResponse(),
            await self.do_rpcrequest_async('DeleteEventRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_event_rule_targets_with_options(
        self,
        request: cms_20190101_models.DeleteEventRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteEventRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRuleTargetsResponse(),
            self.do_rpcrequest('DeleteEventRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_event_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.DeleteEventRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteEventRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteEventRuleTargetsResponse(),
            await self.do_rpcrequest_async('DeleteEventRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_exporter_output_with_options(
        self,
        request: cms_20190101_models.DeleteExporterOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteExporterOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterOutputResponse(),
            self.do_rpcrequest('DeleteExporterOutput', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_exporter_output_with_options_async(
        self,
        request: cms_20190101_models.DeleteExporterOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteExporterOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterOutputResponse(),
            await self.do_rpcrequest_async('DeleteExporterOutput', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterRuleResponse(),
            self.do_rpcrequest('DeleteExporterRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_exporter_rule_with_options_async(
        self,
        request: cms_20190101_models.DeleteExporterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteExporterRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteExporterRuleResponse(),
            await self.do_rpcrequest_async('DeleteExporterRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse(),
            self.do_rpcrequest('DeleteGroupMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_group_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.DeleteGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteGroupMonitoringAgentProcessResponse(),
            await self.do_rpcrequest_async('DeleteGroupMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHostAvailabilityResponse(),
            self.do_rpcrequest('DeleteHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_host_availability_with_options_async(
        self,
        request: cms_20190101_models.DeleteHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteHostAvailabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteHostAvailabilityResponse(),
            await self.do_rpcrequest_async('DeleteHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_log_monitor_with_options(
        self,
        request: cms_20190101_models.DeleteLogMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteLogMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteLogMonitorResponse(),
            self.do_rpcrequest('DeleteLogMonitor', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_log_monitor_with_options_async(
        self,
        request: cms_20190101_models.DeleteLogMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteLogMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteLogMonitorResponse(),
            await self.do_rpcrequest_async('DeleteLogMonitor', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_metric_rule_resources_with_options(
        self,
        request: cms_20190101_models.DeleteMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleResourcesResponse(),
            self.do_rpcrequest('DeleteMetricRuleResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_metric_rule_resources_with_options_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleResourcesResponse(),
            await self.do_rpcrequest_async('DeleteMetricRuleResources', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_metric_rules_with_options(
        self,
        request: cms_20190101_models.DeleteMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRulesResponse(),
            self.do_rpcrequest('DeleteMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.DeleteMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRulesResponse(),
            await self.do_rpcrequest_async('DeleteMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_metric_rule_targets_with_options(
        self,
        request: cms_20190101_models.DeleteMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTargetsResponse(),
            self.do_rpcrequest('DeleteMetricRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_metric_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTargetsResponse(),
            await self.do_rpcrequest_async('DeleteMetricRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTemplateResponse(),
            self.do_rpcrequest('DeleteMetricRuleTemplate', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_metric_rule_template_with_options_async(
        self,
        request: cms_20190101_models.DeleteMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMetricRuleTemplateResponse(),
            await self.do_rpcrequest_async('DeleteMetricRuleTemplate', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def delete_monitor_group_with_options(
        self,
        request: cms_20190101_models.DeleteMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupResponse(),
            self.do_rpcrequest('DeleteMonitorGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_monitor_group_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupResponse(),
            await self.do_rpcrequest_async('DeleteMonitorGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse(),
            self.do_rpcrequest('DeleteMonitorGroupDynamicRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_monitor_group_dynamic_rule_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupDynamicRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupDynamicRuleResponse(),
            await self.do_rpcrequest_async('DeleteMonitorGroupDynamicRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupInstancesResponse(),
            self.do_rpcrequest('DeleteMonitorGroupInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_monitor_group_instances_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupInstancesResponse(),
            await self.do_rpcrequest_async('DeleteMonitorGroupInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse(),
            self.do_rpcrequest('DeleteMonitorGroupNotifyPolicy', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_monitor_group_notify_policy_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitorGroupNotifyPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitorGroupNotifyPolicyResponse(),
            await self.do_rpcrequest_async('DeleteMonitorGroupNotifyPolicy', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitoringAgentProcessResponse(),
            self.do_rpcrequest('DeleteMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.DeleteMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteMonitoringAgentProcessResponse(),
            await self.do_rpcrequest_async('DeleteMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteSiteMonitorsResponse(),
            self.do_rpcrequest('DeleteSiteMonitors', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_site_monitors_with_options_async(
        self,
        request: cms_20190101_models.DeleteSiteMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DeleteSiteMonitorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DeleteSiteMonitorsResponse(),
            await self.do_rpcrequest_async('DeleteSiteMonitors', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeActiveMetricRuleListResponse(),
            self.do_rpcrequest('DescribeActiveMetricRuleList', '2019-01-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_active_metric_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeActiveMetricRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeActiveMetricRuleListResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeActiveMetricRuleListResponse(),
            await self.do_rpcrequest_async('DescribeActiveMetricRuleList', '2019-01-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertHistoryListResponse(),
            self.do_rpcrequest('DescribeAlertHistoryList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_alert_history_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertHistoryListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertHistoryListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertHistoryListResponse(),
            await self.do_rpcrequest_async('DescribeAlertHistoryList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alert_history_list(
        self,
        request: cms_20190101_models.DescribeAlertHistoryListRequest,
    ) -> cms_20190101_models.DescribeAlertHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_history_list_with_options(request, runtime)

    async def describe_alert_history_list_async(
        self,
        request: cms_20190101_models.DescribeAlertHistoryListRequest,
    ) -> cms_20190101_models.DescribeAlertHistoryListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_history_list_with_options_async(request, runtime)

    def describe_alerting_metric_rule_resources_with_options(
        self,
        request: cms_20190101_models.DescribeAlertingMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse(),
            self.do_rpcrequest('DescribeAlertingMetricRuleResources', '2019-01-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_alerting_metric_rule_resources_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertingMetricRuleResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertingMetricRuleResourcesResponse(),
            await self.do_rpcrequest_async('DescribeAlertingMetricRuleResources', '2019-01-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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

    def describe_alert_log_count_with_options(
        self,
        request: cms_20190101_models.DescribeAlertLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogCountResponse(),
            self.do_rpcrequest('DescribeAlertLogCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_alert_log_count_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertLogCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogCountResponse(),
            await self.do_rpcrequest_async('DescribeAlertLogCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alert_log_count(
        self,
        request: cms_20190101_models.DescribeAlertLogCountRequest,
    ) -> cms_20190101_models.DescribeAlertLogCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_log_count_with_options(request, runtime)

    async def describe_alert_log_count_async(
        self,
        request: cms_20190101_models.DescribeAlertLogCountRequest,
    ) -> cms_20190101_models.DescribeAlertLogCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_log_count_with_options_async(request, runtime)

    def describe_alert_log_histogram_with_options(
        self,
        request: cms_20190101_models.DescribeAlertLogHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogHistogramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogHistogramResponse(),
            self.do_rpcrequest('DescribeAlertLogHistogram', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_alert_log_histogram_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertLogHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogHistogramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogHistogramResponse(),
            await self.do_rpcrequest_async('DescribeAlertLogHistogram', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alert_log_histogram(
        self,
        request: cms_20190101_models.DescribeAlertLogHistogramRequest,
    ) -> cms_20190101_models.DescribeAlertLogHistogramResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_log_histogram_with_options(request, runtime)

    async def describe_alert_log_histogram_async(
        self,
        request: cms_20190101_models.DescribeAlertLogHistogramRequest,
    ) -> cms_20190101_models.DescribeAlertLogHistogramResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_log_histogram_with_options_async(request, runtime)

    def describe_alert_log_list_with_options(
        self,
        request: cms_20190101_models.DescribeAlertLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogListResponse(),
            self.do_rpcrequest('DescribeAlertLogList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_alert_log_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeAlertLogListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeAlertLogListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeAlertLogListResponse(),
            await self.do_rpcrequest_async('DescribeAlertLogList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_alert_log_list(
        self,
        request: cms_20190101_models.DescribeAlertLogListRequest,
    ) -> cms_20190101_models.DescribeAlertLogListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_alert_log_list_with_options(request, runtime)

    async def describe_alert_log_list_async(
        self,
        request: cms_20190101_models.DescribeAlertLogListRequest,
    ) -> cms_20190101_models.DescribeAlertLogListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_alert_log_list_with_options_async(request, runtime)

    def describe_contact_group_list_with_options(
        self,
        request: cms_20190101_models.DescribeContactGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactGroupListResponse(),
            self.do_rpcrequest('DescribeContactGroupList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_contact_group_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeContactGroupListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactGroupListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactGroupListResponse(),
            await self.do_rpcrequest_async('DescribeContactGroupList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListResponse(),
            self.do_rpcrequest('DescribeContactList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_contact_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeContactListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListResponse(),
            await self.do_rpcrequest_async('DescribeContactList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListByContactGroupResponse(),
            self.do_rpcrequest('DescribeContactListByContactGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_contact_list_by_contact_group_with_options_async(
        self,
        request: cms_20190101_models.DescribeContactListByContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeContactListByContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeContactListByContactGroupResponse(),
            await self.do_rpcrequest_async('DescribeContactListByContactGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventAttributeResponse(),
            self.do_rpcrequest('DescribeCustomEventAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_custom_event_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeCustomEventAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventAttributeResponse(),
            await self.do_rpcrequest_async('DescribeCustomEventAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventCountResponse(),
            self.do_rpcrequest('DescribeCustomEventCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_custom_event_count_with_options_async(
        self,
        request: cms_20190101_models.DescribeCustomEventCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventCountResponse(),
            await self.do_rpcrequest_async('DescribeCustomEventCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_custom_event_count(
        self,
        request: cms_20190101_models.DescribeCustomEventCountRequest,
    ) -> cms_20190101_models.DescribeCustomEventCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_event_count_with_options(request, runtime)

    async def describe_custom_event_count_async(
        self,
        request: cms_20190101_models.DescribeCustomEventCountRequest,
    ) -> cms_20190101_models.DescribeCustomEventCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_event_count_with_options_async(request, runtime)

    def describe_custom_event_histogram_with_options(
        self,
        request: cms_20190101_models.DescribeCustomEventHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventHistogramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventHistogramResponse(),
            self.do_rpcrequest('DescribeCustomEventHistogram', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_custom_event_histogram_with_options_async(
        self,
        request: cms_20190101_models.DescribeCustomEventHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomEventHistogramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomEventHistogramResponse(),
            await self.do_rpcrequest_async('DescribeCustomEventHistogram', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomMetricListResponse(),
            self.do_rpcrequest('DescribeCustomMetricList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_custom_metric_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeCustomMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeCustomMetricListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeCustomMetricListResponse(),
            await self.do_rpcrequest_async('DescribeCustomMetricList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_custom_metric_list(
        self,
        request: cms_20190101_models.DescribeCustomMetricListRequest,
    ) -> cms_20190101_models.DescribeCustomMetricListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_custom_metric_list_with_options(request, runtime)

    async def describe_custom_metric_list_async(
        self,
        request: cms_20190101_models.DescribeCustomMetricListRequest,
    ) -> cms_20190101_models.DescribeCustomMetricListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_custom_metric_list_with_options_async(request, runtime)

    def describe_dynamic_tag_rule_list_with_options(
        self,
        request: cms_20190101_models.DescribeDynamicTagRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeDynamicTagRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeDynamicTagRuleListResponse(),
            self.do_rpcrequest('DescribeDynamicTagRuleList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_dynamic_tag_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeDynamicTagRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeDynamicTagRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeDynamicTagRuleListResponse(),
            await self.do_rpcrequest_async('DescribeDynamicTagRuleList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dynamic_tag_rule_list(
        self,
        request: cms_20190101_models.DescribeDynamicTagRuleListRequest,
    ) -> cms_20190101_models.DescribeDynamicTagRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_dynamic_tag_rule_list_with_options(request, runtime)

    async def describe_dynamic_tag_rule_list_async(
        self,
        request: cms_20190101_models.DescribeDynamicTagRuleListRequest,
    ) -> cms_20190101_models.DescribeDynamicTagRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_dynamic_tag_rule_list_with_options_async(request, runtime)

    def describe_event_rule_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeEventRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleAttributeResponse(),
            self.do_rpcrequest('DescribeEventRuleAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_event_rule_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeEventRuleAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleAttributeResponse(),
            await self.do_rpcrequest_async('DescribeEventRuleAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_event_rule_attribute(
        self,
        request: cms_20190101_models.DescribeEventRuleAttributeRequest,
    ) -> cms_20190101_models.DescribeEventRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_rule_attribute_with_options(request, runtime)

    async def describe_event_rule_attribute_async(
        self,
        request: cms_20190101_models.DescribeEventRuleAttributeRequest,
    ) -> cms_20190101_models.DescribeEventRuleAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_rule_attribute_with_options_async(request, runtime)

    def describe_event_rule_list_with_options(
        self,
        request: cms_20190101_models.DescribeEventRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleListResponse(),
            self.do_rpcrequest('DescribeEventRuleList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_event_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeEventRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleListResponse(),
            await self.do_rpcrequest_async('DescribeEventRuleList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleTargetListResponse(),
            self.do_rpcrequest('DescribeEventRuleTargetList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_event_rule_target_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeEventRuleTargetListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeEventRuleTargetListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeEventRuleTargetListResponse(),
            await self.do_rpcrequest_async('DescribeEventRuleTargetList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_event_rule_target_list(
        self,
        request: cms_20190101_models.DescribeEventRuleTargetListRequest,
    ) -> cms_20190101_models.DescribeEventRuleTargetListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_event_rule_target_list_with_options(request, runtime)

    async def describe_event_rule_target_list_async(
        self,
        request: cms_20190101_models.DescribeEventRuleTargetListRequest,
    ) -> cms_20190101_models.DescribeEventRuleTargetListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_event_rule_target_list_with_options_async(request, runtime)

    def describe_exporter_output_list_with_options(
        self,
        request: cms_20190101_models.DescribeExporterOutputListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeExporterOutputListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterOutputListResponse(),
            self.do_rpcrequest('DescribeExporterOutputList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_exporter_output_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeExporterOutputListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeExporterOutputListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterOutputListResponse(),
            await self.do_rpcrequest_async('DescribeExporterOutputList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterRuleListResponse(),
            self.do_rpcrequest('DescribeExporterRuleList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_exporter_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeExporterRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeExporterRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeExporterRuleListResponse(),
            await self.do_rpcrequest_async('DescribeExporterRuleList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse(),
            self.do_rpcrequest('DescribeGroupMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_group_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.DescribeGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse(),
            await self.do_rpcrequest_async('DescribeGroupMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_group_monitoring_agent_process(
        self,
        request: cms_20190101_models.DescribeGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_group_monitoring_agent_process_with_options(request, runtime)

    async def describe_group_monitoring_agent_process_async(
        self,
        request: cms_20190101_models.DescribeGroupMonitoringAgentProcessRequest,
    ) -> cms_20190101_models.DescribeGroupMonitoringAgentProcessResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_group_monitoring_agent_process_with_options_async(request, runtime)

    def describe_host_availability_list_with_options(
        self,
        request: cms_20190101_models.DescribeHostAvailabilityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHostAvailabilityListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHostAvailabilityListResponse(),
            self.do_rpcrequest('DescribeHostAvailabilityList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_host_availability_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeHostAvailabilityListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeHostAvailabilityListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeHostAvailabilityListResponse(),
            await self.do_rpcrequest_async('DescribeHostAvailabilityList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_host_availability_list(
        self,
        request: cms_20190101_models.DescribeHostAvailabilityListRequest,
    ) -> cms_20190101_models.DescribeHostAvailabilityListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_host_availability_list_with_options(request, runtime)

    async def describe_host_availability_list_async(
        self,
        request: cms_20190101_models.DescribeHostAvailabilityListRequest,
    ) -> cms_20190101_models.DescribeHostAvailabilityListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_host_availability_list_with_options_async(request, runtime)

    def describe_log_monitor_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeLogMonitorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeLogMonitorAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorAttributeResponse(),
            self.do_rpcrequest('DescribeLogMonitorAttribute', '2019-01-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_log_monitor_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeLogMonitorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeLogMonitorAttributeResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorAttributeResponse(),
            await self.do_rpcrequest_async('DescribeLogMonitorAttribute', '2019-01-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorListResponse(),
            self.do_rpcrequest('DescribeLogMonitorList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_log_monitor_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeLogMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeLogMonitorListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeLogMonitorListResponse(),
            await self.do_rpcrequest_async('DescribeLogMonitorList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricDataResponse(),
            self.do_rpcrequest('DescribeMetricData', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_data_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricDataResponse(),
            await self.do_rpcrequest_async('DescribeMetricData', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_data(
        self,
        request: cms_20190101_models.DescribeMetricDataRequest,
    ) -> cms_20190101_models.DescribeMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_data_with_options(request, runtime)

    async def describe_metric_data_async(
        self,
        request: cms_20190101_models.DescribeMetricDataRequest,
    ) -> cms_20190101_models.DescribeMetricDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_data_with_options_async(request, runtime)

    def describe_metric_last_with_options(
        self,
        request: cms_20190101_models.DescribeMetricLastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricLastResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricLastResponse(),
            self.do_rpcrequest('DescribeMetricLast', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_last_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricLastRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricLastResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricLastResponse(),
            await self.do_rpcrequest_async('DescribeMetricLast', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_last(
        self,
        request: cms_20190101_models.DescribeMetricLastRequest,
    ) -> cms_20190101_models.DescribeMetricLastResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_last_with_options(request, runtime)

    async def describe_metric_last_async(
        self,
        request: cms_20190101_models.DescribeMetricLastRequest,
    ) -> cms_20190101_models.DescribeMetricLastResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_last_with_options_async(request, runtime)

    def describe_metric_list_with_options(
        self,
        request: cms_20190101_models.DescribeMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricListResponse(),
            self.do_rpcrequest('DescribeMetricList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricListResponse(),
            await self.do_rpcrequest_async('DescribeMetricList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_list(
        self,
        request: cms_20190101_models.DescribeMetricListRequest,
    ) -> cms_20190101_models.DescribeMetricListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_list_with_options(request, runtime)

    async def describe_metric_list_async(
        self,
        request: cms_20190101_models.DescribeMetricListRequest,
    ) -> cms_20190101_models.DescribeMetricListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_list_with_options_async(request, runtime)

    def describe_metric_meta_list_with_options(
        self,
        request: cms_20190101_models.DescribeMetricMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricMetaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricMetaListResponse(),
            self.do_rpcrequest('DescribeMetricMetaList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_meta_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricMetaListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricMetaListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricMetaListResponse(),
            await self.do_rpcrequest_async('DescribeMetricMetaList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_meta_list(
        self,
        request: cms_20190101_models.DescribeMetricMetaListRequest,
    ) -> cms_20190101_models.DescribeMetricMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_meta_list_with_options(request, runtime)

    async def describe_metric_meta_list_async(
        self,
        request: cms_20190101_models.DescribeMetricMetaListRequest,
    ) -> cms_20190101_models.DescribeMetricMetaListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_meta_list_with_options_async(request, runtime)

    def describe_metric_rule_count_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleCountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleCountResponse(),
            self.do_rpcrequest('DescribeMetricRuleCount', '2019-01-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    async def describe_metric_rule_count_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleCountResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleCountResponse(),
            await self.do_rpcrequest_async('DescribeMetricRuleCount', '2019-01-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleListResponse(),
            self.do_rpcrequest('DescribeMetricRuleList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_rule_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleListResponse(),
            await self.do_rpcrequest_async('DescribeMetricRuleList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_rule_list(
        self,
        request: cms_20190101_models.DescribeMetricRuleListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_list_with_options(request, runtime)

    async def describe_metric_rule_list_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_list_with_options_async(request, runtime)

    def describe_metric_rule_targets_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTargetsResponse(),
            self.do_rpcrequest('DescribeMetricRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTargetsResponse(),
            await self.do_rpcrequest_async('DescribeMetricRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_rule_targets(
        self,
        request: cms_20190101_models.DescribeMetricRuleTargetsRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_targets_with_options(request, runtime)

    async def describe_metric_rule_targets_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTargetsRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_targets_with_options_async(request, runtime)

    def describe_metric_rule_template_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse(),
            self.do_rpcrequest('DescribeMetricRuleTemplateAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_rule_template_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse(),
            await self.do_rpcrequest_async('DescribeMetricRuleTemplateAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_rule_template_attribute(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateAttributeRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_template_attribute_with_options(request, runtime)

    async def describe_metric_rule_template_attribute_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateAttributeRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_template_attribute_with_options_async(request, runtime)

    def describe_metric_rule_template_list_with_options(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateListResponse(),
            self.do_rpcrequest('DescribeMetricRuleTemplateList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_rule_template_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricRuleTemplateListResponse(),
            await self.do_rpcrequest_async('DescribeMetricRuleTemplateList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_rule_template_list(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_rule_template_list_with_options(request, runtime)

    async def describe_metric_rule_template_list_async(
        self,
        request: cms_20190101_models.DescribeMetricRuleTemplateListRequest,
    ) -> cms_20190101_models.DescribeMetricRuleTemplateListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_rule_template_list_with_options_async(request, runtime)

    def describe_metric_top_with_options(
        self,
        request: cms_20190101_models.DescribeMetricTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricTopResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricTopResponse(),
            self.do_rpcrequest('DescribeMetricTop', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_top_with_options_async(
        self,
        request: cms_20190101_models.DescribeMetricTopRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMetricTopResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMetricTopResponse(),
            await self.do_rpcrequest_async('DescribeMetricTop', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_top(
        self,
        request: cms_20190101_models.DescribeMetricTopRequest,
    ) -> cms_20190101_models.DescribeMetricTopResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_top_with_options(request, runtime)

    async def describe_metric_top_async(
        self,
        request: cms_20190101_models.DescribeMetricTopRequest,
    ) -> cms_20190101_models.DescribeMetricTopResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_top_with_options_async(request, runtime)

    def describe_monitor_group_categories_with_options(
        self,
        request: cms_20190101_models.DescribeMonitorGroupCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupCategoriesResponse(),
            self.do_rpcrequest('DescribeMonitorGroupCategories', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitor_group_categories_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupCategoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupCategoriesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupCategoriesResponse(),
            await self.do_rpcrequest_async('DescribeMonitorGroupCategories', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse(),
            self.do_rpcrequest('DescribeMonitorGroupDynamicRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitor_group_dynamic_rules_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupDynamicRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupDynamicRulesResponse(),
            await self.do_rpcrequest_async('DescribeMonitorGroupDynamicRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse(),
            self.do_rpcrequest('DescribeMonitorGroupInstanceAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitor_group_instance_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstanceAttributeResponse(),
            await self.do_rpcrequest_async('DescribeMonitorGroupInstanceAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstancesResponse(),
            self.do_rpcrequest('DescribeMonitorGroupInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitor_group_instances_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupInstancesResponse(),
            await self.do_rpcrequest_async('DescribeMonitorGroupInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse(),
            self.do_rpcrequest('DescribeMonitorGroupNotifyPolicyList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitor_group_notify_policy_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupNotifyPolicyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupNotifyPolicyListResponse(),
            await self.do_rpcrequest_async('DescribeMonitorGroupNotifyPolicyList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupsResponse(),
            self.do_rpcrequest('DescribeMonitorGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitor_groups_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorGroupsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorGroupsResponse(),
            await self.do_rpcrequest_async('DescribeMonitorGroups', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_monitor_groups(
        self,
        request: cms_20190101_models.DescribeMonitorGroupsRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitor_groups_with_options(request, runtime)

    async def describe_monitor_groups_async(
        self,
        request: cms_20190101_models.DescribeMonitorGroupsRequest,
    ) -> cms_20190101_models.DescribeMonitorGroupsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitor_groups_with_options_async(request, runtime)

    def describe_monitoring_agent_access_key_with_options(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse(),
            self.do_rpcrequest('DescribeMonitoringAgentAccessKey', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitoring_agent_access_key_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentAccessKeyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentAccessKeyResponse(),
            await self.do_rpcrequest_async('DescribeMonitoringAgentAccessKey', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentConfigResponse(),
            self.do_rpcrequest('DescribeMonitoringAgentConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitoring_agent_config_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentConfigResponse(),
            await self.do_rpcrequest_async('DescribeMonitoringAgentConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentHostsResponse(),
            self.do_rpcrequest('DescribeMonitoringAgentHosts', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitoring_agent_hosts_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentHostsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentHostsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentHostsResponse(),
            await self.do_rpcrequest_async('DescribeMonitoringAgentHosts', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentProcessesResponse(),
            self.do_rpcrequest('DescribeMonitoringAgentProcesses', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitoring_agent_processes_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentProcessesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentProcessesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentProcessesResponse(),
            await self.do_rpcrequest_async('DescribeMonitoringAgentProcesses', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_monitoring_agent_processes(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentProcessesRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_processes_with_options(request, runtime)

    async def describe_monitoring_agent_processes_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentProcessesRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentProcessesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitoring_agent_processes_with_options_async(request, runtime)

    def describe_monitoring_agent_statuses_with_options(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentStatusesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentStatusesResponse(),
            self.do_rpcrequest('DescribeMonitoringAgentStatuses', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitoring_agent_statuses_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentStatusesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringAgentStatusesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringAgentStatusesResponse(),
            await self.do_rpcrequest_async('DescribeMonitoringAgentStatuses', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_monitoring_agent_statuses(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentStatusesRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentStatusesResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_monitoring_agent_statuses_with_options(request, runtime)

    async def describe_monitoring_agent_statuses_async(
        self,
        request: cms_20190101_models.DescribeMonitoringAgentStatusesRequest,
    ) -> cms_20190101_models.DescribeMonitoringAgentStatusesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_monitoring_agent_statuses_with_options_async(request, runtime)

    def describe_monitoring_config_with_options(
        self,
        request: cms_20190101_models.DescribeMonitoringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringConfigResponse(),
            self.do_rpcrequest('DescribeMonitoringConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitoring_config_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitoringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitoringConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitoringConfigResponse(),
            await self.do_rpcrequest_async('DescribeMonitoringConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_monitor_resource_quota_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeMonitorResourceQuotaAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse(),
            self.do_rpcrequest('DescribeMonitorResourceQuotaAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_monitor_resource_quota_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeMonitorResourceQuotaAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeMonitorResourceQuotaAttributeResponse(),
            await self.do_rpcrequest_async('DescribeMonitorResourceQuotaAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_product_resource_tag_key_list_with_options(
        self,
        request: cms_20190101_models.DescribeProductResourceTagKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProductResourceTagKeyListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductResourceTagKeyListResponse(),
            self.do_rpcrequest('DescribeProductResourceTagKeyList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_product_resource_tag_key_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeProductResourceTagKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProductResourceTagKeyListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductResourceTagKeyListResponse(),
            await self.do_rpcrequest_async('DescribeProductResourceTagKeyList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_product_resource_tag_key_list(
        self,
        request: cms_20190101_models.DescribeProductResourceTagKeyListRequest,
    ) -> cms_20190101_models.DescribeProductResourceTagKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_product_resource_tag_key_list_with_options(request, runtime)

    async def describe_product_resource_tag_key_list_async(
        self,
        request: cms_20190101_models.DescribeProductResourceTagKeyListRequest,
    ) -> cms_20190101_models.DescribeProductResourceTagKeyListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_product_resource_tag_key_list_with_options_async(request, runtime)

    def describe_products_of_active_metric_rule_with_options(
        self,
        request: cms_20190101_models.DescribeProductsOfActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse(),
            self.do_rpcrequest('DescribeProductsOfActiveMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_products_of_active_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.DescribeProductsOfActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProductsOfActiveMetricRuleResponse(),
            await self.do_rpcrequest_async('DescribeProductsOfActiveMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProjectMetaResponse(),
            self.do_rpcrequest('DescribeProjectMeta', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_project_meta_with_options_async(
        self,
        request: cms_20190101_models.DescribeProjectMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeProjectMetaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeProjectMetaResponse(),
            await self.do_rpcrequest_async('DescribeProjectMeta', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_project_meta(
        self,
        request: cms_20190101_models.DescribeProjectMetaRequest,
    ) -> cms_20190101_models.DescribeProjectMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_project_meta_with_options(request, runtime)

    async def describe_project_meta_async(
        self,
        request: cms_20190101_models.DescribeProjectMetaRequest,
    ) -> cms_20190101_models.DescribeProjectMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_project_meta_with_options_async(request, runtime)

    def describe_site_monitor_attribute_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorAttributeResponse(),
            self.do_rpcrequest('DescribeSiteMonitorAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_site_monitor_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorAttributeResponse(),
            await self.do_rpcrequest_async('DescribeSiteMonitorAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_site_monitor_attribute(
        self,
        request: cms_20190101_models.DescribeSiteMonitorAttributeRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_attribute_with_options(request, runtime)

    async def describe_site_monitor_attribute_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorAttributeRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_site_monitor_attribute_with_options_async(request, runtime)

    def describe_site_monitor_data_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorDataResponse(),
            self.do_rpcrequest('DescribeSiteMonitorData', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_site_monitor_data_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorDataResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorDataResponse(),
            await self.do_rpcrequest_async('DescribeSiteMonitorData', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_site_monitor_list_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorListResponse(),
            self.do_rpcrequest('DescribeSiteMonitorList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_site_monitor_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorListResponse(),
            await self.do_rpcrequest_async('DescribeSiteMonitorList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_site_monitor_list(
        self,
        request: cms_20190101_models.DescribeSiteMonitorListRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_site_monitor_list_with_options(request, runtime)

    async def describe_site_monitor_list_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorListRequest,
    ) -> cms_20190101_models.DescribeSiteMonitorListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_site_monitor_list_with_options_async(request, runtime)

    def describe_site_monitor_quota_with_options(
        self,
        request: cms_20190101_models.DescribeSiteMonitorQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorQuotaResponse(),
            self.do_rpcrequest('DescribeSiteMonitorQuota', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_site_monitor_quota_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorQuotaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorQuotaResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorQuotaResponse(),
            await self.do_rpcrequest_async('DescribeSiteMonitorQuota', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorStatisticsResponse(),
            self.do_rpcrequest('DescribeSiteMonitorStatistics', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_site_monitor_statistics_with_options_async(
        self,
        request: cms_20190101_models.DescribeSiteMonitorStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSiteMonitorStatisticsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSiteMonitorStatisticsResponse(),
            await self.do_rpcrequest_async('DescribeSiteMonitorStatistics', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventAttributeResponse(),
            self.do_rpcrequest('DescribeSystemEventAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_system_event_attribute_with_options_async(
        self,
        request: cms_20190101_models.DescribeSystemEventAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventAttributeResponse(),
            await self.do_rpcrequest_async('DescribeSystemEventAttribute', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventCountResponse(),
            self.do_rpcrequest('DescribeSystemEventCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_system_event_count_with_options_async(
        self,
        request: cms_20190101_models.DescribeSystemEventCountRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventCountResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventCountResponse(),
            await self.do_rpcrequest_async('DescribeSystemEventCount', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_system_event_count(
        self,
        request: cms_20190101_models.DescribeSystemEventCountRequest,
    ) -> cms_20190101_models.DescribeSystemEventCountResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_system_event_count_with_options(request, runtime)

    async def describe_system_event_count_async(
        self,
        request: cms_20190101_models.DescribeSystemEventCountRequest,
    ) -> cms_20190101_models.DescribeSystemEventCountResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_system_event_count_with_options_async(request, runtime)

    def describe_system_event_histogram_with_options(
        self,
        request: cms_20190101_models.DescribeSystemEventHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventHistogramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventHistogramResponse(),
            self.do_rpcrequest('DescribeSystemEventHistogram', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_system_event_histogram_with_options_async(
        self,
        request: cms_20190101_models.DescribeSystemEventHistogramRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeSystemEventHistogramResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeSystemEventHistogramResponse(),
            await self.do_rpcrequest_async('DescribeSystemEventHistogram', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def describe_tag_key_list_with_options(
        self,
        request: cms_20190101_models.DescribeTagKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeTagKeyListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagKeyListResponse(),
            self.do_rpcrequest('DescribeTagKeyList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tag_key_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeTagKeyListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeTagKeyListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagKeyListResponse(),
            await self.do_rpcrequest_async('DescribeTagKeyList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagValueListResponse(),
            self.do_rpcrequest('DescribeTagValueList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_tag_value_list_with_options_async(
        self,
        request: cms_20190101_models.DescribeTagValueListRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeTagValueListResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeTagValueListResponse(),
            await self.do_rpcrequest_async('DescribeTagValueList', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tag_value_list(
        self,
        request: cms_20190101_models.DescribeTagValueListRequest,
    ) -> cms_20190101_models.DescribeTagValueListResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_tag_value_list_with_options(request, runtime)

    async def describe_tag_value_list_async(
        self,
        request: cms_20190101_models.DescribeTagValueListRequest,
    ) -> cms_20190101_models.DescribeTagValueListResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_tag_value_list_with_options_async(request, runtime)

    def describe_unhealthy_host_availability_with_options(
        self,
        request: cms_20190101_models.DescribeUnhealthyHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse(),
            self.do_rpcrequest('DescribeUnhealthyHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_unhealthy_host_availability_with_options_async(
        self,
        request: cms_20190101_models.DescribeUnhealthyHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DescribeUnhealthyHostAvailabilityResponse(),
            await self.do_rpcrequest_async('DescribeUnhealthyHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableActiveMetricRuleResponse(),
            self.do_rpcrequest('DisableActiveMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_active_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.DisableActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableActiveMetricRuleResponse(),
            await self.do_rpcrequest_async('DisableActiveMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableEventRulesResponse(),
            self.do_rpcrequest('DisableEventRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_event_rules_with_options_async(
        self,
        request: cms_20190101_models.DisableEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableEventRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableEventRulesResponse(),
            await self.do_rpcrequest_async('DisableEventRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableHostAvailabilityResponse(),
            self.do_rpcrequest('DisableHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_host_availability_with_options_async(
        self,
        request: cms_20190101_models.DisableHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableHostAvailabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableHostAvailabilityResponse(),
            await self.do_rpcrequest_async('DisableHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableMetricRulesResponse(),
            self.do_rpcrequest('DisableMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.DisableMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableMetricRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableMetricRulesResponse(),
            await self.do_rpcrequest_async('DisableMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableSiteMonitorsResponse(),
            self.do_rpcrequest('DisableSiteMonitors', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_site_monitors_with_options_async(
        self,
        request: cms_20190101_models.DisableSiteMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.DisableSiteMonitorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.DisableSiteMonitorsResponse(),
            await self.do_rpcrequest_async('DisableSiteMonitors', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableActiveMetricRuleResponse(),
            self.do_rpcrequest('EnableActiveMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_active_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.EnableActiveMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableActiveMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableActiveMetricRuleResponse(),
            await self.do_rpcrequest_async('EnableActiveMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableEventRulesResponse(),
            self.do_rpcrequest('EnableEventRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_event_rules_with_options_async(
        self,
        request: cms_20190101_models.EnableEventRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableEventRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableEventRulesResponse(),
            await self.do_rpcrequest_async('EnableEventRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableHostAvailabilityResponse(),
            self.do_rpcrequest('EnableHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_host_availability_with_options_async(
        self,
        request: cms_20190101_models.EnableHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableHostAvailabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableHostAvailabilityResponse(),
            await self.do_rpcrequest_async('EnableHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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

    def enable_metric_rules_with_options(
        self,
        request: cms_20190101_models.EnableMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableMetricRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableMetricRulesResponse(),
            self.do_rpcrequest('EnableMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.EnableMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableMetricRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableMetricRulesResponse(),
            await self.do_rpcrequest_async('EnableMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableSiteMonitorsResponse(),
            self.do_rpcrequest('EnableSiteMonitors', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_site_monitors_with_options_async(
        self,
        request: cms_20190101_models.EnableSiteMonitorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.EnableSiteMonitorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.EnableSiteMonitorsResponse(),
            await self.do_rpcrequest_async('EnableSiteMonitors', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.InstallMonitoringAgentResponse(),
            self.do_rpcrequest('InstallMonitoringAgent', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def install_monitoring_agent_with_options_async(
        self,
        request: cms_20190101_models.InstallMonitoringAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.InstallMonitoringAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.InstallMonitoringAgentResponse(),
            await self.do_rpcrequest_async('InstallMonitoringAgent', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def install_monitoring_agent(
        self,
        request: cms_20190101_models.InstallMonitoringAgentRequest,
    ) -> cms_20190101_models.InstallMonitoringAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.install_monitoring_agent_with_options(request, runtime)

    async def install_monitoring_agent_async(
        self,
        request: cms_20190101_models.InstallMonitoringAgentRequest,
    ) -> cms_20190101_models.InstallMonitoringAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.install_monitoring_agent_with_options_async(request, runtime)

    def modify_group_monitoring_agent_process_with_options(
        self,
        request: cms_20190101_models.ModifyGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse(),
            self.do_rpcrequest('ModifyGroupMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_group_monitoring_agent_process_with_options_async(
        self,
        request: cms_20190101_models.ModifyGroupMonitoringAgentProcessRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyGroupMonitoringAgentProcessResponse(),
            await self.do_rpcrequest_async('ModifyGroupMonitoringAgentProcess', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostAvailabilityResponse(),
            self.do_rpcrequest('ModifyHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_host_availability_with_options_async(
        self,
        request: cms_20190101_models.ModifyHostAvailabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHostAvailabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostAvailabilityResponse(),
            await self.do_rpcrequest_async('ModifyHostAvailability', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_host_availability(
        self,
        request: cms_20190101_models.ModifyHostAvailabilityRequest,
    ) -> cms_20190101_models.ModifyHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_host_availability_with_options(request, runtime)

    async def modify_host_availability_async(
        self,
        request: cms_20190101_models.ModifyHostAvailabilityRequest,
    ) -> cms_20190101_models.ModifyHostAvailabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_availability_with_options_async(request, runtime)

    def modify_host_info_with_options(
        self,
        request: cms_20190101_models.ModifyHostInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHostInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostInfoResponse(),
            self.do_rpcrequest('ModifyHostInfo', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_host_info_with_options_async(
        self,
        request: cms_20190101_models.ModifyHostInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyHostInfoResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyHostInfoResponse(),
            await self.do_rpcrequest_async('ModifyHostInfo', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_host_info(
        self,
        request: cms_20190101_models.ModifyHostInfoRequest,
    ) -> cms_20190101_models.ModifyHostInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_host_info_with_options(request, runtime)

    async def modify_host_info_async(
        self,
        request: cms_20190101_models.ModifyHostInfoRequest,
    ) -> cms_20190101_models.ModifyHostInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_host_info_with_options_async(request, runtime)

    def modify_metric_rule_template_with_options(
        self,
        request: cms_20190101_models.ModifyMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMetricRuleTemplateResponse(),
            self.do_rpcrequest('ModifyMetricRuleTemplate', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_metric_rule_template_with_options_async(
        self,
        request: cms_20190101_models.ModifyMetricRuleTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMetricRuleTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMetricRuleTemplateResponse(),
            await self.do_rpcrequest_async('ModifyMetricRuleTemplate', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_metric_rule_template(
        self,
        request: cms_20190101_models.ModifyMetricRuleTemplateRequest,
    ) -> cms_20190101_models.ModifyMetricRuleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_metric_rule_template_with_options(request, runtime)

    async def modify_metric_rule_template_async(
        self,
        request: cms_20190101_models.ModifyMetricRuleTemplateRequest,
    ) -> cms_20190101_models.ModifyMetricRuleTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_metric_rule_template_with_options_async(request, runtime)

    def modify_monitor_group_with_options(
        self,
        request: cms_20190101_models.ModifyMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMonitorGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupResponse(),
            self.do_rpcrequest('ModifyMonitorGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_monitor_group_with_options_async(
        self,
        request: cms_20190101_models.ModifyMonitorGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMonitorGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupResponse(),
            await self.do_rpcrequest_async('ModifyMonitorGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupInstancesResponse(),
            self.do_rpcrequest('ModifyMonitorGroupInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_monitor_group_instances_with_options_async(
        self,
        request: cms_20190101_models.ModifyMonitorGroupInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifyMonitorGroupInstancesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifyMonitorGroupInstancesResponse(),
            await self.do_rpcrequest_async('ModifyMonitorGroupInstances', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifySiteMonitorResponse(),
            self.do_rpcrequest('ModifySiteMonitor', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_site_monitor_with_options_async(
        self,
        request: cms_20190101_models.ModifySiteMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.ModifySiteMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.ModifySiteMonitorResponse(),
            await self.do_rpcrequest_async('ModifySiteMonitor', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_site_monitor(
        self,
        request: cms_20190101_models.ModifySiteMonitorRequest,
    ) -> cms_20190101_models.ModifySiteMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_site_monitor_with_options(request, runtime)

    async def modify_site_monitor_async(
        self,
        request: cms_20190101_models.ModifySiteMonitorRequest,
    ) -> cms_20190101_models.ModifySiteMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_site_monitor_with_options_async(request, runtime)

    def open_cms_service_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.OpenCmsServiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cms_20190101_models.OpenCmsServiceResponse(),
            self.do_rpcrequest('OpenCmsService', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def open_cms_service_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.OpenCmsServiceResponse:
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            cms_20190101_models.OpenCmsServiceResponse(),
            await self.do_rpcrequest_async('OpenCmsService', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_cms_service(self) -> cms_20190101_models.OpenCmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return self.open_cms_service_with_options(runtime)

    async def open_cms_service_async(self) -> cms_20190101_models.OpenCmsServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.open_cms_service_with_options_async(runtime)

    def put_contact_with_options(
        self,
        request: cms_20190101_models.PutContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactResponse(),
            self.do_rpcrequest('PutContact', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_contact_with_options_async(
        self,
        request: cms_20190101_models.PutContactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutContactResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactResponse(),
            await self.do_rpcrequest_async('PutContact', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactGroupResponse(),
            self.do_rpcrequest('PutContactGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_contact_group_with_options_async(
        self,
        request: cms_20190101_models.PutContactGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutContactGroupResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutContactGroupResponse(),
            await self.do_rpcrequest_async('PutContactGroup', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_contact_group(
        self,
        request: cms_20190101_models.PutContactGroupRequest,
    ) -> cms_20190101_models.PutContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_contact_group_with_options(request, runtime)

    async def put_contact_group_async(
        self,
        request: cms_20190101_models.PutContactGroupRequest,
    ) -> cms_20190101_models.PutContactGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_contact_group_with_options_async(request, runtime)

    def put_custom_event_with_options(
        self,
        request: cms_20190101_models.PutCustomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventResponse(),
            self.do_rpcrequest('PutCustomEvent', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_custom_event_with_options_async(
        self,
        request: cms_20190101_models.PutCustomEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventResponse(),
            await self.do_rpcrequest_async('PutCustomEvent', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventRuleResponse(),
            self.do_rpcrequest('PutCustomEventRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_custom_event_rule_with_options_async(
        self,
        request: cms_20190101_models.PutCustomEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomEventRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomEventRuleResponse(),
            await self.do_rpcrequest_async('PutCustomEventRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_custom_event_rule(
        self,
        request: cms_20190101_models.PutCustomEventRuleRequest,
    ) -> cms_20190101_models.PutCustomEventRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_custom_event_rule_with_options(request, runtime)

    async def put_custom_event_rule_async(
        self,
        request: cms_20190101_models.PutCustomEventRuleRequest,
    ) -> cms_20190101_models.PutCustomEventRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_custom_event_rule_with_options_async(request, runtime)

    def put_custom_metric_with_options(
        self,
        request: cms_20190101_models.PutCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricResponse(),
            self.do_rpcrequest('PutCustomMetric', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_custom_metric_with_options_async(
        self,
        request: cms_20190101_models.PutCustomMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricResponse(),
            await self.do_rpcrequest_async('PutCustomMetric', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_custom_metric(
        self,
        request: cms_20190101_models.PutCustomMetricRequest,
    ) -> cms_20190101_models.PutCustomMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_custom_metric_with_options(request, runtime)

    async def put_custom_metric_async(
        self,
        request: cms_20190101_models.PutCustomMetricRequest,
    ) -> cms_20190101_models.PutCustomMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_custom_metric_with_options_async(request, runtime)

    def put_custom_metric_rule_with_options(
        self,
        request: cms_20190101_models.PutCustomMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricRuleResponse(),
            self.do_rpcrequest('PutCustomMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_custom_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.PutCustomMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutCustomMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutCustomMetricRuleResponse(),
            await self.do_rpcrequest_async('PutCustomMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_custom_metric_rule(
        self,
        request: cms_20190101_models.PutCustomMetricRuleRequest,
    ) -> cms_20190101_models.PutCustomMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_custom_metric_rule_with_options(request, runtime)

    async def put_custom_metric_rule_async(
        self,
        request: cms_20190101_models.PutCustomMetricRuleRequest,
    ) -> cms_20190101_models.PutCustomMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_custom_metric_rule_with_options_async(request, runtime)

    def put_event_rule_with_options(
        self,
        request: cms_20190101_models.PutEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutEventRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleResponse(),
            self.do_rpcrequest('PutEventRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_event_rule_with_options_async(
        self,
        request: cms_20190101_models.PutEventRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutEventRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleResponse(),
            await self.do_rpcrequest_async('PutEventRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_event_rule(
        self,
        request: cms_20190101_models.PutEventRuleRequest,
    ) -> cms_20190101_models.PutEventRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_event_rule_with_options(request, runtime)

    async def put_event_rule_async(
        self,
        request: cms_20190101_models.PutEventRuleRequest,
    ) -> cms_20190101_models.PutEventRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_event_rule_with_options_async(request, runtime)

    def put_event_rule_targets_with_options(
        self,
        request: cms_20190101_models.PutEventRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutEventRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleTargetsResponse(),
            self.do_rpcrequest('PutEventRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_event_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.PutEventRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutEventRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutEventRuleTargetsResponse(),
            await self.do_rpcrequest_async('PutEventRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterOutputResponse(),
            self.do_rpcrequest('PutExporterOutput', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_exporter_output_with_options_async(
        self,
        request: cms_20190101_models.PutExporterOutputRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutExporterOutputResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterOutputResponse(),
            await self.do_rpcrequest_async('PutExporterOutput', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_exporter_output(
        self,
        request: cms_20190101_models.PutExporterOutputRequest,
    ) -> cms_20190101_models.PutExporterOutputResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_exporter_output_with_options(request, runtime)

    async def put_exporter_output_async(
        self,
        request: cms_20190101_models.PutExporterOutputRequest,
    ) -> cms_20190101_models.PutExporterOutputResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_exporter_output_with_options_async(request, runtime)

    def put_exporter_rule_with_options(
        self,
        request: cms_20190101_models.PutExporterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutExporterRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterRuleResponse(),
            self.do_rpcrequest('PutExporterRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_exporter_rule_with_options_async(
        self,
        request: cms_20190101_models.PutExporterRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutExporterRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutExporterRuleResponse(),
            await self.do_rpcrequest_async('PutExporterRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutGroupMetricRuleResponse(),
            self.do_rpcrequest('PutGroupMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_group_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.PutGroupMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutGroupMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutGroupMetricRuleResponse(),
            await self.do_rpcrequest_async('PutGroupMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_group_metric_rule(
        self,
        request: cms_20190101_models.PutGroupMetricRuleRequest,
    ) -> cms_20190101_models.PutGroupMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_group_metric_rule_with_options(request, runtime)

    async def put_group_metric_rule_async(
        self,
        request: cms_20190101_models.PutGroupMetricRuleRequest,
    ) -> cms_20190101_models.PutGroupMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_group_metric_rule_with_options_async(request, runtime)

    def put_log_monitor_with_options(
        self,
        request: cms_20190101_models.PutLogMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutLogMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutLogMonitorResponse(),
            self.do_rpcrequest('PutLogMonitor', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_log_monitor_with_options_async(
        self,
        request: cms_20190101_models.PutLogMonitorRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutLogMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutLogMonitorResponse(),
            await self.do_rpcrequest_async('PutLogMonitor', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_log_monitor(
        self,
        request: cms_20190101_models.PutLogMonitorRequest,
    ) -> cms_20190101_models.PutLogMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_log_monitor_with_options(request, runtime)

    async def put_log_monitor_async(
        self,
        request: cms_20190101_models.PutLogMonitorRequest,
    ) -> cms_20190101_models.PutLogMonitorResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_log_monitor_with_options_async(request, runtime)

    def put_metric_rule_targets_with_options(
        self,
        request: cms_20190101_models.PutMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMetricRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMetricRuleTargetsResponse(),
            self.do_rpcrequest('PutMetricRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_metric_rule_targets_with_options_async(
        self,
        request: cms_20190101_models.PutMetricRuleTargetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMetricRuleTargetsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMetricRuleTargetsResponse(),
            await self.do_rpcrequest_async('PutMetricRuleTargets', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_metric_rule_targets(
        self,
        request: cms_20190101_models.PutMetricRuleTargetsRequest,
    ) -> cms_20190101_models.PutMetricRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_metric_rule_targets_with_options(request, runtime)

    async def put_metric_rule_targets_async(
        self,
        request: cms_20190101_models.PutMetricRuleTargetsRequest,
    ) -> cms_20190101_models.PutMetricRuleTargetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_metric_rule_targets_with_options_async(request, runtime)

    def put_monitor_group_dynamic_rule_with_options(
        self,
        request: cms_20190101_models.PutMonitorGroupDynamicRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMonitorGroupDynamicRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitorGroupDynamicRuleResponse(),
            self.do_rpcrequest('PutMonitorGroupDynamicRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_monitor_group_dynamic_rule_with_options_async(
        self,
        request: cms_20190101_models.PutMonitorGroupDynamicRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMonitorGroupDynamicRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitorGroupDynamicRuleResponse(),
            await self.do_rpcrequest_async('PutMonitorGroupDynamicRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitoringConfigResponse(),
            self.do_rpcrequest('PutMonitoringConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_monitoring_config_with_options_async(
        self,
        request: cms_20190101_models.PutMonitoringConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutMonitoringConfigResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutMonitoringConfigResponse(),
            await self.do_rpcrequest_async('PutMonitoringConfig', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        request: cms_20190101_models.PutResourceMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutResourceMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRuleResponse(),
            self.do_rpcrequest('PutResourceMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_resource_metric_rule_with_options_async(
        self,
        request: cms_20190101_models.PutResourceMetricRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutResourceMetricRuleResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRuleResponse(),
            await self.do_rpcrequest_async('PutResourceMetricRule', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_resource_metric_rule(
        self,
        request: cms_20190101_models.PutResourceMetricRuleRequest,
    ) -> cms_20190101_models.PutResourceMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_resource_metric_rule_with_options(request, runtime)

    async def put_resource_metric_rule_async(
        self,
        request: cms_20190101_models.PutResourceMetricRuleRequest,
    ) -> cms_20190101_models.PutResourceMetricRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_resource_metric_rule_with_options_async(request, runtime)

    def put_resource_metric_rules_with_options(
        self,
        request: cms_20190101_models.PutResourceMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutResourceMetricRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRulesResponse(),
            self.do_rpcrequest('PutResourceMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def put_resource_metric_rules_with_options_async(
        self,
        request: cms_20190101_models.PutResourceMetricRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.PutResourceMetricRulesResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.PutResourceMetricRulesResponse(),
            await self.do_rpcrequest_async('PutResourceMetricRules', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_resource_metric_rules(
        self,
        request: cms_20190101_models.PutResourceMetricRulesRequest,
    ) -> cms_20190101_models.PutResourceMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_resource_metric_rules_with_options(request, runtime)

    async def put_resource_metric_rules_async(
        self,
        request: cms_20190101_models.PutResourceMetricRulesRequest,
    ) -> cms_20190101_models.PutResourceMetricRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_resource_metric_rules_with_options_async(request, runtime)

    def remove_tags_with_options(
        self,
        request: cms_20190101_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.RemoveTagsResponse(),
            self.do_rpcrequest('RemoveTags', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def remove_tags_with_options_async(
        self,
        request: cms_20190101_models.RemoveTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.RemoveTagsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.RemoveTagsResponse(),
            await self.do_rpcrequest_async('RemoveTags', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
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
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.SendDryRunSystemEventResponse(),
            self.do_rpcrequest('SendDryRunSystemEvent', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def send_dry_run_system_event_with_options_async(
        self,
        request: cms_20190101_models.SendDryRunSystemEventRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.SendDryRunSystemEventResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.SendDryRunSystemEventResponse(),
            await self.do_rpcrequest_async('SendDryRunSystemEvent', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_dry_run_system_event(
        self,
        request: cms_20190101_models.SendDryRunSystemEventRequest,
    ) -> cms_20190101_models.SendDryRunSystemEventResponse:
        runtime = util_models.RuntimeOptions()
        return self.send_dry_run_system_event_with_options(request, runtime)

    async def send_dry_run_system_event_async(
        self,
        request: cms_20190101_models.SendDryRunSystemEventRequest,
    ) -> cms_20190101_models.SendDryRunSystemEventResponse:
        runtime = util_models.RuntimeOptions()
        return await self.send_dry_run_system_event_with_options_async(request, runtime)

    def uninstall_monitoring_agent_with_options(
        self,
        request: cms_20190101_models.UninstallMonitoringAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.UninstallMonitoringAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.UninstallMonitoringAgentResponse(),
            self.do_rpcrequest('UninstallMonitoringAgent', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def uninstall_monitoring_agent_with_options_async(
        self,
        request: cms_20190101_models.UninstallMonitoringAgentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> cms_20190101_models.UninstallMonitoringAgentResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            cms_20190101_models.UninstallMonitoringAgentResponse(),
            await self.do_rpcrequest_async('UninstallMonitoringAgent', '2019-01-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def uninstall_monitoring_agent(
        self,
        request: cms_20190101_models.UninstallMonitoringAgentRequest,
    ) -> cms_20190101_models.UninstallMonitoringAgentResponse:
        runtime = util_models.RuntimeOptions()
        return self.uninstall_monitoring_agent_with_options(request, runtime)

    async def uninstall_monitoring_agent_async(
        self,
        request: cms_20190101_models.UninstallMonitoringAgentRequest,
    ) -> cms_20190101_models.UninstallMonitoringAgentResponse:
        runtime = util_models.RuntimeOptions()
        return await self.uninstall_monitoring_agent_with_options_async(request, runtime)
