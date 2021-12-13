# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_config20190108 import models as config_20190108_models
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
        self._endpoint_map = {
            'cn-shanghai': 'config.cn-shanghai.aliyuncs.com',
            'ap-southeast-1': 'config.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('config', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def active_config_rules_with_options(
        self,
        request: config_20190108_models.ActiveConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ActiveConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ActiveConfigRules',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ActiveConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def active_config_rules_with_options_async(
        self,
        request: config_20190108_models.ActiveConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ActiveConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ActiveConfigRules',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ActiveConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def active_config_rules(
        self,
        request: config_20190108_models.ActiveConfigRulesRequest,
    ) -> config_20190108_models.ActiveConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.active_config_rules_with_options(request, runtime)

    async def active_config_rules_async(
        self,
        request: config_20190108_models.ActiveConfigRulesRequest,
    ) -> config_20190108_models.ActiveConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.active_config_rules_with_options_async(request, runtime)

    def delete_config_rules_with_options(
        self,
        request: config_20190108_models.DeleteConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DeleteConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteConfigRules',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DeleteConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_config_rules_with_options_async(
        self,
        request: config_20190108_models.DeleteConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DeleteConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteConfigRules',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DeleteConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_config_rules(
        self,
        request: config_20190108_models.DeleteConfigRulesRequest,
    ) -> config_20190108_models.DeleteConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_config_rules_with_options(request, runtime)

    async def delete_config_rules_async(
        self,
        request: config_20190108_models.DeleteConfigRulesRequest,
    ) -> config_20190108_models.DeleteConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_config_rules_with_options_async(request, runtime)

    def describe_compliance_with_options(
        self,
        request: config_20190108_models.DescribeComplianceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeComplianceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCompliance',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeComplianceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_compliance_with_options_async(
        self,
        request: config_20190108_models.DescribeComplianceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeComplianceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCompliance',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeComplianceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_compliance(
        self,
        request: config_20190108_models.DescribeComplianceRequest,
    ) -> config_20190108_models.DescribeComplianceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_compliance_with_options(request, runtime)

    async def describe_compliance_async(
        self,
        request: config_20190108_models.DescribeComplianceRequest,
    ) -> config_20190108_models.DescribeComplianceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_compliance_with_options_async(request, runtime)

    def describe_compliance_summary_with_options(
        self,
        request: config_20190108_models.DescribeComplianceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeComplianceSummaryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComplianceSummary',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeComplianceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_compliance_summary_with_options_async(
        self,
        request: config_20190108_models.DescribeComplianceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeComplianceSummaryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeComplianceSummary',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeComplianceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_compliance_summary(
        self,
        request: config_20190108_models.DescribeComplianceSummaryRequest,
    ) -> config_20190108_models.DescribeComplianceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_compliance_summary_with_options(request, runtime)

    async def describe_compliance_summary_async(
        self,
        request: config_20190108_models.DescribeComplianceSummaryRequest,
    ) -> config_20190108_models.DescribeComplianceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_compliance_summary_with_options_async(request, runtime)

    def describe_config_rule_with_options(
        self,
        request: config_20190108_models.DescribeConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigRule',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_config_rule_with_options_async(
        self,
        request: config_20190108_models.DescribeConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeConfigRuleResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConfigRule',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_config_rule(
        self,
        request: config_20190108_models.DescribeConfigRuleRequest,
    ) -> config_20190108_models.DescribeConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_config_rule_with_options(request, runtime)

    async def describe_config_rule_async(
        self,
        request: config_20190108_models.DescribeConfigRuleRequest,
    ) -> config_20190108_models.DescribeConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_config_rule_with_options_async(request, runtime)

    def describe_configuration_recorder_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeConfigurationRecorderResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeConfigurationRecorder',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_configuration_recorder_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeConfigurationRecorderResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeConfigurationRecorder',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_configuration_recorder(self) -> config_20190108_models.DescribeConfigurationRecorderResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_configuration_recorder_with_options(runtime)

    async def describe_configuration_recorder_async(self) -> config_20190108_models.DescribeConfigurationRecorderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_configuration_recorder_with_options_async(runtime)

    def describe_delivery_channels_with_options(
        self,
        request: config_20190108_models.DescribeDeliveryChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeDeliveryChannelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeliveryChannels',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeDeliveryChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_delivery_channels_with_options_async(
        self,
        request: config_20190108_models.DescribeDeliveryChannelsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeDeliveryChannelsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeliveryChannels',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeDeliveryChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_delivery_channels(
        self,
        request: config_20190108_models.DescribeDeliveryChannelsRequest,
    ) -> config_20190108_models.DescribeDeliveryChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_delivery_channels_with_options(request, runtime)

    async def describe_delivery_channels_async(
        self,
        request: config_20190108_models.DescribeDeliveryChannelsRequest,
    ) -> config_20190108_models.DescribeDeliveryChannelsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_delivery_channels_with_options_async(request, runtime)

    def describe_discovered_resource_with_options(
        self,
        request: config_20190108_models.DescribeDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeDiscoveredResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiscoveredResource',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_discovered_resource_with_options_async(
        self,
        request: config_20190108_models.DescribeDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeDiscoveredResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDiscoveredResource',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_discovered_resource(
        self,
        request: config_20190108_models.DescribeDiscoveredResourceRequest,
    ) -> config_20190108_models.DescribeDiscoveredResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_discovered_resource_with_options(request, runtime)

    async def describe_discovered_resource_async(
        self,
        request: config_20190108_models.DescribeDiscoveredResourceRequest,
    ) -> config_20190108_models.DescribeDiscoveredResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_discovered_resource_with_options_async(request, runtime)

    def describe_evaluation_results_with_options(
        self,
        request: config_20190108_models.DescribeEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvaluationResults',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_evaluation_results_with_options_async(
        self,
        request: config_20190108_models.DescribeEvaluationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.DescribeEvaluationResultsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEvaluationResults',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.DescribeEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_evaluation_results(
        self,
        request: config_20190108_models.DescribeEvaluationResultsRequest,
    ) -> config_20190108_models.DescribeEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluation_results_with_options(request, runtime)

    async def describe_evaluation_results_async(
        self,
        request: config_20190108_models.DescribeEvaluationResultsRequest,
    ) -> config_20190108_models.DescribeEvaluationResultsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_evaluation_results_with_options_async(request, runtime)

    def get_aggregate_discovered_resource_with_options(
        self,
        request: config_20190108_models.GetAggregateDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetAggregateDiscoveredResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateDiscoveredResource',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetAggregateDiscoveredResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aggregate_discovered_resource_with_options_async(
        self,
        request: config_20190108_models.GetAggregateDiscoveredResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetAggregateDiscoveredResourceResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAggregateDiscoveredResource',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetAggregateDiscoveredResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aggregate_discovered_resource(
        self,
        request: config_20190108_models.GetAggregateDiscoveredResourceRequest,
    ) -> config_20190108_models.GetAggregateDiscoveredResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_aggregate_discovered_resource_with_options(request, runtime)

    async def get_aggregate_discovered_resource_async(
        self,
        request: config_20190108_models.GetAggregateDiscoveredResourceRequest,
    ) -> config_20190108_models.GetAggregateDiscoveredResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_aggregate_discovered_resource_with_options_async(request, runtime)

    def get_discovered_resource_counts_with_options(
        self,
        request: config_20190108_models.GetDiscoveredResourceCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetDiscoveredResourceCountsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCounts',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetDiscoveredResourceCountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_counts_with_options_async(
        self,
        request: config_20190108_models.GetDiscoveredResourceCountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetDiscoveredResourceCountsResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceCounts',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetDiscoveredResourceCountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource_counts(
        self,
        request: config_20190108_models.GetDiscoveredResourceCountsRequest,
    ) -> config_20190108_models.GetDiscoveredResourceCountsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_counts_with_options(request, runtime)

    async def get_discovered_resource_counts_async(
        self,
        request: config_20190108_models.GetDiscoveredResourceCountsRequest,
    ) -> config_20190108_models.GetDiscoveredResourceCountsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_discovered_resource_counts_with_options_async(request, runtime)

    def get_discovered_resource_summary_with_options(
        self,
        request: config_20190108_models.GetDiscoveredResourceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetDiscoveredResourceSummaryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceSummary',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetDiscoveredResourceSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_discovered_resource_summary_with_options_async(
        self,
        request: config_20190108_models.GetDiscoveredResourceSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetDiscoveredResourceSummaryResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDiscoveredResourceSummary',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetDiscoveredResourceSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_discovered_resource_summary(
        self,
        request: config_20190108_models.GetDiscoveredResourceSummaryRequest,
    ) -> config_20190108_models.GetDiscoveredResourceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_summary_with_options(request, runtime)

    async def get_discovered_resource_summary_async(
        self,
        request: config_20190108_models.GetDiscoveredResourceSummaryRequest,
    ) -> config_20190108_models.GetDiscoveredResourceSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_discovered_resource_summary_with_options_async(request, runtime)

    def get_resource_compliance_timeline_with_options(
        self,
        request: config_20190108_models.GetResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetResourceComplianceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceTimeline',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetResourceComplianceTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_compliance_timeline_with_options_async(
        self,
        request: config_20190108_models.GetResourceComplianceTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetResourceComplianceTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceComplianceTimeline',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetResourceComplianceTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_compliance_timeline(
        self,
        request: config_20190108_models.GetResourceComplianceTimelineRequest,
    ) -> config_20190108_models.GetResourceComplianceTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_timeline_with_options(request, runtime)

    async def get_resource_compliance_timeline_async(
        self,
        request: config_20190108_models.GetResourceComplianceTimelineRequest,
    ) -> config_20190108_models.GetResourceComplianceTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_compliance_timeline_with_options_async(request, runtime)

    def get_resource_configuration_timeline_with_options(
        self,
        request: config_20190108_models.GetResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetResourceConfigurationTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceConfigurationTimeline',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetResourceConfigurationTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_configuration_timeline_with_options_async(
        self,
        request: config_20190108_models.GetResourceConfigurationTimelineRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetResourceConfigurationTimelineResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceConfigurationTimeline',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetResourceConfigurationTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_configuration_timeline(
        self,
        request: config_20190108_models.GetResourceConfigurationTimelineRequest,
    ) -> config_20190108_models.GetResourceConfigurationTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_configuration_timeline_with_options(request, runtime)

    async def get_resource_configuration_timeline_async(
        self,
        request: config_20190108_models.GetResourceConfigurationTimelineRequest,
    ) -> config_20190108_models.GetResourceConfigurationTimelineResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_configuration_timeline_with_options_async(request, runtime)

    def get_supported_resource_types_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetSupportedResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSupportedResourceTypes',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetSupportedResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supported_resource_types_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.GetSupportedResourceTypesResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSupportedResourceTypes',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.GetSupportedResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supported_resource_types(self) -> config_20190108_models.GetSupportedResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_supported_resource_types_with_options(runtime)

    async def get_supported_resource_types_async(self) -> config_20190108_models.GetSupportedResourceTypesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_supported_resource_types_with_options_async(runtime)

    def list_aggregate_discovered_resources_with_options(
        self,
        request: config_20190108_models.ListAggregateDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ListAggregateDiscoveredResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateDiscoveredResources',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ListAggregateDiscoveredResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aggregate_discovered_resources_with_options_async(
        self,
        request: config_20190108_models.ListAggregateDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ListAggregateDiscoveredResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAggregateDiscoveredResources',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ListAggregateDiscoveredResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aggregate_discovered_resources(
        self,
        request: config_20190108_models.ListAggregateDiscoveredResourcesRequest,
    ) -> config_20190108_models.ListAggregateDiscoveredResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_aggregate_discovered_resources_with_options(request, runtime)

    async def list_aggregate_discovered_resources_async(
        self,
        request: config_20190108_models.ListAggregateDiscoveredResourcesRequest,
    ) -> config_20190108_models.ListAggregateDiscoveredResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_aggregate_discovered_resources_with_options_async(request, runtime)

    def list_config_rules_with_options(
        self,
        request: config_20190108_models.ListConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ListConfigRulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigRules',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ListConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_rules_with_options_async(
        self,
        request: config_20190108_models.ListConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ListConfigRulesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConfigRules',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ListConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_rules(
        self,
        request: config_20190108_models.ListConfigRulesRequest,
    ) -> config_20190108_models.ListConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_config_rules_with_options(request, runtime)

    async def list_config_rules_async(
        self,
        request: config_20190108_models.ListConfigRulesRequest,
    ) -> config_20190108_models.ListConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_rules_with_options_async(request, runtime)

    def list_discovered_resources_with_options(
        self,
        request: config_20190108_models.ListDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ListDiscoveredResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiscoveredResources',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ListDiscoveredResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_discovered_resources_with_options_async(
        self,
        request: config_20190108_models.ListDiscoveredResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ListDiscoveredResourcesResponse:
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDiscoveredResources',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ListDiscoveredResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_discovered_resources(
        self,
        request: config_20190108_models.ListDiscoveredResourcesRequest,
    ) -> config_20190108_models.ListDiscoveredResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_discovered_resources_with_options(request, runtime)

    async def list_discovered_resources_async(
        self,
        request: config_20190108_models.ListDiscoveredResourcesRequest,
    ) -> config_20190108_models.ListDiscoveredResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_discovered_resources_with_options_async(request, runtime)

    def list_remediation_templates_with_options(
        self,
        request: config_20190108_models.ListRemediationTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ListRemediationTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ManagedRuleIdentifier'] = request.managed_rule_identifier
        query['RemediationType'] = request.remediation_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListRemediationTemplates',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ListRemediationTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_remediation_templates_with_options_async(
        self,
        request: config_20190108_models.ListRemediationTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.ListRemediationTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ManagedRuleIdentifier'] = request.managed_rule_identifier
        query['RemediationType'] = request.remediation_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ListRemediationTemplates',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.ListRemediationTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_remediation_templates(
        self,
        request: config_20190108_models.ListRemediationTemplatesRequest,
    ) -> config_20190108_models.ListRemediationTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_remediation_templates_with_options(request, runtime)

    async def list_remediation_templates_async(
        self,
        request: config_20190108_models.ListRemediationTemplatesRequest,
    ) -> config_20190108_models.ListRemediationTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_remediation_templates_with_options_async(request, runtime)

    def put_config_rule_with_options(
        self,
        request: config_20190108_models.PutConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.PutConfigRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MemberId'] = request.member_id
        query['MultiAccount'] = request.multi_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutConfigRule',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.PutConfigRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_config_rule_with_options_async(
        self,
        request: config_20190108_models.PutConfigRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.PutConfigRuleResponse:
        UtilClient.validate_model(request)
        query = {}
        query['MemberId'] = request.member_id
        query['MultiAccount'] = request.multi_account
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutConfigRule',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.PutConfigRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_config_rule(
        self,
        request: config_20190108_models.PutConfigRuleRequest,
    ) -> config_20190108_models.PutConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_config_rule_with_options(request, runtime)

    async def put_config_rule_async(
        self,
        request: config_20190108_models.PutConfigRuleRequest,
    ) -> config_20190108_models.PutConfigRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_config_rule_with_options_async(request, runtime)

    def put_configuration_recorder_with_options(
        self,
        request: config_20190108_models.PutConfigurationRecorderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.PutConfigurationRecorderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutConfigurationRecorder',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.PutConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_configuration_recorder_with_options_async(
        self,
        request: config_20190108_models.PutConfigurationRecorderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.PutConfigurationRecorderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutConfigurationRecorder',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.PutConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_configuration_recorder(
        self,
        request: config_20190108_models.PutConfigurationRecorderRequest,
    ) -> config_20190108_models.PutConfigurationRecorderResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_configuration_recorder_with_options(request, runtime)

    async def put_configuration_recorder_async(
        self,
        request: config_20190108_models.PutConfigurationRecorderRequest,
    ) -> config_20190108_models.PutConfigurationRecorderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_configuration_recorder_with_options_async(request, runtime)

    def put_delivery_channel_with_options(
        self,
        request: config_20190108_models.PutDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.PutDeliveryChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutDeliveryChannel',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.PutDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_delivery_channel_with_options_async(
        self,
        request: config_20190108_models.PutDeliveryChannelRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.PutDeliveryChannelResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutDeliveryChannel',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.PutDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_delivery_channel(
        self,
        request: config_20190108_models.PutDeliveryChannelRequest,
    ) -> config_20190108_models.PutDeliveryChannelResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_delivery_channel_with_options(request, runtime)

    async def put_delivery_channel_async(
        self,
        request: config_20190108_models.PutDeliveryChannelRequest,
    ) -> config_20190108_models.PutDeliveryChannelResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_delivery_channel_with_options_async(request, runtime)

    def put_evaluations_with_options(
        self,
        request: config_20190108_models.PutEvaluationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.PutEvaluationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutEvaluations',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.PutEvaluationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def put_evaluations_with_options_async(
        self,
        request: config_20190108_models.PutEvaluationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.PutEvaluationsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='PutEvaluations',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.PutEvaluationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def put_evaluations(
        self,
        request: config_20190108_models.PutEvaluationsRequest,
    ) -> config_20190108_models.PutEvaluationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.put_evaluations_with_options(request, runtime)

    async def put_evaluations_async(
        self,
        request: config_20190108_models.PutEvaluationsRequest,
    ) -> config_20190108_models.PutEvaluationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.put_evaluations_with_options_async(request, runtime)

    def start_config_rule_evaluation_with_options(
        self,
        request: config_20190108_models.StartConfigRuleEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.StartConfigRuleEvaluationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleId'] = request.config_rule_id
        query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartConfigRuleEvaluation',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.StartConfigRuleEvaluationResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_config_rule_evaluation_with_options_async(
        self,
        request: config_20190108_models.StartConfigRuleEvaluationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.StartConfigRuleEvaluationResponse:
        UtilClient.validate_model(request)
        query = {}
        query['CompliancePackId'] = request.compliance_pack_id
        query['ConfigRuleId'] = request.config_rule_id
        query['RevertEvaluation'] = request.revert_evaluation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartConfigRuleEvaluation',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.StartConfigRuleEvaluationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_config_rule_evaluation(
        self,
        request: config_20190108_models.StartConfigRuleEvaluationRequest,
    ) -> config_20190108_models.StartConfigRuleEvaluationResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_config_rule_evaluation_with_options(request, runtime)

    async def start_config_rule_evaluation_async(
        self,
        request: config_20190108_models.StartConfigRuleEvaluationRequest,
    ) -> config_20190108_models.StartConfigRuleEvaluationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_config_rule_evaluation_with_options_async(request, runtime)

    def start_configuration_recorder_with_options(
        self,
        request: config_20190108_models.StartConfigurationRecorderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.StartConfigurationRecorderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartConfigurationRecorder',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.StartConfigurationRecorderResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_configuration_recorder_with_options_async(
        self,
        request: config_20190108_models.StartConfigurationRecorderRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.StartConfigurationRecorderResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartConfigurationRecorder',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.StartConfigurationRecorderResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_configuration_recorder(
        self,
        request: config_20190108_models.StartConfigurationRecorderRequest,
    ) -> config_20190108_models.StartConfigurationRecorderResponse:
        runtime = util_models.RuntimeOptions()
        return self.start_configuration_recorder_with_options(request, runtime)

    async def start_configuration_recorder_async(
        self,
        request: config_20190108_models.StartConfigurationRecorderRequest,
    ) -> config_20190108_models.StartConfigurationRecorderResponse:
        runtime = util_models.RuntimeOptions()
        return await self.start_configuration_recorder_with_options_async(request, runtime)

    def stop_config_rules_with_options(
        self,
        request: config_20190108_models.StopConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.StopConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopConfigRules',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.StopConfigRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_config_rules_with_options_async(
        self,
        request: config_20190108_models.StopConfigRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> config_20190108_models.StopConfigRulesResponse:
        UtilClient.validate_model(request)
        query = {}
        query['ConfigRuleIds'] = request.config_rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopConfigRules',
            version='2019-01-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            config_20190108_models.StopConfigRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_config_rules(
        self,
        request: config_20190108_models.StopConfigRulesRequest,
    ) -> config_20190108_models.StopConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_config_rules_with_options(request, runtime)

    async def stop_config_rules_async(
        self,
        request: config_20190108_models.StopConfigRulesRequest,
    ) -> config_20190108_models.StopConfigRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_config_rules_with_options_async(request, runtime)
