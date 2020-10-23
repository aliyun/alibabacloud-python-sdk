# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_config20190108 import models as config_20190108_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_tea_util import models as util_models
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = "central"
        self._endpoint_map = {
            "cn-shanghai": "config.cn-shanghai.aliyuncs.com",
            "ap-southeast-1": "config.ap-southeast-1.aliyuncs.com"
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint("config", self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_resource_compliance_timeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.GetResourceComplianceTimelineResponse().from_map(self.do_request("GetResourceComplianceTimeline", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def get_resource_compliance_timeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_compliance_timeline_with_options(request, runtime)

    def get_resource_configuration_timeline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.GetResourceConfigurationTimelineResponse().from_map(self.do_request("GetResourceConfigurationTimeline", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def get_resource_configuration_timeline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_configuration_timeline_with_options(request, runtime)

    def describe_delivery_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.DescribeDeliveryChannelsResponse().from_map(self.do_request("DescribeDeliveryChannels", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def describe_delivery_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_delivery_channels_with_options(request, runtime)

    def put_configuration_recorder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.PutConfigurationRecorderResponse().from_map(self.do_request("PutConfigurationRecorder", "HTTPS", "POST", "2019-01-08", "AK", None, request.to_map(), runtime))

    def put_configuration_recorder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_configuration_recorder_with_options(request, runtime)

    def get_discovered_resource_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.GetDiscoveredResourceSummaryResponse().from_map(self.do_request("GetDiscoveredResourceSummary", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def get_discovered_resource_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_summary_with_options(request, runtime)

    def active_config_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.ActiveConfigRulesResponse().from_map(self.do_request("ActiveConfigRules", "HTTPS", "POST", "2019-01-08", "AK", None, request.to_map(), runtime))

    def active_config_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.active_config_rules_with_options(request, runtime)

    def stop_config_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.StopConfigRulesResponse().from_map(self.do_request("StopConfigRules", "HTTPS", "POST", "2019-01-08", "AK", None, request.to_map(), runtime))

    def stop_config_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_config_rules_with_options(request, runtime)

    def describe_compliance_summary_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.DescribeComplianceSummaryResponse().from_map(self.do_request("DescribeComplianceSummary", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def describe_compliance_summary(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_compliance_summary_with_options(request, runtime)

    def list_config_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.ListConfigRulesResponse().from_map(self.do_request("ListConfigRules", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def list_config_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_config_rules_with_options(request, runtime)

    def put_config_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.PutConfigRuleResponse().from_map(self.do_request("PutConfigRule", "HTTPS", "POST", "2019-01-08", "AK", None, request.to_map(), runtime))

    def put_config_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_config_rule_with_options(request, runtime)

    def describe_evaluation_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.DescribeEvaluationResultsResponse().from_map(self.do_request("DescribeEvaluationResults", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def describe_evaluation_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_evaluation_results_with_options(request, runtime)

    def delete_config_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.DeleteConfigRulesResponse().from_map(self.do_request("DeleteConfigRules", "HTTPS", "POST", "2019-01-08", "AK", None, request.to_map(), runtime))

    def delete_config_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_config_rules_with_options(request, runtime)

    def describe_compliance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.DescribeComplianceResponse().from_map(self.do_request("DescribeCompliance", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def describe_compliance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_compliance_with_options(request, runtime)

    def get_discovered_resource_counts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.GetDiscoveredResourceCountsResponse().from_map(self.do_request("GetDiscoveredResourceCounts", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def get_discovered_resource_counts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_discovered_resource_counts_with_options(request, runtime)

    def list_discovered_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.ListDiscoveredResourcesResponse().from_map(self.do_request("ListDiscoveredResources", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def list_discovered_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_discovered_resources_with_options(request, runtime)

    def describe_configuration_recorder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.DescribeConfigurationRecorderResponse().from_map(self.do_request("DescribeConfigurationRecorder", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def describe_configuration_recorder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_configuration_recorder_with_options(request, runtime)

    def describe_discovered_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.DescribeDiscoveredResourceResponse().from_map(self.do_request("DescribeDiscoveredResource", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def describe_discovered_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_discovered_resource_with_options(request, runtime)

    def start_configuration_recorder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.StartConfigurationRecorderResponse().from_map(self.do_request("StartConfigurationRecorder", "HTTPS", "POST", "2019-01-08", "AK", None, request.to_map(), runtime))

    def start_configuration_recorder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_configuration_recorder_with_options(request, runtime)

    def describe_config_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.DescribeConfigRuleResponse().from_map(self.do_request("DescribeConfigRule", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def describe_config_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_config_rule_with_options(request, runtime)

    def get_supported_resource_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.GetSupportedResourceTypesResponse().from_map(self.do_request("GetSupportedResourceTypes", "HTTPS", "GET", "2019-01-08", "AK", request.to_map(), None, runtime))

    def get_supported_resource_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_supported_resource_types_with_options(request, runtime)

    def put_delivery_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.PutDeliveryChannelResponse().from_map(self.do_request("PutDeliveryChannel", "HTTPS", "POST", "2019-01-08", "AK", None, request.to_map(), runtime))

    def put_delivery_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_delivery_channel_with_options(request, runtime)

    def put_evaluations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.PutEvaluationsResponse().from_map(self.do_request("PutEvaluations", "HTTPS", "POST", "2019-01-08", "AK", None, request.to_map(), runtime))

    def put_evaluations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_evaluations_with_options(request, runtime)

    def start_config_rule_evaluation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return config_20190108_models.StartConfigRuleEvaluationResponse().from_map(self.do_request("StartConfigRuleEvaluation", "HTTPS", "POST", "2019-01-08", "AK", None, request.to_map(), runtime))

    def start_config_rule_evaluation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_config_rule_evaluation_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get('regionId')):
            return endpoint_map.get('regionId')
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
