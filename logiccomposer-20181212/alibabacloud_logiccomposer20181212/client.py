# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_logiccomposer20181212 import models as logiccomposer_20181212_models
from alibabacloud_tea_util import models as util_models


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
        self._endpoint = self.get_endpoint('logiccomposer', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def abolish_flow_with_options(
        self,
        request: logiccomposer_20181212_models.AbolishFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.AbolishFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.AbolishFlowResponse().from_map(
            self.do_rpcrequest('AbolishFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def abolish_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.AbolishFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.AbolishFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.AbolishFlowResponse().from_map(
            await self.do_rpcrequest_async('AbolishFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def abolish_flow(
        self,
        request: logiccomposer_20181212_models.AbolishFlowRequest,
    ) -> logiccomposer_20181212_models.AbolishFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.abolish_flow_with_options(request, runtime)

    async def abolish_flow_async(
        self,
        request: logiccomposer_20181212_models.AbolishFlowRequest,
    ) -> logiccomposer_20181212_models.AbolishFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.abolish_flow_with_options_async(request, runtime)

    def clone_flow_with_options(
        self,
        request: logiccomposer_20181212_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.CloneFlowResponse().from_map(
            self.do_rpcrequest('CloneFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def clone_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.CloneFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.CloneFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.CloneFlowResponse().from_map(
            await self.do_rpcrequest_async('CloneFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_flow(
        self,
        request: logiccomposer_20181212_models.CloneFlowRequest,
    ) -> logiccomposer_20181212_models.CloneFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.clone_flow_with_options(request, runtime)

    async def clone_flow_async(
        self,
        request: logiccomposer_20181212_models.CloneFlowRequest,
    ) -> logiccomposer_20181212_models.CloneFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.clone_flow_with_options_async(request, runtime)

    def create_flow_with_options(
        self,
        request: logiccomposer_20181212_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.CreateFlowResponse().from_map(
            self.do_rpcrequest('CreateFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def create_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.CreateFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.CreateFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.CreateFlowResponse().from_map(
            await self.do_rpcrequest_async('CreateFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_flow(
        self,
        request: logiccomposer_20181212_models.CreateFlowRequest,
    ) -> logiccomposer_20181212_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_flow_with_options(request, runtime)

    async def create_flow_async(
        self,
        request: logiccomposer_20181212_models.CreateFlowRequest,
    ) -> logiccomposer_20181212_models.CreateFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_flow_with_options_async(request, runtime)

    def delete_flow_with_options(
        self,
        request: logiccomposer_20181212_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DeleteFlowResponse().from_map(
            self.do_rpcrequest('DeleteFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def delete_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.DeleteFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DeleteFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DeleteFlowResponse().from_map(
            await self.do_rpcrequest_async('DeleteFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_flow(
        self,
        request: logiccomposer_20181212_models.DeleteFlowRequest,
    ) -> logiccomposer_20181212_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_flow_with_options(request, runtime)

    async def delete_flow_async(
        self,
        request: logiccomposer_20181212_models.DeleteFlowRequest,
    ) -> logiccomposer_20181212_models.DeleteFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_flow_with_options_async(request, runtime)

    def deploy_flow_with_options(
        self,
        request: logiccomposer_20181212_models.DeployFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DeployFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DeployFlowResponse().from_map(
            self.do_rpcrequest('DeployFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def deploy_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.DeployFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DeployFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DeployFlowResponse().from_map(
            await self.do_rpcrequest_async('DeployFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_flow(
        self,
        request: logiccomposer_20181212_models.DeployFlowRequest,
    ) -> logiccomposer_20181212_models.DeployFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_flow_with_options(request, runtime)

    async def deploy_flow_async(
        self,
        request: logiccomposer_20181212_models.DeployFlowRequest,
    ) -> logiccomposer_20181212_models.DeployFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_flow_with_options_async(request, runtime)

    def describe_account_summary_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeAccountSummaryResponse:
        req = open_api_models.OpenApiRequest()
        return logiccomposer_20181212_models.DescribeAccountSummaryResponse().from_map(
            self.do_rpcrequest('DescribeAccountSummary', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_account_summary_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeAccountSummaryResponse:
        req = open_api_models.OpenApiRequest()
        return logiccomposer_20181212_models.DescribeAccountSummaryResponse().from_map(
            await self.do_rpcrequest_async('DescribeAccountSummary', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_account_summary(self) -> logiccomposer_20181212_models.DescribeAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_account_summary_with_options(runtime)

    async def describe_account_summary_async(self) -> logiccomposer_20181212_models.DescribeAccountSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_account_summary_with_options_async(runtime)

    def describe_connector_attribute_with_options(
        self,
        request: logiccomposer_20181212_models.DescribeConnectorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeConnectorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeConnectorAttributeResponse().from_map(
            self.do_rpcrequest('DescribeConnectorAttribute', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_connector_attribute_with_options_async(
        self,
        request: logiccomposer_20181212_models.DescribeConnectorAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeConnectorAttributeResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeConnectorAttributeResponse().from_map(
            await self.do_rpcrequest_async('DescribeConnectorAttribute', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_connector_attribute(
        self,
        request: logiccomposer_20181212_models.DescribeConnectorAttributeRequest,
    ) -> logiccomposer_20181212_models.DescribeConnectorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_connector_attribute_with_options(request, runtime)

    async def describe_connector_attribute_async(
        self,
        request: logiccomposer_20181212_models.DescribeConnectorAttributeRequest,
    ) -> logiccomposer_20181212_models.DescribeConnectorAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_connector_attribute_with_options_async(request, runtime)

    def describe_connector_capability_with_options(
        self,
        request: logiccomposer_20181212_models.DescribeConnectorCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeConnectorCapabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeConnectorCapabilityResponse().from_map(
            self.do_rpcrequest('DescribeConnectorCapability', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_connector_capability_with_options_async(
        self,
        request: logiccomposer_20181212_models.DescribeConnectorCapabilityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeConnectorCapabilityResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeConnectorCapabilityResponse().from_map(
            await self.do_rpcrequest_async('DescribeConnectorCapability', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_connector_capability(
        self,
        request: logiccomposer_20181212_models.DescribeConnectorCapabilityRequest,
    ) -> logiccomposer_20181212_models.DescribeConnectorCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_connector_capability_with_options(request, runtime)

    async def describe_connector_capability_async(
        self,
        request: logiccomposer_20181212_models.DescribeConnectorCapabilityRequest,
    ) -> logiccomposer_20181212_models.DescribeConnectorCapabilityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_connector_capability_with_options_async(request, runtime)

    def describe_flow_with_options(
        self,
        request: logiccomposer_20181212_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeFlowResponse().from_map(
            self.do_rpcrequest('DescribeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.DescribeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeFlowResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow(
        self,
        request: logiccomposer_20181212_models.DescribeFlowRequest,
    ) -> logiccomposer_20181212_models.DescribeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_with_options(request, runtime)

    async def describe_flow_async(
        self,
        request: logiccomposer_20181212_models.DescribeFlowRequest,
    ) -> logiccomposer_20181212_models.DescribeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_with_options_async(request, runtime)

    def describe_flow_metric_with_options(
        self,
        request: logiccomposer_20181212_models.DescribeFlowMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeFlowMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeFlowMetricResponse().from_map(
            self.do_rpcrequest('DescribeFlowMetric', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_metric_with_options_async(
        self,
        request: logiccomposer_20181212_models.DescribeFlowMetricRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeFlowMetricResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeFlowMetricResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowMetric', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_metric(
        self,
        request: logiccomposer_20181212_models.DescribeFlowMetricRequest,
    ) -> logiccomposer_20181212_models.DescribeFlowMetricResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_metric_with_options(request, runtime)

    async def describe_flow_metric_async(
        self,
        request: logiccomposer_20181212_models.DescribeFlowMetricRequest,
    ) -> logiccomposer_20181212_models.DescribeFlowMetricResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_metric_with_options_async(request, runtime)

    def describe_flow_template_with_options(
        self,
        request: logiccomposer_20181212_models.DescribeFlowTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeFlowTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeFlowTemplateResponse().from_map(
            self.do_rpcrequest('DescribeFlowTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_flow_template_with_options_async(
        self,
        request: logiccomposer_20181212_models.DescribeFlowTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeFlowTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeFlowTemplateResponse().from_map(
            await self.do_rpcrequest_async('DescribeFlowTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_flow_template(
        self,
        request: logiccomposer_20181212_models.DescribeFlowTemplateRequest,
    ) -> logiccomposer_20181212_models.DescribeFlowTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_flow_template_with_options(request, runtime)

    async def describe_flow_template_async(
        self,
        request: logiccomposer_20181212_models.DescribeFlowTemplateRequest,
    ) -> logiccomposer_20181212_models.DescribeFlowTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_flow_template_with_options_async(request, runtime)

    def describe_invocation_log_with_options(
        self,
        request: logiccomposer_20181212_models.DescribeInvocationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeInvocationLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeInvocationLogResponse().from_map(
            self.do_rpcrequest('DescribeInvocationLog', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_invocation_log_with_options_async(
        self,
        request: logiccomposer_20181212_models.DescribeInvocationLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeInvocationLogResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeInvocationLogResponse().from_map(
            await self.do_rpcrequest_async('DescribeInvocationLog', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_invocation_log(
        self,
        request: logiccomposer_20181212_models.DescribeInvocationLogRequest,
    ) -> logiccomposer_20181212_models.DescribeInvocationLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_invocation_log_with_options(request, runtime)

    async def describe_invocation_log_async(
        self,
        request: logiccomposer_20181212_models.DescribeInvocationLogRequest,
    ) -> logiccomposer_20181212_models.DescribeInvocationLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_invocation_log_with_options_async(request, runtime)

    def describe_metric_detail_with_options(
        self,
        request: logiccomposer_20181212_models.DescribeMetricDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeMetricDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeMetricDetailResponse().from_map(
            self.do_rpcrequest('DescribeMetricDetail', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def describe_metric_detail_with_options_async(
        self,
        request: logiccomposer_20181212_models.DescribeMetricDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DescribeMetricDetailResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DescribeMetricDetailResponse().from_map(
            await self.do_rpcrequest_async('DescribeMetricDetail', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_metric_detail(
        self,
        request: logiccomposer_20181212_models.DescribeMetricDetailRequest,
    ) -> logiccomposer_20181212_models.DescribeMetricDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_metric_detail_with_options(request, runtime)

    async def describe_metric_detail_async(
        self,
        request: logiccomposer_20181212_models.DescribeMetricDetailRequest,
    ) -> logiccomposer_20181212_models.DescribeMetricDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_metric_detail_with_options_async(request, runtime)

    def disable_flow_with_options(
        self,
        request: logiccomposer_20181212_models.DisableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DisableFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DisableFlowResponse().from_map(
            self.do_rpcrequest('DisableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def disable_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.DisableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.DisableFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.DisableFlowResponse().from_map(
            await self.do_rpcrequest_async('DisableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_flow(
        self,
        request: logiccomposer_20181212_models.DisableFlowRequest,
    ) -> logiccomposer_20181212_models.DisableFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_flow_with_options(request, runtime)

    async def disable_flow_async(
        self,
        request: logiccomposer_20181212_models.DisableFlowRequest,
    ) -> logiccomposer_20181212_models.DisableFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_flow_with_options_async(request, runtime)

    def enable_flow_with_options(
        self,
        request: logiccomposer_20181212_models.EnableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.EnableFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.EnableFlowResponse().from_map(
            self.do_rpcrequest('EnableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def enable_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.EnableFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.EnableFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.EnableFlowResponse().from_map(
            await self.do_rpcrequest_async('EnableFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_flow(
        self,
        request: logiccomposer_20181212_models.EnableFlowRequest,
    ) -> logiccomposer_20181212_models.EnableFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_flow_with_options(request, runtime)

    async def enable_flow_async(
        self,
        request: logiccomposer_20181212_models.EnableFlowRequest,
    ) -> logiccomposer_20181212_models.EnableFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_flow_with_options_async(request, runtime)

    def invoke_flow_with_options(
        self,
        request: logiccomposer_20181212_models.InvokeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.InvokeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.InvokeFlowResponse().from_map(
            self.do_rpcrequest('InvokeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def invoke_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.InvokeFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.InvokeFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.InvokeFlowResponse().from_map(
            await self.do_rpcrequest_async('InvokeFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_flow(
        self,
        request: logiccomposer_20181212_models.InvokeFlowRequest,
    ) -> logiccomposer_20181212_models.InvokeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.invoke_flow_with_options(request, runtime)

    async def invoke_flow_async(
        self,
        request: logiccomposer_20181212_models.InvokeFlowRequest,
    ) -> logiccomposer_20181212_models.InvokeFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.invoke_flow_with_options_async(request, runtime)

    def list_connectors_with_options(
        self,
        request: logiccomposer_20181212_models.ListConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListConnectorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListConnectorsResponse().from_map(
            self.do_rpcrequest('ListConnectors', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_connectors_with_options_async(
        self,
        request: logiccomposer_20181212_models.ListConnectorsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListConnectorsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListConnectorsResponse().from_map(
            await self.do_rpcrequest_async('ListConnectors', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_connectors(
        self,
        request: logiccomposer_20181212_models.ListConnectorsRequest,
    ) -> logiccomposer_20181212_models.ListConnectorsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_connectors_with_options(request, runtime)

    async def list_connectors_async(
        self,
        request: logiccomposer_20181212_models.ListConnectorsRequest,
    ) -> logiccomposer_20181212_models.ListConnectorsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_connectors_with_options_async(request, runtime)

    def list_connector_triggers_with_options(
        self,
        request: logiccomposer_20181212_models.ListConnectorTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListConnectorTriggersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListConnectorTriggersResponse().from_map(
            self.do_rpcrequest('ListConnectorTriggers', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_connector_triggers_with_options_async(
        self,
        request: logiccomposer_20181212_models.ListConnectorTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListConnectorTriggersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListConnectorTriggersResponse().from_map(
            await self.do_rpcrequest_async('ListConnectorTriggers', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_connector_triggers(
        self,
        request: logiccomposer_20181212_models.ListConnectorTriggersRequest,
    ) -> logiccomposer_20181212_models.ListConnectorTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_connector_triggers_with_options(request, runtime)

    async def list_connector_triggers_async(
        self,
        request: logiccomposer_20181212_models.ListConnectorTriggersRequest,
    ) -> logiccomposer_20181212_models.ListConnectorTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_connector_triggers_with_options_async(request, runtime)

    def list_flow_with_options(
        self,
        request: logiccomposer_20181212_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowResponse().from_map(
            self.do_rpcrequest('ListFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.ListFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowResponse().from_map(
            await self.do_rpcrequest_async('ListFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow(
        self,
        request: logiccomposer_20181212_models.ListFlowRequest,
    ) -> logiccomposer_20181212_models.ListFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_with_options(request, runtime)

    async def list_flow_async(
        self,
        request: logiccomposer_20181212_models.ListFlowRequest,
    ) -> logiccomposer_20181212_models.ListFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_with_options_async(request, runtime)

    def list_flow_connections_with_options(
        self,
        request: logiccomposer_20181212_models.ListFlowConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowConnectionsResponse().from_map(
            self.do_rpcrequest('ListFlowConnections', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_connections_with_options_async(
        self,
        request: logiccomposer_20181212_models.ListFlowConnectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowConnectionsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowConnectionsResponse().from_map(
            await self.do_rpcrequest_async('ListFlowConnections', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_connections(
        self,
        request: logiccomposer_20181212_models.ListFlowConnectionsRequest,
    ) -> logiccomposer_20181212_models.ListFlowConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_connections_with_options(request, runtime)

    async def list_flow_connections_async(
        self,
        request: logiccomposer_20181212_models.ListFlowConnectionsRequest,
    ) -> logiccomposer_20181212_models.ListFlowConnectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_connections_with_options_async(request, runtime)

    def list_flow_template_with_options(
        self,
        request: logiccomposer_20181212_models.ListFlowTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowTemplateResponse().from_map(
            self.do_rpcrequest('ListFlowTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_template_with_options_async(
        self,
        request: logiccomposer_20181212_models.ListFlowTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowTemplateResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowTemplateResponse().from_map(
            await self.do_rpcrequest_async('ListFlowTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_template(
        self,
        request: logiccomposer_20181212_models.ListFlowTemplateRequest,
    ) -> logiccomposer_20181212_models.ListFlowTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_template_with_options(request, runtime)

    async def list_flow_template_async(
        self,
        request: logiccomposer_20181212_models.ListFlowTemplateRequest,
    ) -> logiccomposer_20181212_models.ListFlowTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_template_with_options_async(request, runtime)

    def list_flow_triggers_with_options(
        self,
        request: logiccomposer_20181212_models.ListFlowTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowTriggersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowTriggersResponse().from_map(
            self.do_rpcrequest('ListFlowTriggers', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_triggers_with_options_async(
        self,
        request: logiccomposer_20181212_models.ListFlowTriggersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowTriggersResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowTriggersResponse().from_map(
            await self.do_rpcrequest_async('ListFlowTriggers', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_triggers(
        self,
        request: logiccomposer_20181212_models.ListFlowTriggersRequest,
    ) -> logiccomposer_20181212_models.ListFlowTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_triggers_with_options(request, runtime)

    async def list_flow_triggers_async(
        self,
        request: logiccomposer_20181212_models.ListFlowTriggersRequest,
    ) -> logiccomposer_20181212_models.ListFlowTriggersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_triggers_with_options_async(request, runtime)

    def list_flow_version_with_options(
        self,
        request: logiccomposer_20181212_models.ListFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowVersionResponse().from_map(
            self.do_rpcrequest('ListFlowVersion', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_flow_version_with_options_async(
        self,
        request: logiccomposer_20181212_models.ListFlowVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListFlowVersionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListFlowVersionResponse().from_map(
            await self.do_rpcrequest_async('ListFlowVersion', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_flow_version(
        self,
        request: logiccomposer_20181212_models.ListFlowVersionRequest,
    ) -> logiccomposer_20181212_models.ListFlowVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_flow_version_with_options(request, runtime)

    async def list_flow_version_async(
        self,
        request: logiccomposer_20181212_models.ListFlowVersionRequest,
    ) -> logiccomposer_20181212_models.ListFlowVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_flow_version_with_options_async(request, runtime)

    def list_invocation_logs_with_options(
        self,
        request: logiccomposer_20181212_models.ListInvocationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListInvocationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListInvocationLogsResponse().from_map(
            self.do_rpcrequest('ListInvocationLogs', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_invocation_logs_with_options_async(
        self,
        request: logiccomposer_20181212_models.ListInvocationLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListInvocationLogsResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ListInvocationLogsResponse().from_map(
            await self.do_rpcrequest_async('ListInvocationLogs', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_invocation_logs(
        self,
        request: logiccomposer_20181212_models.ListInvocationLogsRequest,
    ) -> logiccomposer_20181212_models.ListInvocationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_invocation_logs_with_options(request, runtime)

    async def list_invocation_logs_async(
        self,
        request: logiccomposer_20181212_models.ListInvocationLogsRequest,
    ) -> logiccomposer_20181212_models.ListInvocationLogsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_invocation_logs_with_options_async(request, runtime)

    def list_tag_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListTagResponse:
        req = open_api_models.OpenApiRequest()
        return logiccomposer_20181212_models.ListTagResponse().from_map(
            self.do_rpcrequest('ListTag', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def list_tag_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ListTagResponse:
        req = open_api_models.OpenApiRequest()
        return logiccomposer_20181212_models.ListTagResponse().from_map(
            await self.do_rpcrequest_async('ListTag', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag(self) -> logiccomposer_20181212_models.ListTagResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_tag_with_options(runtime)

    async def list_tag_async(self) -> logiccomposer_20181212_models.ListTagResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_with_options_async(runtime)

    def modify_flow_with_options(
        self,
        request: logiccomposer_20181212_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ModifyFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ModifyFlowResponse().from_map(
            self.do_rpcrequest('ModifyFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def modify_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.ModifyFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.ModifyFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.ModifyFlowResponse().from_map(
            await self.do_rpcrequest_async('ModifyFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_flow(
        self,
        request: logiccomposer_20181212_models.ModifyFlowRequest,
    ) -> logiccomposer_20181212_models.ModifyFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_flow_with_options(request, runtime)

    async def modify_flow_async(
        self,
        request: logiccomposer_20181212_models.ModifyFlowRequest,
    ) -> logiccomposer_20181212_models.ModifyFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_flow_with_options_async(request, runtime)

    def roll_back_flow_with_options(
        self,
        request: logiccomposer_20181212_models.RollBackFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.RollBackFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.RollBackFlowResponse().from_map(
            self.do_rpcrequest('RollBackFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def roll_back_flow_with_options_async(
        self,
        request: logiccomposer_20181212_models.RollBackFlowRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.RollBackFlowResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.RollBackFlowResponse().from_map(
            await self.do_rpcrequest_async('RollBackFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def roll_back_flow(
        self,
        request: logiccomposer_20181212_models.RollBackFlowRequest,
    ) -> logiccomposer_20181212_models.RollBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        return self.roll_back_flow_with_options(request, runtime)

    async def roll_back_flow_async(
        self,
        request: logiccomposer_20181212_models.RollBackFlowRequest,
    ) -> logiccomposer_20181212_models.RollBackFlowResponse:
        runtime = util_models.RuntimeOptions()
        return await self.roll_back_flow_with_options_async(request, runtime)

    def update_connection_with_options(
        self,
        request: logiccomposer_20181212_models.UpdateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.UpdateConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.UpdateConnectionResponse().from_map(
            self.do_rpcrequest('UpdateConnection', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    async def update_connection_with_options_async(
        self,
        request: logiccomposer_20181212_models.UpdateConnectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> logiccomposer_20181212_models.UpdateConnectionResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return logiccomposer_20181212_models.UpdateConnectionResponse().from_map(
            await self.do_rpcrequest_async('UpdateConnection', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_connection(
        self,
        request: logiccomposer_20181212_models.UpdateConnectionRequest,
    ) -> logiccomposer_20181212_models.UpdateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_connection_with_options(request, runtime)

    async def update_connection_async(
        self,
        request: logiccomposer_20181212_models.UpdateConnectionRequest,
    ) -> logiccomposer_20181212_models.UpdateConnectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_connection_with_options_async(request, runtime)
