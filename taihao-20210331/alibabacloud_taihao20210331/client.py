# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_taihao20210331 import models as taihao_20210331_models
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
        self._endpoint = self.get_endpoint('taihao', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_cluster_application_with_options(
        self,
        tmp_req: taihao_20210331_models.AddClusterApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.AddClusterApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.AddClusterApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_application_param):
            request.add_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.add_application_param), 'addApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.add_application_param_shrink):
            body['addApplicationParam'] = request.add_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddClusterApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.AddClusterApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_cluster_application_with_options_async(
        self,
        tmp_req: taihao_20210331_models.AddClusterApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.AddClusterApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.AddClusterApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_application_param):
            request.add_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.add_application_param), 'addApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.add_application_param_shrink):
            body['addApplicationParam'] = request.add_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddClusterApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.AddClusterApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_cluster_application(
        self,
        request: taihao_20210331_models.AddClusterApplicationRequest,
    ) -> taihao_20210331_models.AddClusterApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_cluster_application_with_options(request, runtime)

    async def add_cluster_application_async(
        self,
        request: taihao_20210331_models.AddClusterApplicationRequest,
    ) -> taihao_20210331_models.AddClusterApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_cluster_application_with_options_async(request, runtime)

    def add_suspend_point_on_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.AddSuspendPointOnWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.AddSuspendPointOnWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.AddSuspendPointOnWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_suspend_on_workflow_instance_param):
            request.add_suspend_on_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.add_suspend_on_workflow_instance_param), 'addSuspendOnWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.add_suspend_on_workflow_instance_param_shrink):
            body['addSuspendOnWorkflowInstanceParam'] = request.add_suspend_on_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSuspendPointOnWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.AddSuspendPointOnWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_suspend_point_on_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.AddSuspendPointOnWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.AddSuspendPointOnWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.AddSuspendPointOnWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.add_suspend_on_workflow_instance_param):
            request.add_suspend_on_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.add_suspend_on_workflow_instance_param), 'addSuspendOnWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.add_suspend_on_workflow_instance_param_shrink):
            body['addSuspendOnWorkflowInstanceParam'] = request.add_suspend_on_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSuspendPointOnWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.AddSuspendPointOnWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_suspend_point_on_workflow_instance(
        self,
        request: taihao_20210331_models.AddSuspendPointOnWorkflowInstanceRequest,
    ) -> taihao_20210331_models.AddSuspendPointOnWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.add_suspend_point_on_workflow_instance_with_options(request, runtime)

    async def add_suspend_point_on_workflow_instance_async(
        self,
        request: taihao_20210331_models.AddSuspendPointOnWorkflowInstanceRequest,
    ) -> taihao_20210331_models.AddSuspendPointOnWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.add_suspend_point_on_workflow_instance_with_options_async(request, runtime)

    def cancel_cluster_orders_with_options(
        self,
        tmp_req: taihao_20210331_models.CancelClusterOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CancelClusterOrdersResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CancelClusterOrdersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cancel_cluster_orders_param):
            request.cancel_cluster_orders_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.cancel_cluster_orders_param), 'cancelClusterOrdersParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.cancel_cluster_orders_param_shrink):
            body['cancelClusterOrdersParam'] = request.cancel_cluster_orders_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelClusterOrders',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CancelClusterOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_cluster_orders_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CancelClusterOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CancelClusterOrdersResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CancelClusterOrdersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cancel_cluster_orders_param):
            request.cancel_cluster_orders_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.cancel_cluster_orders_param), 'cancelClusterOrdersParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.cancel_cluster_orders_param_shrink):
            body['cancelClusterOrdersParam'] = request.cancel_cluster_orders_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelClusterOrders',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CancelClusterOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_cluster_orders(
        self,
        request: taihao_20210331_models.CancelClusterOrdersRequest,
    ) -> taihao_20210331_models.CancelClusterOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_cluster_orders_with_options(request, runtime)

    async def cancel_cluster_orders_async(
        self,
        request: taihao_20210331_models.CancelClusterOrdersRequest,
    ) -> taihao_20210331_models.CancelClusterOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_cluster_orders_with_options_async(request, runtime)

    def com_alibaba_tcc_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ComAlibabaTccResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ComAlibabaTcc',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ComAlibabaTccResponse(),
            self.call_api(params, req, runtime)
        )

    async def com_alibaba_tcc_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ComAlibabaTccResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ComAlibabaTcc',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ComAlibabaTccResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def com_alibaba_tcc(self) -> taihao_20210331_models.ComAlibabaTccResponse:
        runtime = util_models.RuntimeOptions()
        return self.com_alibaba_tcc_with_options(runtime)

    async def com_alibaba_tcc_async(self) -> taihao_20210331_models.ComAlibabaTccResponse:
        runtime = util_models.RuntimeOptions()
        return await self.com_alibaba_tcc_with_options_async(runtime)

    def create_auto_scaling_policy_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_auto_scaling_policy_param):
            request.create_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_auto_scaling_policy_param), 'createAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_auto_scaling_policy_param_shrink):
            body['createAutoScalingPolicyParam'] = request.create_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_scaling_policy_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_auto_scaling_policy_param):
            request.create_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_auto_scaling_policy_param), 'createAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_auto_scaling_policy_param_shrink):
            body['createAutoScalingPolicyParam'] = request.create_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_scaling_policy(
        self,
        request: taihao_20210331_models.CreateAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.CreateAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_auto_scaling_policy_with_options(request, runtime)

    async def create_auto_scaling_policy_async(
        self,
        request: taihao_20210331_models.CreateAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.CreateAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_scaling_policy_with_options_async(request, runtime)

    def create_auto_scaling_rule_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateAutoScalingRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateAutoScalingRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_auto_scaling_rule_param):
            request.create_auto_scaling_rule_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_auto_scaling_rule_param), 'createAutoScalingRuleParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_auto_scaling_rule_param_shrink):
            body['createAutoScalingRuleParam'] = request.create_auto_scaling_rule_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAutoScalingRule',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateAutoScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_auto_scaling_rule_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateAutoScalingRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateAutoScalingRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_auto_scaling_rule_param):
            request.create_auto_scaling_rule_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_auto_scaling_rule_param), 'createAutoScalingRuleParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_auto_scaling_rule_param_shrink):
            body['createAutoScalingRuleParam'] = request.create_auto_scaling_rule_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAutoScalingRule',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateAutoScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_auto_scaling_rule(
        self,
        request: taihao_20210331_models.CreateAutoScalingRuleRequest,
    ) -> taihao_20210331_models.CreateAutoScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_auto_scaling_rule_with_options(request, runtime)

    async def create_auto_scaling_rule_async(
        self,
        request: taihao_20210331_models.CreateAutoScalingRuleRequest,
    ) -> taihao_20210331_models.CreateAutoScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_auto_scaling_rule_with_options_async(request, runtime)

    def create_binding_ack_cluster_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateBindingAckClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateBindingAckClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateBindingAckClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_binding_ack_cluster_param):
            request.create_binding_ack_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_binding_ack_cluster_param), 'createBindingAckClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_binding_ack_cluster_param_shrink):
            body['createBindingAckClusterParam'] = request.create_binding_ack_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBindingAckCluster',
            version='2021-03-31',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateBindingAckClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_binding_ack_cluster_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateBindingAckClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateBindingAckClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateBindingAckClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_binding_ack_cluster_param):
            request.create_binding_ack_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_binding_ack_cluster_param), 'createBindingAckClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_binding_ack_cluster_param_shrink):
            body['createBindingAckClusterParam'] = request.create_binding_ack_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateBindingAckCluster',
            version='2021-03-31',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateBindingAckClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_binding_ack_cluster(
        self,
        request: taihao_20210331_models.CreateBindingAckClusterRequest,
    ) -> taihao_20210331_models.CreateBindingAckClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_binding_ack_cluster_with_options(request, runtime)

    async def create_binding_ack_cluster_async(
        self,
        request: taihao_20210331_models.CreateBindingAckClusterRequest,
    ) -> taihao_20210331_models.CreateBindingAckClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_binding_ack_cluster_with_options_async(request, runtime)

    def create_cluster_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_cluster_param):
            request.create_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_cluster_param), 'createClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_cluster_param_shrink):
            body['createClusterParam'] = request.create_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_cluster_param):
            request.create_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_cluster_param), 'createClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_cluster_param_shrink):
            body['createClusterParam'] = request.create_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster(
        self,
        request: taihao_20210331_models.CreateClusterRequest,
    ) -> taihao_20210331_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    async def create_cluster_async(
        self,
        request: taihao_20210331_models.CreateClusterRequest,
    ) -> taihao_20210331_models.CreateClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_with_options_async(request, runtime)

    def create_cluster_node_group_with_options(
        self,
        request: taihao_20210331_models.CreateClusterNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateClusterNodeGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.create_cluster_node_group_param):
            body_flat['createClusterNodeGroupParam'] = request.create_cluster_node_group_param
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateClusterNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_node_group_with_options_async(
        self,
        request: taihao_20210331_models.CreateClusterNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateClusterNodeGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.create_cluster_node_group_param):
            body_flat['createClusterNodeGroupParam'] = request.create_cluster_node_group_param
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateClusterNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster_node_group(
        self,
        request: taihao_20210331_models.CreateClusterNodeGroupRequest,
    ) -> taihao_20210331_models.CreateClusterNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_node_group_with_options(request, runtime)

    async def create_cluster_node_group_async(
        self,
        request: taihao_20210331_models.CreateClusterNodeGroupRequest,
    ) -> taihao_20210331_models.CreateClusterNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_node_group_with_options_async(request, runtime)

    def create_cluster_script_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateClusterScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateClusterScriptResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateClusterScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_cluster_script_param):
            request.create_cluster_script_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_cluster_script_param), 'createClusterScriptParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_cluster_script_param_shrink):
            body['createClusterScriptParam'] = request.create_cluster_script_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterScript',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateClusterScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_script_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateClusterScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateClusterScriptResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateClusterScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_cluster_script_param):
            request.create_cluster_script_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_cluster_script_param), 'createClusterScriptParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_cluster_script_param_shrink):
            body['createClusterScriptParam'] = request.create_cluster_script_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterScript',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateClusterScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster_script(
        self,
        request: taihao_20210331_models.CreateClusterScriptRequest,
    ) -> taihao_20210331_models.CreateClusterScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_script_with_options(request, runtime)

    async def create_cluster_script_async(
        self,
        request: taihao_20210331_models.CreateClusterScriptRequest,
    ) -> taihao_20210331_models.CreateClusterScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_script_with_options_async(request, runtime)

    def create_cluster_user_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateClusterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateClusterUserResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateClusterUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_cluster_user_param):
            request.create_cluster_user_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_cluster_user_param), 'createClusterUserParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_cluster_user_param_shrink):
            body['createClusterUserParam'] = request.create_cluster_user_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterUser',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateClusterUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_cluster_user_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateClusterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateClusterUserResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateClusterUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_cluster_user_param):
            request.create_cluster_user_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_cluster_user_param), 'createClusterUserParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_cluster_user_param_shrink):
            body['createClusterUserParam'] = request.create_cluster_user_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateClusterUser',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateClusterUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_cluster_user(
        self,
        request: taihao_20210331_models.CreateClusterUserRequest,
    ) -> taihao_20210331_models.CreateClusterUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_user_with_options(request, runtime)

    async def create_cluster_user_async(
        self,
        request: taihao_20210331_models.CreateClusterUserRequest,
    ) -> taihao_20210331_models.CreateClusterUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_cluster_user_with_options_async(request, runtime)

    def create_full_cluster_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateFullClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateFullClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateFullClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_full_cluster_param):
            request.create_full_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_full_cluster_param), 'createFullClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_full_cluster_param_shrink):
            body['createFullClusterParam'] = request.create_full_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFullCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateFullClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_full_cluster_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateFullClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateFullClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateFullClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_full_cluster_param):
            request.create_full_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_full_cluster_param), 'createFullClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_full_cluster_param_shrink):
            body['createFullClusterParam'] = request.create_full_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFullCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateFullClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_full_cluster(
        self,
        request: taihao_20210331_models.CreateFullClusterRequest,
    ) -> taihao_20210331_models.CreateFullClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_full_cluster_with_options(request, runtime)

    async def create_full_cluster_async(
        self,
        request: taihao_20210331_models.CreateFullClusterRequest,
    ) -> taihao_20210331_models.CreateFullClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_full_cluster_with_options_async(request, runtime)

    def create_full_cluster_by_main_version_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateFullClusterByMainVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateFullClusterByMainVersionResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateFullClusterByMainVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_full_cluster_by_main_version_param):
            request.create_full_cluster_by_main_version_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_full_cluster_by_main_version_param), 'createFullClusterByMainVersionParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_full_cluster_by_main_version_param_shrink):
            body['createFullClusterByMainVersionParam'] = request.create_full_cluster_by_main_version_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFullClusterByMainVersion',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateFullClusterByMainVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_full_cluster_by_main_version_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateFullClusterByMainVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateFullClusterByMainVersionResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateFullClusterByMainVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_full_cluster_by_main_version_param):
            request.create_full_cluster_by_main_version_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_full_cluster_by_main_version_param), 'createFullClusterByMainVersionParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_full_cluster_by_main_version_param_shrink):
            body['createFullClusterByMainVersionParam'] = request.create_full_cluster_by_main_version_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateFullClusterByMainVersion',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateFullClusterByMainVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_full_cluster_by_main_version(
        self,
        request: taihao_20210331_models.CreateFullClusterByMainVersionRequest,
    ) -> taihao_20210331_models.CreateFullClusterByMainVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_full_cluster_by_main_version_with_options(request, runtime)

    async def create_full_cluster_by_main_version_async(
        self,
        request: taihao_20210331_models.CreateFullClusterByMainVersionRequest,
    ) -> taihao_20210331_models.CreateFullClusterByMainVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_full_cluster_by_main_version_with_options_async(request, runtime)

    def create_main_version_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateMainVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateMainVersionResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateMainVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_main_version_param):
            request.create_main_version_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_main_version_param), 'CreateMainVersionParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_main_version_param_shrink):
            body['CreateMainVersionParam'] = request.create_main_version_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMainVersion',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateMainVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_main_version_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateMainVersionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateMainVersionResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateMainVersionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_main_version_param):
            request.create_main_version_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_main_version_param), 'CreateMainVersionParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_main_version_param_shrink):
            body['CreateMainVersionParam'] = request.create_main_version_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMainVersion',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateMainVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_main_version(
        self,
        request: taihao_20210331_models.CreateMainVersionRequest,
    ) -> taihao_20210331_models.CreateMainVersionResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_main_version_with_options(request, runtime)

    async def create_main_version_async(
        self,
        request: taihao_20210331_models.CreateMainVersionRequest,
    ) -> taihao_20210331_models.CreateMainVersionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_main_version_with_options_async(request, runtime)

    def create_stack_application_with_options(
        self,
        tmp_req: taihao_20210331_models.CreateStackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateStackApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateStackApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_stack_application_param):
            request.create_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_stack_application_param), 'createStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_stack_application_param_shrink):
            body['createStackApplicationParam'] = request.create_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStackApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateStackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stack_application_with_options_async(
        self,
        tmp_req: taihao_20210331_models.CreateStackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.CreateStackApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.CreateStackApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.create_stack_application_param):
            request.create_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.create_stack_application_param), 'createStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.create_stack_application_param_shrink):
            body['createStackApplicationParam'] = request.create_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStackApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.CreateStackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stack_application(
        self,
        request: taihao_20210331_models.CreateStackApplicationRequest,
    ) -> taihao_20210331_models.CreateStackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.create_stack_application_with_options(request, runtime)

    async def create_stack_application_async(
        self,
        request: taihao_20210331_models.CreateStackApplicationRequest,
    ) -> taihao_20210331_models.CreateStackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_application_with_options_async(request, runtime)

    def decrease_node_group_with_options(
        self,
        tmp_req: taihao_20210331_models.DecreaseNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DecreaseNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DecreaseNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.decrease_node_group_param):
            request.decrease_node_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.decrease_node_group_param), 'DecreaseNodeGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.decrease_node_group_param_shrink):
            body['DecreaseNodeGroupParam'] = request.decrease_node_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DecreaseNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DecreaseNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def decrease_node_group_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DecreaseNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DecreaseNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DecreaseNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.decrease_node_group_param):
            request.decrease_node_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.decrease_node_group_param), 'DecreaseNodeGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.decrease_node_group_param_shrink):
            body['DecreaseNodeGroupParam'] = request.decrease_node_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DecreaseNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DecreaseNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def decrease_node_group(
        self,
        request: taihao_20210331_models.DecreaseNodeGroupRequest,
    ) -> taihao_20210331_models.DecreaseNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.decrease_node_group_with_options(request, runtime)

    async def decrease_node_group_async(
        self,
        request: taihao_20210331_models.DecreaseNodeGroupRequest,
    ) -> taihao_20210331_models.DecreaseNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.decrease_node_group_with_options_async(request, runtime)

    def delete_auto_scaling_policy_with_options(
        self,
        tmp_req: taihao_20210331_models.DeleteAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_auto_scaling_policy_param):
            request.delete_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_auto_scaling_policy_param), 'deleteAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_auto_scaling_policy_param_shrink):
            body['deleteAutoScalingPolicyParam'] = request.delete_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_scaling_policy_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DeleteAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_auto_scaling_policy_param):
            request.delete_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_auto_scaling_policy_param), 'deleteAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_auto_scaling_policy_param_shrink):
            body['deleteAutoScalingPolicyParam'] = request.delete_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_scaling_policy(
        self,
        request: taihao_20210331_models.DeleteAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.DeleteAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_scaling_policy_with_options(request, runtime)

    async def delete_auto_scaling_policy_async(
        self,
        request: taihao_20210331_models.DeleteAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.DeleteAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_scaling_policy_with_options_async(request, runtime)

    def delete_auto_scaling_rule_with_options(
        self,
        tmp_req: taihao_20210331_models.DeleteAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteAutoScalingRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteAutoScalingRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_auto_scaling_rule_param):
            request.delete_auto_scaling_rule_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_auto_scaling_rule_param), 'deleteAutoScalingRuleParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_auto_scaling_rule_param_shrink):
            body['deleteAutoScalingRuleParam'] = request.delete_auto_scaling_rule_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAutoScalingRule',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteAutoScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_auto_scaling_rule_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DeleteAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteAutoScalingRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteAutoScalingRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_auto_scaling_rule_param):
            request.delete_auto_scaling_rule_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_auto_scaling_rule_param), 'deleteAutoScalingRuleParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_auto_scaling_rule_param_shrink):
            body['deleteAutoScalingRuleParam'] = request.delete_auto_scaling_rule_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAutoScalingRule',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteAutoScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_auto_scaling_rule(
        self,
        request: taihao_20210331_models.DeleteAutoScalingRuleRequest,
    ) -> taihao_20210331_models.DeleteAutoScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_scaling_rule_with_options(request, runtime)

    async def delete_auto_scaling_rule_async(
        self,
        request: taihao_20210331_models.DeleteAutoScalingRuleRequest,
    ) -> taihao_20210331_models.DeleteAutoScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_auto_scaling_rule_with_options_async(request, runtime)

    def delete_cluster_node_group_with_options(
        self,
        tmp_req: taihao_20210331_models.DeleteClusterNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteClusterNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteClusterNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_node_group_param):
            request.delete_node_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_node_group_param), 'deleteNodeGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_node_group_param_shrink):
            body['deleteNodeGroupParam'] = request.delete_node_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClusterNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteClusterNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_node_group_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DeleteClusterNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteClusterNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteClusterNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_node_group_param):
            request.delete_node_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_node_group_param), 'deleteNodeGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_node_group_param_shrink):
            body['deleteNodeGroupParam'] = request.delete_node_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClusterNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteClusterNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_node_group(
        self,
        request: taihao_20210331_models.DeleteClusterNodeGroupRequest,
    ) -> taihao_20210331_models.DeleteClusterNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_node_group_with_options(request, runtime)

    async def delete_cluster_node_group_async(
        self,
        request: taihao_20210331_models.DeleteClusterNodeGroupRequest,
    ) -> taihao_20210331_models.DeleteClusterNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_node_group_with_options_async(request, runtime)

    def delete_cluster_script_with_options(
        self,
        tmp_req: taihao_20210331_models.DeleteClusterScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteClusterScriptResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteClusterScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_cluster_script_param):
            request.delete_cluster_script_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_cluster_script_param), 'deleteClusterScriptParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_cluster_script_param_shrink):
            body['deleteClusterScriptParam'] = request.delete_cluster_script_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClusterScript',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteClusterScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_script_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DeleteClusterScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteClusterScriptResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteClusterScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_cluster_script_param):
            request.delete_cluster_script_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_cluster_script_param), 'deleteClusterScriptParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_cluster_script_param_shrink):
            body['deleteClusterScriptParam'] = request.delete_cluster_script_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClusterScript',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteClusterScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_script(
        self,
        request: taihao_20210331_models.DeleteClusterScriptRequest,
    ) -> taihao_20210331_models.DeleteClusterScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_script_with_options(request, runtime)

    async def delete_cluster_script_async(
        self,
        request: taihao_20210331_models.DeleteClusterScriptRequest,
    ) -> taihao_20210331_models.DeleteClusterScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_script_with_options_async(request, runtime)

    def delete_cluster_user_with_options(
        self,
        tmp_req: taihao_20210331_models.DeleteClusterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteClusterUserResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteClusterUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_cluster_user_param):
            request.delete_cluster_user_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_cluster_user_param), 'deleteClusterUserParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_cluster_user_param_shrink):
            body['deleteClusterUserParam'] = request.delete_cluster_user_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClusterUser',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteClusterUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_cluster_user_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DeleteClusterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteClusterUserResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteClusterUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_cluster_user_param):
            request.delete_cluster_user_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_cluster_user_param), 'deleteClusterUserParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_cluster_user_param_shrink):
            body['deleteClusterUserParam'] = request.delete_cluster_user_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteClusterUser',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteClusterUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_cluster_user(
        self,
        request: taihao_20210331_models.DeleteClusterUserRequest,
    ) -> taihao_20210331_models.DeleteClusterUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_user_with_options(request, runtime)

    async def delete_cluster_user_async(
        self,
        request: taihao_20210331_models.DeleteClusterUserRequest,
    ) -> taihao_20210331_models.DeleteClusterUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_cluster_user_with_options_async(request, runtime)

    def delete_kube_customer_resource_with_options(
        self,
        tmp_req: taihao_20210331_models.DeleteKubeCustomerResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteKubeCustomerResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteKubeCustomerResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_kube_customer_resources_param):
            request.delete_kube_customer_resources_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_kube_customer_resources_param), 'deleteKubeCustomerResourcesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_kube_customer_resources_param_shrink):
            body['deleteKubeCustomerResourcesParam'] = request.delete_kube_customer_resources_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteKubeCustomerResource',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteKubeCustomerResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_kube_customer_resource_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DeleteKubeCustomerResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteKubeCustomerResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteKubeCustomerResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_kube_customer_resources_param):
            request.delete_kube_customer_resources_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_kube_customer_resources_param), 'deleteKubeCustomerResourcesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_kube_customer_resources_param_shrink):
            body['deleteKubeCustomerResourcesParam'] = request.delete_kube_customer_resources_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteKubeCustomerResource',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteKubeCustomerResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_kube_customer_resource(
        self,
        request: taihao_20210331_models.DeleteKubeCustomerResourceRequest,
    ) -> taihao_20210331_models.DeleteKubeCustomerResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_kube_customer_resource_with_options(request, runtime)

    async def delete_kube_customer_resource_async(
        self,
        request: taihao_20210331_models.DeleteKubeCustomerResourceRequest,
    ) -> taihao_20210331_models.DeleteKubeCustomerResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_kube_customer_resource_with_options_async(request, runtime)

    def delete_kube_native_resources_with_options(
        self,
        tmp_req: taihao_20210331_models.DeleteKubeNativeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteKubeNativeResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteKubeNativeResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_kube_native_resources_param):
            request.delete_kube_native_resources_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_kube_native_resources_param), 'deleteKubeNativeResourcesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_kube_native_resources_param_shrink):
            body['deleteKubeNativeResourcesParam'] = request.delete_kube_native_resources_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteKubeNativeResources',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteKubeNativeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_kube_native_resources_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DeleteKubeNativeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteKubeNativeResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteKubeNativeResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_kube_native_resources_param):
            request.delete_kube_native_resources_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_kube_native_resources_param), 'deleteKubeNativeResourcesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_kube_native_resources_param_shrink):
            body['deleteKubeNativeResourcesParam'] = request.delete_kube_native_resources_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteKubeNativeResources',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteKubeNativeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_kube_native_resources(
        self,
        request: taihao_20210331_models.DeleteKubeNativeResourcesRequest,
    ) -> taihao_20210331_models.DeleteKubeNativeResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_kube_native_resources_with_options(request, runtime)

    async def delete_kube_native_resources_async(
        self,
        request: taihao_20210331_models.DeleteKubeNativeResourcesRequest,
    ) -> taihao_20210331_models.DeleteKubeNativeResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_kube_native_resources_with_options_async(request, runtime)

    def delete_stack_application_with_options(
        self,
        tmp_req: taihao_20210331_models.DeleteStackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteStackApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteStackApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_stack_application_param):
            request.delete_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_stack_application_param), 'deleteStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_stack_application_param_shrink):
            body['deleteStackApplicationParam'] = request.delete_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteStackApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteStackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stack_application_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DeleteStackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeleteStackApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeleteStackApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.delete_stack_application_param):
            request.delete_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.delete_stack_application_param), 'deleteStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.delete_stack_application_param_shrink):
            body['deleteStackApplicationParam'] = request.delete_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteStackApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeleteStackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stack_application(
        self,
        request: taihao_20210331_models.DeleteStackApplicationRequest,
    ) -> taihao_20210331_models.DeleteStackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_application_with_options(request, runtime)

    async def delete_stack_application_async(
        self,
        request: taihao_20210331_models.DeleteStackApplicationRequest,
    ) -> taihao_20210331_models.DeleteStackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_application_with_options_async(request, runtime)

    def deploy_applications_with_options(
        self,
        tmp_req: taihao_20210331_models.DeployApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeployApplicationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeployApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deploy_application_param):
            request.deploy_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.deploy_application_param), 'deployApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.deploy_application_param_shrink):
            body['deployApplicationParam'] = request.deploy_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplications',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeployApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_applications_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DeployApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DeployApplicationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DeployApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.deploy_application_param):
            request.deploy_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.deploy_application_param), 'deployApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.deploy_application_param_shrink):
            body['deployApplicationParam'] = request.deploy_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeployApplications',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DeployApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_applications(
        self,
        request: taihao_20210331_models.DeployApplicationsRequest,
    ) -> taihao_20210331_models.DeployApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.deploy_applications_with_options(request, runtime)

    async def deploy_applications_async(
        self,
        request: taihao_20210331_models.DeployApplicationsRequest,
    ) -> taihao_20210331_models.DeployApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deploy_applications_with_options_async(request, runtime)

    def disable_auto_scaling_policy_with_options(
        self,
        tmp_req: taihao_20210331_models.DisableAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DisableAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DisableAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.disable_auto_scaling_policy_param):
            request.disable_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.disable_auto_scaling_policy_param), 'disableAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.disable_auto_scaling_policy_param_shrink):
            body['disableAutoScalingPolicyParam'] = request.disable_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DisableAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_auto_scaling_policy_with_options_async(
        self,
        tmp_req: taihao_20210331_models.DisableAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.DisableAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.DisableAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.disable_auto_scaling_policy_param):
            request.disable_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.disable_auto_scaling_policy_param), 'disableAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.disable_auto_scaling_policy_param_shrink):
            body['disableAutoScalingPolicyParam'] = request.disable_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.DisableAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_auto_scaling_policy(
        self,
        request: taihao_20210331_models.DisableAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.DisableAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_scaling_policy_with_options(request, runtime)

    async def disable_auto_scaling_policy_async(
        self,
        request: taihao_20210331_models.DisableAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.DisableAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.disable_auto_scaling_policy_with_options_async(request, runtime)

    def enable_auto_scaling_policy_with_options(
        self,
        tmp_req: taihao_20210331_models.EnableAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.EnableAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.EnableAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.enable_auto_scaling_policy_param):
            request.enable_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.enable_auto_scaling_policy_param), 'enableAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_auto_scaling_policy_param_shrink):
            body['enableAutoScalingPolicyParam'] = request.enable_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.EnableAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_auto_scaling_policy_with_options_async(
        self,
        tmp_req: taihao_20210331_models.EnableAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.EnableAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.EnableAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.enable_auto_scaling_policy_param):
            request.enable_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.enable_auto_scaling_policy_param), 'enableAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_auto_scaling_policy_param_shrink):
            body['enableAutoScalingPolicyParam'] = request.enable_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.EnableAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_auto_scaling_policy(
        self,
        request: taihao_20210331_models.EnableAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.EnableAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.enable_auto_scaling_policy_with_options(request, runtime)

    async def enable_auto_scaling_policy_async(
        self,
        request: taihao_20210331_models.EnableAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.EnableAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.enable_auto_scaling_policy_with_options_async(request, runtime)

    def execute_cluster_script_with_options(
        self,
        tmp_req: taihao_20210331_models.ExecuteClusterScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ExecuteClusterScriptResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ExecuteClusterScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_cluster_script_param):
            request.execute_cluster_script_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.execute_cluster_script_param), 'executeClusterScriptParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.execute_cluster_script_param_shrink):
            body['executeClusterScriptParam'] = request.execute_cluster_script_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteClusterScript',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ExecuteClusterScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_cluster_script_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ExecuteClusterScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ExecuteClusterScriptResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ExecuteClusterScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.execute_cluster_script_param):
            request.execute_cluster_script_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.execute_cluster_script_param), 'executeClusterScriptParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.execute_cluster_script_param_shrink):
            body['executeClusterScriptParam'] = request.execute_cluster_script_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExecuteClusterScript',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ExecuteClusterScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_cluster_script(
        self,
        request: taihao_20210331_models.ExecuteClusterScriptRequest,
    ) -> taihao_20210331_models.ExecuteClusterScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.execute_cluster_script_with_options(request, runtime)

    async def execute_cluster_script_async(
        self,
        request: taihao_20210331_models.ExecuteClusterScriptRequest,
    ) -> taihao_20210331_models.ExecuteClusterScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.execute_cluster_script_with_options_async(request, runtime)

    def get_application_actions_with_options(
        self,
        tmp_req: taihao_20210331_models.GetApplicationActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetApplicationActionsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetApplicationActionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_application_actions_param):
            request.get_application_actions_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_application_actions_param), 'getApplicationActionsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_application_actions_param_shrink):
            body['getApplicationActionsParam'] = request.get_application_actions_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplicationActions',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetApplicationActionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_application_actions_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetApplicationActionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetApplicationActionsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetApplicationActionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_application_actions_param):
            request.get_application_actions_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_application_actions_param), 'getApplicationActionsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_application_actions_param_shrink):
            body['getApplicationActionsParam'] = request.get_application_actions_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetApplicationActions',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetApplicationActionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_application_actions(
        self,
        request: taihao_20210331_models.GetApplicationActionsRequest,
    ) -> taihao_20210331_models.GetApplicationActionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_application_actions_with_options(request, runtime)

    async def get_application_actions_async(
        self,
        request: taihao_20210331_models.GetApplicationActionsRequest,
    ) -> taihao_20210331_models.GetApplicationActionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_application_actions_with_options_async(request, runtime)

    def get_auto_scaling_activity_with_options(
        self,
        tmp_req: taihao_20210331_models.GetAutoScalingActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetAutoScalingActivityResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetAutoScalingActivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_auto_scaling_activity_param):
            request.get_auto_scaling_activity_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_auto_scaling_activity_param), 'getAutoScalingActivityParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_auto_scaling_activity_param_shrink):
            body['getAutoScalingActivityParam'] = request.get_auto_scaling_activity_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAutoScalingActivity',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetAutoScalingActivityResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_activity_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetAutoScalingActivityRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetAutoScalingActivityResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetAutoScalingActivityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_auto_scaling_activity_param):
            request.get_auto_scaling_activity_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_auto_scaling_activity_param), 'getAutoScalingActivityParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_auto_scaling_activity_param_shrink):
            body['getAutoScalingActivityParam'] = request.get_auto_scaling_activity_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAutoScalingActivity',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetAutoScalingActivityResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_activity(
        self,
        request: taihao_20210331_models.GetAutoScalingActivityRequest,
    ) -> taihao_20210331_models.GetAutoScalingActivityResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scaling_activity_with_options(request, runtime)

    async def get_auto_scaling_activity_async(
        self,
        request: taihao_20210331_models.GetAutoScalingActivityRequest,
    ) -> taihao_20210331_models.GetAutoScalingActivityResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scaling_activity_with_options_async(request, runtime)

    def get_auto_scaling_policy_with_options(
        self,
        tmp_req: taihao_20210331_models.GetAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_auto_scaling_policy_param):
            request.get_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_auto_scaling_policy_param), 'getAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_auto_scaling_policy_param_shrink):
            body['getAutoScalingPolicyParam'] = request.get_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_auto_scaling_policy_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_auto_scaling_policy_param):
            request.get_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_auto_scaling_policy_param), 'getAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_auto_scaling_policy_param_shrink):
            body['getAutoScalingPolicyParam'] = request.get_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_auto_scaling_policy(
        self,
        request: taihao_20210331_models.GetAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.GetAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scaling_policy_with_options(request, runtime)

    async def get_auto_scaling_policy_async(
        self,
        request: taihao_20210331_models.GetAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.GetAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_auto_scaling_policy_with_options_async(request, runtime)

    def get_cluster_with_options(
        self,
        tmp_req: taihao_20210331_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_base_param):
            request.cluster_base_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.cluster_base_param), 'clusterBaseParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_base_param_shrink):
            body['clusterBaseParam'] = request.cluster_base_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.cluster_base_param):
            request.cluster_base_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.cluster_base_param), 'clusterBaseParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.cluster_base_param_shrink):
            body['clusterBaseParam'] = request.cluster_base_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster(
        self,
        request: taihao_20210331_models.GetClusterRequest,
    ) -> taihao_20210331_models.GetClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    async def get_cluster_async(
        self,
        request: taihao_20210331_models.GetClusterRequest,
    ) -> taihao_20210331_models.GetClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_with_options_async(request, runtime)

    def get_cluster_operation_with_options(
        self,
        tmp_req: taihao_20210331_models.GetClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterOperationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterOperationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_cluster_operation_param):
            request.get_cluster_operation_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_cluster_operation_param), 'getClusterOperationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_cluster_operation_param_shrink):
            body['getClusterOperationParam'] = request.get_cluster_operation_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClusterOperation',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_operation_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterOperationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterOperationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_cluster_operation_param):
            request.get_cluster_operation_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_cluster_operation_param), 'getClusterOperationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_cluster_operation_param_shrink):
            body['getClusterOperationParam'] = request.get_cluster_operation_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClusterOperation',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_operation(
        self,
        request: taihao_20210331_models.GetClusterOperationRequest,
    ) -> taihao_20210331_models.GetClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_operation_with_options(request, runtime)

    async def get_cluster_operation_async(
        self,
        request: taihao_20210331_models.GetClusterOperationRequest,
    ) -> taihao_20210331_models.GetClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_operation_with_options_async(request, runtime)

    def get_cluster_operation_node_with_options(
        self,
        tmp_req: taihao_20210331_models.GetClusterOperationNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterOperationNodeResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterOperationNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_cluster_operation_node_param):
            request.get_cluster_operation_node_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_cluster_operation_node_param), 'getClusterOperationNodeParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_cluster_operation_node_param_shrink):
            body['getClusterOperationNodeParam'] = request.get_cluster_operation_node_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClusterOperationNode',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterOperationNodeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_operation_node_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetClusterOperationNodeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterOperationNodeResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterOperationNodeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_cluster_operation_node_param):
            request.get_cluster_operation_node_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_cluster_operation_node_param), 'getClusterOperationNodeParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_cluster_operation_node_param_shrink):
            body['getClusterOperationNodeParam'] = request.get_cluster_operation_node_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClusterOperationNode',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterOperationNodeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_operation_node(
        self,
        request: taihao_20210331_models.GetClusterOperationNodeRequest,
    ) -> taihao_20210331_models.GetClusterOperationNodeResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_operation_node_with_options(request, runtime)

    async def get_cluster_operation_node_async(
        self,
        request: taihao_20210331_models.GetClusterOperationNodeRequest,
    ) -> taihao_20210331_models.GetClusterOperationNodeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_operation_node_with_options_async(request, runtime)

    def get_cluster_operation_task_log_with_options(
        self,
        tmp_req: taihao_20210331_models.GetClusterOperationTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterOperationTaskLogResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterOperationTaskLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_cluster_operation_task_log_param):
            request.get_cluster_operation_task_log_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_cluster_operation_task_log_param), 'getClusterOperationTaskLogParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_cluster_operation_task_log_param_shrink):
            body['getClusterOperationTaskLogParam'] = request.get_cluster_operation_task_log_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClusterOperationTaskLog',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterOperationTaskLogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_operation_task_log_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetClusterOperationTaskLogRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterOperationTaskLogResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterOperationTaskLogShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_cluster_operation_task_log_param):
            request.get_cluster_operation_task_log_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_cluster_operation_task_log_param), 'getClusterOperationTaskLogParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_cluster_operation_task_log_param_shrink):
            body['getClusterOperationTaskLogParam'] = request.get_cluster_operation_task_log_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClusterOperationTaskLog',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterOperationTaskLogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_operation_task_log(
        self,
        request: taihao_20210331_models.GetClusterOperationTaskLogRequest,
    ) -> taihao_20210331_models.GetClusterOperationTaskLogResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_operation_task_log_with_options(request, runtime)

    async def get_cluster_operation_task_log_async(
        self,
        request: taihao_20210331_models.GetClusterOperationTaskLogRequest,
    ) -> taihao_20210331_models.GetClusterOperationTaskLogResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_operation_task_log_with_options_async(request, runtime)

    def get_cluster_script_detail_with_options(
        self,
        tmp_req: taihao_20210331_models.GetClusterScriptDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterScriptDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterScriptDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_cluster_script_detail_param):
            request.get_cluster_script_detail_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_cluster_script_detail_param), 'getClusterScriptDetailParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_cluster_script_detail_param_shrink):
            body['getClusterScriptDetailParam'] = request.get_cluster_script_detail_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClusterScriptDetail',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterScriptDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_cluster_script_detail_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetClusterScriptDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetClusterScriptDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetClusterScriptDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_cluster_script_detail_param):
            request.get_cluster_script_detail_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_cluster_script_detail_param), 'getClusterScriptDetailParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_cluster_script_detail_param_shrink):
            body['getClusterScriptDetailParam'] = request.get_cluster_script_detail_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetClusterScriptDetail',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetClusterScriptDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_cluster_script_detail(
        self,
        request: taihao_20210331_models.GetClusterScriptDetailRequest,
    ) -> taihao_20210331_models.GetClusterScriptDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_script_detail_with_options(request, runtime)

    async def get_cluster_script_detail_async(
        self,
        request: taihao_20210331_models.GetClusterScriptDetailRequest,
    ) -> taihao_20210331_models.GetClusterScriptDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_cluster_script_detail_with_options_async(request, runtime)

    def get_config_tags_with_options(
        self,
        tmp_req: taihao_20210331_models.GetConfigTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetConfigTagsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetConfigTagsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_config_tags_param):
            request.get_config_tags_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_config_tags_param), 'getConfigTagsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_config_tags_param_shrink):
            body['getConfigTagsParam'] = request.get_config_tags_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConfigTags',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetConfigTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_config_tags_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetConfigTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetConfigTagsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetConfigTagsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_config_tags_param):
            request.get_config_tags_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_config_tags_param), 'getConfigTagsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_config_tags_param_shrink):
            body['getConfigTagsParam'] = request.get_config_tags_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetConfigTags',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetConfigTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_config_tags(
        self,
        request: taihao_20210331_models.GetConfigTagsRequest,
    ) -> taihao_20210331_models.GetConfigTagsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_config_tags_with_options(request, runtime)

    async def get_config_tags_async(
        self,
        request: taihao_20210331_models.GetConfigTagsRequest,
    ) -> taihao_20210331_models.GetConfigTagsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_config_tags_with_options_async(request, runtime)

    def get_depend_applications_with_options(
        self,
        tmp_req: taihao_20210331_models.GetDependApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetDependApplicationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetDependApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_depend_applications_param):
            request.get_depend_applications_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_depend_applications_param), 'getDependApplicationsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_depend_applications_param_shrink):
            body['getDependApplicationsParam'] = request.get_depend_applications_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDependApplications',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetDependApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_depend_applications_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetDependApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetDependApplicationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetDependApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_depend_applications_param):
            request.get_depend_applications_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_depend_applications_param), 'getDependApplicationsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_depend_applications_param_shrink):
            body['getDependApplicationsParam'] = request.get_depend_applications_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDependApplications',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetDependApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_depend_applications(
        self,
        request: taihao_20210331_models.GetDependApplicationsRequest,
    ) -> taihao_20210331_models.GetDependApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_depend_applications_with_options(request, runtime)

    async def get_depend_applications_async(
        self,
        request: taihao_20210331_models.GetDependApplicationsRequest,
    ) -> taihao_20210331_models.GetDependApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_depend_applications_with_options_async(request, runtime)

    def get_main_version_detail_with_options(
        self,
        tmp_req: taihao_20210331_models.GetMainVersionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetMainVersionDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetMainVersionDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_main_version_detail_param):
            request.get_main_version_detail_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_main_version_detail_param), 'getMainVersionDetailParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_main_version_detail_param_shrink):
            body['getMainVersionDetailParam'] = request.get_main_version_detail_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMainVersionDetail',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetMainVersionDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_main_version_detail_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetMainVersionDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetMainVersionDetailResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetMainVersionDetailShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_main_version_detail_param):
            request.get_main_version_detail_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_main_version_detail_param), 'getMainVersionDetailParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_main_version_detail_param_shrink):
            body['getMainVersionDetailParam'] = request.get_main_version_detail_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMainVersionDetail',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetMainVersionDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_main_version_detail(
        self,
        request: taihao_20210331_models.GetMainVersionDetailRequest,
    ) -> taihao_20210331_models.GetMainVersionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_main_version_detail_with_options(request, runtime)

    async def get_main_version_detail_async(
        self,
        request: taihao_20210331_models.GetMainVersionDetailRequest,
    ) -> taihao_20210331_models.GetMainVersionDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_main_version_detail_with_options_async(request, runtime)

    def get_report_with_options(
        self,
        tmp_req: taihao_20210331_models.GetReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetReportResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_report_param):
            request.get_report_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_report_param), 'getReportParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_report_param_shrink):
            body['getReportParam'] = request.get_report_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReport',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_report_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetReportRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetReportResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetReportShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_report_param):
            request.get_report_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_report_param), 'getReportParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_report_param_shrink):
            body['getReportParam'] = request.get_report_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReport',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_report(
        self,
        request: taihao_20210331_models.GetReportRequest,
    ) -> taihao_20210331_models.GetReportResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_report_with_options(request, runtime)

    async def get_report_async(
        self,
        request: taihao_20210331_models.GetReportRequest,
    ) -> taihao_20210331_models.GetReportResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_report_with_options_async(request, runtime)

    def get_report_data_with_options(
        self,
        tmp_req: taihao_20210331_models.GetReportDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetReportDataResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetReportDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_report_data_param):
            request.get_report_data_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_report_data_param), 'getReportDataParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_report_data_param_shrink):
            body['getReportDataParam'] = request.get_report_data_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReportData',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetReportDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_report_data_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetReportDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetReportDataResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetReportDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_report_data_param):
            request.get_report_data_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_report_data_param), 'getReportDataParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_report_data_param_shrink):
            body['getReportDataParam'] = request.get_report_data_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetReportData',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetReportDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_report_data(
        self,
        request: taihao_20210331_models.GetReportDataRequest,
    ) -> taihao_20210331_models.GetReportDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_report_data_with_options(request, runtime)

    async def get_report_data_async(
        self,
        request: taihao_20210331_models.GetReportDataRequest,
    ) -> taihao_20210331_models.GetReportDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_report_data_with_options_async(request, runtime)

    def get_stack_application_with_options(
        self,
        tmp_req: taihao_20210331_models.GetStackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetStackApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetStackApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_stack_application_param):
            request.get_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_stack_application_param), 'getStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_stack_application_param_shrink):
            body['getStackApplicationParam'] = request.get_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStackApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetStackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_application_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetStackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetStackApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetStackApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_stack_application_param):
            request.get_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_stack_application_param), 'getStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_stack_application_param_shrink):
            body['getStackApplicationParam'] = request.get_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStackApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetStackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_application(
        self,
        request: taihao_20210331_models.GetStackApplicationRequest,
    ) -> taihao_20210331_models.GetStackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_stack_application_with_options(request, runtime)

    async def get_stack_application_async(
        self,
        request: taihao_20210331_models.GetStackApplicationRequest,
    ) -> taihao_20210331_models.GetStackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_application_with_options_async(request, runtime)

    def get_workflow_definition_with_options(
        self,
        tmp_req: taihao_20210331_models.GetWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetWorkflowDefinitionResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetWorkflowDefinitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_workflow_definition_param):
            request.get_workflow_definition_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_workflow_definition_param), 'getWorkflowDefinitionParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_workflow_definition_param_shrink):
            body['getWorkflowDefinitionParam'] = request.get_workflow_definition_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkflowDefinition',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetWorkflowDefinitionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_definition_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetWorkflowDefinitionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetWorkflowDefinitionResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetWorkflowDefinitionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_workflow_definition_param):
            request.get_workflow_definition_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_workflow_definition_param), 'getWorkflowDefinitionParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_workflow_definition_param_shrink):
            body['getWorkflowDefinitionParam'] = request.get_workflow_definition_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkflowDefinition',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetWorkflowDefinitionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_definition(
        self,
        request: taihao_20210331_models.GetWorkflowDefinitionRequest,
    ) -> taihao_20210331_models.GetWorkflowDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_workflow_definition_with_options(request, runtime)

    async def get_workflow_definition_async(
        self,
        request: taihao_20210331_models.GetWorkflowDefinitionRequest,
    ) -> taihao_20210331_models.GetWorkflowDefinitionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_workflow_definition_with_options_async(request, runtime)

    def get_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.GetWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_workflow_instance_param):
            request.get_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_workflow_instance_param), 'getWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_workflow_instance_param_shrink):
            body['getWorkflowInstanceParam'] = request.get_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.GetWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.GetWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.GetWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_workflow_instance_param):
            request.get_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_workflow_instance_param), 'getWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_workflow_instance_param_shrink):
            body['getWorkflowInstanceParam'] = request.get_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.GetWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workflow_instance(
        self,
        request: taihao_20210331_models.GetWorkflowInstanceRequest,
    ) -> taihao_20210331_models.GetWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_workflow_instance_with_options(request, runtime)

    async def get_workflow_instance_async(
        self,
        request: taihao_20210331_models.GetWorkflowInstanceRequest,
    ) -> taihao_20210331_models.GetWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_workflow_instance_with_options_async(request, runtime)

    def increase_node_group_with_options(
        self,
        tmp_req: taihao_20210331_models.IncreaseNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.IncreaseNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.IncreaseNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.increase_node_group_param):
            request.increase_node_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.increase_node_group_param), 'increaseNodeGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.increase_node_group_param_shrink):
            body['increaseNodeGroupParam'] = request.increase_node_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IncreaseNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.IncreaseNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def increase_node_group_with_options_async(
        self,
        tmp_req: taihao_20210331_models.IncreaseNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.IncreaseNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.IncreaseNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.increase_node_group_param):
            request.increase_node_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.increase_node_group_param), 'increaseNodeGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.increase_node_group_param_shrink):
            body['increaseNodeGroupParam'] = request.increase_node_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IncreaseNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.IncreaseNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def increase_node_group(
        self,
        request: taihao_20210331_models.IncreaseNodeGroupRequest,
    ) -> taihao_20210331_models.IncreaseNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.increase_node_group_with_options(request, runtime)

    async def increase_node_group_async(
        self,
        request: taihao_20210331_models.IncreaseNodeGroupRequest,
    ) -> taihao_20210331_models.IncreaseNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.increase_node_group_with_options_async(request, runtime)

    def increase_node_group_disk_with_options(
        self,
        tmp_req: taihao_20210331_models.IncreaseNodeGroupDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.IncreaseNodeGroupDiskResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.IncreaseNodeGroupDiskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.increase_disk_param):
            request.increase_disk_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.increase_disk_param), 'increaseDiskParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.increase_disk_param_shrink):
            body['increaseDiskParam'] = request.increase_disk_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IncreaseNodeGroupDisk',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.IncreaseNodeGroupDiskResponse(),
            self.call_api(params, req, runtime)
        )

    async def increase_node_group_disk_with_options_async(
        self,
        tmp_req: taihao_20210331_models.IncreaseNodeGroupDiskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.IncreaseNodeGroupDiskResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.IncreaseNodeGroupDiskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.increase_disk_param):
            request.increase_disk_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.increase_disk_param), 'increaseDiskParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.increase_disk_param_shrink):
            body['increaseDiskParam'] = request.increase_disk_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IncreaseNodeGroupDisk',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.IncreaseNodeGroupDiskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def increase_node_group_disk(
        self,
        request: taihao_20210331_models.IncreaseNodeGroupDiskRequest,
    ) -> taihao_20210331_models.IncreaseNodeGroupDiskResponse:
        runtime = util_models.RuntimeOptions()
        return self.increase_node_group_disk_with_options(request, runtime)

    async def increase_node_group_disk_async(
        self,
        request: taihao_20210331_models.IncreaseNodeGroupDiskRequest,
    ) -> taihao_20210331_models.IncreaseNodeGroupDiskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.increase_node_group_disk_with_options_async(request, runtime)

    def join_resource_group_with_options(
        self,
        tmp_req: taihao_20210331_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.JoinResourceGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.JoinResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.join_resource_group_param):
            request.join_resource_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.join_resource_group_param), 'joinResourceGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.join_resource_group_param_shrink):
            body['joinResourceGroupParam'] = request.join_resource_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinResourceGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.JoinResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def join_resource_group_with_options_async(
        self,
        tmp_req: taihao_20210331_models.JoinResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.JoinResourceGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.JoinResourceGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.join_resource_group_param):
            request.join_resource_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.join_resource_group_param), 'joinResourceGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.join_resource_group_param_shrink):
            body['joinResourceGroupParam'] = request.join_resource_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinResourceGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.JoinResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def join_resource_group(
        self,
        request: taihao_20210331_models.JoinResourceGroupRequest,
    ) -> taihao_20210331_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    async def join_resource_group_async(
        self,
        request: taihao_20210331_models.JoinResourceGroupRequest,
    ) -> taihao_20210331_models.JoinResourceGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.join_resource_group_with_options_async(request, runtime)

    def list_ack_cluster_node_pools_with_options(
        self,
        tmp_req: taihao_20210331_models.ListAckClusterNodePoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAckClusterNodePoolsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAckClusterNodePoolsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_ack_cluster_node_pools_param):
            request.list_ack_cluster_node_pools_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_ack_cluster_node_pools_param), 'listAckClusterNodePoolsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_ack_cluster_node_pools_param_shrink):
            body['listAckClusterNodePoolsParam'] = request.list_ack_cluster_node_pools_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAckClusterNodePools',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAckClusterNodePoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ack_cluster_node_pools_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListAckClusterNodePoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAckClusterNodePoolsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAckClusterNodePoolsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_ack_cluster_node_pools_param):
            request.list_ack_cluster_node_pools_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_ack_cluster_node_pools_param), 'listAckClusterNodePoolsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_ack_cluster_node_pools_param_shrink):
            body['listAckClusterNodePoolsParam'] = request.list_ack_cluster_node_pools_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAckClusterNodePools',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAckClusterNodePoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ack_cluster_node_pools(
        self,
        request: taihao_20210331_models.ListAckClusterNodePoolsRequest,
    ) -> taihao_20210331_models.ListAckClusterNodePoolsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ack_cluster_node_pools_with_options(request, runtime)

    async def list_ack_cluster_node_pools_async(
        self,
        request: taihao_20210331_models.ListAckClusterNodePoolsRequest,
    ) -> taihao_20210331_models.ListAckClusterNodePoolsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ack_cluster_node_pools_with_options_async(request, runtime)

    def list_ack_cluster_nodes_with_options(
        self,
        tmp_req: taihao_20210331_models.ListAckClusterNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAckClusterNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAckClusterNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_ack_cluster_nodes_param):
            request.list_ack_cluster_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_ack_cluster_nodes_param), 'listAckClusterNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_ack_cluster_nodes_param_shrink):
            body['listAckClusterNodesParam'] = request.list_ack_cluster_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAckClusterNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAckClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ack_cluster_nodes_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListAckClusterNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAckClusterNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAckClusterNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_ack_cluster_nodes_param):
            request.list_ack_cluster_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_ack_cluster_nodes_param), 'listAckClusterNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_ack_cluster_nodes_param_shrink):
            body['listAckClusterNodesParam'] = request.list_ack_cluster_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAckClusterNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAckClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ack_cluster_nodes(
        self,
        request: taihao_20210331_models.ListAckClusterNodesRequest,
    ) -> taihao_20210331_models.ListAckClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_ack_cluster_nodes_with_options(request, runtime)

    async def list_ack_cluster_nodes_async(
        self,
        request: taihao_20210331_models.ListAckClusterNodesRequest,
    ) -> taihao_20210331_models.ListAckClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_ack_cluster_nodes_with_options_async(request, runtime)

    def list_application_meta_with_options(
        self,
        tmp_req: taihao_20210331_models.ListApplicationMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListApplicationMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListApplicationMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_application_meta_param):
            request.list_application_meta_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_application_meta_param), 'listApplicationMetaParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_application_meta_param_shrink):
            body['listApplicationMetaParam'] = request.list_application_meta_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApplicationMeta',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListApplicationMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_application_meta_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListApplicationMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListApplicationMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListApplicationMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_application_meta_param):
            request.list_application_meta_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_application_meta_param), 'listApplicationMetaParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_application_meta_param_shrink):
            body['listApplicationMetaParam'] = request.list_application_meta_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApplicationMeta',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListApplicationMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_application_meta(
        self,
        request: taihao_20210331_models.ListApplicationMetaRequest,
    ) -> taihao_20210331_models.ListApplicationMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_application_meta_with_options(request, runtime)

    async def list_application_meta_async(
        self,
        request: taihao_20210331_models.ListApplicationMetaRequest,
    ) -> taihao_20210331_models.ListApplicationMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_application_meta_with_options_async(request, runtime)

    def list_applications_with_options(
        self,
        tmp_req: taihao_20210331_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListApplicationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_applications_param):
            request.list_applications_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_applications_param), 'listApplicationsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_applications_param_shrink):
            body['listApplicationsParam'] = request.list_applications_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_applications_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListApplicationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_applications_param):
            request.list_applications_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_applications_param), 'listApplicationsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_applications_param_shrink):
            body['listApplicationsParam'] = request.list_applications_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_applications(
        self,
        request: taihao_20210331_models.ListApplicationsRequest,
    ) -> taihao_20210331_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    async def list_applications_async(
        self,
        request: taihao_20210331_models.ListApplicationsRequest,
    ) -> taihao_20210331_models.ListApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_applications_with_options_async(request, runtime)

    def list_auto_scaling_activities_with_options(
        self,
        tmp_req: taihao_20210331_models.ListAutoScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAutoScalingActivitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAutoScalingActivitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_auto_scaling_activities_param):
            request.list_auto_scaling_activities_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_auto_scaling_activities_param), 'listAutoScalingActivitiesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_auto_scaling_activities_param_shrink):
            body['listAutoScalingActivitiesParam'] = request.list_auto_scaling_activities_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutoScalingActivities',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAutoScalingActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_scaling_activities_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListAutoScalingActivitiesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAutoScalingActivitiesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAutoScalingActivitiesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_auto_scaling_activities_param):
            request.list_auto_scaling_activities_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_auto_scaling_activities_param), 'listAutoScalingActivitiesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_auto_scaling_activities_param_shrink):
            body['listAutoScalingActivitiesParam'] = request.list_auto_scaling_activities_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutoScalingActivities',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAutoScalingActivitiesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_scaling_activities(
        self,
        request: taihao_20210331_models.ListAutoScalingActivitiesRequest,
    ) -> taihao_20210331_models.ListAutoScalingActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_auto_scaling_activities_with_options(request, runtime)

    async def list_auto_scaling_activities_async(
        self,
        request: taihao_20210331_models.ListAutoScalingActivitiesRequest,
    ) -> taihao_20210331_models.ListAutoScalingActivitiesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_scaling_activities_with_options_async(request, runtime)

    def list_auto_scaling_metrics_with_options(
        self,
        tmp_req: taihao_20210331_models.ListAutoScalingMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAutoScalingMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAutoScalingMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_auto_scaling_metrics_param):
            request.list_auto_scaling_metrics_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_auto_scaling_metrics_param), 'listAutoScalingMetricsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_auto_scaling_metrics_param_shrink):
            body['listAutoScalingMetricsParam'] = request.list_auto_scaling_metrics_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutoScalingMetrics',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAutoScalingMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_scaling_metrics_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListAutoScalingMetricsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAutoScalingMetricsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAutoScalingMetricsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_auto_scaling_metrics_param):
            request.list_auto_scaling_metrics_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_auto_scaling_metrics_param), 'listAutoScalingMetricsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_auto_scaling_metrics_param_shrink):
            body['listAutoScalingMetricsParam'] = request.list_auto_scaling_metrics_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutoScalingMetrics',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAutoScalingMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_scaling_metrics(
        self,
        request: taihao_20210331_models.ListAutoScalingMetricsRequest,
    ) -> taihao_20210331_models.ListAutoScalingMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_auto_scaling_metrics_with_options(request, runtime)

    async def list_auto_scaling_metrics_async(
        self,
        request: taihao_20210331_models.ListAutoScalingMetricsRequest,
    ) -> taihao_20210331_models.ListAutoScalingMetricsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_scaling_metrics_with_options_async(request, runtime)

    def list_auto_scaling_policies_with_options(
        self,
        tmp_req: taihao_20210331_models.ListAutoScalingPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAutoScalingPoliciesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAutoScalingPoliciesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_auto_scaling_policies_param):
            request.list_auto_scaling_policies_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_auto_scaling_policies_param), 'listAutoScalingPoliciesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_auto_scaling_policies_param_shrink):
            body['listAutoScalingPoliciesParam'] = request.list_auto_scaling_policies_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutoScalingPolicies',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAutoScalingPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_scaling_policies_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListAutoScalingPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAutoScalingPoliciesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAutoScalingPoliciesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_auto_scaling_policies_param):
            request.list_auto_scaling_policies_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_auto_scaling_policies_param), 'listAutoScalingPoliciesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_auto_scaling_policies_param_shrink):
            body['listAutoScalingPoliciesParam'] = request.list_auto_scaling_policies_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutoScalingPolicies',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAutoScalingPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_scaling_policies(
        self,
        request: taihao_20210331_models.ListAutoScalingPoliciesRequest,
    ) -> taihao_20210331_models.ListAutoScalingPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_auto_scaling_policies_with_options(request, runtime)

    async def list_auto_scaling_policies_async(
        self,
        request: taihao_20210331_models.ListAutoScalingPoliciesRequest,
    ) -> taihao_20210331_models.ListAutoScalingPoliciesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_scaling_policies_with_options_async(request, runtime)

    def list_auto_scaling_rules_with_options(
        self,
        tmp_req: taihao_20210331_models.ListAutoScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAutoScalingRulesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAutoScalingRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_auto_scaling_rules_param):
            request.list_auto_scaling_rules_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_auto_scaling_rules_param), 'listAutoScalingRulesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_auto_scaling_rules_param_shrink):
            body['listAutoScalingRulesParam'] = request.list_auto_scaling_rules_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutoScalingRules',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAutoScalingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_auto_scaling_rules_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListAutoScalingRulesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListAutoScalingRulesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListAutoScalingRulesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_auto_scaling_rules_param):
            request.list_auto_scaling_rules_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_auto_scaling_rules_param), 'listAutoScalingRulesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_auto_scaling_rules_param_shrink):
            body['listAutoScalingRulesParam'] = request.list_auto_scaling_rules_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAutoScalingRules',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListAutoScalingRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_auto_scaling_rules(
        self,
        request: taihao_20210331_models.ListAutoScalingRulesRequest,
    ) -> taihao_20210331_models.ListAutoScalingRulesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_auto_scaling_rules_with_options(request, runtime)

    async def list_auto_scaling_rules_async(
        self,
        request: taihao_20210331_models.ListAutoScalingRulesRequest,
    ) -> taihao_20210331_models.ListAutoScalingRulesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_auto_scaling_rules_with_options_async(request, runtime)

    def list_cluster_ack_by_ack_instance_ids_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClusterAckByAckInstanceIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterAckByAckInstanceIdsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterAckByAckInstanceIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_ack_by_instance_ids_param):
            request.list_cluster_ack_by_instance_ids_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_ack_by_instance_ids_param), 'listClusterAckByInstanceIdsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_ack_by_instance_ids_param_shrink):
            body['listClusterAckByInstanceIdsParam'] = request.list_cluster_ack_by_instance_ids_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterAckByAckInstanceIds',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterAckByAckInstanceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_ack_by_ack_instance_ids_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClusterAckByAckInstanceIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterAckByAckInstanceIdsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterAckByAckInstanceIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_ack_by_instance_ids_param):
            request.list_cluster_ack_by_instance_ids_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_ack_by_instance_ids_param), 'listClusterAckByInstanceIdsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_ack_by_instance_ids_param_shrink):
            body['listClusterAckByInstanceIdsParam'] = request.list_cluster_ack_by_instance_ids_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterAckByAckInstanceIds',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterAckByAckInstanceIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_ack_by_ack_instance_ids(
        self,
        request: taihao_20210331_models.ListClusterAckByAckInstanceIdsRequest,
    ) -> taihao_20210331_models.ListClusterAckByAckInstanceIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_ack_by_ack_instance_ids_with_options(request, runtime)

    async def list_cluster_ack_by_ack_instance_ids_async(
        self,
        request: taihao_20210331_models.ListClusterAckByAckInstanceIdsRequest,
    ) -> taihao_20210331_models.ListClusterAckByAckInstanceIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_ack_by_ack_instance_ids_with_options_async(request, runtime)

    def list_cluster_ack_by_cluster_ids_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClusterAckByClusterIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterAckByClusterIdsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterAckByClusterIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_ack_cluster_by_cluster_ids_param):
            request.list_cluster_ack_cluster_by_cluster_ids_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_ack_cluster_by_cluster_ids_param), 'listClusterAckClusterByClusterIdsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_ack_cluster_by_cluster_ids_param_shrink):
            body['listClusterAckClusterByClusterIdsParam'] = request.list_cluster_ack_cluster_by_cluster_ids_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterAckByClusterIds',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterAckByClusterIdsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_ack_by_cluster_ids_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClusterAckByClusterIdsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterAckByClusterIdsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterAckByClusterIdsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_ack_cluster_by_cluster_ids_param):
            request.list_cluster_ack_cluster_by_cluster_ids_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_ack_cluster_by_cluster_ids_param), 'listClusterAckClusterByClusterIdsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_ack_cluster_by_cluster_ids_param_shrink):
            body['listClusterAckClusterByClusterIdsParam'] = request.list_cluster_ack_cluster_by_cluster_ids_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterAckByClusterIds',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterAckByClusterIdsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_ack_by_cluster_ids(
        self,
        request: taihao_20210331_models.ListClusterAckByClusterIdsRequest,
    ) -> taihao_20210331_models.ListClusterAckByClusterIdsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_ack_by_cluster_ids_with_options(request, runtime)

    async def list_cluster_ack_by_cluster_ids_async(
        self,
        request: taihao_20210331_models.ListClusterAckByClusterIdsRequest,
    ) -> taihao_20210331_models.ListClusterAckByClusterIdsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_ack_by_cluster_ids_with_options_async(request, runtime)

    def list_cluster_node_group_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClusterNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_node_groups_param):
            request.list_cluster_node_groups_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_node_groups_param), 'listClusterNodeGroupsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_node_groups_param_shrink):
            body['listClusterNodeGroupsParam'] = request.list_cluster_node_groups_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_node_group_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClusterNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_node_groups_param):
            request.list_cluster_node_groups_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_node_groups_param), 'listClusterNodeGroupsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_node_groups_param_shrink):
            body['listClusterNodeGroupsParam'] = request.list_cluster_node_groups_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_node_group(
        self,
        request: taihao_20210331_models.ListClusterNodeGroupRequest,
    ) -> taihao_20210331_models.ListClusterNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_node_group_with_options(request, runtime)

    async def list_cluster_node_group_async(
        self,
        request: taihao_20210331_models.ListClusterNodeGroupRequest,
    ) -> taihao_20210331_models.ListClusterNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_node_group_with_options_async(request, runtime)

    def list_cluster_operation_nodes_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClusterOperationNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterOperationNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterOperationNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_operation_nodes_param):
            request.list_cluster_operation_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_operation_nodes_param), 'listClusterOperationNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_operation_nodes_param_shrink):
            body['listClusterOperationNodesParam'] = request.list_cluster_operation_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterOperationNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterOperationNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_operation_nodes_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClusterOperationNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterOperationNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterOperationNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_operation_nodes_param):
            request.list_cluster_operation_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_operation_nodes_param), 'listClusterOperationNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_operation_nodes_param_shrink):
            body['listClusterOperationNodesParam'] = request.list_cluster_operation_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterOperationNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterOperationNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_operation_nodes(
        self,
        request: taihao_20210331_models.ListClusterOperationNodesRequest,
    ) -> taihao_20210331_models.ListClusterOperationNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_nodes_with_options(request, runtime)

    async def list_cluster_operation_nodes_async(
        self,
        request: taihao_20210331_models.ListClusterOperationNodesRequest,
    ) -> taihao_20210331_models.ListClusterOperationNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operation_nodes_with_options_async(request, runtime)

    def list_cluster_operation_tasks_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClusterOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterOperationTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterOperationTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_operation_tasks_param):
            request.list_cluster_operation_tasks_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_operation_tasks_param), 'listClusterOperationTasksParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_operation_tasks_param_shrink):
            body['listClusterOperationTasksParam'] = request.list_cluster_operation_tasks_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterOperationTasks',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterOperationTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_operation_tasks_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClusterOperationTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterOperationTasksResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterOperationTasksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_operation_tasks_param):
            request.list_cluster_operation_tasks_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_operation_tasks_param), 'listClusterOperationTasksParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_operation_tasks_param_shrink):
            body['listClusterOperationTasksParam'] = request.list_cluster_operation_tasks_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterOperationTasks',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterOperationTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_operation_tasks(
        self,
        request: taihao_20210331_models.ListClusterOperationTasksRequest,
    ) -> taihao_20210331_models.ListClusterOperationTasksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operation_tasks_with_options(request, runtime)

    async def list_cluster_operation_tasks_async(
        self,
        request: taihao_20210331_models.ListClusterOperationTasksRequest,
    ) -> taihao_20210331_models.ListClusterOperationTasksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operation_tasks_with_options_async(request, runtime)

    def list_cluster_operations_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClusterOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterOperationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterOperationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_operations_param):
            request.list_cluster_operations_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_operations_param), 'listClusterOperationsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_operations_param_shrink):
            body['listClusterOperationsParam'] = request.list_cluster_operations_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterOperations',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_operations_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClusterOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterOperationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterOperationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_operations_param):
            request.list_cluster_operations_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_operations_param), 'listClusterOperationsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_operations_param_shrink):
            body['listClusterOperationsParam'] = request.list_cluster_operations_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterOperations',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_operations(
        self,
        request: taihao_20210331_models.ListClusterOperationsRequest,
    ) -> taihao_20210331_models.ListClusterOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_operations_with_options(request, runtime)

    async def list_cluster_operations_async(
        self,
        request: taihao_20210331_models.ListClusterOperationsRequest,
    ) -> taihao_20210331_models.ListClusterOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_operations_with_options_async(request, runtime)

    def list_cluster_orders_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClusterOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterOrdersResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterOrdersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_orders_param):
            request.list_cluster_orders_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_orders_param), 'listClusterOrdersParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_orders_param_shrink):
            body['listClusterOrdersParam'] = request.list_cluster_orders_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterOrders',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_orders_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClusterOrdersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterOrdersResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterOrdersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_orders_param):
            request.list_cluster_orders_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_orders_param), 'listClusterOrdersParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_orders_param_shrink):
            body['listClusterOrdersParam'] = request.list_cluster_orders_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterOrders',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterOrdersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_orders(
        self,
        request: taihao_20210331_models.ListClusterOrdersRequest,
    ) -> taihao_20210331_models.ListClusterOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_orders_with_options(request, runtime)

    async def list_cluster_orders_async(
        self,
        request: taihao_20210331_models.ListClusterOrdersRequest,
    ) -> taihao_20210331_models.ListClusterOrdersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_orders_with_options_async(request, runtime)

    def list_cluster_scripts_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClusterScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterScriptsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterScriptsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_scripts_param):
            request.list_cluster_scripts_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_scripts_param), 'listClusterScriptsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_scripts_param_shrink):
            body['listClusterScriptsParam'] = request.list_cluster_scripts_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterScripts',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterScriptsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_scripts_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClusterScriptsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterScriptsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterScriptsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_scripts_param):
            request.list_cluster_scripts_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_scripts_param), 'listClusterScriptsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_scripts_param_shrink):
            body['listClusterScriptsParam'] = request.list_cluster_scripts_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterScripts',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterScriptsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_scripts(
        self,
        request: taihao_20210331_models.ListClusterScriptsRequest,
    ) -> taihao_20210331_models.ListClusterScriptsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_scripts_with_options(request, runtime)

    async def list_cluster_scripts_async(
        self,
        request: taihao_20210331_models.ListClusterScriptsRequest,
    ) -> taihao_20210331_models.ListClusterScriptsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_scripts_with_options_async(request, runtime)

    def list_cluster_users_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClusterUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_users_param):
            request.list_cluster_users_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_users_param), 'listClusterUsersParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_users_param_shrink):
            body['listClusterUsersParam'] = request.list_cluster_users_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterUsers',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_cluster_users_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClusterUsersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClusterUsersResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClusterUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_cluster_users_param):
            request.list_cluster_users_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_cluster_users_param), 'listClusterUsersParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_cluster_users_param_shrink):
            body['listClusterUsersParam'] = request.list_cluster_users_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusterUsers',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClusterUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_cluster_users(
        self,
        request: taihao_20210331_models.ListClusterUsersRequest,
    ) -> taihao_20210331_models.ListClusterUsersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_users_with_options(request, runtime)

    async def list_cluster_users_async(
        self,
        request: taihao_20210331_models.ListClusterUsersRequest,
    ) -> taihao_20210331_models.ListClusterUsersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_cluster_users_with_options_async(request, runtime)

    def list_clusters_with_options(
        self,
        tmp_req: taihao_20210331_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClustersResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_clusters_param):
            request.list_clusters_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_clusters_param), 'listClustersParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_clusters_param_shrink):
            body['listClustersParam'] = request.list_clusters_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_clusters_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListClustersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListClustersResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListClustersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_clusters_param):
            request.list_clusters_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_clusters_param), 'listClustersParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_clusters_param_shrink):
            body['listClustersParam'] = request.list_clusters_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListClusters',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListClustersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_clusters(
        self,
        request: taihao_20210331_models.ListClustersRequest,
    ) -> taihao_20210331_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    async def list_clusters_async(
        self,
        request: taihao_20210331_models.ListClustersRequest,
    ) -> taihao_20210331_models.ListClustersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_clusters_with_options_async(request, runtime)

    def list_component_instances_with_options(
        self,
        tmp_req: taihao_20210331_models.ListComponentInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListComponentInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListComponentInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_component_instances_param):
            request.list_component_instances_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_component_instances_param), 'listComponentInstancesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_component_instances_param_shrink):
            body['listComponentInstancesParam'] = request.list_component_instances_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponentInstances',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListComponentInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_component_instances_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListComponentInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListComponentInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListComponentInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_component_instances_param):
            request.list_component_instances_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_component_instances_param), 'listComponentInstancesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_component_instances_param_shrink):
            body['listComponentInstancesParam'] = request.list_component_instances_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponentInstances',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListComponentInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_component_instances(
        self,
        request: taihao_20210331_models.ListComponentInstancesRequest,
    ) -> taihao_20210331_models.ListComponentInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_component_instances_with_options(request, runtime)

    async def list_component_instances_async(
        self,
        request: taihao_20210331_models.ListComponentInstancesRequest,
    ) -> taihao_20210331_models.ListComponentInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_component_instances_with_options_async(request, runtime)

    def list_components_with_options(
        self,
        tmp_req: taihao_20210331_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListComponentsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListComponentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_components_param):
            request.list_components_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_components_param), 'listComponentsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_components_param_shrink):
            body['listComponentsParam'] = request.list_components_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListComponentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListComponentsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListComponentsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_components_param):
            request.list_components_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_components_param), 'listComponentsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_components_param_shrink):
            body['listComponentsParam'] = request.list_components_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListComponents',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: taihao_20210331_models.ListComponentsRequest,
    ) -> taihao_20210331_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_components_with_options(request, runtime)

    async def list_components_async(
        self,
        request: taihao_20210331_models.ListComponentsRequest,
    ) -> taihao_20210331_models.ListComponentsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_components_with_options_async(request, runtime)

    def list_config_files_with_options(
        self,
        tmp_req: taihao_20210331_models.ListConfigFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListConfigFilesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListConfigFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_config_files_param):
            request.list_config_files_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_config_files_param), 'listConfigFilesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_config_files_param_shrink):
            body['listConfigFilesParam'] = request.list_config_files_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigFiles',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListConfigFilesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_files_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListConfigFilesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListConfigFilesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListConfigFilesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_config_files_param):
            request.list_config_files_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_config_files_param), 'listConfigFilesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_config_files_param_shrink):
            body['listConfigFilesParam'] = request.list_config_files_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigFiles',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListConfigFilesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_files(
        self,
        request: taihao_20210331_models.ListConfigFilesRequest,
    ) -> taihao_20210331_models.ListConfigFilesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_config_files_with_options(request, runtime)

    async def list_config_files_async(
        self,
        request: taihao_20210331_models.ListConfigFilesRequest,
    ) -> taihao_20210331_models.ListConfigFilesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_files_with_options_async(request, runtime)

    def list_config_history_with_options(
        self,
        tmp_req: taihao_20210331_models.ListConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListConfigHistoryResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListConfigHistoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_config_history_param):
            request.list_config_history_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_config_history_param), 'listConfigHistoryParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_config_history_param_shrink):
            body['listConfigHistoryParam'] = request.list_config_history_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigHistory',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListConfigHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_history_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListConfigHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListConfigHistoryResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListConfigHistoryShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_config_history_param):
            request.list_config_history_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_config_history_param), 'listConfigHistoryParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_config_history_param_shrink):
            body['listConfigHistoryParam'] = request.list_config_history_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigHistory',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListConfigHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_history(
        self,
        request: taihao_20210331_models.ListConfigHistoryRequest,
    ) -> taihao_20210331_models.ListConfigHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_config_history_with_options(request, runtime)

    async def list_config_history_async(
        self,
        request: taihao_20210331_models.ListConfigHistoryRequest,
    ) -> taihao_20210331_models.ListConfigHistoryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_history_with_options_async(request, runtime)

    def list_config_versions_with_options(
        self,
        tmp_req: taihao_20210331_models.ListConfigVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListConfigVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListConfigVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_config_versions_param):
            request.list_config_versions_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_config_versions_param), 'listConfigVersionsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_config_versions_param_shrink):
            body['listConfigVersionsParam'] = request.list_config_versions_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigVersions',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListConfigVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_config_versions_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListConfigVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListConfigVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListConfigVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_config_versions_param):
            request.list_config_versions_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_config_versions_param), 'listConfigVersionsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_config_versions_param_shrink):
            body['listConfigVersionsParam'] = request.list_config_versions_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigVersions',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListConfigVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_config_versions(
        self,
        request: taihao_20210331_models.ListConfigVersionsRequest,
    ) -> taihao_20210331_models.ListConfigVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_config_versions_with_options(request, runtime)

    async def list_config_versions_async(
        self,
        request: taihao_20210331_models.ListConfigVersionsRequest,
    ) -> taihao_20210331_models.ListConfigVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_config_versions_with_options_async(request, runtime)

    def list_configs_with_options(
        self,
        tmp_req: taihao_20210331_models.ListConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListConfigsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListConfigsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_configs_param):
            request.list_configs_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_configs_param), 'listConfigsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_configs_param_shrink):
            body['listConfigsParam'] = request.list_configs_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigs',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_configs_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListConfigsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListConfigsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListConfigsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_configs_param):
            request.list_configs_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_configs_param), 'listConfigsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_configs_param_shrink):
            body['listConfigsParam'] = request.list_configs_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigs',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_configs(
        self,
        request: taihao_20210331_models.ListConfigsRequest,
    ) -> taihao_20210331_models.ListConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_configs_with_options(request, runtime)

    async def list_configs_async(
        self,
        request: taihao_20210331_models.ListConfigsRequest,
    ) -> taihao_20210331_models.ListConfigsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_configs_with_options_async(request, runtime)

    def list_kube_customer_resource_with_options(
        self,
        tmp_req: taihao_20210331_models.ListKubeCustomerResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListKubeCustomerResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListKubeCustomerResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_kube_customer_resources_param):
            request.list_kube_customer_resources_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_kube_customer_resources_param), 'listKubeCustomerResourcesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_kube_customer_resources_param_shrink):
            body['listKubeCustomerResourcesParam'] = request.list_kube_customer_resources_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListKubeCustomerResource',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListKubeCustomerResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kube_customer_resource_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListKubeCustomerResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListKubeCustomerResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListKubeCustomerResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_kube_customer_resources_param):
            request.list_kube_customer_resources_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_kube_customer_resources_param), 'listKubeCustomerResourcesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_kube_customer_resources_param_shrink):
            body['listKubeCustomerResourcesParam'] = request.list_kube_customer_resources_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListKubeCustomerResource',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListKubeCustomerResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kube_customer_resource(
        self,
        request: taihao_20210331_models.ListKubeCustomerResourceRequest,
    ) -> taihao_20210331_models.ListKubeCustomerResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_kube_customer_resource_with_options(request, runtime)

    async def list_kube_customer_resource_async(
        self,
        request: taihao_20210331_models.ListKubeCustomerResourceRequest,
    ) -> taihao_20210331_models.ListKubeCustomerResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_kube_customer_resource_with_options_async(request, runtime)

    def list_kube_native_resources_with_options(
        self,
        tmp_req: taihao_20210331_models.ListKubeNativeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListKubeNativeResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListKubeNativeResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_kube_native_resources_param):
            request.list_kube_native_resources_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_kube_native_resources_param), 'listKubeNativeResourcesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_kube_native_resources_param_shrink):
            body['listKubeNativeResourcesParam'] = request.list_kube_native_resources_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListKubeNativeResources',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListKubeNativeResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kube_native_resources_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListKubeNativeResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListKubeNativeResourcesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListKubeNativeResourcesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_kube_native_resources_param):
            request.list_kube_native_resources_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_kube_native_resources_param), 'listKubeNativeResourcesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_kube_native_resources_param_shrink):
            body['listKubeNativeResourcesParam'] = request.list_kube_native_resources_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListKubeNativeResources',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListKubeNativeResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kube_native_resources(
        self,
        request: taihao_20210331_models.ListKubeNativeResourcesRequest,
    ) -> taihao_20210331_models.ListKubeNativeResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_kube_native_resources_with_options(request, runtime)

    async def list_kube_native_resources_async(
        self,
        request: taihao_20210331_models.ListKubeNativeResourcesRequest,
    ) -> taihao_20210331_models.ListKubeNativeResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_kube_native_resources_with_options_async(request, runtime)

    def list_main_versions_with_options(
        self,
        tmp_req: taihao_20210331_models.ListMainVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListMainVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListMainVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_main_versions_param):
            request.list_main_versions_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_main_versions_param), 'listMainVersionsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_main_versions_param_shrink):
            body['listMainVersionsParam'] = request.list_main_versions_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMainVersions',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListMainVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_main_versions_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListMainVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListMainVersionsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListMainVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_main_versions_param):
            request.list_main_versions_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_main_versions_param), 'listMainVersionsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_main_versions_param_shrink):
            body['listMainVersionsParam'] = request.list_main_versions_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMainVersions',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListMainVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_main_versions(
        self,
        request: taihao_20210331_models.ListMainVersionsRequest,
    ) -> taihao_20210331_models.ListMainVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_main_versions_with_options(request, runtime)

    async def list_main_versions_async(
        self,
        request: taihao_20210331_models.ListMainVersionsRequest,
    ) -> taihao_20210331_models.ListMainVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_main_versions_with_options_async(request, runtime)

    def list_node_disks_with_options(
        self,
        tmp_req: taihao_20210331_models.ListNodeDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListNodeDisksResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListNodeDisksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_node_disk_param):
            request.list_node_disk_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_node_disk_param), 'listNodeDiskParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_node_disk_param_shrink):
            body['listNodeDiskParam'] = request.list_node_disk_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeDisks',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListNodeDisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_disks_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListNodeDisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListNodeDisksResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListNodeDisksShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_node_disk_param):
            request.list_node_disk_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_node_disk_param), 'listNodeDiskParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_node_disk_param_shrink):
            body['listNodeDiskParam'] = request.list_node_disk_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeDisks',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListNodeDisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_disks(
        self,
        request: taihao_20210331_models.ListNodeDisksRequest,
    ) -> taihao_20210331_models.ListNodeDisksResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_node_disks_with_options(request, runtime)

    async def list_node_disks_async(
        self,
        request: taihao_20210331_models.ListNodeDisksRequest,
    ) -> taihao_20210331_models.ListNodeDisksResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_node_disks_with_options_async(request, runtime)

    def list_node_group_meta_with_options(
        self,
        tmp_req: taihao_20210331_models.ListNodeGroupMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListNodeGroupMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListNodeGroupMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_node_group_meta_param):
            request.list_node_group_meta_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_node_group_meta_param), 'listNodeGroupMetaParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_node_group_meta_param_shrink):
            body['listNodeGroupMetaParam'] = request.list_node_group_meta_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeGroupMeta',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListNodeGroupMetaResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_node_group_meta_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListNodeGroupMetaRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListNodeGroupMetaResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListNodeGroupMetaShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_node_group_meta_param):
            request.list_node_group_meta_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_node_group_meta_param), 'listNodeGroupMetaParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_node_group_meta_param_shrink):
            body['listNodeGroupMetaParam'] = request.list_node_group_meta_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodeGroupMeta',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListNodeGroupMetaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_node_group_meta(
        self,
        request: taihao_20210331_models.ListNodeGroupMetaRequest,
    ) -> taihao_20210331_models.ListNodeGroupMetaResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_node_group_meta_with_options(request, runtime)

    async def list_node_group_meta_async(
        self,
        request: taihao_20210331_models.ListNodeGroupMetaRequest,
    ) -> taihao_20210331_models.ListNodeGroupMetaResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_node_group_meta_with_options_async(request, runtime)

    def list_nodes_with_options(
        self,
        tmp_req: taihao_20210331_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_node_param):
            request.list_node_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_node_param), 'listNodeParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_node_param_shrink):
            body['listNodeParam'] = request.list_node_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_nodes_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_node_param):
            request.list_node_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_node_param), 'listNodeParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_node_param_shrink):
            body['listNodeParam'] = request.list_node_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_nodes(
        self,
        request: taihao_20210331_models.ListNodesRequest,
    ) -> taihao_20210331_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    async def list_nodes_async(
        self,
        request: taihao_20210331_models.ListNodesRequest,
    ) -> taihao_20210331_models.ListNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_nodes_with_options_async(request, runtime)

    def list_on_kube_dedicated_nodes_with_options(
        self,
        tmp_req: taihao_20210331_models.ListOnKubeDedicatedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListOnKubeDedicatedNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListOnKubeDedicatedNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_on_kube_dedicated_nodes_param):
            request.list_on_kube_dedicated_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_on_kube_dedicated_nodes_param), 'listOnKubeDedicatedNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_on_kube_dedicated_nodes_param_shrink):
            body['listOnKubeDedicatedNodesParam'] = request.list_on_kube_dedicated_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListOnKubeDedicatedNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListOnKubeDedicatedNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_on_kube_dedicated_nodes_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListOnKubeDedicatedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListOnKubeDedicatedNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListOnKubeDedicatedNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_on_kube_dedicated_nodes_param):
            request.list_on_kube_dedicated_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_on_kube_dedicated_nodes_param), 'listOnKubeDedicatedNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_on_kube_dedicated_nodes_param_shrink):
            body['listOnKubeDedicatedNodesParam'] = request.list_on_kube_dedicated_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListOnKubeDedicatedNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListOnKubeDedicatedNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_on_kube_dedicated_nodes(
        self,
        request: taihao_20210331_models.ListOnKubeDedicatedNodesRequest,
    ) -> taihao_20210331_models.ListOnKubeDedicatedNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_on_kube_dedicated_nodes_with_options(request, runtime)

    async def list_on_kube_dedicated_nodes_async(
        self,
        request: taihao_20210331_models.ListOnKubeDedicatedNodesRequest,
    ) -> taihao_20210331_models.ListOnKubeDedicatedNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_on_kube_dedicated_nodes_with_options_async(request, runtime)

    def list_reports_with_options(
        self,
        tmp_req: taihao_20210331_models.ListReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListReportsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListReportsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_reports_param):
            request.list_reports_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_reports_param), 'listReportsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_reports_param_shrink):
            body['listReportsParam'] = request.list_reports_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListReports',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListReportsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_reports_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListReportsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListReportsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListReportsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_reports_param):
            request.list_reports_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_reports_param), 'listReportsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_reports_param_shrink):
            body['listReportsParam'] = request.list_reports_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListReports',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListReportsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_reports(
        self,
        request: taihao_20210331_models.ListReportsRequest,
    ) -> taihao_20210331_models.ListReportsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_reports_with_options(request, runtime)

    async def list_reports_async(
        self,
        request: taihao_20210331_models.ListReportsRequest,
    ) -> taihao_20210331_models.ListReportsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_reports_with_options_async(request, runtime)

    def list_resource_health_with_options(
        self,
        tmp_req: taihao_20210331_models.ListResourceHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListResourceHealthResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListResourceHealthShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_resource_health_param):
            request.list_resource_health_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_resource_health_param), 'listResourceHealthParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_resource_health_param_shrink):
            body['listResourceHealthParam'] = request.list_resource_health_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListResourceHealth',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListResourceHealthResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_health_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListResourceHealthRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListResourceHealthResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListResourceHealthShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_resource_health_param):
            request.list_resource_health_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_resource_health_param), 'listResourceHealthParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_resource_health_param_shrink):
            body['listResourceHealthParam'] = request.list_resource_health_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListResourceHealth',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListResourceHealthResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_health(
        self,
        request: taihao_20210331_models.ListResourceHealthRequest,
    ) -> taihao_20210331_models.ListResourceHealthResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_health_with_options(request, runtime)

    async def list_resource_health_async(
        self,
        request: taihao_20210331_models.ListResourceHealthRequest,
    ) -> taihao_20210331_models.ListResourceHealthResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_health_with_options_async(request, runtime)

    def list_resource_health_inspections_with_options(
        self,
        tmp_req: taihao_20210331_models.ListResourceHealthInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListResourceHealthInspectionsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListResourceHealthInspectionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_resource_health_inspections_param):
            request.list_resource_health_inspections_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_resource_health_inspections_param), 'listResourceHealthInspectionsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_resource_health_inspections_param_shrink):
            body['listResourceHealthInspectionsParam'] = request.list_resource_health_inspections_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListResourceHealthInspections',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListResourceHealthInspectionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_health_inspections_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListResourceHealthInspectionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListResourceHealthInspectionsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListResourceHealthInspectionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_resource_health_inspections_param):
            request.list_resource_health_inspections_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_resource_health_inspections_param), 'listResourceHealthInspectionsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_resource_health_inspections_param_shrink):
            body['listResourceHealthInspectionsParam'] = request.list_resource_health_inspections_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListResourceHealthInspections',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListResourceHealthInspectionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_health_inspections(
        self,
        request: taihao_20210331_models.ListResourceHealthInspectionsRequest,
    ) -> taihao_20210331_models.ListResourceHealthInspectionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_health_inspections_with_options(request, runtime)

    async def list_resource_health_inspections_async(
        self,
        request: taihao_20210331_models.ListResourceHealthInspectionsRequest,
    ) -> taihao_20210331_models.ListResourceHealthInspectionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_health_inspections_with_options_async(request, runtime)

    def list_stack_applications_with_options(
        self,
        tmp_req: taihao_20210331_models.ListStackApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListStackApplicationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListStackApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_stack_application_param):
            request.list_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_stack_application_param), 'listStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_stack_application_param_shrink):
            body['listStackApplicationParam'] = request.list_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListStackApplications',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListStackApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_applications_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListStackApplicationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListStackApplicationsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListStackApplicationsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_stack_application_param):
            request.list_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_stack_application_param), 'listStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_stack_application_param_shrink):
            body['listStackApplicationParam'] = request.list_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListStackApplications',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListStackApplicationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_applications(
        self,
        request: taihao_20210331_models.ListStackApplicationsRequest,
    ) -> taihao_20210331_models.ListStackApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_applications_with_options(request, runtime)

    async def list_stack_applications_async(
        self,
        request: taihao_20210331_models.ListStackApplicationsRequest,
    ) -> taihao_20210331_models.ListStackApplicationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_applications_with_options_async(request, runtime)

    def list_workflow_activity_instances_with_options(
        self,
        tmp_req: taihao_20210331_models.ListWorkflowActivityInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListWorkflowActivityInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListWorkflowActivityInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_workflow_activity_instances_param):
            request.list_workflow_activity_instances_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_workflow_activity_instances_param), 'listWorkflowActivityInstancesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_workflow_activity_instances_param_shrink):
            body['listWorkflowActivityInstancesParam'] = request.list_workflow_activity_instances_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWorkflowActivityInstances',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListWorkflowActivityInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workflow_activity_instances_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ListWorkflowActivityInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ListWorkflowActivityInstancesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ListWorkflowActivityInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.list_workflow_activity_instances_param):
            request.list_workflow_activity_instances_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.list_workflow_activity_instances_param), 'listWorkflowActivityInstancesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.list_workflow_activity_instances_param_shrink):
            body['listWorkflowActivityInstancesParam'] = request.list_workflow_activity_instances_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListWorkflowActivityInstances',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ListWorkflowActivityInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workflow_activity_instances(
        self,
        request: taihao_20210331_models.ListWorkflowActivityInstancesRequest,
    ) -> taihao_20210331_models.ListWorkflowActivityInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_workflow_activity_instances_with_options(request, runtime)

    async def list_workflow_activity_instances_async(
        self,
        request: taihao_20210331_models.ListWorkflowActivityInstancesRequest,
    ) -> taihao_20210331_models.ListWorkflowActivityInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_workflow_activity_instances_with_options_async(request, runtime)

    def modify_prepay_instance_spec_with_options(
        self,
        tmp_req: taihao_20210331_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ModifyPrepayInstanceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.modify_prepay_instance_spec_param):
            request.modify_prepay_instance_spec_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.modify_prepay_instance_spec_param), 'modifyPrepayInstanceSpecParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.modify_prepay_instance_spec_param_shrink):
            body['modifyPrepayInstanceSpecParam'] = request.modify_prepay_instance_spec_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayInstanceSpec',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ModifyPrepayInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_prepay_instance_spec_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ModifyPrepayInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ModifyPrepayInstanceSpecResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ModifyPrepayInstanceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.modify_prepay_instance_spec_param):
            request.modify_prepay_instance_spec_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.modify_prepay_instance_spec_param), 'modifyPrepayInstanceSpecParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.modify_prepay_instance_spec_param_shrink):
            body['modifyPrepayInstanceSpecParam'] = request.modify_prepay_instance_spec_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyPrepayInstanceSpec',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ModifyPrepayInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_prepay_instance_spec(
        self,
        request: taihao_20210331_models.ModifyPrepayInstanceSpecRequest,
    ) -> taihao_20210331_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return self.modify_prepay_instance_spec_with_options(request, runtime)

    async def modify_prepay_instance_spec_async(
        self,
        request: taihao_20210331_models.ModifyPrepayInstanceSpecRequest,
    ) -> taihao_20210331_models.ModifyPrepayInstanceSpecResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_prepay_instance_spec_with_options_async(request, runtime)

    def plan_portal_get_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.PlanPortalGetResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='PlanPortalGet',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.PlanPortalGetResponse(),
            self.call_api(params, req, runtime)
        )

    async def plan_portal_get_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.PlanPortalGetResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='PlanPortalGet',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.PlanPortalGetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def plan_portal_get(self) -> taihao_20210331_models.PlanPortalGetResponse:
        runtime = util_models.RuntimeOptions()
        return self.plan_portal_get_with_options(runtime)

    async def plan_portal_get_async(self) -> taihao_20210331_models.PlanPortalGetResponse:
        runtime = util_models.RuntimeOptions()
        return await self.plan_portal_get_with_options_async(runtime)

    def query_grafana_data_with_options(
        self,
        tmp_req: taihao_20210331_models.QueryGrafanaDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.QueryGrafanaDataResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.QueryGrafanaDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_grafana_data_param):
            request.get_grafana_data_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_grafana_data_param), 'getGrafanaDataParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_grafana_data_param_shrink):
            body['getGrafanaDataParam'] = request.get_grafana_data_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryGrafanaData',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.QueryGrafanaDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_grafana_data_with_options_async(
        self,
        tmp_req: taihao_20210331_models.QueryGrafanaDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.QueryGrafanaDataResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.QueryGrafanaDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.get_grafana_data_param):
            request.get_grafana_data_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.get_grafana_data_param), 'getGrafanaDataParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.get_grafana_data_param_shrink):
            body['getGrafanaDataParam'] = request.get_grafana_data_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryGrafanaData',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.QueryGrafanaDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_grafana_data(
        self,
        request: taihao_20210331_models.QueryGrafanaDataRequest,
    ) -> taihao_20210331_models.QueryGrafanaDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.query_grafana_data_with_options(request, runtime)

    async def query_grafana_data_async(
        self,
        request: taihao_20210331_models.QueryGrafanaDataRequest,
    ) -> taihao_20210331_models.QueryGrafanaDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.query_grafana_data_with_options_async(request, runtime)

    def refresh_stack_application_with_options(
        self,
        tmp_req: taihao_20210331_models.RefreshStackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RefreshStackApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RefreshStackApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.refresh_stack_application_param):
            request.refresh_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.refresh_stack_application_param), 'refreshStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.refresh_stack_application_param_shrink):
            body['refreshStackApplicationParam'] = request.refresh_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshStackApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RefreshStackApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_stack_application_with_options_async(
        self,
        tmp_req: taihao_20210331_models.RefreshStackApplicationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RefreshStackApplicationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RefreshStackApplicationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.refresh_stack_application_param):
            request.refresh_stack_application_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.refresh_stack_application_param), 'refreshStackApplicationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.refresh_stack_application_param_shrink):
            body['refreshStackApplicationParam'] = request.refresh_stack_application_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshStackApplication',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RefreshStackApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_stack_application(
        self,
        request: taihao_20210331_models.RefreshStackApplicationRequest,
    ) -> taihao_20210331_models.RefreshStackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return self.refresh_stack_application_with_options(request, runtime)

    async def refresh_stack_application_async(
        self,
        request: taihao_20210331_models.RefreshStackApplicationRequest,
    ) -> taihao_20210331_models.RefreshStackApplicationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.refresh_stack_application_with_options_async(request, runtime)

    def register_cluster_ack_resource_with_options(
        self,
        tmp_req: taihao_20210331_models.RegisterClusterAckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RegisterClusterAckResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RegisterClusterAckResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.register_cluster_ack_resource_param):
            request.register_cluster_ack_resource_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.register_cluster_ack_resource_param), 'registerClusterAckResourceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.register_cluster_ack_resource_param_shrink):
            body['registerClusterAckResourceParam'] = request.register_cluster_ack_resource_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterClusterAckResource',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RegisterClusterAckResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_cluster_ack_resource_with_options_async(
        self,
        tmp_req: taihao_20210331_models.RegisterClusterAckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RegisterClusterAckResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RegisterClusterAckResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.register_cluster_ack_resource_param):
            request.register_cluster_ack_resource_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.register_cluster_ack_resource_param), 'registerClusterAckResourceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.register_cluster_ack_resource_param_shrink):
            body['registerClusterAckResourceParam'] = request.register_cluster_ack_resource_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterClusterAckResource',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RegisterClusterAckResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_cluster_ack_resource(
        self,
        request: taihao_20210331_models.RegisterClusterAckResourceRequest,
    ) -> taihao_20210331_models.RegisterClusterAckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_cluster_ack_resource_with_options(request, runtime)

    async def register_cluster_ack_resource_async(
        self,
        request: taihao_20210331_models.RegisterClusterAckResourceRequest,
    ) -> taihao_20210331_models.RegisterClusterAckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_cluster_ack_resource_with_options_async(request, runtime)

    def register_product_role_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RegisterProductRoleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RegisterProductRole',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RegisterProductRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_product_role_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RegisterProductRoleResponse:
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='RegisterProductRole',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RegisterProductRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_product_role(self) -> taihao_20210331_models.RegisterProductRoleResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_product_role_with_options(runtime)

    async def register_product_role_async(self) -> taihao_20210331_models.RegisterProductRoleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_product_role_with_options_async(runtime)

    def release_binding_ack_cluster_with_options(
        self,
        tmp_req: taihao_20210331_models.ReleaseBindingAckClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ReleaseBindingAckClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ReleaseBindingAckClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.release_binding_ack_cluster_param):
            request.release_binding_ack_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.release_binding_ack_cluster_param), 'releaseBindingAckClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.release_binding_ack_cluster_param_shrink):
            body['releaseBindingAckClusterParam'] = request.release_binding_ack_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseBindingAckCluster',
            version='2021-03-31',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ReleaseBindingAckClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_binding_ack_cluster_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ReleaseBindingAckClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ReleaseBindingAckClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ReleaseBindingAckClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.release_binding_ack_cluster_param):
            request.release_binding_ack_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.release_binding_ack_cluster_param), 'releaseBindingAckClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.release_binding_ack_cluster_param_shrink):
            body['releaseBindingAckClusterParam'] = request.release_binding_ack_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseBindingAckCluster',
            version='2021-03-31',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ReleaseBindingAckClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_binding_ack_cluster(
        self,
        request: taihao_20210331_models.ReleaseBindingAckClusterRequest,
    ) -> taihao_20210331_models.ReleaseBindingAckClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_binding_ack_cluster_with_options(request, runtime)

    async def release_binding_ack_cluster_async(
        self,
        request: taihao_20210331_models.ReleaseBindingAckClusterRequest,
    ) -> taihao_20210331_models.ReleaseBindingAckClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_binding_ack_cluster_with_options_async(request, runtime)

    def release_cluster_with_options(
        self,
        tmp_req: taihao_20210331_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ReleaseClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ReleaseClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.release_cluster_param):
            request.release_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.release_cluster_param), 'releaseClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.release_cluster_param_shrink):
            body['releaseClusterParam'] = request.release_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ReleaseClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_cluster_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ReleaseClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ReleaseClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ReleaseClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.release_cluster_param):
            request.release_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.release_cluster_param), 'releaseClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.release_cluster_param_shrink):
            body['releaseClusterParam'] = request.release_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ReleaseClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_cluster(
        self,
        request: taihao_20210331_models.ReleaseClusterRequest,
    ) -> taihao_20210331_models.ReleaseClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_cluster_with_options(request, runtime)

    async def release_cluster_async(
        self,
        request: taihao_20210331_models.ReleaseClusterRequest,
    ) -> taihao_20210331_models.ReleaseClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_cluster_with_options_async(request, runtime)

    def release_on_ecs_cluster_with_options(
        self,
        tmp_req: taihao_20210331_models.ReleaseOnEcsClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ReleaseOnEcsClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ReleaseOnEcsClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.release_on_ecs_cluster_param):
            request.release_on_ecs_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.release_on_ecs_cluster_param), 'ReleaseOnEcsClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.release_on_ecs_cluster_param_shrink):
            body['ReleaseOnEcsClusterParam'] = request.release_on_ecs_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseOnEcsCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ReleaseOnEcsClusterResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_on_ecs_cluster_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ReleaseOnEcsClusterRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ReleaseOnEcsClusterResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ReleaseOnEcsClusterShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.release_on_ecs_cluster_param):
            request.release_on_ecs_cluster_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.release_on_ecs_cluster_param), 'ReleaseOnEcsClusterParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.release_on_ecs_cluster_param_shrink):
            body['ReleaseOnEcsClusterParam'] = request.release_on_ecs_cluster_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReleaseOnEcsCluster',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ReleaseOnEcsClusterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_on_ecs_cluster(
        self,
        request: taihao_20210331_models.ReleaseOnEcsClusterRequest,
    ) -> taihao_20210331_models.ReleaseOnEcsClusterResponse:
        runtime = util_models.RuntimeOptions()
        return self.release_on_ecs_cluster_with_options(request, runtime)

    async def release_on_ecs_cluster_async(
        self,
        request: taihao_20210331_models.ReleaseOnEcsClusterRequest,
    ) -> taihao_20210331_models.ReleaseOnEcsClusterResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_on_ecs_cluster_with_options_async(request, runtime)

    def remove_suspend_point_on_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remove_suspend_point_on_workflow_instance_param):
            request.remove_suspend_point_on_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.remove_suspend_point_on_workflow_instance_param), 'removeSuspendPointOnWorkflowInstanceParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.remove_suspend_point_on_workflow_instance_param_shrink):
            query['removeSuspendPointOnWorkflowInstanceParam'] = request.remove_suspend_point_on_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSuspendPointOnWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_suspend_point_on_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.remove_suspend_point_on_workflow_instance_param):
            request.remove_suspend_point_on_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.remove_suspend_point_on_workflow_instance_param), 'removeSuspendPointOnWorkflowInstanceParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.remove_suspend_point_on_workflow_instance_param_shrink):
            query['removeSuspendPointOnWorkflowInstanceParam'] = request.remove_suspend_point_on_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSuspendPointOnWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_suspend_point_on_workflow_instance(
        self,
        request: taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceRequest,
    ) -> taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.remove_suspend_point_on_workflow_instance_with_options(request, runtime)

    async def remove_suspend_point_on_workflow_instance_async(
        self,
        request: taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceRequest,
    ) -> taihao_20210331_models.RemoveSuspendPointOnWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.remove_suspend_point_on_workflow_instance_with_options_async(request, runtime)

    def restart_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.RestartWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RestartWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RestartWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.restart_workflow_instance_param):
            request.restart_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.restart_workflow_instance_param), 'restartWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.restart_workflow_instance_param_shrink):
            body['restartWorkflowInstanceParam'] = request.restart_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RestartWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.RestartWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RestartWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RestartWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.restart_workflow_instance_param):
            request.restart_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.restart_workflow_instance_param), 'restartWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.restart_workflow_instance_param_shrink):
            body['restartWorkflowInstanceParam'] = request.restart_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RestartWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RestartWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_workflow_instance(
        self,
        request: taihao_20210331_models.RestartWorkflowInstanceRequest,
    ) -> taihao_20210331_models.RestartWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.restart_workflow_instance_with_options(request, runtime)

    async def restart_workflow_instance_async(
        self,
        request: taihao_20210331_models.RestartWorkflowInstanceRequest,
    ) -> taihao_20210331_models.RestartWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.restart_workflow_instance_with_options_async(request, runtime)

    def resume_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.ResumeWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ResumeWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ResumeWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resume_workflow_instance_param):
            request.resume_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.resume_workflow_instance_param), 'resumeWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.resume_workflow_instance_param_shrink):
            body['resumeWorkflowInstanceParam'] = request.resume_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ResumeWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.ResumeWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.ResumeWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.ResumeWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.resume_workflow_instance_param):
            request.resume_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.resume_workflow_instance_param), 'resumeWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.resume_workflow_instance_param_shrink):
            body['resumeWorkflowInstanceParam'] = request.resume_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResumeWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.ResumeWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_workflow_instance(
        self,
        request: taihao_20210331_models.ResumeWorkflowInstanceRequest,
    ) -> taihao_20210331_models.ResumeWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_workflow_instance_with_options(request, runtime)

    async def resume_workflow_instance_async(
        self,
        request: taihao_20210331_models.ResumeWorkflowInstanceRequest,
    ) -> taihao_20210331_models.ResumeWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_workflow_instance_with_options_async(request, runtime)

    def retry_cluster_operation_with_options(
        self,
        tmp_req: taihao_20210331_models.RetryClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RetryClusterOperationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RetryClusterOperationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_cluster_operation_param):
            request.retry_cluster_operation_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.retry_cluster_operation_param), 'retryClusterOperationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.retry_cluster_operation_param_shrink):
            body['retryClusterOperationParam'] = request.retry_cluster_operation_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryClusterOperation',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RetryClusterOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_cluster_operation_with_options_async(
        self,
        tmp_req: taihao_20210331_models.RetryClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RetryClusterOperationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RetryClusterOperationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_cluster_operation_param):
            request.retry_cluster_operation_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.retry_cluster_operation_param), 'retryClusterOperationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.retry_cluster_operation_param_shrink):
            body['retryClusterOperationParam'] = request.retry_cluster_operation_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryClusterOperation',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RetryClusterOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_cluster_operation(
        self,
        request: taihao_20210331_models.RetryClusterOperationRequest,
    ) -> taihao_20210331_models.RetryClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_cluster_operation_with_options(request, runtime)

    async def retry_cluster_operation_async(
        self,
        request: taihao_20210331_models.RetryClusterOperationRequest,
    ) -> taihao_20210331_models.RetryClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_cluster_operation_with_options_async(request, runtime)

    def retry_cluster_operation_task_with_options(
        self,
        tmp_req: taihao_20210331_models.RetryClusterOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RetryClusterOperationTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RetryClusterOperationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_cluster_operation_task_param):
            request.retry_cluster_operation_task_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.retry_cluster_operation_task_param), 'retryClusterOperationTaskParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.retry_cluster_operation_task_param_shrink):
            body['retryClusterOperationTaskParam'] = request.retry_cluster_operation_task_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryClusterOperationTask',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RetryClusterOperationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_cluster_operation_task_with_options_async(
        self,
        tmp_req: taihao_20210331_models.RetryClusterOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RetryClusterOperationTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RetryClusterOperationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_cluster_operation_task_param):
            request.retry_cluster_operation_task_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.retry_cluster_operation_task_param), 'retryClusterOperationTaskParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.retry_cluster_operation_task_param_shrink):
            body['retryClusterOperationTaskParam'] = request.retry_cluster_operation_task_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryClusterOperationTask',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RetryClusterOperationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_cluster_operation_task(
        self,
        request: taihao_20210331_models.RetryClusterOperationTaskRequest,
    ) -> taihao_20210331_models.RetryClusterOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_cluster_operation_task_with_options(request, runtime)

    async def retry_cluster_operation_task_async(
        self,
        request: taihao_20210331_models.RetryClusterOperationTaskRequest,
    ) -> taihao_20210331_models.RetryClusterOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_cluster_operation_task_with_options_async(request, runtime)

    def retry_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.RetryWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RetryWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RetryWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_workflow_instance_param):
            request.retry_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.retry_workflow_instance_param), 'retryWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.retry_workflow_instance_param_shrink):
            body['retryWorkflowInstanceParam'] = request.retry_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RetryWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def retry_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.RetryWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RetryWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RetryWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.retry_workflow_instance_param):
            request.retry_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.retry_workflow_instance_param), 'retryWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.retry_workflow_instance_param_shrink):
            body['retryWorkflowInstanceParam'] = request.retry_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetryWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RetryWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def retry_workflow_instance(
        self,
        request: taihao_20210331_models.RetryWorkflowInstanceRequest,
    ) -> taihao_20210331_models.RetryWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.retry_workflow_instance_with_options(request, runtime)

    async def retry_workflow_instance_async(
        self,
        request: taihao_20210331_models.RetryWorkflowInstanceRequest,
    ) -> taihao_20210331_models.RetryWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.retry_workflow_instance_with_options_async(request, runtime)

    def rollback_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.RollbackWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RollbackWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RollbackWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rollback_workflow_instance_param):
            request.rollback_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.rollback_workflow_instance_param), 'rollbackWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.rollback_workflow_instance_param_shrink):
            body['rollbackWorkflowInstanceParam'] = request.rollback_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RollbackWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RollbackWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.RollbackWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RollbackWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RollbackWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rollback_workflow_instance_param):
            request.rollback_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.rollback_workflow_instance_param), 'rollbackWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.rollback_workflow_instance_param_shrink):
            body['rollbackWorkflowInstanceParam'] = request.rollback_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RollbackWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RollbackWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_workflow_instance(
        self,
        request: taihao_20210331_models.RollbackWorkflowInstanceRequest,
    ) -> taihao_20210331_models.RollbackWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.rollback_workflow_instance_with_options(request, runtime)

    async def rollback_workflow_instance_async(
        self,
        request: taihao_20210331_models.RollbackWorkflowInstanceRequest,
    ) -> taihao_20210331_models.RollbackWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rollback_workflow_instance_with_options_async(request, runtime)

    def run_action_with_options(
        self,
        tmp_req: taihao_20210331_models.RunActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RunActionResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RunActionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_action_param):
            request.run_action_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.run_action_param), 'runActionParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.run_action_param_shrink):
            body['runActionParam'] = request.run_action_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunAction',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RunActionResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_action_with_options_async(
        self,
        tmp_req: taihao_20210331_models.RunActionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.RunActionResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.RunActionShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.run_action_param):
            request.run_action_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.run_action_param), 'runActionParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.run_action_param_shrink):
            body['runActionParam'] = request.run_action_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunAction',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.RunActionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_action(
        self,
        request: taihao_20210331_models.RunActionRequest,
    ) -> taihao_20210331_models.RunActionResponse:
        runtime = util_models.RuntimeOptions()
        return self.run_action_with_options(request, runtime)

    async def run_action_async(
        self,
        request: taihao_20210331_models.RunActionRequest,
    ) -> taihao_20210331_models.RunActionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.run_action_with_options_async(request, runtime)

    def signal_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.SignalWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.SignalWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.SignalWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.signal_workflow_instance_param):
            request.signal_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.signal_workflow_instance_param), 'SignalWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.signal_workflow_instance_param_shrink):
            body['SignalWorkflowInstanceParam'] = request.signal_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SignalWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.SignalWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def signal_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.SignalWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.SignalWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.SignalWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.signal_workflow_instance_param):
            request.signal_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.signal_workflow_instance_param), 'SignalWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.signal_workflow_instance_param_shrink):
            body['SignalWorkflowInstanceParam'] = request.signal_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SignalWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.SignalWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def signal_workflow_instance(
        self,
        request: taihao_20210331_models.SignalWorkflowInstanceRequest,
    ) -> taihao_20210331_models.SignalWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.signal_workflow_instance_with_options(request, runtime)

    async def signal_workflow_instance_async(
        self,
        request: taihao_20210331_models.SignalWorkflowInstanceRequest,
    ) -> taihao_20210331_models.SignalWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.signal_workflow_instance_with_options_async(request, runtime)

    def skip_cluster_operation_task_with_options(
        self,
        tmp_req: taihao_20210331_models.SkipClusterOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.SkipClusterOperationTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.SkipClusterOperationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.skip_cluster_operation_task_param):
            request.skip_cluster_operation_task_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.skip_cluster_operation_task_param), 'skipClusterOperationTaskParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.skip_cluster_operation_task_param_shrink):
            body['skipClusterOperationTaskParam'] = request.skip_cluster_operation_task_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SkipClusterOperationTask',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.SkipClusterOperationTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_cluster_operation_task_with_options_async(
        self,
        tmp_req: taihao_20210331_models.SkipClusterOperationTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.SkipClusterOperationTaskResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.SkipClusterOperationTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.skip_cluster_operation_task_param):
            request.skip_cluster_operation_task_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.skip_cluster_operation_task_param), 'skipClusterOperationTaskParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.skip_cluster_operation_task_param_shrink):
            body['skipClusterOperationTaskParam'] = request.skip_cluster_operation_task_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SkipClusterOperationTask',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.SkipClusterOperationTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_cluster_operation_task(
        self,
        request: taihao_20210331_models.SkipClusterOperationTaskRequest,
    ) -> taihao_20210331_models.SkipClusterOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return self.skip_cluster_operation_task_with_options(request, runtime)

    async def skip_cluster_operation_task_async(
        self,
        request: taihao_20210331_models.SkipClusterOperationTaskRequest,
    ) -> taihao_20210331_models.SkipClusterOperationTaskResponse:
        runtime = util_models.RuntimeOptions()
        return await self.skip_cluster_operation_task_with_options_async(request, runtime)

    def skip_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.SkipWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.SkipWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.SkipWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.skip_workflow_instance_param):
            request.skip_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.skip_workflow_instance_param), 'skipWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.skip_workflow_instance_param_shrink):
            body['skipWorkflowInstanceParam'] = request.skip_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SkipWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.SkipWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def skip_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.SkipWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.SkipWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.SkipWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.skip_workflow_instance_param):
            request.skip_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.skip_workflow_instance_param), 'skipWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.skip_workflow_instance_param_shrink):
            body['skipWorkflowInstanceParam'] = request.skip_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SkipWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.SkipWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def skip_workflow_instance(
        self,
        request: taihao_20210331_models.SkipWorkflowInstanceRequest,
    ) -> taihao_20210331_models.SkipWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.skip_workflow_instance_with_options(request, runtime)

    async def skip_workflow_instance_async(
        self,
        request: taihao_20210331_models.SkipWorkflowInstanceRequest,
    ) -> taihao_20210331_models.SkipWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.skip_workflow_instance_with_options_async(request, runtime)

    def suspend_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.SuspendWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.SuspendWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.SuspendWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.suspend_workflow_instance_param):
            request.suspend_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.suspend_workflow_instance_param), 'suspendWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.suspend_workflow_instance_param_shrink):
            body['suspendWorkflowInstanceParam'] = request.suspend_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.SuspendWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def suspend_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.SuspendWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.SuspendWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.SuspendWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.suspend_workflow_instance_param):
            request.suspend_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.suspend_workflow_instance_param), 'suspendWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.suspend_workflow_instance_param_shrink):
            body['suspendWorkflowInstanceParam'] = request.suspend_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SuspendWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.SuspendWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def suspend_workflow_instance(
        self,
        request: taihao_20210331_models.SuspendWorkflowInstanceRequest,
    ) -> taihao_20210331_models.SuspendWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.suspend_workflow_instance_with_options(request, runtime)

    async def suspend_workflow_instance_async(
        self,
        request: taihao_20210331_models.SuspendWorkflowInstanceRequest,
    ) -> taihao_20210331_models.SuspendWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.suspend_workflow_instance_with_options_async(request, runtime)

    def terminate_cluster_operation_with_options(
        self,
        tmp_req: taihao_20210331_models.TerminateClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.TerminateClusterOperationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.TerminateClusterOperationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.terminate_cluster_operation_param):
            request.terminate_cluster_operation_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.terminate_cluster_operation_param), 'terminateClusterOperationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.terminate_cluster_operation_param_shrink):
            body['terminateClusterOperationParam'] = request.terminate_cluster_operation_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateClusterOperation',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.TerminateClusterOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_cluster_operation_with_options_async(
        self,
        tmp_req: taihao_20210331_models.TerminateClusterOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.TerminateClusterOperationResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.TerminateClusterOperationShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.terminate_cluster_operation_param):
            request.terminate_cluster_operation_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.terminate_cluster_operation_param), 'terminateClusterOperationParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.terminate_cluster_operation_param_shrink):
            body['terminateClusterOperationParam'] = request.terminate_cluster_operation_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateClusterOperation',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.TerminateClusterOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_cluster_operation(
        self,
        request: taihao_20210331_models.TerminateClusterOperationRequest,
    ) -> taihao_20210331_models.TerminateClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_cluster_operation_with_options(request, runtime)

    async def terminate_cluster_operation_async(
        self,
        request: taihao_20210331_models.TerminateClusterOperationRequest,
    ) -> taihao_20210331_models.TerminateClusterOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_cluster_operation_with_options_async(request, runtime)

    def terminate_workflow_instance_with_options(
        self,
        tmp_req: taihao_20210331_models.TerminateWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.TerminateWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.TerminateWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.terminate_workflow_instance_param):
            request.terminate_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.terminate_workflow_instance_param), 'terminateWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.terminate_workflow_instance_param_shrink):
            body['terminateWorkflowInstanceParam'] = request.terminate_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.TerminateWorkflowInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_workflow_instance_with_options_async(
        self,
        tmp_req: taihao_20210331_models.TerminateWorkflowInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.TerminateWorkflowInstanceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.TerminateWorkflowInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.terminate_workflow_instance_param):
            request.terminate_workflow_instance_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.terminate_workflow_instance_param), 'terminateWorkflowInstanceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.terminate_workflow_instance_param_shrink):
            body['terminateWorkflowInstanceParam'] = request.terminate_workflow_instance_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TerminateWorkflowInstance',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.TerminateWorkflowInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_workflow_instance(
        self,
        request: taihao_20210331_models.TerminateWorkflowInstanceRequest,
    ) -> taihao_20210331_models.TerminateWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return self.terminate_workflow_instance_with_options(request, runtime)

    async def terminate_workflow_instance_async(
        self,
        request: taihao_20210331_models.TerminateWorkflowInstanceRequest,
    ) -> taihao_20210331_models.TerminateWorkflowInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.terminate_workflow_instance_with_options_async(request, runtime)

    def un_register_cluster_ack_resource_with_options(
        self,
        tmp_req: taihao_20210331_models.UnRegisterClusterAckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UnRegisterClusterAckResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UnRegisterClusterAckResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.un_register_cluster_ack_resource_param):
            request.un_register_cluster_ack_resource_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.un_register_cluster_ack_resource_param), 'unRegisterClusterAckResourceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.un_register_cluster_ack_resource_param_shrink):
            body['unRegisterClusterAckResourceParam'] = request.un_register_cluster_ack_resource_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnRegisterClusterAckResource',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UnRegisterClusterAckResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_register_cluster_ack_resource_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UnRegisterClusterAckResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UnRegisterClusterAckResourceResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UnRegisterClusterAckResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.un_register_cluster_ack_resource_param):
            request.un_register_cluster_ack_resource_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.un_register_cluster_ack_resource_param), 'unRegisterClusterAckResourceParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.un_register_cluster_ack_resource_param_shrink):
            body['unRegisterClusterAckResourceParam'] = request.un_register_cluster_ack_resource_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnRegisterClusterAckResource',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UnRegisterClusterAckResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_register_cluster_ack_resource(
        self,
        request: taihao_20210331_models.UnRegisterClusterAckResourceRequest,
    ) -> taihao_20210331_models.UnRegisterClusterAckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.un_register_cluster_ack_resource_with_options(request, runtime)

    async def un_register_cluster_ack_resource_async(
        self,
        request: taihao_20210331_models.UnRegisterClusterAckResourceRequest,
    ) -> taihao_20210331_models.UnRegisterClusterAckResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.un_register_cluster_ack_resource_with_options_async(request, runtime)

    def universal_ops_with_options(
        self,
        request: taihao_20210331_models.UniversalOpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UniversalOpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['apiName'] = request.api_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.payload):
            body['payload'] = request.payload
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UniversalOps',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UniversalOpsResponse(),
            self.call_api(params, req, runtime)
        )

    async def universal_ops_with_options_async(
        self,
        request: taihao_20210331_models.UniversalOpsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UniversalOpsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_name):
            query['apiName'] = request.api_name
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.payload):
            body['payload'] = request.payload
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UniversalOps',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UniversalOpsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def universal_ops(
        self,
        request: taihao_20210331_models.UniversalOpsRequest,
    ) -> taihao_20210331_models.UniversalOpsResponse:
        runtime = util_models.RuntimeOptions()
        return self.universal_ops_with_options(request, runtime)

    async def universal_ops_async(
        self,
        request: taihao_20210331_models.UniversalOpsRequest,
    ) -> taihao_20210331_models.UniversalOpsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.universal_ops_with_options_async(request, runtime)

    def update_ack_cluster_node_pools_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateAckClusterNodePoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateAckClusterNodePoolsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateAckClusterNodePoolsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_ack_cluster_node_pools_param):
            request.update_ack_cluster_node_pools_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_ack_cluster_node_pools_param), 'updateAckClusterNodePoolsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_ack_cluster_node_pools_param_shrink):
            body['updateAckClusterNodePoolsParam'] = request.update_ack_cluster_node_pools_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAckClusterNodePools',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateAckClusterNodePoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ack_cluster_node_pools_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateAckClusterNodePoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateAckClusterNodePoolsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateAckClusterNodePoolsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_ack_cluster_node_pools_param):
            request.update_ack_cluster_node_pools_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_ack_cluster_node_pools_param), 'updateAckClusterNodePoolsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_ack_cluster_node_pools_param_shrink):
            body['updateAckClusterNodePoolsParam'] = request.update_ack_cluster_node_pools_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAckClusterNodePools',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateAckClusterNodePoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ack_cluster_node_pools(
        self,
        request: taihao_20210331_models.UpdateAckClusterNodePoolsRequest,
    ) -> taihao_20210331_models.UpdateAckClusterNodePoolsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ack_cluster_node_pools_with_options(request, runtime)

    async def update_ack_cluster_node_pools_async(
        self,
        request: taihao_20210331_models.UpdateAckClusterNodePoolsRequest,
    ) -> taihao_20210331_models.UpdateAckClusterNodePoolsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ack_cluster_node_pools_with_options_async(request, runtime)

    def update_ack_cluster_nodes_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateAckClusterNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateAckClusterNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateAckClusterNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_ack_cluster_nodes_param):
            request.update_ack_cluster_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_ack_cluster_nodes_param), 'updateAckClusterNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_ack_cluster_nodes_param_shrink):
            body['updateAckClusterNodesParam'] = request.update_ack_cluster_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAckClusterNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateAckClusterNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_ack_cluster_nodes_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateAckClusterNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateAckClusterNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateAckClusterNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_ack_cluster_nodes_param):
            request.update_ack_cluster_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_ack_cluster_nodes_param), 'updateAckClusterNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_ack_cluster_nodes_param_shrink):
            body['updateAckClusterNodesParam'] = request.update_ack_cluster_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAckClusterNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateAckClusterNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_ack_cluster_nodes(
        self,
        request: taihao_20210331_models.UpdateAckClusterNodesRequest,
    ) -> taihao_20210331_models.UpdateAckClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_ack_cluster_nodes_with_options(request, runtime)

    async def update_ack_cluster_nodes_async(
        self,
        request: taihao_20210331_models.UpdateAckClusterNodesRequest,
    ) -> taihao_20210331_models.UpdateAckClusterNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_ack_cluster_nodes_with_options_async(request, runtime)

    def update_auto_scaling_policy_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_auto_scaling_policy_param):
            request.update_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_auto_scaling_policy_param), 'updateAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_auto_scaling_policy_param_shrink):
            body['updateAutoScalingPolicyParam'] = request.update_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_scaling_policy_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateAutoScalingPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateAutoScalingPolicyResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateAutoScalingPolicyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_auto_scaling_policy_param):
            request.update_auto_scaling_policy_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_auto_scaling_policy_param), 'updateAutoScalingPolicyParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_auto_scaling_policy_param_shrink):
            body['updateAutoScalingPolicyParam'] = request.update_auto_scaling_policy_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAutoScalingPolicy',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateAutoScalingPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_scaling_policy(
        self,
        request: taihao_20210331_models.UpdateAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.UpdateAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_auto_scaling_policy_with_options(request, runtime)

    async def update_auto_scaling_policy_async(
        self,
        request: taihao_20210331_models.UpdateAutoScalingPolicyRequest,
    ) -> taihao_20210331_models.UpdateAutoScalingPolicyResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_scaling_policy_with_options_async(request, runtime)

    def update_auto_scaling_rule_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateAutoScalingRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateAutoScalingRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_auto_scaling_rule_param):
            request.update_auto_scaling_rule_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_auto_scaling_rule_param), 'updateAutoScalingRuleParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_auto_scaling_rule_param_shrink):
            body['updateAutoScalingRuleParam'] = request.update_auto_scaling_rule_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAutoScalingRule',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateAutoScalingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_auto_scaling_rule_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateAutoScalingRuleRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateAutoScalingRuleResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateAutoScalingRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_auto_scaling_rule_param):
            request.update_auto_scaling_rule_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_auto_scaling_rule_param), 'updateAutoScalingRuleParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_auto_scaling_rule_param_shrink):
            body['updateAutoScalingRuleParam'] = request.update_auto_scaling_rule_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAutoScalingRule',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateAutoScalingRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_auto_scaling_rule(
        self,
        request: taihao_20210331_models.UpdateAutoScalingRuleRequest,
    ) -> taihao_20210331_models.UpdateAutoScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_auto_scaling_rule_with_options(request, runtime)

    async def update_auto_scaling_rule_async(
        self,
        request: taihao_20210331_models.UpdateAutoScalingRuleRequest,
    ) -> taihao_20210331_models.UpdateAutoScalingRuleResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_auto_scaling_rule_with_options_async(request, runtime)

    def update_cluster_attribute_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateClusterAttributeResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateClusterAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'param', 'json')
        query = {}
        if not UtilClient.is_unset(request.param_shrink):
            query['param'] = request.param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterAttribute',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateClusterAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_attribute_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateClusterAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateClusterAttributeResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateClusterAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.param):
            request.param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.param), 'param', 'json')
        query = {}
        if not UtilClient.is_unset(request.param_shrink):
            query['param'] = request.param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateClusterAttribute',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateClusterAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_attribute(
        self,
        request: taihao_20210331_models.UpdateClusterAttributeRequest,
    ) -> taihao_20210331_models.UpdateClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_attribute_with_options(request, runtime)

    async def update_cluster_attribute_async(
        self,
        request: taihao_20210331_models.UpdateClusterAttributeRequest,
    ) -> taihao_20210331_models.UpdateClusterAttributeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_attribute_with_options_async(request, runtime)

    def update_cluster_node_group_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateClusterNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateClusterNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateClusterNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_cluster_node_group_param):
            request.update_cluster_node_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_cluster_node_group_param), 'updateClusterNodeGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_cluster_node_group_param_shrink):
            body['updateClusterNodeGroupParam'] = request.update_cluster_node_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClusterNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateClusterNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_node_group_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateClusterNodeGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateClusterNodeGroupResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateClusterNodeGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_cluster_node_group_param):
            request.update_cluster_node_group_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_cluster_node_group_param), 'updateClusterNodeGroupParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_cluster_node_group_param_shrink):
            body['updateClusterNodeGroupParam'] = request.update_cluster_node_group_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClusterNodeGroup',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateClusterNodeGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_node_group(
        self,
        request: taihao_20210331_models.UpdateClusterNodeGroupRequest,
    ) -> taihao_20210331_models.UpdateClusterNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_node_group_with_options(request, runtime)

    async def update_cluster_node_group_async(
        self,
        request: taihao_20210331_models.UpdateClusterNodeGroupRequest,
    ) -> taihao_20210331_models.UpdateClusterNodeGroupResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_node_group_with_options_async(request, runtime)

    def update_cluster_script_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateClusterScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateClusterScriptResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateClusterScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_cluster_script_param):
            request.update_cluster_script_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_cluster_script_param), 'updateClusterScriptParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_cluster_script_param_shrink):
            body['updateClusterScriptParam'] = request.update_cluster_script_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClusterScript',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateClusterScriptResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_script_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateClusterScriptRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateClusterScriptResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateClusterScriptShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_cluster_script_param):
            request.update_cluster_script_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_cluster_script_param), 'updateClusterScriptParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_cluster_script_param_shrink):
            body['updateClusterScriptParam'] = request.update_cluster_script_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClusterScript',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateClusterScriptResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_script(
        self,
        request: taihao_20210331_models.UpdateClusterScriptRequest,
    ) -> taihao_20210331_models.UpdateClusterScriptResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_script_with_options(request, runtime)

    async def update_cluster_script_async(
        self,
        request: taihao_20210331_models.UpdateClusterScriptRequest,
    ) -> taihao_20210331_models.UpdateClusterScriptResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_script_with_options_async(request, runtime)

    def update_cluster_user_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateClusterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateClusterUserResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateClusterUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_cluster_user_param):
            request.update_cluster_user_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_cluster_user_param), 'updateClusterUserParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_cluster_user_param_shrink):
            body['updateClusterUserParam'] = request.update_cluster_user_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClusterUser',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateClusterUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_cluster_user_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateClusterUserRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateClusterUserResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateClusterUserShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_cluster_user_param):
            request.update_cluster_user_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_cluster_user_param), 'updateClusterUserParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_cluster_user_param_shrink):
            body['updateClusterUserParam'] = request.update_cluster_user_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateClusterUser',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateClusterUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_cluster_user(
        self,
        request: taihao_20210331_models.UpdateClusterUserRequest,
    ) -> taihao_20210331_models.UpdateClusterUserResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_user_with_options(request, runtime)

    async def update_cluster_user_async(
        self,
        request: taihao_20210331_models.UpdateClusterUserRequest,
    ) -> taihao_20210331_models.UpdateClusterUserResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_cluster_user_with_options_async(request, runtime)

    def update_config_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_config_param):
            request.update_config_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_config_param), 'updateConfigParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_config_param_shrink):
            body['updateConfigParam'] = request.update_config_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_config_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateConfigResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_config_param):
            request.update_config_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_config_param), 'updateConfigParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_config_param_shrink):
            body['updateConfigParam'] = request.update_config_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateConfig',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_config(
        self,
        request: taihao_20210331_models.UpdateConfigRequest,
    ) -> taihao_20210331_models.UpdateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_config_with_options(request, runtime)

    async def update_config_async(
        self,
        request: taihao_20210331_models.UpdateConfigRequest,
    ) -> taihao_20210331_models.UpdateConfigResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_config_with_options_async(request, runtime)

    def update_on_kube_dedicated_nodes_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateOnKubeDedicatedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateOnKubeDedicatedNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateOnKubeDedicatedNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_on_kube_dedicated_nodes_param):
            request.update_on_kube_dedicated_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_on_kube_dedicated_nodes_param), 'updateOnKubeDedicatedNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_on_kube_dedicated_nodes_param_shrink):
            body['updateOnKubeDedicatedNodesParam'] = request.update_on_kube_dedicated_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOnKubeDedicatedNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateOnKubeDedicatedNodesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_on_kube_dedicated_nodes_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateOnKubeDedicatedNodesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateOnKubeDedicatedNodesResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateOnKubeDedicatedNodesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_on_kube_dedicated_nodes_param):
            request.update_on_kube_dedicated_nodes_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_on_kube_dedicated_nodes_param), 'updateOnKubeDedicatedNodesParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_on_kube_dedicated_nodes_param_shrink):
            body['updateOnKubeDedicatedNodesParam'] = request.update_on_kube_dedicated_nodes_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateOnKubeDedicatedNodes',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateOnKubeDedicatedNodesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_on_kube_dedicated_nodes(
        self,
        request: taihao_20210331_models.UpdateOnKubeDedicatedNodesRequest,
    ) -> taihao_20210331_models.UpdateOnKubeDedicatedNodesResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_on_kube_dedicated_nodes_with_options(request, runtime)

    async def update_on_kube_dedicated_nodes_async(
        self,
        request: taihao_20210331_models.UpdateOnKubeDedicatedNodesRequest,
    ) -> taihao_20210331_models.UpdateOnKubeDedicatedNodesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_on_kube_dedicated_nodes_with_options_async(request, runtime)

    def update_security_mode_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateSecurityModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateSecurityModeResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateSecurityModeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_cluster_security_mode_param):
            request.update_cluster_security_mode_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_cluster_security_mode_param), 'updateClusterSecurityModeParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_cluster_security_mode_param_shrink):
            body['updateClusterSecurityModeParam'] = request.update_cluster_security_mode_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSecurityMode',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateSecurityModeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_security_mode_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateSecurityModeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateSecurityModeResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateSecurityModeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_cluster_security_mode_param):
            request.update_cluster_security_mode_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_cluster_security_mode_param), 'updateClusterSecurityModeParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_cluster_security_mode_param_shrink):
            body['updateClusterSecurityModeParam'] = request.update_cluster_security_mode_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSecurityMode',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateSecurityModeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_security_mode(
        self,
        request: taihao_20210331_models.UpdateSecurityModeRequest,
    ) -> taihao_20210331_models.UpdateSecurityModeResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_security_mode_with_options(request, runtime)

    async def update_security_mode_async(
        self,
        request: taihao_20210331_models.UpdateSecurityModeRequest,
    ) -> taihao_20210331_models.UpdateSecurityModeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_security_mode_with_options_async(request, runtime)

    def update_on_kube_dedicated_node_pools_with_options(
        self,
        tmp_req: taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_on_kube_dedicated_node_pools_param):
            request.update_on_kube_dedicated_node_pools_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_on_kube_dedicated_node_pools_param), 'updateOnKubeDedicatedNodePoolsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_on_kube_dedicated_node_pools_param_shrink):
            body['updateOnKubeDedicatedNodePoolsParam'] = request.update_on_kube_dedicated_node_pools_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='updateOnKubeDedicatedNodePools',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_on_kube_dedicated_node_pools_with_options_async(
        self,
        tmp_req: taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsResponse:
        UtilClient.validate_model(tmp_req)
        request = taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_on_kube_dedicated_node_pools_param):
            request.update_on_kube_dedicated_node_pools_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.update_on_kube_dedicated_node_pools_param), 'updateOnKubeDedicatedNodePoolsParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_on_kube_dedicated_node_pools_param_shrink):
            body['updateOnKubeDedicatedNodePoolsParam'] = request.update_on_kube_dedicated_node_pools_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='updateOnKubeDedicatedNodePools',
            version='2021-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_on_kube_dedicated_node_pools(
        self,
        request: taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsRequest,
    ) -> taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsResponse:
        runtime = util_models.RuntimeOptions()
        return self.update_on_kube_dedicated_node_pools_with_options(request, runtime)

    async def update_on_kube_dedicated_node_pools_async(
        self,
        request: taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsRequest,
    ) -> taihao_20210331_models.UpdateOnKubeDedicatedNodePoolsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_on_kube_dedicated_node_pools_with_options_async(request, runtime)
