# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_gemp20210413 import models as gemp20210413_models
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
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('gemp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_problem_service_group_with_options(
        self,
        request: gemp20210413_models.AddProblemServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.AddProblemServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProblemServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/addServiceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.AddProblemServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_problem_service_group_with_options_async(
        self,
        request: gemp20210413_models.AddProblemServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.AddProblemServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProblemServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/addServiceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.AddProblemServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_problem_service_group(
        self,
        request: gemp20210413_models.AddProblemServiceGroupRequest,
    ) -> gemp20210413_models.AddProblemServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.add_problem_service_group_with_options(request, headers, runtime)

    async def add_problem_service_group_async(
        self,
        request: gemp20210413_models.AddProblemServiceGroupRequest,
    ) -> gemp20210413_models.AddProblemServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.add_problem_service_group_with_options_async(request, headers, runtime)

    def billing_statistics_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.BillingStatisticsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='BillingStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/charging/details',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.BillingStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def billing_statistics_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.BillingStatisticsResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='BillingStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/charging/details',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.BillingStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def billing_statistics(self) -> gemp20210413_models.BillingStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.billing_statistics_with_options(headers, runtime)

    async def billing_statistics_async(self) -> gemp20210413_models.BillingStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.billing_statistics_with_options_async(headers, runtime)

    def cancel_problem_with_options(
        self,
        request: gemp20210413_models.CancelProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CancelProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cancel_reason):
            body['cancelReason'] = request.cancel_reason
        if not UtilClient.is_unset(request.cancel_reason_description):
            body['cancelReasonDescription'] = request.cancel_reason_description
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CancelProblemResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_problem_with_options_async(
        self,
        request: gemp20210413_models.CancelProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CancelProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cancel_reason):
            body['cancelReason'] = request.cancel_reason
        if not UtilClient.is_unset(request.cancel_reason_description):
            body['cancelReasonDescription'] = request.cancel_reason_description
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/cancel',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CancelProblemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_problem(
        self,
        request: gemp20210413_models.CancelProblemRequest,
    ) -> gemp20210413_models.CancelProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.cancel_problem_with_options(request, headers, runtime)

    async def cancel_problem_async(
        self,
        request: gemp20210413_models.CancelProblemRequest,
    ) -> gemp20210413_models.CancelProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.cancel_problem_with_options_async(request, headers, runtime)

    def check_webhook_with_options(
        self,
        request: gemp20210413_models.CheckWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CheckWebhookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.webhook):
            body['webhook'] = request.webhook
        if not UtilClient.is_unset(request.webhook_type):
            body['webhookType'] = request.webhook_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckWebhook',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/check/webhook',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CheckWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_webhook_with_options_async(
        self,
        request: gemp20210413_models.CheckWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CheckWebhookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.webhook):
            body['webhook'] = request.webhook
        if not UtilClient.is_unset(request.webhook_type):
            body['webhookType'] = request.webhook_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckWebhook',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/check/webhook',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CheckWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_webhook(
        self,
        request: gemp20210413_models.CheckWebhookRequest,
    ) -> gemp20210413_models.CheckWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.check_webhook_with_options(request, headers, runtime)

    async def check_webhook_async(
        self,
        request: gemp20210413_models.CheckWebhookRequest,
    ) -> gemp20210413_models.CheckWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.check_webhook_with_options_async(request, headers, runtime)

    def confirm_integration_config_with_options(
        self,
        request: gemp20210413_models.ConfirmIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ConfirmIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfirmIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/confirm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ConfirmIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def confirm_integration_config_with_options_async(
        self,
        request: gemp20210413_models.ConfirmIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ConfirmIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ConfirmIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/confirm',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ConfirmIntegrationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def confirm_integration_config(
        self,
        request: gemp20210413_models.ConfirmIntegrationConfigRequest,
    ) -> gemp20210413_models.ConfirmIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.confirm_integration_config_with_options(request, headers, runtime)

    async def confirm_integration_config_async(
        self,
        request: gemp20210413_models.ConfirmIntegrationConfigRequest,
    ) -> gemp20210413_models.ConfirmIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.confirm_integration_config_with_options_async(request, headers, runtime)

    def create_escalation_plan_with_options(
        self,
        request: gemp20210413_models.CreateEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_description):
            body['escalationPlanDescription'] = request.escalation_plan_description
        if not UtilClient.is_unset(request.escalation_plan_name):
            body['escalationPlanName'] = request.escalation_plan_name
        if not UtilClient.is_unset(request.escalation_plan_rules):
            body['escalationPlanRules'] = request.escalation_plan_rules
        if not UtilClient.is_unset(request.escalation_plan_scope_objects):
            body['escalationPlanScopeObjects'] = request.escalation_plan_scope_objects
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_escalation_plan_with_options_async(
        self,
        request: gemp20210413_models.CreateEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_description):
            body['escalationPlanDescription'] = request.escalation_plan_description
        if not UtilClient.is_unset(request.escalation_plan_name):
            body['escalationPlanName'] = request.escalation_plan_name
        if not UtilClient.is_unset(request.escalation_plan_rules):
            body['escalationPlanRules'] = request.escalation_plan_rules
        if not UtilClient.is_unset(request.escalation_plan_scope_objects):
            body['escalationPlanScopeObjects'] = request.escalation_plan_scope_objects
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateEscalationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_escalation_plan(
        self,
        request: gemp20210413_models.CreateEscalationPlanRequest,
    ) -> gemp20210413_models.CreateEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_escalation_plan_with_options(request, headers, runtime)

    async def create_escalation_plan_async(
        self,
        request: gemp20210413_models.CreateEscalationPlanRequest,
    ) -> gemp20210413_models.CreateEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_escalation_plan_with_options_async(request, headers, runtime)

    def create_incident_with_options(
        self,
        request: gemp20210413_models.CreateIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_user_id):
            body['assignUserId'] = request.assign_user_id
        if not UtilClient.is_unset(request.channels):
            body['channels'] = request.channels
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effect):
            body['effect'] = request.effect
        if not UtilClient.is_unset(request.incident_description):
            body['incidentDescription'] = request.incident_description
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.incident_title):
            body['incidentTitle'] = request.incident_title
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/manualSave',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_incident_with_options_async(
        self,
        request: gemp20210413_models.CreateIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_user_id):
            body['assignUserId'] = request.assign_user_id
        if not UtilClient.is_unset(request.channels):
            body['channels'] = request.channels
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effect):
            body['effect'] = request.effect
        if not UtilClient.is_unset(request.incident_description):
            body['incidentDescription'] = request.incident_description
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.incident_title):
            body['incidentTitle'] = request.incident_title
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/manualSave',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_incident(
        self,
        request: gemp20210413_models.CreateIncidentRequest,
    ) -> gemp20210413_models.CreateIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_incident_with_options(request, headers, runtime)

    async def create_incident_async(
        self,
        request: gemp20210413_models.CreateIncidentRequest,
    ) -> gemp20210413_models.CreateIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_incident_with_options_async(request, headers, runtime)

    def create_incident_subtotal_with_options(
        self,
        request: gemp20210413_models.CreateIncidentSubtotalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateIncidentSubtotalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIncidentSubtotal',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/save/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateIncidentSubtotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_incident_subtotal_with_options_async(
        self,
        request: gemp20210413_models.CreateIncidentSubtotalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateIncidentSubtotalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIncidentSubtotal',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/save/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateIncidentSubtotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_incident_subtotal(
        self,
        request: gemp20210413_models.CreateIncidentSubtotalRequest,
    ) -> gemp20210413_models.CreateIncidentSubtotalResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_incident_subtotal_with_options(request, headers, runtime)

    async def create_incident_subtotal_async(
        self,
        request: gemp20210413_models.CreateIncidentSubtotalRequest,
    ) -> gemp20210413_models.CreateIncidentSubtotalResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_incident_subtotal_with_options_async(request, headers, runtime)

    def create_integration_config_with_options(
        self,
        request: gemp20210413_models.CreateIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_integration_config_with_options_async(
        self,
        request: gemp20210413_models.CreateIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateIntegrationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_integration_config(
        self,
        request: gemp20210413_models.CreateIntegrationConfigRequest,
    ) -> gemp20210413_models.CreateIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_integration_config_with_options(request, headers, runtime)

    async def create_integration_config_async(
        self,
        request: gemp20210413_models.CreateIntegrationConfigRequest,
    ) -> gemp20210413_models.CreateIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_integration_config_with_options_async(request, headers, runtime)

    def create_problem_with_options(
        self,
        request: gemp20210413_models.CreateProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.affect_service_ids):
            body['affectServiceIds'] = request.affect_service_ids
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.discover_time):
            body['discoverTime'] = request.discover_time
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.main_handler_id):
            body['mainHandlerId'] = request.main_handler_id
        if not UtilClient.is_unset(request.preliminary_reason):
            body['preliminaryReason'] = request.preliminary_reason
        if not UtilClient.is_unset(request.problem_level):
            body['problemLevel'] = request.problem_level
        if not UtilClient.is_unset(request.problem_name):
            body['problemName'] = request.problem_name
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        if not UtilClient.is_unset(request.problem_status):
            body['problemStatus'] = request.problem_status
        if not UtilClient.is_unset(request.progress_summary):
            body['progressSummary'] = request.progress_summary
        if not UtilClient.is_unset(request.progress_summary_rich_text_id):
            body['progressSummaryRichTextId'] = request.progress_summary_rich_text_id
        if not UtilClient.is_unset(request.recovery_time):
            body['recoveryTime'] = request.recovery_time
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_problem_with_options_async(
        self,
        request: gemp20210413_models.CreateProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.affect_service_ids):
            body['affectServiceIds'] = request.affect_service_ids
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.discover_time):
            body['discoverTime'] = request.discover_time
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.main_handler_id):
            body['mainHandlerId'] = request.main_handler_id
        if not UtilClient.is_unset(request.preliminary_reason):
            body['preliminaryReason'] = request.preliminary_reason
        if not UtilClient.is_unset(request.problem_level):
            body['problemLevel'] = request.problem_level
        if not UtilClient.is_unset(request.problem_name):
            body['problemName'] = request.problem_name
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        if not UtilClient.is_unset(request.problem_status):
            body['problemStatus'] = request.problem_status
        if not UtilClient.is_unset(request.progress_summary):
            body['progressSummary'] = request.progress_summary
        if not UtilClient.is_unset(request.progress_summary_rich_text_id):
            body['progressSummaryRichTextId'] = request.progress_summary_rich_text_id
        if not UtilClient.is_unset(request.recovery_time):
            body['recoveryTime'] = request.recovery_time
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/upgrade',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_problem(
        self,
        request: gemp20210413_models.CreateProblemRequest,
    ) -> gemp20210413_models.CreateProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_with_options(request, headers, runtime)

    async def create_problem_async(
        self,
        request: gemp20210413_models.CreateProblemRequest,
    ) -> gemp20210413_models.CreateProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_problem_with_options_async(request, headers, runtime)

    def create_problem_effection_service_with_options(
        self,
        request: gemp20210413_models.CreateProblemEffectionServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemEffectionServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/effectionService/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemEffectionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_problem_effection_service_with_options_async(
        self,
        request: gemp20210413_models.CreateProblemEffectionServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemEffectionServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        if not UtilClient.is_unset(request.picture_url):
            body['pictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/effectionService/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemEffectionServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_problem_effection_service(
        self,
        request: gemp20210413_models.CreateProblemEffectionServiceRequest,
    ) -> gemp20210413_models.CreateProblemEffectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_effection_service_with_options(request, headers, runtime)

    async def create_problem_effection_service_async(
        self,
        request: gemp20210413_models.CreateProblemEffectionServiceRequest,
    ) -> gemp20210413_models.CreateProblemEffectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_problem_effection_service_with_options_async(request, headers, runtime)

    def create_problem_measure_with_options(
        self,
        request: gemp20210413_models.CreateProblemMeasureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemMeasureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_standard):
            body['checkStandard'] = request.check_standard
        if not UtilClient.is_unset(request.check_user_id):
            body['checkUserId'] = request.check_user_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.director_id):
            body['directorId'] = request.director_id
        if not UtilClient.is_unset(request.plan_finish_time):
            body['planFinishTime'] = request.plan_finish_time
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.stalker_id):
            body['stalkerId'] = request.stalker_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemMeasure',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/measure/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_problem_measure_with_options_async(
        self,
        request: gemp20210413_models.CreateProblemMeasureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemMeasureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_standard):
            body['checkStandard'] = request.check_standard
        if not UtilClient.is_unset(request.check_user_id):
            body['checkUserId'] = request.check_user_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.director_id):
            body['directorId'] = request.director_id
        if not UtilClient.is_unset(request.plan_finish_time):
            body['planFinishTime'] = request.plan_finish_time
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.stalker_id):
            body['stalkerId'] = request.stalker_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemMeasure',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/measure/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemMeasureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_problem_measure(
        self,
        request: gemp20210413_models.CreateProblemMeasureRequest,
    ) -> gemp20210413_models.CreateProblemMeasureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_measure_with_options(request, headers, runtime)

    async def create_problem_measure_async(
        self,
        request: gemp20210413_models.CreateProblemMeasureRequest,
    ) -> gemp20210413_models.CreateProblemMeasureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_problem_measure_with_options_async(request, headers, runtime)

    def create_problem_subtotal_with_options(
        self,
        request: gemp20210413_models.CreateProblemSubtotalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemSubtotalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemSubtotal',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/save/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemSubtotalResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_problem_subtotal_with_options_async(
        self,
        request: gemp20210413_models.CreateProblemSubtotalRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemSubtotalResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemSubtotal',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/save/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemSubtotalResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_problem_subtotal(
        self,
        request: gemp20210413_models.CreateProblemSubtotalRequest,
    ) -> gemp20210413_models.CreateProblemSubtotalResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_subtotal_with_options(request, headers, runtime)

    async def create_problem_subtotal_async(
        self,
        request: gemp20210413_models.CreateProblemSubtotalRequest,
    ) -> gemp20210413_models.CreateProblemSubtotalResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_problem_subtotal_with_options_async(request, headers, runtime)

    def create_problem_timeline_with_options(
        self,
        request: gemp20210413_models.CreateProblemTimelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemTimelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.key_node):
            body['keyNode'] = request.key_node
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.time):
            body['time'] = request.time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemTimeline',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/timeline/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_problem_timeline_with_options_async(
        self,
        request: gemp20210413_models.CreateProblemTimelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemTimelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.key_node):
            body['keyNode'] = request.key_node
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.time):
            body['time'] = request.time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemTimeline',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/timeline/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_problem_timeline(
        self,
        request: gemp20210413_models.CreateProblemTimelineRequest,
    ) -> gemp20210413_models.CreateProblemTimelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_timeline_with_options(request, headers, runtime)

    async def create_problem_timeline_async(
        self,
        request: gemp20210413_models.CreateProblemTimelineRequest,
    ) -> gemp20210413_models.CreateProblemTimelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_problem_timeline_with_options_async(request, headers, runtime)

    def create_problem_timelines_with_options(
        self,
        request: gemp20210413_models.CreateProblemTimelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemTimelinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.timeline_nodes):
            body['timelineNodes'] = request.timeline_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/timeline/batchCreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemTimelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_problem_timelines_with_options_async(
        self,
        request: gemp20210413_models.CreateProblemTimelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateProblemTimelinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.timeline_nodes):
            body['timelineNodes'] = request.timeline_nodes
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProblemTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/timeline/batchCreate',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateProblemTimelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_problem_timelines(
        self,
        request: gemp20210413_models.CreateProblemTimelinesRequest,
    ) -> gemp20210413_models.CreateProblemTimelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_problem_timelines_with_options(request, headers, runtime)

    async def create_problem_timelines_async(
        self,
        request: gemp20210413_models.CreateProblemTimelinesRequest,
    ) -> gemp20210413_models.CreateProblemTimelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_problem_timelines_with_options_async(request, headers, runtime)

    def create_rich_text_with_options(
        self,
        request: gemp20210413_models.CreateRichTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateRichTextResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.rich_text):
            body['richText'] = request.rich_text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRichText',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateRichTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_rich_text_with_options_async(
        self,
        request: gemp20210413_models.CreateRichTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateRichTextResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.rich_text):
            body['richText'] = request.rich_text
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRichText',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateRichTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_rich_text(
        self,
        request: gemp20210413_models.CreateRichTextRequest,
    ) -> gemp20210413_models.CreateRichTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_rich_text_with_options(request, headers, runtime)

    async def create_rich_text_async(
        self,
        request: gemp20210413_models.CreateRichTextRequest,
    ) -> gemp20210413_models.CreateRichTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_rich_text_with_options_async(request, headers, runtime)

    def create_route_rule_with_options(
        self,
        request: gemp20210413_models.CreateRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_object_id):
            body['assignObjectId'] = request.assign_object_id
        if not UtilClient.is_unset(request.assign_object_type):
            body['assignObjectType'] = request.assign_object_type
        if not UtilClient.is_unset(request.child_rule_relation):
            body['childRuleRelation'] = request.child_rule_relation
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.convergence_fields):
            body['convergenceFields'] = request.convergence_fields
        if not UtilClient.is_unset(request.convergence_type):
            body['convergenceType'] = request.convergence_type
        if not UtilClient.is_unset(request.coverage_problem_levels):
            body['coverageProblemLevels'] = request.coverage_problem_levels
        if not UtilClient.is_unset(request.effection):
            body['effection'] = request.effection
        if not UtilClient.is_unset(request.enable_status):
            body['enableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.match_count):
            body['matchCount'] = request.match_count
        if not UtilClient.is_unset(request.notify_channels):
            body['notifyChannels'] = request.notify_channels
        if not UtilClient.is_unset(request.problem_effection_services):
            body['problemEffectionServices'] = request.problem_effection_services
        if not UtilClient.is_unset(request.problem_level_group):
            body['problemLevelGroup'] = request.problem_level_group
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.route_child_rules):
            body['routeChildRules'] = request.route_child_rules
        if not UtilClient.is_unset(request.route_type):
            body['routeType'] = request.route_type
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.time_window):
            body['timeWindow'] = request.time_window
        if not UtilClient.is_unset(request.time_window_unit):
            body['timeWindowUnit'] = request.time_window_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_route_rule_with_options_async(
        self,
        request: gemp20210413_models.CreateRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_object_id):
            body['assignObjectId'] = request.assign_object_id
        if not UtilClient.is_unset(request.assign_object_type):
            body['assignObjectType'] = request.assign_object_type
        if not UtilClient.is_unset(request.child_rule_relation):
            body['childRuleRelation'] = request.child_rule_relation
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.convergence_fields):
            body['convergenceFields'] = request.convergence_fields
        if not UtilClient.is_unset(request.convergence_type):
            body['convergenceType'] = request.convergence_type
        if not UtilClient.is_unset(request.coverage_problem_levels):
            body['coverageProblemLevels'] = request.coverage_problem_levels
        if not UtilClient.is_unset(request.effection):
            body['effection'] = request.effection
        if not UtilClient.is_unset(request.enable_status):
            body['enableStatus'] = request.enable_status
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.match_count):
            body['matchCount'] = request.match_count
        if not UtilClient.is_unset(request.notify_channels):
            body['notifyChannels'] = request.notify_channels
        if not UtilClient.is_unset(request.problem_effection_services):
            body['problemEffectionServices'] = request.problem_effection_services
        if not UtilClient.is_unset(request.problem_level_group):
            body['problemLevelGroup'] = request.problem_level_group
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.route_child_rules):
            body['routeChildRules'] = request.route_child_rules
        if not UtilClient.is_unset(request.route_type):
            body['routeType'] = request.route_type
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.time_window):
            body['timeWindow'] = request.time_window
        if not UtilClient.is_unset(request.time_window_unit):
            body['timeWindowUnit'] = request.time_window_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_route_rule(
        self,
        request: gemp20210413_models.CreateRouteRuleRequest,
    ) -> gemp20210413_models.CreateRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_route_rule_with_options(request, headers, runtime)

    async def create_route_rule_async(
        self,
        request: gemp20210413_models.CreateRouteRuleRequest,
    ) -> gemp20210413_models.CreateRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_route_rule_with_options_async(request, headers, runtime)

    def create_service_with_options(
        self,
        request: gemp20210413_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_description):
            body['serviceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: gemp20210413_models.CreateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_description):
            body['serviceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: gemp20210413_models.CreateServiceRequest,
    ) -> gemp20210413_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_with_options(request, headers, runtime)

    async def create_service_async(
        self,
        request: gemp20210413_models.CreateServiceRequest,
    ) -> gemp20210413_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_with_options_async(request, headers, runtime)

    def create_service_group_with_options(
        self,
        request: gemp20210413_models.CreateServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_webhook):
            body['enableWebhook'] = request.enable_webhook
        if not UtilClient.is_unset(request.monitor_source_templates):
            body['monitorSourceTemplates'] = request.monitor_source_templates
        if not UtilClient.is_unset(request.service_group_description):
            body['serviceGroupDescription'] = request.service_group_description
        if not UtilClient.is_unset(request.service_group_name):
            body['serviceGroupName'] = request.service_group_name
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.webhook_link):
            body['webhookLink'] = request.webhook_link
        if not UtilClient.is_unset(request.webhook_type):
            body['webhookType'] = request.webhook_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/insert',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_group_with_options_async(
        self,
        request: gemp20210413_models.CreateServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_webhook):
            body['enableWebhook'] = request.enable_webhook
        if not UtilClient.is_unset(request.monitor_source_templates):
            body['monitorSourceTemplates'] = request.monitor_source_templates
        if not UtilClient.is_unset(request.service_group_description):
            body['serviceGroupDescription'] = request.service_group_description
        if not UtilClient.is_unset(request.service_group_name):
            body['serviceGroupName'] = request.service_group_name
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.webhook_link):
            body['webhookLink'] = request.webhook_link
        if not UtilClient.is_unset(request.webhook_type):
            body['webhookType'] = request.webhook_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/insert',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_group(
        self,
        request: gemp20210413_models.CreateServiceGroupRequest,
    ) -> gemp20210413_models.CreateServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_group_with_options(request, headers, runtime)

    async def create_service_group_async(
        self,
        request: gemp20210413_models.CreateServiceGroupRequest,
    ) -> gemp20210413_models.CreateServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_group_with_options_async(request, headers, runtime)

    def create_service_group_scheduling_with_options(
        self,
        request: gemp20210413_models.CreateServiceGroupSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateServiceGroupSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.fast_scheduling):
            body['fastScheduling'] = request.fast_scheduling
        if not UtilClient.is_unset(request.fine_scheduling):
            body['fineScheduling'] = request.fine_scheduling
        if not UtilClient.is_unset(request.scheduling_way):
            body['schedulingWay'] = request.scheduling_way
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceGroupSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_group_scheduling_with_options_async(
        self,
        request: gemp20210413_models.CreateServiceGroupSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateServiceGroupSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.fast_scheduling):
            body['fastScheduling'] = request.fast_scheduling
        if not UtilClient.is_unset(request.fine_scheduling):
            body['fineScheduling'] = request.fine_scheduling
        if not UtilClient.is_unset(request.scheduling_way):
            body['schedulingWay'] = request.scheduling_way
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/save',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateServiceGroupSchedulingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_group_scheduling(
        self,
        request: gemp20210413_models.CreateServiceGroupSchedulingRequest,
    ) -> gemp20210413_models.CreateServiceGroupSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_service_group_scheduling_with_options(request, headers, runtime)

    async def create_service_group_scheduling_async(
        self,
        request: gemp20210413_models.CreateServiceGroupSchedulingRequest,
    ) -> gemp20210413_models.CreateServiceGroupSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_service_group_scheduling_with_options_async(request, headers, runtime)

    def create_subscription_with_options(
        self,
        request: gemp20210413_models.CreateSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.expired_type):
            body['expiredType'] = request.expired_type
        if not UtilClient.is_unset(request.notify_object_list):
            body['notifyObjectList'] = request.notify_object_list
        if not UtilClient.is_unset(request.notify_object_type):
            body['notifyObjectType'] = request.notify_object_type
        if not UtilClient.is_unset(request.notify_strategy_list):
            body['notifyStrategyList'] = request.notify_strategy_list
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.scope_object_list):
            body['scopeObjectList'] = request.scope_object_list
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.subscription_title):
            body['subscriptionTitle'] = request.subscription_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_subscription_with_options_async(
        self,
        request: gemp20210413_models.CreateSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.expired_type):
            body['expiredType'] = request.expired_type
        if not UtilClient.is_unset(request.notify_object_list):
            body['notifyObjectList'] = request.notify_object_list
        if not UtilClient.is_unset(request.notify_object_type):
            body['notifyObjectType'] = request.notify_object_type
        if not UtilClient.is_unset(request.notify_strategy_list):
            body['notifyStrategyList'] = request.notify_strategy_list
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.scope_object_list):
            body['scopeObjectList'] = request.scope_object_list
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.subscription_title):
            body['subscriptionTitle'] = request.subscription_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_subscription(
        self,
        request: gemp20210413_models.CreateSubscriptionRequest,
    ) -> gemp20210413_models.CreateSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_subscription_with_options(request, headers, runtime)

    async def create_subscription_async(
        self,
        request: gemp20210413_models.CreateSubscriptionRequest,
    ) -> gemp20210413_models.CreateSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_subscription_with_options_async(request, headers, runtime)

    def create_tenant_application_with_options(
        self,
        request: gemp20210413_models.CreateTenantApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateTenantApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantApplication',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/mobileApp/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateTenantApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tenant_application_with_options_async(
        self,
        request: gemp20210413_models.CreateTenantApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateTenantApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.channel):
            body['channel'] = request.channel
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateTenantApplication',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/mobileApp/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateTenantApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tenant_application(
        self,
        request: gemp20210413_models.CreateTenantApplicationRequest,
    ) -> gemp20210413_models.CreateTenantApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_tenant_application_with_options(request, headers, runtime)

    async def create_tenant_application_async(
        self,
        request: gemp20210413_models.CreateTenantApplicationRequest,
    ) -> gemp20210413_models.CreateTenantApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_tenant_application_with_options_async(request, headers, runtime)

    def create_user_with_options(
        self,
        request: gemp20210413_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.ram_id):
            body['ramId'] = request.ram_id
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_user_with_options_async(
        self,
        request: gemp20210413_models.CreateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.CreateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.ram_id):
            body['ramId'] = request.ram_id
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/create',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.CreateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_user(
        self,
        request: gemp20210413_models.CreateUserRequest,
    ) -> gemp20210413_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.create_user_with_options(request, headers, runtime)

    async def create_user_async(
        self,
        request: gemp20210413_models.CreateUserRequest,
    ) -> gemp20210413_models.CreateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.create_user_with_options_async(request, headers, runtime)

    def delete_escalation_plan_with_options(
        self,
        request: gemp20210413_models.DeleteEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_escalation_plan_with_options_async(
        self,
        request: gemp20210413_models.DeleteEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteEscalationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_escalation_plan(
        self,
        request: gemp20210413_models.DeleteEscalationPlanRequest,
    ) -> gemp20210413_models.DeleteEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_escalation_plan_with_options(request, headers, runtime)

    async def delete_escalation_plan_async(
        self,
        request: gemp20210413_models.DeleteEscalationPlanRequest,
    ) -> gemp20210413_models.DeleteEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_escalation_plan_with_options_async(request, headers, runtime)

    def delete_incident_with_options(
        self,
        request: gemp20210413_models.DeleteIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_incident_with_options_async(
        self,
        request: gemp20210413_models.DeleteIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_incident(
        self,
        request: gemp20210413_models.DeleteIncidentRequest,
    ) -> gemp20210413_models.DeleteIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_incident_with_options(request, headers, runtime)

    async def delete_incident_async(
        self,
        request: gemp20210413_models.DeleteIncidentRequest,
    ) -> gemp20210413_models.DeleteIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_incident_with_options_async(request, headers, runtime)

    def delete_integration_config_with_options(
        self,
        request: gemp20210413_models.DeleteIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_integration_config_with_options_async(
        self,
        request: gemp20210413_models.DeleteIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteIntegrationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_integration_config(
        self,
        request: gemp20210413_models.DeleteIntegrationConfigRequest,
    ) -> gemp20210413_models.DeleteIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_integration_config_with_options(request, headers, runtime)

    async def delete_integration_config_async(
        self,
        request: gemp20210413_models.DeleteIntegrationConfigRequest,
    ) -> gemp20210413_models.DeleteIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_integration_config_with_options_async(request, headers, runtime)

    def delete_problem_with_options(
        self,
        request: gemp20210413_models.DeleteProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_problem_with_options_async(
        self,
        request: gemp20210413_models.DeleteProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_problem(
        self,
        request: gemp20210413_models.DeleteProblemRequest,
    ) -> gemp20210413_models.DeleteProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_with_options(request, headers, runtime)

    async def delete_problem_async(
        self,
        request: gemp20210413_models.DeleteProblemRequest,
    ) -> gemp20210413_models.DeleteProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_problem_with_options_async(request, headers, runtime)

    def delete_problem_effection_service_with_options(
        self,
        request: gemp20210413_models.DeleteProblemEffectionServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteProblemEffectionServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effection_service_id):
            body['effectionServiceId'] = request.effection_service_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/effectionService/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemEffectionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_problem_effection_service_with_options_async(
        self,
        request: gemp20210413_models.DeleteProblemEffectionServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteProblemEffectionServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effection_service_id):
            body['effectionServiceId'] = request.effection_service_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/effectionService/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemEffectionServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_problem_effection_service(
        self,
        request: gemp20210413_models.DeleteProblemEffectionServiceRequest,
    ) -> gemp20210413_models.DeleteProblemEffectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_effection_service_with_options(request, headers, runtime)

    async def delete_problem_effection_service_async(
        self,
        request: gemp20210413_models.DeleteProblemEffectionServiceRequest,
    ) -> gemp20210413_models.DeleteProblemEffectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_problem_effection_service_with_options_async(request, headers, runtime)

    def delete_problem_measure_with_options(
        self,
        request: gemp20210413_models.DeleteProblemMeasureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteProblemMeasureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.measure_id):
            body['measureId'] = request.measure_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblemMeasure',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/measure/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_problem_measure_with_options_async(
        self,
        request: gemp20210413_models.DeleteProblemMeasureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteProblemMeasureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.measure_id):
            body['measureId'] = request.measure_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblemMeasure',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/measure/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemMeasureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_problem_measure(
        self,
        request: gemp20210413_models.DeleteProblemMeasureRequest,
    ) -> gemp20210413_models.DeleteProblemMeasureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_measure_with_options(request, headers, runtime)

    async def delete_problem_measure_async(
        self,
        request: gemp20210413_models.DeleteProblemMeasureRequest,
    ) -> gemp20210413_models.DeleteProblemMeasureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_problem_measure_with_options_async(request, headers, runtime)

    def delete_problem_timeline_with_options(
        self,
        request: gemp20210413_models.DeleteProblemTimelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteProblemTimelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_timeline_id):
            body['problemTimelineId'] = request.problem_timeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblemTimeline',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/timeline/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_problem_timeline_with_options_async(
        self,
        request: gemp20210413_models.DeleteProblemTimelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteProblemTimelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_timeline_id):
            body['problemTimelineId'] = request.problem_timeline_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProblemTimeline',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/timeline/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteProblemTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_problem_timeline(
        self,
        request: gemp20210413_models.DeleteProblemTimelineRequest,
    ) -> gemp20210413_models.DeleteProblemTimelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_problem_timeline_with_options(request, headers, runtime)

    async def delete_problem_timeline_async(
        self,
        request: gemp20210413_models.DeleteProblemTimelineRequest,
    ) -> gemp20210413_models.DeleteProblemTimelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_problem_timeline_with_options_async(request, headers, runtime)

    def delete_route_rule_with_options(
        self,
        request: gemp20210413_models.DeleteRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_route_rule_with_options_async(
        self,
        request: gemp20210413_models.DeleteRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_route_rule(
        self,
        request: gemp20210413_models.DeleteRouteRuleRequest,
    ) -> gemp20210413_models.DeleteRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_route_rule_with_options(request, headers, runtime)

    async def delete_route_rule_async(
        self,
        request: gemp20210413_models.DeleteRouteRuleRequest,
    ) -> gemp20210413_models.DeleteRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_route_rule_with_options_async(request, headers, runtime)

    def delete_service_with_options(
        self,
        request: gemp20210413_models.DeleteServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        request: gemp20210413_models.DeleteServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        request: gemp20210413_models.DeleteServiceRequest,
    ) -> gemp20210413_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_with_options(request, headers, runtime)

    async def delete_service_async(
        self,
        request: gemp20210413_models.DeleteServiceRequest,
    ) -> gemp20210413_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_with_options_async(request, headers, runtime)

    def delete_service_group_with_options(
        self,
        request: gemp20210413_models.DeleteServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_group_with_options_async(
        self,
        request: gemp20210413_models.DeleteServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_group(
        self,
        request: gemp20210413_models.DeleteServiceGroupRequest,
    ) -> gemp20210413_models.DeleteServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_group_with_options(request, headers, runtime)

    async def delete_service_group_async(
        self,
        request: gemp20210413_models.DeleteServiceGroupRequest,
    ) -> gemp20210413_models.DeleteServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_group_with_options_async(request, headers, runtime)

    def delete_service_group_scheduling_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteServiceGroupSchedulingResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_group_scheduling_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteServiceGroupSchedulingResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='DeleteServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupSchedulingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_group_scheduling(self) -> gemp20210413_models.DeleteServiceGroupSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_group_scheduling_with_options(headers, runtime)

    async def delete_service_group_scheduling_async(self) -> gemp20210413_models.DeleteServiceGroupSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_group_scheduling_with_options_async(headers, runtime)

    def delete_service_group_user_with_options(
        self,
        request: gemp20210413_models.DeleteServiceGroupUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteServiceGroupUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.new_user_id):
            body['newUserId'] = request.new_user_id
        if not UtilClient.is_unset(request.old_user_id):
            body['oldUserId'] = request.old_user_id
        if not UtilClient.is_unset(request.remove_user):
            body['removeUser'] = request.remove_user
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceGroupUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/deleteServiceGroupUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_group_user_with_options_async(
        self,
        request: gemp20210413_models.DeleteServiceGroupUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteServiceGroupUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.new_user_id):
            body['newUserId'] = request.new_user_id
        if not UtilClient.is_unset(request.old_user_id):
            body['oldUserId'] = request.old_user_id
        if not UtilClient.is_unset(request.remove_user):
            body['removeUser'] = request.remove_user
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteServiceGroupUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/deleteServiceGroupUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteServiceGroupUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_group_user(
        self,
        request: gemp20210413_models.DeleteServiceGroupUserRequest,
    ) -> gemp20210413_models.DeleteServiceGroupUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_service_group_user_with_options(request, headers, runtime)

    async def delete_service_group_user_async(
        self,
        request: gemp20210413_models.DeleteServiceGroupUserRequest,
    ) -> gemp20210413_models.DeleteServiceGroupUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_service_group_user_with_options_async(request, headers, runtime)

    def delete_subscription_with_options(
        self,
        request: gemp20210413_models.DeleteSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_subscription_with_options_async(
        self,
        request: gemp20210413_models.DeleteSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_subscription(
        self,
        request: gemp20210413_models.DeleteSubscriptionRequest,
    ) -> gemp20210413_models.DeleteSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_subscription_with_options(request, headers, runtime)

    async def delete_subscription_async(
        self,
        request: gemp20210413_models.DeleteSubscriptionRequest,
    ) -> gemp20210413_models.DeleteSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_subscription_with_options_async(request, headers, runtime)

    def delete_user_with_options(
        self,
        request: gemp20210413_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_user_with_options_async(
        self,
        request: gemp20210413_models.DeleteUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeleteUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/delete',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeleteUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_user(
        self,
        request: gemp20210413_models.DeleteUserRequest,
    ) -> gemp20210413_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.delete_user_with_options(request, headers, runtime)

    async def delete_user_async(
        self,
        request: gemp20210413_models.DeleteUserRequest,
    ) -> gemp20210413_models.DeleteUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.delete_user_with_options_async(request, headers, runtime)

    def deliver_incident_with_options(
        self,
        request: gemp20210413_models.DeliverIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeliverIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_user_id):
            body['assignUserId'] = request.assign_user_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeliverIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/deliver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeliverIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def deliver_incident_with_options_async(
        self,
        request: gemp20210413_models.DeliverIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DeliverIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_user_id):
            body['assignUserId'] = request.assign_user_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeliverIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/deliver',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DeliverIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deliver_incident(
        self,
        request: gemp20210413_models.DeliverIncidentRequest,
    ) -> gemp20210413_models.DeliverIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.deliver_incident_with_options(request, headers, runtime)

    async def deliver_incident_async(
        self,
        request: gemp20210413_models.DeliverIncidentRequest,
    ) -> gemp20210413_models.DeliverIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.deliver_incident_with_options_async(request, headers, runtime)

    def disable_escalation_plan_with_options(
        self,
        request: gemp20210413_models.DisableEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_escalation_plan_with_options_async(
        self,
        request: gemp20210413_models.DisableEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableEscalationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_escalation_plan(
        self,
        request: gemp20210413_models.DisableEscalationPlanRequest,
    ) -> gemp20210413_models.DisableEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_escalation_plan_with_options(request, headers, runtime)

    async def disable_escalation_plan_async(
        self,
        request: gemp20210413_models.DisableEscalationPlanRequest,
    ) -> gemp20210413_models.DisableEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_escalation_plan_with_options_async(request, headers, runtime)

    def disable_integration_config_with_options(
        self,
        request: gemp20210413_models.DisableIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_integration_config_with_options_async(
        self,
        request: gemp20210413_models.DisableIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableIntegrationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_integration_config(
        self,
        request: gemp20210413_models.DisableIntegrationConfigRequest,
    ) -> gemp20210413_models.DisableIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_integration_config_with_options(request, headers, runtime)

    async def disable_integration_config_async(
        self,
        request: gemp20210413_models.DisableIntegrationConfigRequest,
    ) -> gemp20210413_models.DisableIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_integration_config_with_options_async(request, headers, runtime)

    def disable_route_rule_with_options(
        self,
        request: gemp20210413_models.DisableRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_route_rule_with_options_async(
        self,
        request: gemp20210413_models.DisableRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/disable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_route_rule(
        self,
        request: gemp20210413_models.DisableRouteRuleRequest,
    ) -> gemp20210413_models.DisableRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_route_rule_with_options(request, headers, runtime)

    async def disable_route_rule_async(
        self,
        request: gemp20210413_models.DisableRouteRuleRequest,
    ) -> gemp20210413_models.DisableRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_route_rule_with_options_async(request, headers, runtime)

    def disable_service_group_webhook_with_options(
        self,
        request: gemp20210413_models.DisableServiceGroupWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableServiceGroupWebhookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableServiceGroupWebhook',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/disableWebhook',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableServiceGroupWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_service_group_webhook_with_options_async(
        self,
        request: gemp20210413_models.DisableServiceGroupWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableServiceGroupWebhookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableServiceGroupWebhook',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/disableWebhook',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableServiceGroupWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_service_group_webhook(
        self,
        request: gemp20210413_models.DisableServiceGroupWebhookRequest,
    ) -> gemp20210413_models.DisableServiceGroupWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_service_group_webhook_with_options(request, headers, runtime)

    async def disable_service_group_webhook_async(
        self,
        request: gemp20210413_models.DisableServiceGroupWebhookRequest,
    ) -> gemp20210413_models.DisableServiceGroupWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_service_group_webhook_with_options_async(request, headers, runtime)

    def disable_subscription_with_options(
        self,
        request: gemp20210413_models.DisableSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/doDisable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_subscription_with_options_async(
        self,
        request: gemp20210413_models.DisableSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.DisableSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DisableSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/doDisable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.DisableSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_subscription(
        self,
        request: gemp20210413_models.DisableSubscriptionRequest,
    ) -> gemp20210413_models.DisableSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.disable_subscription_with_options(request, headers, runtime)

    async def disable_subscription_async(
        self,
        request: gemp20210413_models.DisableSubscriptionRequest,
    ) -> gemp20210413_models.DisableSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.disable_subscription_with_options_async(request, headers, runtime)

    def enable_escalation_plan_with_options(
        self,
        request: gemp20210413_models.EnableEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_escalation_plan_with_options_async(
        self,
        request: gemp20210413_models.EnableEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableEscalationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_escalation_plan(
        self,
        request: gemp20210413_models.EnableEscalationPlanRequest,
    ) -> gemp20210413_models.EnableEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_escalation_plan_with_options(request, headers, runtime)

    async def enable_escalation_plan_async(
        self,
        request: gemp20210413_models.EnableEscalationPlanRequest,
    ) -> gemp20210413_models.EnableEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_escalation_plan_with_options_async(request, headers, runtime)

    def enable_integration_config_with_options(
        self,
        request: gemp20210413_models.EnableIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_integration_config_with_options_async(
        self,
        request: gemp20210413_models.EnableIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableIntegrationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_integration_config(
        self,
        request: gemp20210413_models.EnableIntegrationConfigRequest,
    ) -> gemp20210413_models.EnableIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_integration_config_with_options(request, headers, runtime)

    async def enable_integration_config_async(
        self,
        request: gemp20210413_models.EnableIntegrationConfigRequest,
    ) -> gemp20210413_models.EnableIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_integration_config_with_options_async(request, headers, runtime)

    def enable_route_rule_with_options(
        self,
        request: gemp20210413_models.EnableRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_route_rule_with_options_async(
        self,
        request: gemp20210413_models.EnableRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_route_rule(
        self,
        request: gemp20210413_models.EnableRouteRuleRequest,
    ) -> gemp20210413_models.EnableRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_route_rule_with_options(request, headers, runtime)

    async def enable_route_rule_async(
        self,
        request: gemp20210413_models.EnableRouteRuleRequest,
    ) -> gemp20210413_models.EnableRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_route_rule_with_options_async(request, headers, runtime)

    def enable_service_group_webhook_with_options(
        self,
        request: gemp20210413_models.EnableServiceGroupWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableServiceGroupWebhookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableServiceGroupWebhook',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/enableWebhook',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableServiceGroupWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_service_group_webhook_with_options_async(
        self,
        request: gemp20210413_models.EnableServiceGroupWebhookRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableServiceGroupWebhookResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableServiceGroupWebhook',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/enableWebhook',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableServiceGroupWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_service_group_webhook(
        self,
        request: gemp20210413_models.EnableServiceGroupWebhookRequest,
    ) -> gemp20210413_models.EnableServiceGroupWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_service_group_webhook_with_options(request, headers, runtime)

    async def enable_service_group_webhook_async(
        self,
        request: gemp20210413_models.EnableServiceGroupWebhookRequest,
    ) -> gemp20210413_models.EnableServiceGroupWebhookResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_service_group_webhook_with_options_async(request, headers, runtime)

    def enable_subscription_with_options(
        self,
        request: gemp20210413_models.EnableSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_subscription_with_options_async(
        self,
        request: gemp20210413_models.EnableSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.EnableSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='EnableSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/enable',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.EnableSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_subscription(
        self,
        request: gemp20210413_models.EnableSubscriptionRequest,
    ) -> gemp20210413_models.EnableSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.enable_subscription_with_options(request, headers, runtime)

    async def enable_subscription_async(
        self,
        request: gemp20210413_models.EnableSubscriptionRequest,
    ) -> gemp20210413_models.EnableSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.enable_subscription_with_options_async(request, headers, runtime)

    def finish_incident_with_options(
        self,
        request: gemp20210413_models.FinishIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.FinishIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_finish_reason):
            body['incidentFinishReason'] = request.incident_finish_reason
        if not UtilClient.is_unset(request.incident_finish_reason_description):
            body['incidentFinishReasonDescription'] = request.incident_finish_reason_description
        if not UtilClient.is_unset(request.incident_finish_solution):
            body['incidentFinishSolution'] = request.incident_finish_solution
        if not UtilClient.is_unset(request.incident_finish_solution_description):
            body['incidentFinishSolutionDescription'] = request.incident_finish_solution_description
        if not UtilClient.is_unset(request.incident_ids):
            body['incidentIds'] = request.incident_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/finish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.FinishIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_incident_with_options_async(
        self,
        request: gemp20210413_models.FinishIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.FinishIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_finish_reason):
            body['incidentFinishReason'] = request.incident_finish_reason
        if not UtilClient.is_unset(request.incident_finish_reason_description):
            body['incidentFinishReasonDescription'] = request.incident_finish_reason_description
        if not UtilClient.is_unset(request.incident_finish_solution):
            body['incidentFinishSolution'] = request.incident_finish_solution
        if not UtilClient.is_unset(request.incident_finish_solution_description):
            body['incidentFinishSolutionDescription'] = request.incident_finish_solution_description
        if not UtilClient.is_unset(request.incident_ids):
            body['incidentIds'] = request.incident_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/finish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.FinishIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_incident(
        self,
        request: gemp20210413_models.FinishIncidentRequest,
    ) -> gemp20210413_models.FinishIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.finish_incident_with_options(request, headers, runtime)

    async def finish_incident_async(
        self,
        request: gemp20210413_models.FinishIncidentRequest,
    ) -> gemp20210413_models.FinishIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.finish_incident_with_options_async(request, headers, runtime)

    def finish_problem_with_options(
        self,
        request: gemp20210413_models.FinishProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.FinishProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/finish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.FinishProblemResponse(),
            self.call_api(params, req, runtime)
        )

    async def finish_problem_with_options_async(
        self,
        request: gemp20210413_models.FinishProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.FinishProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='FinishProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/finish',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.FinishProblemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def finish_problem(
        self,
        request: gemp20210413_models.FinishProblemRequest,
    ) -> gemp20210413_models.FinishProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.finish_problem_with_options(request, headers, runtime)

    async def finish_problem_async(
        self,
        request: gemp20210413_models.FinishProblemRequest,
    ) -> gemp20210413_models.FinishProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.finish_problem_with_options_async(request, headers, runtime)

    def generate_picture_link_with_options(
        self,
        request: gemp20210413_models.GeneratePictureLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GeneratePictureLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GeneratePictureLink',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/oss/getPictureLink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GeneratePictureLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_picture_link_with_options_async(
        self,
        request: gemp20210413_models.GeneratePictureLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GeneratePictureLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GeneratePictureLink',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/oss/getPictureLink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GeneratePictureLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_picture_link(
        self,
        request: gemp20210413_models.GeneratePictureLinkRequest,
    ) -> gemp20210413_models.GeneratePictureLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_picture_link_with_options(request, headers, runtime)

    async def generate_picture_link_async(
        self,
        request: gemp20210413_models.GeneratePictureLinkRequest,
    ) -> gemp20210413_models.GeneratePictureLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_picture_link_with_options_async(request, headers, runtime)

    def generate_picture_upload_sign_with_options(
        self,
        request: gemp20210413_models.GeneratePictureUploadSignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GeneratePictureUploadSignResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GeneratePictureUploadSign',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/oss/generatePostPolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GeneratePictureUploadSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_picture_upload_sign_with_options_async(
        self,
        request: gemp20210413_models.GeneratePictureUploadSignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GeneratePictureUploadSignResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.files):
            body['files'] = request.files
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GeneratePictureUploadSign',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/oss/generatePostPolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GeneratePictureUploadSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_picture_upload_sign(
        self,
        request: gemp20210413_models.GeneratePictureUploadSignRequest,
    ) -> gemp20210413_models.GeneratePictureUploadSignResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_picture_upload_sign_with_options(request, headers, runtime)

    async def generate_picture_upload_sign_async(
        self,
        request: gemp20210413_models.GeneratePictureUploadSignRequest,
    ) -> gemp20210413_models.GeneratePictureUploadSignResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_picture_upload_sign_with_options_async(request, headers, runtime)

    def generate_problem_picture_link_with_options(
        self,
        request: gemp20210413_models.GenerateProblemPictureLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GenerateProblemPictureLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateProblemPictureLink',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/oss/getPresignedLink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GenerateProblemPictureLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_problem_picture_link_with_options_async(
        self,
        request: gemp20210413_models.GenerateProblemPictureLinkRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GenerateProblemPictureLinkResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.keys):
            body['keys'] = request.keys
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateProblemPictureLink',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/oss/getPresignedLink',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GenerateProblemPictureLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_problem_picture_link(
        self,
        request: gemp20210413_models.GenerateProblemPictureLinkRequest,
    ) -> gemp20210413_models.GenerateProblemPictureLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_problem_picture_link_with_options(request, headers, runtime)

    async def generate_problem_picture_link_async(
        self,
        request: gemp20210413_models.GenerateProblemPictureLinkRequest,
    ) -> gemp20210413_models.GenerateProblemPictureLinkResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_problem_picture_link_with_options_async(request, headers, runtime)

    def generate_problem_picture_upload_sign_with_options(
        self,
        request: gemp20210413_models.GenerateProblemPictureUploadSignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GenerateProblemPictureUploadSignResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_size):
            body['fileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_type):
            body['fileType'] = request.file_type
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateProblemPictureUploadSign',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/oss/generatePostPolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GenerateProblemPictureUploadSignResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_problem_picture_upload_sign_with_options_async(
        self,
        request: gemp20210413_models.GenerateProblemPictureUploadSignRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GenerateProblemPictureUploadSignResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.file_name):
            body['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_size):
            body['fileSize'] = request.file_size
        if not UtilClient.is_unset(request.file_type):
            body['fileType'] = request.file_type
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateProblemPictureUploadSign',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/oss/generatePostPolicy',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GenerateProblemPictureUploadSignResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_problem_picture_upload_sign(
        self,
        request: gemp20210413_models.GenerateProblemPictureUploadSignRequest,
    ) -> gemp20210413_models.GenerateProblemPictureUploadSignResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.generate_problem_picture_upload_sign_with_options(request, headers, runtime)

    async def generate_problem_picture_upload_sign_async(
        self,
        request: gemp20210413_models.GenerateProblemPictureUploadSignRequest,
    ) -> gemp20210413_models.GenerateProblemPictureUploadSignResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.generate_problem_picture_upload_sign_with_options_async(request, headers, runtime)

    def get_escalation_plan_with_options(
        self,
        request: gemp20210413_models.GetEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_escalation_plan_with_options_async(
        self,
        request: gemp20210413_models.GetEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetEscalationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_escalation_plan(
        self,
        request: gemp20210413_models.GetEscalationPlanRequest,
    ) -> gemp20210413_models.GetEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_escalation_plan_with_options(request, headers, runtime)

    async def get_escalation_plan_async(
        self,
        request: gemp20210413_models.GetEscalationPlanRequest,
    ) -> gemp20210413_models.GetEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_escalation_plan_with_options_async(request, headers, runtime)

    def get_event_with_options(
        self,
        request: gemp20210413_models.GetEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEvent',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/events/getLastTimeEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_event_with_options_async(
        self,
        request: gemp20210413_models.GetEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetEvent',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/events/getLastTimeEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_event(
        self,
        request: gemp20210413_models.GetEventRequest,
    ) -> gemp20210413_models.GetEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_event_with_options(request, headers, runtime)

    async def get_event_async(
        self,
        request: gemp20210413_models.GetEventRequest,
    ) -> gemp20210413_models.GetEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_event_with_options_async(request, headers, runtime)

    def get_home_page_guidance_with_options(
        self,
        request: gemp20210413_models.GetHomePageGuidanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetHomePageGuidanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHomePageGuidance',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/guidance/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetHomePageGuidanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_home_page_guidance_with_options_async(
        self,
        request: gemp20210413_models.GetHomePageGuidanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetHomePageGuidanceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetHomePageGuidance',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/guidance/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetHomePageGuidanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_home_page_guidance(
        self,
        request: gemp20210413_models.GetHomePageGuidanceRequest,
    ) -> gemp20210413_models.GetHomePageGuidanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_home_page_guidance_with_options(request, headers, runtime)

    async def get_home_page_guidance_async(
        self,
        request: gemp20210413_models.GetHomePageGuidanceRequest,
    ) -> gemp20210413_models.GetHomePageGuidanceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_home_page_guidance_with_options_async(request, headers, runtime)

    def get_incident_with_options(
        self,
        request: gemp20210413_models.GetIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_incident_with_options_async(
        self,
        request: gemp20210413_models.GetIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_incident(
        self,
        request: gemp20210413_models.GetIncidentRequest,
    ) -> gemp20210413_models.GetIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_with_options(request, headers, runtime)

    async def get_incident_async(
        self,
        request: gemp20210413_models.GetIncidentRequest,
    ) -> gemp20210413_models.GetIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_incident_with_options_async(request, headers, runtime)

    def get_incident_list_by_id_list_with_options(
        self,
        request: gemp20210413_models.GetIncidentListByIdListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIncidentListByIdListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id_list):
            body['incidentIdList'] = request.incident_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncidentListByIdList',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/getIncidentListByIdList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentListByIdListResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_incident_list_by_id_list_with_options_async(
        self,
        request: gemp20210413_models.GetIncidentListByIdListRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIncidentListByIdListResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id_list):
            body['incidentIdList'] = request.incident_id_list
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncidentListByIdList',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/getIncidentListByIdList',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentListByIdListResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_incident_list_by_id_list(
        self,
        request: gemp20210413_models.GetIncidentListByIdListRequest,
    ) -> gemp20210413_models.GetIncidentListByIdListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_list_by_id_list_with_options(request, headers, runtime)

    async def get_incident_list_by_id_list_async(
        self,
        request: gemp20210413_models.GetIncidentListByIdListRequest,
    ) -> gemp20210413_models.GetIncidentListByIdListResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_incident_list_by_id_list_with_options_async(request, headers, runtime)

    def get_incident_statistics_with_options(
        self,
        request: gemp20210413_models.GetIncidentStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIncidentStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncidentStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/count',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_incident_statistics_with_options_async(
        self,
        request: gemp20210413_models.GetIncidentStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIncidentStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncidentStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/count',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_incident_statistics(
        self,
        request: gemp20210413_models.GetIncidentStatisticsRequest,
    ) -> gemp20210413_models.GetIncidentStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_statistics_with_options(request, headers, runtime)

    async def get_incident_statistics_async(
        self,
        request: gemp20210413_models.GetIncidentStatisticsRequest,
    ) -> gemp20210413_models.GetIncidentStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_incident_statistics_with_options_async(request, headers, runtime)

    def get_incident_subtotal_count_with_options(
        self,
        request: gemp20210413_models.GetIncidentSubtotalCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIncidentSubtotalCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_ids):
            body['incidentIds'] = request.incident_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncidentSubtotalCount',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/subtotal/count',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentSubtotalCountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_incident_subtotal_count_with_options_async(
        self,
        request: gemp20210413_models.GetIncidentSubtotalCountRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIncidentSubtotalCountResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_ids):
            body['incidentIds'] = request.incident_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIncidentSubtotalCount',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/subtotal/count',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIncidentSubtotalCountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_incident_subtotal_count(
        self,
        request: gemp20210413_models.GetIncidentSubtotalCountRequest,
    ) -> gemp20210413_models.GetIncidentSubtotalCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_incident_subtotal_count_with_options(request, headers, runtime)

    async def get_incident_subtotal_count_async(
        self,
        request: gemp20210413_models.GetIncidentSubtotalCountRequest,
    ) -> gemp20210413_models.GetIncidentSubtotalCountResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_incident_subtotal_count_with_options_async(request, headers, runtime)

    def get_integration_config_with_options(
        self,
        request: gemp20210413_models.GetIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_integration_config_with_options_async(
        self,
        request: gemp20210413_models.GetIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetIntegrationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_integration_config(
        self,
        request: gemp20210413_models.GetIntegrationConfigRequest,
    ) -> gemp20210413_models.GetIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_integration_config_with_options(request, headers, runtime)

    async def get_integration_config_async(
        self,
        request: gemp20210413_models.GetIntegrationConfigRequest,
    ) -> gemp20210413_models.GetIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_integration_config_with_options_async(request, headers, runtime)

    def get_problem_with_options(
        self,
        request: gemp20210413_models.GetProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_problem_with_options_async(
        self,
        request: gemp20210413_models.GetProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_problem(
        self,
        request: gemp20210413_models.GetProblemRequest,
    ) -> gemp20210413_models.GetProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_with_options(request, headers, runtime)

    async def get_problem_async(
        self,
        request: gemp20210413_models.GetProblemRequest,
    ) -> gemp20210413_models.GetProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_problem_with_options_async(request, headers, runtime)

    def get_problem_effection_service_with_options(
        self,
        request: gemp20210413_models.GetProblemEffectionServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetProblemEffectionServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effection_service_id):
            body['effectionServiceId'] = request.effection_service_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/effectionService/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemEffectionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_problem_effection_service_with_options_async(
        self,
        request: gemp20210413_models.GetProblemEffectionServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetProblemEffectionServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effection_service_id):
            body['effectionServiceId'] = request.effection_service_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/effectionService/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemEffectionServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_problem_effection_service(
        self,
        request: gemp20210413_models.GetProblemEffectionServiceRequest,
    ) -> gemp20210413_models.GetProblemEffectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_effection_service_with_options(request, headers, runtime)

    async def get_problem_effection_service_async(
        self,
        request: gemp20210413_models.GetProblemEffectionServiceRequest,
    ) -> gemp20210413_models.GetProblemEffectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_problem_effection_service_with_options_async(request, headers, runtime)

    def get_problem_improvement_with_options(
        self,
        request: gemp20210413_models.GetProblemImprovementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetProblemImprovementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblemImprovement',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemImprovementResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_problem_improvement_with_options_async(
        self,
        request: gemp20210413_models.GetProblemImprovementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetProblemImprovementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblemImprovement',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemImprovementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_problem_improvement(
        self,
        request: gemp20210413_models.GetProblemImprovementRequest,
    ) -> gemp20210413_models.GetProblemImprovementResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_improvement_with_options(request, headers, runtime)

    async def get_problem_improvement_async(
        self,
        request: gemp20210413_models.GetProblemImprovementRequest,
    ) -> gemp20210413_models.GetProblemImprovementResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_problem_improvement_with_options_async(request, headers, runtime)

    def get_problem_preview_with_options(
        self,
        request: gemp20210413_models.GetProblemPreviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetProblemPreviewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effect_service_ids):
            body['effectServiceIds'] = request.effect_service_ids
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_level):
            body['problemLevel'] = request.problem_level
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblemPreview',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/preview',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_problem_preview_with_options_async(
        self,
        request: gemp20210413_models.GetProblemPreviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetProblemPreviewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effect_service_ids):
            body['effectServiceIds'] = request.effect_service_ids
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_level):
            body['problemLevel'] = request.problem_level
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProblemPreview',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/preview',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetProblemPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_problem_preview(
        self,
        request: gemp20210413_models.GetProblemPreviewRequest,
    ) -> gemp20210413_models.GetProblemPreviewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_problem_preview_with_options(request, headers, runtime)

    async def get_problem_preview_async(
        self,
        request: gemp20210413_models.GetProblemPreviewRequest,
    ) -> gemp20210413_models.GetProblemPreviewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_problem_preview_with_options_async(request, headers, runtime)

    def get_resource_statistics_with_options(
        self,
        request: gemp20210413_models.GetResourceStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetResourceStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResourceStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/config/resource/count',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetResourceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_statistics_with_options_async(
        self,
        request: gemp20210413_models.GetResourceStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetResourceStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetResourceStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/config/resource/count',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetResourceStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_statistics(
        self,
        request: gemp20210413_models.GetResourceStatisticsRequest,
    ) -> gemp20210413_models.GetResourceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_resource_statistics_with_options(request, headers, runtime)

    async def get_resource_statistics_async(
        self,
        request: gemp20210413_models.GetResourceStatisticsRequest,
    ) -> gemp20210413_models.GetResourceStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_resource_statistics_with_options_async(request, headers, runtime)

    def get_rich_text_with_options(
        self,
        request: gemp20210413_models.GetRichTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetRichTextResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.rich_text_id):
            body['richTextId'] = request.rich_text_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRichText',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetRichTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_rich_text_with_options_async(
        self,
        request: gemp20210413_models.GetRichTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetRichTextResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.rich_text_id):
            body['richTextId'] = request.rich_text_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRichText',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetRichTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_rich_text(
        self,
        request: gemp20210413_models.GetRichTextRequest,
    ) -> gemp20210413_models.GetRichTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_rich_text_with_options(request, headers, runtime)

    async def get_rich_text_async(
        self,
        request: gemp20210413_models.GetRichTextRequest,
    ) -> gemp20210413_models.GetRichTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_rich_text_with_options_async(request, headers, runtime)

    def get_route_rule_with_options(
        self,
        request: gemp20210413_models.GetRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_route_rule_with_options_async(
        self,
        request: gemp20210413_models.GetRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_route_rule(
        self,
        request: gemp20210413_models.GetRouteRuleRequest,
    ) -> gemp20210413_models.GetRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_route_rule_with_options(request, headers, runtime)

    async def get_route_rule_async(
        self,
        request: gemp20210413_models.GetRouteRuleRequest,
    ) -> gemp20210413_models.GetRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_route_rule_with_options_async(request, headers, runtime)

    def get_service_with_options(
        self,
        request: gemp20210413_models.GetServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        request: gemp20210413_models.GetServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        request: gemp20210413_models.GetServiceRequest,
    ) -> gemp20210413_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_with_options(request, headers, runtime)

    async def get_service_async(
        self,
        request: gemp20210413_models.GetServiceRequest,
    ) -> gemp20210413_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_with_options_async(request, headers, runtime)

    def get_service_group_with_options(
        self,
        request: gemp20210413_models.GetServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_group_with_options_async(
        self,
        request: gemp20210413_models.GetServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_group(
        self,
        request: gemp20210413_models.GetServiceGroupRequest,
    ) -> gemp20210413_models.GetServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_with_options(request, headers, runtime)

    async def get_service_group_async(
        self,
        request: gemp20210413_models.GetServiceGroupRequest,
    ) -> gemp20210413_models.GetServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_group_with_options_async(request, headers, runtime)

    def get_service_group_person_scheduling_with_options(
        self,
        request: gemp20210413_models.GetServiceGroupPersonSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupPersonSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupPersonScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/user/getScheduling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupPersonSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_group_person_scheduling_with_options_async(
        self,
        request: gemp20210413_models.GetServiceGroupPersonSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupPersonSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupPersonScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/user/getScheduling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupPersonSchedulingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_group_person_scheduling(
        self,
        request: gemp20210413_models.GetServiceGroupPersonSchedulingRequest,
    ) -> gemp20210413_models.GetServiceGroupPersonSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_person_scheduling_with_options(request, headers, runtime)

    async def get_service_group_person_scheduling_async(
        self,
        request: gemp20210413_models.GetServiceGroupPersonSchedulingRequest,
    ) -> gemp20210413_models.GetServiceGroupPersonSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_group_person_scheduling_with_options_async(request, headers, runtime)

    def get_service_group_scheduling_with_options(
        self,
        request: gemp20210413_models.GetServiceGroupSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_group_scheduling_with_options_async(
        self,
        request: gemp20210413_models.GetServiceGroupSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSchedulingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_group_scheduling(
        self,
        request: gemp20210413_models.GetServiceGroupSchedulingRequest,
    ) -> gemp20210413_models.GetServiceGroupSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_scheduling_with_options(request, headers, runtime)

    async def get_service_group_scheduling_async(
        self,
        request: gemp20210413_models.GetServiceGroupSchedulingRequest,
    ) -> gemp20210413_models.GetServiceGroupSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_group_scheduling_with_options_async(request, headers, runtime)

    def get_service_group_scheduling_preview_with_options(
        self,
        request: gemp20210413_models.GetServiceGroupSchedulingPreviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupSchedulingPreviewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.fast_scheduling):
            body['fastScheduling'] = request.fast_scheduling
        if not UtilClient.is_unset(request.fine_scheduling):
            body['fineScheduling'] = request.fine_scheduling
        if not UtilClient.is_unset(request.scheduling_way):
            body['schedulingWay'] = request.scheduling_way
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupSchedulingPreview',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/preview',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSchedulingPreviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_group_scheduling_preview_with_options_async(
        self,
        request: gemp20210413_models.GetServiceGroupSchedulingPreviewRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupSchedulingPreviewResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.fast_scheduling):
            body['fastScheduling'] = request.fast_scheduling
        if not UtilClient.is_unset(request.fine_scheduling):
            body['fineScheduling'] = request.fine_scheduling
        if not UtilClient.is_unset(request.scheduling_way):
            body['schedulingWay'] = request.scheduling_way
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupSchedulingPreview',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/preview',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSchedulingPreviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_group_scheduling_preview(
        self,
        request: gemp20210413_models.GetServiceGroupSchedulingPreviewRequest,
    ) -> gemp20210413_models.GetServiceGroupSchedulingPreviewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_scheduling_preview_with_options(request, headers, runtime)

    async def get_service_group_scheduling_preview_async(
        self,
        request: gemp20210413_models.GetServiceGroupSchedulingPreviewRequest,
    ) -> gemp20210413_models.GetServiceGroupSchedulingPreviewResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_group_scheduling_preview_with_options_async(request, headers, runtime)

    def get_service_group_special_person_scheduling_with_options(
        self,
        request: gemp20210413_models.GetServiceGroupSpecialPersonSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupSpecialPersonSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupSpecialPersonScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/getUserScheduling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSpecialPersonSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_group_special_person_scheduling_with_options_async(
        self,
        request: gemp20210413_models.GetServiceGroupSpecialPersonSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetServiceGroupSpecialPersonSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetServiceGroupSpecialPersonScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/getUserScheduling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetServiceGroupSpecialPersonSchedulingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_group_special_person_scheduling(
        self,
        request: gemp20210413_models.GetServiceGroupSpecialPersonSchedulingRequest,
    ) -> gemp20210413_models.GetServiceGroupSpecialPersonSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_service_group_special_person_scheduling_with_options(request, headers, runtime)

    async def get_service_group_special_person_scheduling_async(
        self,
        request: gemp20210413_models.GetServiceGroupSpecialPersonSchedulingRequest,
    ) -> gemp20210413_models.GetServiceGroupSpecialPersonSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_service_group_special_person_scheduling_with_options_async(request, headers, runtime)

    def get_similar_incident_statistics_with_options(
        self,
        request: gemp20210413_models.GetSimilarIncidentStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetSimilarIncidentStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time):
            body['createTime'] = request.create_time
        if not UtilClient.is_unset(request.events):
            body['events'] = request.events
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.incident_title):
            body['incidentTitle'] = request.incident_title
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSimilarIncidentStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/similarIncident/statistics',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetSimilarIncidentStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_similar_incident_statistics_with_options_async(
        self,
        request: gemp20210413_models.GetSimilarIncidentStatisticsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetSimilarIncidentStatisticsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time):
            body['createTime'] = request.create_time
        if not UtilClient.is_unset(request.events):
            body['events'] = request.events
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.incident_title):
            body['incidentTitle'] = request.incident_title
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSimilarIncidentStatistics',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/similarIncident/statistics',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetSimilarIncidentStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_similar_incident_statistics(
        self,
        request: gemp20210413_models.GetSimilarIncidentStatisticsRequest,
    ) -> gemp20210413_models.GetSimilarIncidentStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_similar_incident_statistics_with_options(request, headers, runtime)

    async def get_similar_incident_statistics_async(
        self,
        request: gemp20210413_models.GetSimilarIncidentStatisticsRequest,
    ) -> gemp20210413_models.GetSimilarIncidentStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_similar_incident_statistics_with_options_async(request, headers, runtime)

    def get_subscription_with_options(
        self,
        request: gemp20210413_models.GetSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.not_filter_scope_object_deleted):
            body['notFilterScopeObjectDeleted'] = request.not_filter_scope_object_deleted
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_subscription_with_options_async(
        self,
        request: gemp20210413_models.GetSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.not_filter_scope_object_deleted):
            body['notFilterScopeObjectDeleted'] = request.not_filter_scope_object_deleted
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_subscription(
        self,
        request: gemp20210413_models.GetSubscriptionRequest,
    ) -> gemp20210413_models.GetSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_subscription_with_options(request, headers, runtime)

    async def get_subscription_async(
        self,
        request: gemp20210413_models.GetSubscriptionRequest,
    ) -> gemp20210413_models.GetSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_subscription_with_options_async(request, headers, runtime)

    def get_tenant_application_with_options(
        self,
        request: gemp20210413_models.GetTenantApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetTenantApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTenantApplication',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/mobileApp/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetTenantApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tenant_application_with_options_async(
        self,
        request: gemp20210413_models.GetTenantApplicationRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetTenantApplicationResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTenantApplication',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/mobileApp/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetTenantApplicationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tenant_application(
        self,
        request: gemp20210413_models.GetTenantApplicationRequest,
    ) -> gemp20210413_models.GetTenantApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tenant_application_with_options(request, headers, runtime)

    async def get_tenant_application_async(
        self,
        request: gemp20210413_models.GetTenantApplicationRequest,
    ) -> gemp20210413_models.GetTenantApplicationResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_tenant_application_with_options_async(request, headers, runtime)

    def get_tenant_status_with_options(
        self,
        request: gemp20210413_models.GetTenantStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetTenantStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tenant_ram_id):
            body['tenantRamId'] = request.tenant_ram_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTenantStatus',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/tenant/getTenantStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetTenantStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tenant_status_with_options_async(
        self,
        request: gemp20210413_models.GetTenantStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetTenantStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.tenant_ram_id):
            body['tenantRamId'] = request.tenant_ram_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTenantStatus',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/tenant/getTenantStatus',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetTenantStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tenant_status(
        self,
        request: gemp20210413_models.GetTenantStatusRequest,
    ) -> gemp20210413_models.GetTenantStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_tenant_status_with_options(request, headers, runtime)

    async def get_tenant_status_async(
        self,
        request: gemp20210413_models.GetTenantStatusRequest,
    ) -> gemp20210413_models.GetTenantStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_tenant_status_with_options_async(request, headers, runtime)

    def get_user_with_options(
        self,
        request: gemp20210413_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/getUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: gemp20210413_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/getUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: gemp20210413_models.GetUserRequest,
    ) -> gemp20210413_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: gemp20210413_models.GetUserRequest,
    ) -> gemp20210413_models.GetUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(request, headers, runtime)

    def get_user_guide_status_with_options(
        self,
        request: gemp20210413_models.GetUserGuideStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetUserGuideStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserGuideStatus',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/guide/status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetUserGuideStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_guide_status_with_options_async(
        self,
        request: gemp20210413_models.GetUserGuideStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.GetUserGuideStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserGuideStatus',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/guide/status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.GetUserGuideStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_guide_status(
        self,
        request: gemp20210413_models.GetUserGuideStatusRequest,
    ) -> gemp20210413_models.GetUserGuideStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_user_guide_status_with_options(request, headers, runtime)

    async def get_user_guide_status_async(
        self,
        request: gemp20210413_models.GetUserGuideStatusRequest,
    ) -> gemp20210413_models.GetUserGuideStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_user_guide_status_with_options_async(request, headers, runtime)

    def list_alerts_with_options(
        self,
        request: gemp20210413_models.ListAlertsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListAlertsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_level):
            body['alertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_name):
            body['alertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_source_name):
            body['alertSourceName'] = request.alert_source_name
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlerts',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/alerts/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_alerts_with_options_async(
        self,
        request: gemp20210413_models.ListAlertsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListAlertsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_level):
            body['alertLevel'] = request.alert_level
        if not UtilClient.is_unset(request.alert_name):
            body['alertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_source_name):
            body['alertSourceName'] = request.alert_source_name
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAlerts',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/alerts/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_alerts(
        self,
        request: gemp20210413_models.ListAlertsRequest,
    ) -> gemp20210413_models.ListAlertsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_alerts_with_options(request, headers, runtime)

    async def list_alerts_async(
        self,
        request: gemp20210413_models.ListAlertsRequest,
    ) -> gemp20210413_models.ListAlertsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_alerts_with_options_async(request, headers, runtime)

    def list_by_monitor_source_id_with_options(
        self,
        request: gemp20210413_models.ListByMonitorSourceIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListByMonitorSourceIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListByMonitorSourceId',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/listByMonitorSourceId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListByMonitorSourceIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_by_monitor_source_id_with_options_async(
        self,
        request: gemp20210413_models.ListByMonitorSourceIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListByMonitorSourceIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListByMonitorSourceId',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/listByMonitorSourceId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListByMonitorSourceIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_by_monitor_source_id(
        self,
        request: gemp20210413_models.ListByMonitorSourceIdRequest,
    ) -> gemp20210413_models.ListByMonitorSourceIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_by_monitor_source_id_with_options(request, headers, runtime)

    async def list_by_monitor_source_id_async(
        self,
        request: gemp20210413_models.ListByMonitorSourceIdRequest,
    ) -> gemp20210413_models.ListByMonitorSourceIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_by_monitor_source_id_with_options_async(request, headers, runtime)

    def list_chart_data_for_service_group_with_options(
        self,
        request: gemp20210413_models.ListChartDataForServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListChartDataForServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListChartDataForServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/statistics/chartDataForServiceGroup/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListChartDataForServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chart_data_for_service_group_with_options_async(
        self,
        request: gemp20210413_models.ListChartDataForServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListChartDataForServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListChartDataForServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/statistics/chartDataForServiceGroup/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListChartDataForServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chart_data_for_service_group(
        self,
        request: gemp20210413_models.ListChartDataForServiceGroupRequest,
    ) -> gemp20210413_models.ListChartDataForServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_chart_data_for_service_group_with_options(request, headers, runtime)

    async def list_chart_data_for_service_group_async(
        self,
        request: gemp20210413_models.ListChartDataForServiceGroupRequest,
    ) -> gemp20210413_models.ListChartDataForServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_chart_data_for_service_group_with_options_async(request, headers, runtime)

    def list_chart_data_for_user_with_options(
        self,
        request: gemp20210413_models.ListChartDataForUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListChartDataForUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListChartDataForUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/statistics/chartDataForUser/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListChartDataForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_chart_data_for_user_with_options_async(
        self,
        request: gemp20210413_models.ListChartDataForUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListChartDataForUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListChartDataForUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/statistics/chartDataForUser/',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListChartDataForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_chart_data_for_user(
        self,
        request: gemp20210413_models.ListChartDataForUserRequest,
    ) -> gemp20210413_models.ListChartDataForUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_chart_data_for_user_with_options(request, headers, runtime)

    async def list_chart_data_for_user_async(
        self,
        request: gemp20210413_models.ListChartDataForUserRequest,
    ) -> gemp20210413_models.ListChartDataForUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_chart_data_for_user_with_options_async(request, headers, runtime)

    def list_configs_with_options(
        self,
        request: gemp20210413_models.ListConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigs',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/config/all',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_configs_with_options_async(
        self,
        request: gemp20210413_models.ListConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListConfigs',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/config/all',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_configs(
        self,
        request: gemp20210413_models.ListConfigsRequest,
    ) -> gemp20210413_models.ListConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_configs_with_options(request, headers, runtime)

    async def list_configs_async(
        self,
        request: gemp20210413_models.ListConfigsRequest,
    ) -> gemp20210413_models.ListConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_configs_with_options_async(request, headers, runtime)

    def list_data_report_for_service_group_with_options(
        self,
        request: gemp20210413_models.ListDataReportForServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListDataReportForServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.service_group_name):
            body['serviceGroupName'] = request.service_group_name
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataReportForServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/statistics/listDataReportForServiceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDataReportForServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_report_for_service_group_with_options_async(
        self,
        request: gemp20210413_models.ListDataReportForServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListDataReportForServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.service_group_name):
            body['serviceGroupName'] = request.service_group_name
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataReportForServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/statistics/listDataReportForServiceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDataReportForServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_report_for_service_group(
        self,
        request: gemp20210413_models.ListDataReportForServiceGroupRequest,
    ) -> gemp20210413_models.ListDataReportForServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_report_for_service_group_with_options(request, headers, runtime)

    async def list_data_report_for_service_group_async(
        self,
        request: gemp20210413_models.ListDataReportForServiceGroupRequest,
    ) -> gemp20210413_models.ListDataReportForServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_report_for_service_group_with_options_async(request, headers, runtime)

    def list_data_report_for_user_with_options(
        self,
        request: gemp20210413_models.ListDataReportForUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListDataReportForUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataReportForUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/statistics/listDataReportForUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDataReportForUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_data_report_for_user_with_options_async(
        self,
        request: gemp20210413_models.ListDataReportForUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListDataReportForUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDataReportForUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/statistics/listDataReportForUser',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDataReportForUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_data_report_for_user(
        self,
        request: gemp20210413_models.ListDataReportForUserRequest,
    ) -> gemp20210413_models.ListDataReportForUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_data_report_for_user_with_options(request, headers, runtime)

    async def list_data_report_for_user_async(
        self,
        request: gemp20210413_models.ListDataReportForUserRequest,
    ) -> gemp20210413_models.ListDataReportForUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_data_report_for_user_with_options_async(request, headers, runtime)

    def list_dictionaries_with_options(
        self,
        request: gemp20210413_models.ListDictionariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListDictionariesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDictionaries',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/dict/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDictionariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_dictionaries_with_options_async(
        self,
        request: gemp20210413_models.ListDictionariesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListDictionariesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDictionaries',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/dict/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListDictionariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_dictionaries(
        self,
        request: gemp20210413_models.ListDictionariesRequest,
    ) -> gemp20210413_models.ListDictionariesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_dictionaries_with_options(request, headers, runtime)

    async def list_dictionaries_async(
        self,
        request: gemp20210413_models.ListDictionariesRequest,
    ) -> gemp20210413_models.ListDictionariesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_dictionaries_with_options_async(request, headers, runtime)

    def list_escalation_plan_services_with_options(
        self,
        request: gemp20210413_models.ListEscalationPlanServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListEscalationPlanServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEscalationPlanServices',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlanServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_escalation_plan_services_with_options_async(
        self,
        request: gemp20210413_models.ListEscalationPlanServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListEscalationPlanServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEscalationPlanServices',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/services',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlanServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_escalation_plan_services(
        self,
        request: gemp20210413_models.ListEscalationPlanServicesRequest,
    ) -> gemp20210413_models.ListEscalationPlanServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_escalation_plan_services_with_options(request, headers, runtime)

    async def list_escalation_plan_services_async(
        self,
        request: gemp20210413_models.ListEscalationPlanServicesRequest,
    ) -> gemp20210413_models.ListEscalationPlanServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_escalation_plan_services_with_options_async(request, headers, runtime)

    def list_escalation_plans_with_options(
        self,
        request: gemp20210413_models.ListEscalationPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListEscalationPlansResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_name):
            body['escalationPlanName'] = request.escalation_plan_name
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEscalationPlans',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_escalation_plans_with_options_async(
        self,
        request: gemp20210413_models.ListEscalationPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListEscalationPlansResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_name):
            body['escalationPlanName'] = request.escalation_plan_name
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEscalationPlans',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_escalation_plans(
        self,
        request: gemp20210413_models.ListEscalationPlansRequest,
    ) -> gemp20210413_models.ListEscalationPlansResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_escalation_plans_with_options(request, headers, runtime)

    async def list_escalation_plans_async(
        self,
        request: gemp20210413_models.ListEscalationPlansRequest,
    ) -> gemp20210413_models.ListEscalationPlansResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_escalation_plans_with_options_async(request, headers, runtime)

    def list_escalation_plans_by_notice_object_with_options(
        self,
        request: gemp20210413_models.ListEscalationPlansByNoticeObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListEscalationPlansByNoticeObjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.notice_object_id):
            body['noticeObjectId'] = request.notice_object_id
        if not UtilClient.is_unset(request.notice_object_type):
            body['noticeObjectType'] = request.notice_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEscalationPlansByNoticeObject',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/listByNoticeObject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlansByNoticeObjectResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_escalation_plans_by_notice_object_with_options_async(
        self,
        request: gemp20210413_models.ListEscalationPlansByNoticeObjectRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListEscalationPlansByNoticeObjectResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.notice_object_id):
            body['noticeObjectId'] = request.notice_object_id
        if not UtilClient.is_unset(request.notice_object_type):
            body['noticeObjectType'] = request.notice_object_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEscalationPlansByNoticeObject',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/listByNoticeObject',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListEscalationPlansByNoticeObjectResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_escalation_plans_by_notice_object(
        self,
        request: gemp20210413_models.ListEscalationPlansByNoticeObjectRequest,
    ) -> gemp20210413_models.ListEscalationPlansByNoticeObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_escalation_plans_by_notice_object_with_options(request, headers, runtime)

    async def list_escalation_plans_by_notice_object_async(
        self,
        request: gemp20210413_models.ListEscalationPlansByNoticeObjectRequest,
    ) -> gemp20210413_models.ListEscalationPlansByNoticeObjectResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_escalation_plans_by_notice_object_with_options_async(request, headers, runtime)

    def list_incident_detail_escalation_plans_with_options(
        self,
        request: gemp20210413_models.ListIncidentDetailEscalationPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentDetailEscalationPlansResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentDetailEscalationPlans',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/detail/escalation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentDetailEscalationPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_incident_detail_escalation_plans_with_options_async(
        self,
        request: gemp20210413_models.ListIncidentDetailEscalationPlansRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentDetailEscalationPlansResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentDetailEscalationPlans',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/detail/escalation',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentDetailEscalationPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_incident_detail_escalation_plans(
        self,
        request: gemp20210413_models.ListIncidentDetailEscalationPlansRequest,
    ) -> gemp20210413_models.ListIncidentDetailEscalationPlansResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_detail_escalation_plans_with_options(request, headers, runtime)

    async def list_incident_detail_escalation_plans_async(
        self,
        request: gemp20210413_models.ListIncidentDetailEscalationPlansRequest,
    ) -> gemp20210413_models.ListIncidentDetailEscalationPlansResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_incident_detail_escalation_plans_with_options_async(request, headers, runtime)

    def list_incident_detail_timelines_with_options(
        self,
        request: gemp20210413_models.ListIncidentDetailTimelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentDetailTimelinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.id_sort):
            body['idSort'] = request.id_sort
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentDetailTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/detail/timeline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentDetailTimelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_incident_detail_timelines_with_options_async(
        self,
        request: gemp20210413_models.ListIncidentDetailTimelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentDetailTimelinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.id_sort):
            body['idSort'] = request.id_sort
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentDetailTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/detail/timeline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentDetailTimelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_incident_detail_timelines(
        self,
        request: gemp20210413_models.ListIncidentDetailTimelinesRequest,
    ) -> gemp20210413_models.ListIncidentDetailTimelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_detail_timelines_with_options(request, headers, runtime)

    async def list_incident_detail_timelines_async(
        self,
        request: gemp20210413_models.ListIncidentDetailTimelinesRequest,
    ) -> gemp20210413_models.ListIncidentDetailTimelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_incident_detail_timelines_with_options_async(request, headers, runtime)

    def list_incident_subtotals_with_options(
        self,
        request: gemp20210413_models.ListIncidentSubtotalsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentSubtotalsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentSubtotals',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/list/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentSubtotalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_incident_subtotals_with_options_async(
        self,
        request: gemp20210413_models.ListIncidentSubtotalsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentSubtotalsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentSubtotals',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/list/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentSubtotalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_incident_subtotals(
        self,
        request: gemp20210413_models.ListIncidentSubtotalsRequest,
    ) -> gemp20210413_models.ListIncidentSubtotalsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_subtotals_with_options(request, headers, runtime)

    async def list_incident_subtotals_async(
        self,
        request: gemp20210413_models.ListIncidentSubtotalsRequest,
    ) -> gemp20210413_models.ListIncidentSubtotalsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_incident_subtotals_with_options_async(request, headers, runtime)

    def list_incident_timelines_with_options(
        self,
        request: gemp20210413_models.ListIncidentTimelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentTimelinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/timeline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentTimelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_incident_timelines_with_options_async(
        self,
        request: gemp20210413_models.ListIncidentTimelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentTimelinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidentTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/timeline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentTimelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_incident_timelines(
        self,
        request: gemp20210413_models.ListIncidentTimelinesRequest,
    ) -> gemp20210413_models.ListIncidentTimelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incident_timelines_with_options(request, headers, runtime)

    async def list_incident_timelines_async(
        self,
        request: gemp20210413_models.ListIncidentTimelinesRequest,
    ) -> gemp20210413_models.ListIncidentTimelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_incident_timelines_with_options_async(request, headers, runtime)

    def list_incidents_with_options(
        self,
        request: gemp20210413_models.ListIncidentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_end_time):
            body['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            body['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.effect):
            body['effect'] = request.effect
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.incident_status):
            body['incidentStatus'] = request.incident_status
        if not UtilClient.is_unset(request.me):
            body['me'] = request.me
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.relation_service_id):
            body['relationServiceId'] = request.relation_service_id
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidents',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_incidents_with_options_async(
        self,
        request: gemp20210413_models.ListIncidentsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIncidentsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_end_time):
            body['createEndTime'] = request.create_end_time
        if not UtilClient.is_unset(request.create_start_time):
            body['createStartTime'] = request.create_start_time
        if not UtilClient.is_unset(request.effect):
            body['effect'] = request.effect
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.incident_status):
            body['incidentStatus'] = request.incident_status
        if not UtilClient.is_unset(request.me):
            body['me'] = request.me
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.relation_service_id):
            body['relationServiceId'] = request.relation_service_id
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIncidents',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIncidentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_incidents(
        self,
        request: gemp20210413_models.ListIncidentsRequest,
    ) -> gemp20210413_models.ListIncidentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_incidents_with_options(request, headers, runtime)

    async def list_incidents_async(
        self,
        request: gemp20210413_models.ListIncidentsRequest,
    ) -> gemp20210413_models.ListIncidentsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_incidents_with_options_async(request, headers, runtime)

    def list_integration_config_timelines_with_options(
        self,
        request: gemp20210413_models.ListIntegrationConfigTimelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIntegrationConfigTimelinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntegrationConfigTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/timeline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIntegrationConfigTimelinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_config_timelines_with_options_async(
        self,
        request: gemp20210413_models.ListIntegrationConfigTimelinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIntegrationConfigTimelinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntegrationConfigTimelines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/timeline',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIntegrationConfigTimelinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_config_timelines(
        self,
        request: gemp20210413_models.ListIntegrationConfigTimelinesRequest,
    ) -> gemp20210413_models.ListIntegrationConfigTimelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_config_timelines_with_options(request, headers, runtime)

    async def list_integration_config_timelines_async(
        self,
        request: gemp20210413_models.ListIntegrationConfigTimelinesRequest,
    ) -> gemp20210413_models.ListIntegrationConfigTimelinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_config_timelines_with_options_async(request, headers, runtime)

    def list_integration_configs_with_options(
        self,
        request: gemp20210413_models.ListIntegrationConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIntegrationConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.monitor_source_name):
            body['monitorSourceName'] = request.monitor_source_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntegrationConfigs',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIntegrationConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_integration_configs_with_options_async(
        self,
        request: gemp20210413_models.ListIntegrationConfigsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListIntegrationConfigsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.monitor_source_name):
            body['monitorSourceName'] = request.monitor_source_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListIntegrationConfigs',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListIntegrationConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_integration_configs(
        self,
        request: gemp20210413_models.ListIntegrationConfigsRequest,
    ) -> gemp20210413_models.ListIntegrationConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_integration_configs_with_options(request, headers, runtime)

    async def list_integration_configs_async(
        self,
        request: gemp20210413_models.ListIntegrationConfigsRequest,
    ) -> gemp20210413_models.ListIntegrationConfigsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_integration_configs_with_options_async(request, headers, runtime)

    def list_monitor_sources_with_options(
        self,
        request: gemp20210413_models.ListMonitorSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListMonitorSourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMonitorSources',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/monitorSource/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListMonitorSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_monitor_sources_with_options_async(
        self,
        request: gemp20210413_models.ListMonitorSourcesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListMonitorSourcesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMonitorSources',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/monitorSource/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListMonitorSourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_monitor_sources(
        self,
        request: gemp20210413_models.ListMonitorSourcesRequest,
    ) -> gemp20210413_models.ListMonitorSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_monitor_sources_with_options(request, headers, runtime)

    async def list_monitor_sources_async(
        self,
        request: gemp20210413_models.ListMonitorSourcesRequest,
    ) -> gemp20210413_models.ListMonitorSourcesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_monitor_sources_with_options_async(request, headers, runtime)

    def list_problem_detail_operations_with_options(
        self,
        request: gemp20210413_models.ListProblemDetailOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemDetailOperationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time_sort):
            body['createTimeSort'] = request.create_time_sort
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemDetailOperations',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/detail/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemDetailOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_problem_detail_operations_with_options_async(
        self,
        request: gemp20210413_models.ListProblemDetailOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemDetailOperationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_time_sort):
            body['createTimeSort'] = request.create_time_sort
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemDetailOperations',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/detail/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemDetailOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_problem_detail_operations(
        self,
        request: gemp20210413_models.ListProblemDetailOperationsRequest,
    ) -> gemp20210413_models.ListProblemDetailOperationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_detail_operations_with_options(request, headers, runtime)

    async def list_problem_detail_operations_async(
        self,
        request: gemp20210413_models.ListProblemDetailOperationsRequest,
    ) -> gemp20210413_models.ListProblemDetailOperationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_problem_detail_operations_with_options_async(request, headers, runtime)

    def list_problem_operations_with_options(
        self,
        request: gemp20210413_models.ListProblemOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemOperationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemOperations',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_problem_operations_with_options_async(
        self,
        request: gemp20210413_models.ListProblemOperationsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemOperationsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemOperations',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/operations',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_problem_operations(
        self,
        request: gemp20210413_models.ListProblemOperationsRequest,
    ) -> gemp20210413_models.ListProblemOperationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_operations_with_options(request, headers, runtime)

    async def list_problem_operations_async(
        self,
        request: gemp20210413_models.ListProblemOperationsRequest,
    ) -> gemp20210413_models.ListProblemOperationsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_problem_operations_with_options_async(request, headers, runtime)

    def list_problem_subtotals_with_options(
        self,
        request: gemp20210413_models.ListProblemSubtotalsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemSubtotalsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemSubtotals',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/list/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemSubtotalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_problem_subtotals_with_options_async(
        self,
        request: gemp20210413_models.ListProblemSubtotalsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemSubtotalsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemSubtotals',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/list/subtotal',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemSubtotalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_problem_subtotals(
        self,
        request: gemp20210413_models.ListProblemSubtotalsRequest,
    ) -> gemp20210413_models.ListProblemSubtotalsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_subtotals_with_options(request, headers, runtime)

    async def list_problem_subtotals_async(
        self,
        request: gemp20210413_models.ListProblemSubtotalsRequest,
    ) -> gemp20210413_models.ListProblemSubtotalsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_problem_subtotals_with_options_async(request, headers, runtime)

    def list_problem_time_lines_with_options(
        self,
        request: gemp20210413_models.ListProblemTimeLinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemTimeLinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemTimeLines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/detail/timeLines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemTimeLinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_problem_time_lines_with_options_async(
        self,
        request: gemp20210413_models.ListProblemTimeLinesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemTimeLinesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblemTimeLines',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/detail/timeLines',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemTimeLinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_problem_time_lines(
        self,
        request: gemp20210413_models.ListProblemTimeLinesRequest,
    ) -> gemp20210413_models.ListProblemTimeLinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problem_time_lines_with_options(request, headers, runtime)

    async def list_problem_time_lines_async(
        self,
        request: gemp20210413_models.ListProblemTimeLinesRequest,
    ) -> gemp20210413_models.ListProblemTimeLinesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_problem_time_lines_with_options_async(request, headers, runtime)

    def list_problems_with_options(
        self,
        request: gemp20210413_models.ListProblemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.affect_service_id):
            body['affectServiceId'] = request.affect_service_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.discovery_end_time):
            body['discoveryEndTime'] = request.discovery_end_time
        if not UtilClient.is_unset(request.discovery_start_time):
            body['discoveryStartTime'] = request.discovery_start_time
        if not UtilClient.is_unset(request.main_handler_id):
            body['mainHandlerId'] = request.main_handler_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.problem_level):
            body['problemLevel'] = request.problem_level
        if not UtilClient.is_unset(request.problem_status):
            body['problemStatus'] = request.problem_status
        if not UtilClient.is_unset(request.query_type):
            body['queryType'] = request.query_type
        if not UtilClient.is_unset(request.repeater_id):
            body['repeaterId'] = request.repeater_id
        if not UtilClient.is_unset(request.restore_end_time):
            body['restoreEndTime'] = request.restore_end_time
        if not UtilClient.is_unset(request.restore_start_time):
            body['restoreStartTime'] = request.restore_start_time
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblems',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/listProblems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_problems_with_options_async(
        self,
        request: gemp20210413_models.ListProblemsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListProblemsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.affect_service_id):
            body['affectServiceId'] = request.affect_service_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.discovery_end_time):
            body['discoveryEndTime'] = request.discovery_end_time
        if not UtilClient.is_unset(request.discovery_start_time):
            body['discoveryStartTime'] = request.discovery_start_time
        if not UtilClient.is_unset(request.main_handler_id):
            body['mainHandlerId'] = request.main_handler_id
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.problem_level):
            body['problemLevel'] = request.problem_level
        if not UtilClient.is_unset(request.problem_status):
            body['problemStatus'] = request.problem_status
        if not UtilClient.is_unset(request.query_type):
            body['queryType'] = request.query_type
        if not UtilClient.is_unset(request.repeater_id):
            body['repeaterId'] = request.repeater_id
        if not UtilClient.is_unset(request.restore_end_time):
            body['restoreEndTime'] = request.restore_end_time
        if not UtilClient.is_unset(request.restore_start_time):
            body['restoreStartTime'] = request.restore_start_time
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListProblems',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/listProblems',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListProblemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_problems(
        self,
        request: gemp20210413_models.ListProblemsRequest,
    ) -> gemp20210413_models.ListProblemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_problems_with_options(request, headers, runtime)

    async def list_problems_async(
        self,
        request: gemp20210413_models.ListProblemsRequest,
    ) -> gemp20210413_models.ListProblemsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_problems_with_options_async(request, headers, runtime)

    def list_route_rules_with_options(
        self,
        request: gemp20210413_models.ListRouteRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListRouteRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.not_filter_route_rule_deleted):
            body['notFilterRouteRuleDeleted'] = request.not_filter_route_rule_deleted
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.route_type):
            body['routeType'] = request.route_type
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRouteRules',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_route_rules_with_options_async(
        self,
        request: gemp20210413_models.ListRouteRulesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListRouteRulesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.not_filter_route_rule_deleted):
            body['notFilterRouteRuleDeleted'] = request.not_filter_route_rule_deleted
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.route_type):
            body['routeType'] = request.route_type
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRouteRules',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_route_rules(
        self,
        request: gemp20210413_models.ListRouteRulesRequest,
    ) -> gemp20210413_models.ListRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_route_rules_with_options(request, headers, runtime)

    async def list_route_rules_async(
        self,
        request: gemp20210413_models.ListRouteRulesRequest,
    ) -> gemp20210413_models.ListRouteRulesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_route_rules_with_options_async(request, headers, runtime)

    def list_route_rules_by_assign_who_id_with_options(
        self,
        request: gemp20210413_models.ListRouteRulesByAssignWhoIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListRouteRulesByAssignWhoIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_who_id):
            body['assignWhoId'] = request.assign_who_id
        if not UtilClient.is_unset(request.assign_who_type):
            body['assignWhoType'] = request.assign_who_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRouteRulesByAssignWhoId',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/listByAssignWhoId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesByAssignWhoIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_route_rules_by_assign_who_id_with_options_async(
        self,
        request: gemp20210413_models.ListRouteRulesByAssignWhoIdRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListRouteRulesByAssignWhoIdResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_who_id):
            body['assignWhoId'] = request.assign_who_id
        if not UtilClient.is_unset(request.assign_who_type):
            body['assignWhoType'] = request.assign_who_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListRouteRulesByAssignWhoId',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/listByAssignWhoId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesByAssignWhoIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_route_rules_by_assign_who_id(
        self,
        request: gemp20210413_models.ListRouteRulesByAssignWhoIdRequest,
    ) -> gemp20210413_models.ListRouteRulesByAssignWhoIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_route_rules_by_assign_who_id_with_options(request, headers, runtime)

    async def list_route_rules_by_assign_who_id_async(
        self,
        request: gemp20210413_models.ListRouteRulesByAssignWhoIdRequest,
    ) -> gemp20210413_models.ListRouteRulesByAssignWhoIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_route_rules_by_assign_who_id_with_options_async(request, headers, runtime)

    def list_route_rules_by_service_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListRouteRulesByServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRouteRulesByService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/listByService',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesByServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_route_rules_by_service_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListRouteRulesByServiceResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListRouteRulesByService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/listByService',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListRouteRulesByServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_route_rules_by_service(self) -> gemp20210413_models.ListRouteRulesByServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_route_rules_by_service_with_options(headers, runtime)

    async def list_route_rules_by_service_async(self) -> gemp20210413_models.ListRouteRulesByServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_route_rules_by_service_with_options_async(headers, runtime)

    def list_service_group_monitor_source_templates_with_options(
        self,
        request: gemp20210413_models.ListServiceGroupMonitorSourceTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListServiceGroupMonitorSourceTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceGroupMonitorSourceTemplates',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/listServiceGroupMonitorSourceTemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupMonitorSourceTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_group_monitor_source_templates_with_options_async(
        self,
        request: gemp20210413_models.ListServiceGroupMonitorSourceTemplatesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListServiceGroupMonitorSourceTemplatesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceGroupMonitorSourceTemplates',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/listServiceGroupMonitorSourceTemplates',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupMonitorSourceTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_group_monitor_source_templates(
        self,
        request: gemp20210413_models.ListServiceGroupMonitorSourceTemplatesRequest,
    ) -> gemp20210413_models.ListServiceGroupMonitorSourceTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_group_monitor_source_templates_with_options(request, headers, runtime)

    async def list_service_group_monitor_source_templates_async(
        self,
        request: gemp20210413_models.ListServiceGroupMonitorSourceTemplatesRequest,
    ) -> gemp20210413_models.ListServiceGroupMonitorSourceTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_group_monitor_source_templates_with_options_async(request, headers, runtime)

    def list_service_groups_with_options(
        self,
        request: gemp20210413_models.ListServiceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListServiceGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.is_scheduled):
            body['isScheduled'] = request.is_scheduled
        if not UtilClient.is_unset(request.order_by_schedule_status):
            body['orderByScheduleStatus'] = request.order_by_schedule_status
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_name):
            body['queryName'] = request.query_name
        if not UtilClient.is_unset(request.query_type):
            body['queryType'] = request.query_type
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceGroups',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_groups_with_options_async(
        self,
        request: gemp20210413_models.ListServiceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListServiceGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.is_scheduled):
            body['isScheduled'] = request.is_scheduled
        if not UtilClient.is_unset(request.order_by_schedule_status):
            body['orderByScheduleStatus'] = request.order_by_schedule_status
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_name):
            body['queryName'] = request.query_name
        if not UtilClient.is_unset(request.query_type):
            body['queryType'] = request.query_type
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServiceGroups',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_groups(
        self,
        request: gemp20210413_models.ListServiceGroupsRequest,
    ) -> gemp20210413_models.ListServiceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_groups_with_options(request, headers, runtime)

    async def list_service_groups_async(
        self,
        request: gemp20210413_models.ListServiceGroupsRequest,
    ) -> gemp20210413_models.ListServiceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_groups_with_options_async(request, headers, runtime)

    def list_service_groups_by_user_id_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListServiceGroupsByUserIdResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServiceGroupsByUserId',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/listByUserId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupsByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_groups_by_user_id_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListServiceGroupsByUserIdResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='ListServiceGroupsByUserId',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/listByUserId',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServiceGroupsByUserIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_groups_by_user_id(self) -> gemp20210413_models.ListServiceGroupsByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_service_groups_by_user_id_with_options(headers, runtime)

    async def list_service_groups_by_user_id_async(self) -> gemp20210413_models.ListServiceGroupsByUserIdResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_service_groups_by_user_id_with_options_async(headers, runtime)

    def list_services_with_options(
        self,
        request: gemp20210413_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: gemp20210413_models.ListServicesRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListServicesResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: gemp20210413_models.ListServicesRequest,
    ) -> gemp20210413_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_services_with_options(request, headers, runtime)

    async def list_services_async(
        self,
        request: gemp20210413_models.ListServicesRequest,
    ) -> gemp20210413_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_services_with_options_async(request, headers, runtime)

    def list_source_events_with_options(
        self,
        request: gemp20210413_models.ListSourceEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListSourceEventsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_row_key):
            body['startRowKey'] = request.start_row_key
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_row_key):
            body['stopRowKey'] = request.stop_row_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSourceEvents',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/events/listOriginalEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSourceEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_source_events_with_options_async(
        self,
        request: gemp20210413_models.ListSourceEventsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListSourceEventsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_row_key):
            body['startRowKey'] = request.start_row_key
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.stop_row_key):
            body['stopRowKey'] = request.stop_row_key
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSourceEvents',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/events/listOriginalEvent',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSourceEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_source_events(
        self,
        request: gemp20210413_models.ListSourceEventsRequest,
    ) -> gemp20210413_models.ListSourceEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_source_events_with_options(request, headers, runtime)

    async def list_source_events_async(
        self,
        request: gemp20210413_models.ListSourceEventsRequest,
    ) -> gemp20210413_models.ListSourceEventsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_source_events_with_options_async(request, headers, runtime)

    def list_source_events_for_monitor_source_with_options(
        self,
        request: gemp20210413_models.ListSourceEventsForMonitorSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListSourceEventsForMonitorSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSourceEventsForMonitorSource',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/events/queryLastestEvents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSourceEventsForMonitorSourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_source_events_for_monitor_source_with_options_async(
        self,
        request: gemp20210413_models.ListSourceEventsForMonitorSourceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListSourceEventsForMonitorSourceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.monitor_source_id):
            body['monitorSourceId'] = request.monitor_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSourceEventsForMonitorSource',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/events/queryLastestEvents',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSourceEventsForMonitorSourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_source_events_for_monitor_source(
        self,
        request: gemp20210413_models.ListSourceEventsForMonitorSourceRequest,
    ) -> gemp20210413_models.ListSourceEventsForMonitorSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_source_events_for_monitor_source_with_options(request, headers, runtime)

    async def list_source_events_for_monitor_source_async(
        self,
        request: gemp20210413_models.ListSourceEventsForMonitorSourceRequest,
    ) -> gemp20210413_models.ListSourceEventsForMonitorSourceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_source_events_for_monitor_source_with_options_async(request, headers, runtime)

    def list_subscription_service_groups_with_options(
        self,
        request: gemp20210413_models.ListSubscriptionServiceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListSubscriptionServiceGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_ids):
            body['serviceIds'] = request.service_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubscriptionServiceGroups',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/serviceGroup/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSubscriptionServiceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscription_service_groups_with_options_async(
        self,
        request: gemp20210413_models.ListSubscriptionServiceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListSubscriptionServiceGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_ids):
            body['serviceIds'] = request.service_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubscriptionServiceGroups',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/serviceGroup/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSubscriptionServiceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscription_service_groups(
        self,
        request: gemp20210413_models.ListSubscriptionServiceGroupsRequest,
    ) -> gemp20210413_models.ListSubscriptionServiceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subscription_service_groups_with_options(request, headers, runtime)

    async def list_subscription_service_groups_async(
        self,
        request: gemp20210413_models.ListSubscriptionServiceGroupsRequest,
    ) -> gemp20210413_models.ListSubscriptionServiceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_subscription_service_groups_with_options_async(request, headers, runtime)

    def list_subscriptions_with_options(
        self,
        request: gemp20210413_models.ListSubscriptionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListSubscriptionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.not_filter_scope_object_deleted):
            body['notFilterScopeObjectDeleted'] = request.not_filter_scope_object_deleted
        if not UtilClient.is_unset(request.notify_object):
            body['notifyObject'] = request.notify_object
        if not UtilClient.is_unset(request.notify_object_type):
            body['notifyObjectType'] = request.notify_object_type
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.scope_object):
            body['scopeObject'] = request.scope_object
        if not UtilClient.is_unset(request.subscription_title):
            body['subscriptionTitle'] = request.subscription_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubscriptions',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSubscriptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscriptions_with_options_async(
        self,
        request: gemp20210413_models.ListSubscriptionsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListSubscriptionsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.not_filter_scope_object_deleted):
            body['notFilterScopeObjectDeleted'] = request.not_filter_scope_object_deleted
        if not UtilClient.is_unset(request.notify_object):
            body['notifyObject'] = request.notify_object
        if not UtilClient.is_unset(request.notify_object_type):
            body['notifyObjectType'] = request.notify_object_type
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.scope_object):
            body['scopeObject'] = request.scope_object
        if not UtilClient.is_unset(request.subscription_title):
            body['subscriptionTitle'] = request.subscription_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSubscriptions',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListSubscriptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscriptions(
        self,
        request: gemp20210413_models.ListSubscriptionsRequest,
    ) -> gemp20210413_models.ListSubscriptionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_subscriptions_with_options(request, headers, runtime)

    async def list_subscriptions_async(
        self,
        request: gemp20210413_models.ListSubscriptionsRequest,
    ) -> gemp20210413_models.ListSubscriptionsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_subscriptions_with_options_async(request, headers, runtime)

    def list_trend_for_source_event_with_options(
        self,
        request: gemp20210413_models.ListTrendForSourceEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListTrendForSourceEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.time_unit):
            body['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTrendForSourceEvent',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/events/querySourceEventTrend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListTrendForSourceEventResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_trend_for_source_event_with_options_async(
        self,
        request: gemp20210413_models.ListTrendForSourceEventRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListTrendForSourceEventResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.request_id):
            body['requestId'] = request.request_id
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.time_unit):
            body['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListTrendForSourceEvent',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/events/querySourceEventTrend',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListTrendForSourceEventResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_trend_for_source_event(
        self,
        request: gemp20210413_models.ListTrendForSourceEventRequest,
    ) -> gemp20210413_models.ListTrendForSourceEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_trend_for_source_event_with_options(request, headers, runtime)

    async def list_trend_for_source_event_async(
        self,
        request: gemp20210413_models.ListTrendForSourceEventRequest,
    ) -> gemp20210413_models.ListTrendForSourceEventResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_trend_for_source_event_with_options_async(request, headers, runtime)

    def list_user_serivce_groups_with_options(
        self,
        request: gemp20210413_models.ListUserSerivceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListUserSerivceGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserSerivceGroups',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/preview/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListUserSerivceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_serivce_groups_with_options_async(
        self,
        request: gemp20210413_models.ListUserSerivceGroupsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListUserSerivceGroupsResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUserSerivceGroups',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/preview/detail',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListUserSerivceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_serivce_groups(
        self,
        request: gemp20210413_models.ListUserSerivceGroupsRequest,
    ) -> gemp20210413_models.ListUserSerivceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_user_serivce_groups_with_options(request, headers, runtime)

    async def list_user_serivce_groups_async(
        self,
        request: gemp20210413_models.ListUserSerivceGroupsRequest,
    ) -> gemp20210413_models.ListUserSerivceGroupsResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_user_serivce_groups_with_options_async(request, headers, runtime)

    def list_users_with_options(
        self,
        request: gemp20210413_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.ram_id):
            body['ramId'] = request.ram_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.synergy_channel):
            body['synergyChannel'] = request.synergy_channel
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: gemp20210413_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ListUsersResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.page_number):
            body['pageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['pageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.ram_id):
            body['ramId'] = request.ram_id
        if not UtilClient.is_unset(request.scene):
            body['scene'] = request.scene
        if not UtilClient.is_unset(request.synergy_channel):
            body['synergyChannel'] = request.synergy_channel
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/list',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: gemp20210413_models.ListUsersRequest,
    ) -> gemp20210413_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

    async def list_users_async(
        self,
        request: gemp20210413_models.ListUsersRequest,
    ) -> gemp20210413_models.ListUsersResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(request, headers, runtime)

    def push_monitor_with_options(
        self,
        api_key: str,
        request: gemp20210413_models.PushMonitorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.PushMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='PushMonitor',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/api/monitor/push/{OpenApiUtilClient.get_encode_param(api_key)}',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.PushMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_monitor_with_options_async(
        self,
        api_key: str,
        request: gemp20210413_models.PushMonitorRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.PushMonitorResponse:
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=request.body
        )
        params = open_api_models.Params(
            action='PushMonitor',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/api/monitor/push/{OpenApiUtilClient.get_encode_param(api_key)}',
            method='POST',
            auth_type='Anonymous',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.PushMonitorResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_monitor(
        self,
        api_key: str,
        request: gemp20210413_models.PushMonitorRequest,
    ) -> gemp20210413_models.PushMonitorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.push_monitor_with_options(api_key, request, headers, runtime)

    async def push_monitor_async(
        self,
        api_key: str,
        request: gemp20210413_models.PushMonitorRequest,
    ) -> gemp20210413_models.PushMonitorResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.push_monitor_with_options_async(api_key, request, headers, runtime)

    def recover_problem_with_options(
        self,
        request: gemp20210413_models.RecoverProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RecoverProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        if not UtilClient.is_unset(request.recovery_time):
            body['recoveryTime'] = request.recovery_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecoverProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/recovery',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RecoverProblemResponse(),
            self.call_api(params, req, runtime)
        )

    async def recover_problem_with_options_async(
        self,
        request: gemp20210413_models.RecoverProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RecoverProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        if not UtilClient.is_unset(request.recovery_time):
            body['recoveryTime'] = request.recovery_time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecoverProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/recovery',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RecoverProblemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def recover_problem(
        self,
        request: gemp20210413_models.RecoverProblemRequest,
    ) -> gemp20210413_models.RecoverProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.recover_problem_with_options(request, headers, runtime)

    async def recover_problem_async(
        self,
        request: gemp20210413_models.RecoverProblemRequest,
    ) -> gemp20210413_models.RecoverProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.recover_problem_with_options_async(request, headers, runtime)

    def refresh_integration_config_key_with_options(
        self,
        request: gemp20210413_models.RefreshIntegrationConfigKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RefreshIntegrationConfigKeyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshIntegrationConfigKey',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/refreshKey',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RefreshIntegrationConfigKeyResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_integration_config_key_with_options_async(
        self,
        request: gemp20210413_models.RefreshIntegrationConfigKeyRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RefreshIntegrationConfigKeyResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshIntegrationConfigKey',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/refreshKey',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RefreshIntegrationConfigKeyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_integration_config_key(
        self,
        request: gemp20210413_models.RefreshIntegrationConfigKeyRequest,
    ) -> gemp20210413_models.RefreshIntegrationConfigKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.refresh_integration_config_key_with_options(request, headers, runtime)

    async def refresh_integration_config_key_async(
        self,
        request: gemp20210413_models.RefreshIntegrationConfigKeyRequest,
    ) -> gemp20210413_models.RefreshIntegrationConfigKeyResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.refresh_integration_config_key_with_options_async(request, headers, runtime)

    def remove_integration_config_with_options(
        self,
        request: gemp20210413_models.RemoveIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RemoveIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RemoveIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_integration_config_with_options_async(
        self,
        request: gemp20210413_models.RemoveIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RemoveIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/remove',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RemoveIntegrationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_integration_config(
        self,
        request: gemp20210413_models.RemoveIntegrationConfigRequest,
    ) -> gemp20210413_models.RemoveIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_integration_config_with_options(request, headers, runtime)

    async def remove_integration_config_async(
        self,
        request: gemp20210413_models.RemoveIntegrationConfigRequest,
    ) -> gemp20210413_models.RemoveIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_integration_config_with_options_async(request, headers, runtime)

    def remove_problem_service_group_with_options(
        self,
        request: gemp20210413_models.RemoveProblemServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RemoveProblemServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveProblemServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/removeServiceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RemoveProblemServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_problem_service_group_with_options_async(
        self,
        request: gemp20210413_models.RemoveProblemServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RemoveProblemServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveProblemServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/removeServiceGroup',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RemoveProblemServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_problem_service_group(
        self,
        request: gemp20210413_models.RemoveProblemServiceGroupRequest,
    ) -> gemp20210413_models.RemoveProblemServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.remove_problem_service_group_with_options(request, headers, runtime)

    async def remove_problem_service_group_async(
        self,
        request: gemp20210413_models.RemoveProblemServiceGroupRequest,
    ) -> gemp20210413_models.RemoveProblemServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.remove_problem_service_group_with_options_async(request, headers, runtime)

    def replay_problem_with_options(
        self,
        request: gemp20210413_models.ReplayProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ReplayProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.replay_duty_user_id):
            body['replayDutyUserId'] = request.replay_duty_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReplayProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/replay',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ReplayProblemResponse(),
            self.call_api(params, req, runtime)
        )

    async def replay_problem_with_options_async(
        self,
        request: gemp20210413_models.ReplayProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.ReplayProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.replay_duty_user_id):
            body['replayDutyUserId'] = request.replay_duty_user_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ReplayProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/replay',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.ReplayProblemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def replay_problem(
        self,
        request: gemp20210413_models.ReplayProblemRequest,
    ) -> gemp20210413_models.ReplayProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.replay_problem_with_options(request, headers, runtime)

    async def replay_problem_async(
        self,
        request: gemp20210413_models.ReplayProblemRequest,
    ) -> gemp20210413_models.ReplayProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.replay_problem_with_options_async(request, headers, runtime)

    def respond_incident_with_options(
        self,
        request: gemp20210413_models.RespondIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RespondIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_ids):
            body['incidentIds'] = request.incident_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RespondIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/response',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RespondIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def respond_incident_with_options_async(
        self,
        request: gemp20210413_models.RespondIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RespondIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.incident_ids):
            body['incidentIds'] = request.incident_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RespondIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/response',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RespondIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def respond_incident(
        self,
        request: gemp20210413_models.RespondIncidentRequest,
    ) -> gemp20210413_models.RespondIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.respond_incident_with_options(request, headers, runtime)

    async def respond_incident_async(
        self,
        request: gemp20210413_models.RespondIncidentRequest,
    ) -> gemp20210413_models.RespondIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.respond_incident_with_options_async(request, headers, runtime)

    def revoke_problem_recovery_with_options(
        self,
        request: gemp20210413_models.RevokeProblemRecoveryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RevokeProblemRecoveryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeProblemRecovery',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RevokeProblemRecoveryResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_problem_recovery_with_options_async(
        self,
        request: gemp20210413_models.RevokeProblemRecoveryRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.RevokeProblemRecoveryResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokeProblemRecovery',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/revoke',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.RevokeProblemRecoveryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_problem_recovery(
        self,
        request: gemp20210413_models.RevokeProblemRecoveryRequest,
    ) -> gemp20210413_models.RevokeProblemRecoveryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.revoke_problem_recovery_with_options(request, headers, runtime)

    async def revoke_problem_recovery_async(
        self,
        request: gemp20210413_models.RevokeProblemRecoveryRequest,
    ) -> gemp20210413_models.RevokeProblemRecoveryResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.revoke_problem_recovery_with_options_async(request, headers, runtime)

    def unbind_user_with_options(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UnbindUserResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/unbind',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UnbindUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def unbind_user_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UnbindUserResponse:
        req = open_api_models.OpenApiRequest(
            headers=headers
        )
        params = open_api_models.Params(
            action='UnbindUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/unbind',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UnbindUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def unbind_user(self) -> gemp20210413_models.UnbindUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.unbind_user_with_options(headers, runtime)

    async def unbind_user_async(self) -> gemp20210413_models.UnbindUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.unbind_user_with_options_async(headers, runtime)

    def update_escalation_plan_with_options(
        self,
        request: gemp20210413_models.UpdateEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_description):
            body['escalationPlanDescription'] = request.escalation_plan_description
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        if not UtilClient.is_unset(request.escalation_plan_name):
            body['escalationPlanName'] = request.escalation_plan_name
        if not UtilClient.is_unset(request.escalation_plan_rules):
            body['escalationPlanRules'] = request.escalation_plan_rules
        if not UtilClient.is_unset(request.escalation_plan_scope_objects):
            body['escalationPlanScopeObjects'] = request.escalation_plan_scope_objects
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateEscalationPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_escalation_plan_with_options_async(
        self,
        request: gemp20210413_models.UpdateEscalationPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateEscalationPlanResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.escalation_plan_description):
            body['escalationPlanDescription'] = request.escalation_plan_description
        if not UtilClient.is_unset(request.escalation_plan_id):
            body['escalationPlanId'] = request.escalation_plan_id
        if not UtilClient.is_unset(request.escalation_plan_name):
            body['escalationPlanName'] = request.escalation_plan_name
        if not UtilClient.is_unset(request.escalation_plan_rules):
            body['escalationPlanRules'] = request.escalation_plan_rules
        if not UtilClient.is_unset(request.escalation_plan_scope_objects):
            body['escalationPlanScopeObjects'] = request.escalation_plan_scope_objects
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEscalationPlan',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/escalationPlan/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateEscalationPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_escalation_plan(
        self,
        request: gemp20210413_models.UpdateEscalationPlanRequest,
    ) -> gemp20210413_models.UpdateEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_escalation_plan_with_options(request, headers, runtime)

    async def update_escalation_plan_async(
        self,
        request: gemp20210413_models.UpdateEscalationPlanRequest,
    ) -> gemp20210413_models.UpdateEscalationPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_escalation_plan_with_options_async(request, headers, runtime)

    def update_incident_with_options(
        self,
        request: gemp20210413_models.UpdateIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effect):
            body['effect'] = request.effect
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.incident_title):
            body['incidentTitle'] = request.incident_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_incident_with_options_async(
        self,
        request: gemp20210413_models.UpdateIncidentRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateIncidentResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.effect):
            body['effect'] = request.effect
        if not UtilClient.is_unset(request.incident_id):
            body['incidentId'] = request.incident_id
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.incident_title):
            body['incidentTitle'] = request.incident_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIncident',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/incident/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateIncidentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_incident(
        self,
        request: gemp20210413_models.UpdateIncidentRequest,
    ) -> gemp20210413_models.UpdateIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_incident_with_options(request, headers, runtime)

    async def update_incident_async(
        self,
        request: gemp20210413_models.UpdateIncidentRequest,
    ) -> gemp20210413_models.UpdateIncidentResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_incident_with_options_async(request, headers, runtime)

    def update_integration_config_with_options(
        self,
        request: gemp20210413_models.UpdateIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateIntegrationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_integration_config_with_options_async(
        self,
        request: gemp20210413_models.UpdateIntegrationConfigRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateIntegrationConfigResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['accessKey'] = request.access_key
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.integration_config_id):
            body['integrationConfigId'] = request.integration_config_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegrationConfig',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/integrationConfig/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateIntegrationConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_integration_config(
        self,
        request: gemp20210413_models.UpdateIntegrationConfigRequest,
    ) -> gemp20210413_models.UpdateIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_integration_config_with_options(request, headers, runtime)

    async def update_integration_config_async(
        self,
        request: gemp20210413_models.UpdateIntegrationConfigRequest,
    ) -> gemp20210413_models.UpdateIntegrationConfigResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_integration_config_with_options_async(request, headers, runtime)

    def update_problem_with_options(
        self,
        request: gemp20210413_models.UpdateProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feedback):
            body['feedback'] = request.feedback
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        if not UtilClient.is_unset(request.main_handler_id):
            body['mainHandlerId'] = request.main_handler_id
        if not UtilClient.is_unset(request.preliminary_reason):
            body['preliminaryReason'] = request.preliminary_reason
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_name):
            body['problemName'] = request.problem_name
        if not UtilClient.is_unset(request.progress_summary):
            body['progressSummary'] = request.progress_summary
        if not UtilClient.is_unset(request.progress_summary_rich_text_id):
            body['progressSummaryRichTextId'] = request.progress_summary_rich_text_id
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_problem_with_options_async(
        self,
        request: gemp20210413_models.UpdateProblemRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.feedback):
            body['feedback'] = request.feedback
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        if not UtilClient.is_unset(request.main_handler_id):
            body['mainHandlerId'] = request.main_handler_id
        if not UtilClient.is_unset(request.preliminary_reason):
            body['preliminaryReason'] = request.preliminary_reason
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_name):
            body['problemName'] = request.problem_name
        if not UtilClient.is_unset(request.progress_summary):
            body['progressSummary'] = request.progress_summary
        if not UtilClient.is_unset(request.progress_summary_rich_text_id):
            body['progressSummaryRichTextId'] = request.progress_summary_rich_text_id
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.service_group_ids):
            body['serviceGroupIds'] = request.service_group_ids
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblem',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_problem(
        self,
        request: gemp20210413_models.UpdateProblemRequest,
    ) -> gemp20210413_models.UpdateProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_with_options(request, headers, runtime)

    async def update_problem_async(
        self,
        request: gemp20210413_models.UpdateProblemRequest,
    ) -> gemp20210413_models.UpdateProblemResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_problem_with_options_async(request, headers, runtime)

    def update_problem_effection_service_with_options(
        self,
        request: gemp20210413_models.UpdateProblemEffectionServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemEffectionServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.effection_service_id):
            body['effectionServiceId'] = request.effection_service_id
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        if not UtilClient.is_unset(request.pic_url):
            body['picUrl'] = request.pic_url
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/effectionService/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemEffectionServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_problem_effection_service_with_options_async(
        self,
        request: gemp20210413_models.UpdateProblemEffectionServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemEffectionServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            body['description'] = request.description
        if not UtilClient.is_unset(request.effection_service_id):
            body['effectionServiceId'] = request.effection_service_id
        if not UtilClient.is_unset(request.level):
            body['level'] = request.level
        if not UtilClient.is_unset(request.pic_url):
            body['picUrl'] = request.pic_url
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemEffectionService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/effectionService/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemEffectionServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_problem_effection_service(
        self,
        request: gemp20210413_models.UpdateProblemEffectionServiceRequest,
    ) -> gemp20210413_models.UpdateProblemEffectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_effection_service_with_options(request, headers, runtime)

    async def update_problem_effection_service_async(
        self,
        request: gemp20210413_models.UpdateProblemEffectionServiceRequest,
    ) -> gemp20210413_models.UpdateProblemEffectionServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_problem_effection_service_with_options_async(request, headers, runtime)

    def update_problem_improvement_with_options(
        self,
        request: gemp20210413_models.UpdateProblemImprovementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemImprovementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.custom_problem_reason):
            body['customProblemReason'] = request.custom_problem_reason
        if not UtilClient.is_unset(request.discover_source):
            body['discoverSource'] = request.discover_source
        if not UtilClient.is_unset(request.duty_department_id):
            body['dutyDepartmentId'] = request.duty_department_id
        if not UtilClient.is_unset(request.duty_department_name):
            body['dutyDepartmentName'] = request.duty_department_name
        if not UtilClient.is_unset(request.duty_user_id):
            body['dutyUserId'] = request.duty_user_id
        if not UtilClient.is_unset(request.injection_mode):
            body['injectionMode'] = request.injection_mode
        if not UtilClient.is_unset(request.monitor_source_name):
            body['monitorSourceName'] = request.monitor_source_name
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_reason):
            body['problemReason'] = request.problem_reason
        if not UtilClient.is_unset(request.recent_activity):
            body['recentActivity'] = request.recent_activity
        if not UtilClient.is_unset(request.recovery_mode):
            body['recoveryMode'] = request.recovery_mode
        if not UtilClient.is_unset(request.relation_changes):
            body['relationChanges'] = request.relation_changes
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.replay_duty_user_id):
            body['replayDutyUserId'] = request.replay_duty_user_id
        if not UtilClient.is_unset(request.user_report):
            body['userReport'] = request.user_report
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemImprovement',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemImprovementResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_problem_improvement_with_options_async(
        self,
        request: gemp20210413_models.UpdateProblemImprovementRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemImprovementResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.custom_problem_reason):
            body['customProblemReason'] = request.custom_problem_reason
        if not UtilClient.is_unset(request.discover_source):
            body['discoverSource'] = request.discover_source
        if not UtilClient.is_unset(request.duty_department_id):
            body['dutyDepartmentId'] = request.duty_department_id
        if not UtilClient.is_unset(request.duty_department_name):
            body['dutyDepartmentName'] = request.duty_department_name
        if not UtilClient.is_unset(request.duty_user_id):
            body['dutyUserId'] = request.duty_user_id
        if not UtilClient.is_unset(request.injection_mode):
            body['injectionMode'] = request.injection_mode
        if not UtilClient.is_unset(request.monitor_source_name):
            body['monitorSourceName'] = request.monitor_source_name
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_reason):
            body['problemReason'] = request.problem_reason
        if not UtilClient.is_unset(request.recent_activity):
            body['recentActivity'] = request.recent_activity
        if not UtilClient.is_unset(request.recovery_mode):
            body['recoveryMode'] = request.recovery_mode
        if not UtilClient.is_unset(request.relation_changes):
            body['relationChanges'] = request.relation_changes
        if not UtilClient.is_unset(request.remark):
            body['remark'] = request.remark
        if not UtilClient.is_unset(request.replay_duty_user_id):
            body['replayDutyUserId'] = request.replay_duty_user_id
        if not UtilClient.is_unset(request.user_report):
            body['userReport'] = request.user_report
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemImprovement',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemImprovementResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_problem_improvement(
        self,
        request: gemp20210413_models.UpdateProblemImprovementRequest,
    ) -> gemp20210413_models.UpdateProblemImprovementResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_improvement_with_options(request, headers, runtime)

    async def update_problem_improvement_async(
        self,
        request: gemp20210413_models.UpdateProblemImprovementRequest,
    ) -> gemp20210413_models.UpdateProblemImprovementResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_problem_improvement_with_options_async(request, headers, runtime)

    def update_problem_measure_with_options(
        self,
        request: gemp20210413_models.UpdateProblemMeasureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemMeasureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_standard):
            body['checkStandard'] = request.check_standard
        if not UtilClient.is_unset(request.check_user_id):
            body['checkUserId'] = request.check_user_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.director_id):
            body['directorId'] = request.director_id
        if not UtilClient.is_unset(request.measure_id):
            body['measureId'] = request.measure_id
        if not UtilClient.is_unset(request.plan_finish_time):
            body['planFinishTime'] = request.plan_finish_time
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.stalker_id):
            body['stalkerId'] = request.stalker_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemMeasure',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/measure/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemMeasureResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_problem_measure_with_options_async(
        self,
        request: gemp20210413_models.UpdateProblemMeasureRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemMeasureResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.check_standard):
            body['checkStandard'] = request.check_standard
        if not UtilClient.is_unset(request.check_user_id):
            body['checkUserId'] = request.check_user_id
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.director_id):
            body['directorId'] = request.director_id
        if not UtilClient.is_unset(request.measure_id):
            body['measureId'] = request.measure_id
        if not UtilClient.is_unset(request.plan_finish_time):
            body['planFinishTime'] = request.plan_finish_time
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.stalker_id):
            body['stalkerId'] = request.stalker_id
        if not UtilClient.is_unset(request.status):
            body['status'] = request.status
        if not UtilClient.is_unset(request.type):
            body['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemMeasure',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/improvement/measure/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemMeasureResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_problem_measure(
        self,
        request: gemp20210413_models.UpdateProblemMeasureRequest,
    ) -> gemp20210413_models.UpdateProblemMeasureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_measure_with_options(request, headers, runtime)

    async def update_problem_measure_async(
        self,
        request: gemp20210413_models.UpdateProblemMeasureRequest,
    ) -> gemp20210413_models.UpdateProblemMeasureResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_problem_measure_with_options_async(request, headers, runtime)

    def update_problem_notice_with_options(
        self,
        request: gemp20210413_models.UpdateProblemNoticeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemNoticeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemNotice',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/notify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_problem_notice_with_options_async(
        self,
        request: gemp20210413_models.UpdateProblemNoticeRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemNoticeResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_notify_type):
            body['problemNotifyType'] = request.problem_notify_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemNotice',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/notify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_problem_notice(
        self,
        request: gemp20210413_models.UpdateProblemNoticeRequest,
    ) -> gemp20210413_models.UpdateProblemNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_notice_with_options(request, headers, runtime)

    async def update_problem_notice_async(
        self,
        request: gemp20210413_models.UpdateProblemNoticeRequest,
    ) -> gemp20210413_models.UpdateProblemNoticeResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_problem_notice_with_options_async(request, headers, runtime)

    def update_problem_timeline_with_options(
        self,
        request: gemp20210413_models.UpdateProblemTimelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemTimelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.key_node):
            body['keyNode'] = request.key_node
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_timeline_id):
            body['problemTimelineId'] = request.problem_timeline_id
        if not UtilClient.is_unset(request.time):
            body['time'] = request.time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemTimeline',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/timeline/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemTimelineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_problem_timeline_with_options_async(
        self,
        request: gemp20210413_models.UpdateProblemTimelineRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateProblemTimelineResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            body['content'] = request.content
        if not UtilClient.is_unset(request.key_node):
            body['keyNode'] = request.key_node
        if not UtilClient.is_unset(request.problem_id):
            body['problemId'] = request.problem_id
        if not UtilClient.is_unset(request.problem_timeline_id):
            body['problemTimelineId'] = request.problem_timeline_id
        if not UtilClient.is_unset(request.time):
            body['time'] = request.time
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProblemTimeline',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/problem/process/timeline/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateProblemTimelineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_problem_timeline(
        self,
        request: gemp20210413_models.UpdateProblemTimelineRequest,
    ) -> gemp20210413_models.UpdateProblemTimelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_problem_timeline_with_options(request, headers, runtime)

    async def update_problem_timeline_async(
        self,
        request: gemp20210413_models.UpdateProblemTimelineRequest,
    ) -> gemp20210413_models.UpdateProblemTimelineResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_problem_timeline_with_options_async(request, headers, runtime)

    def update_rich_text_with_options(
        self,
        request: gemp20210413_models.UpdateRichTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateRichTextResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.rich_text):
            body['richText'] = request.rich_text
        if not UtilClient.is_unset(request.rich_text_id):
            body['richTextId'] = request.rich_text_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRichText',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateRichTextResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_rich_text_with_options_async(
        self,
        request: gemp20210413_models.UpdateRichTextRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateRichTextResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['instanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            body['instanceType'] = request.instance_type
        if not UtilClient.is_unset(request.rich_text):
            body['richText'] = request.rich_text
        if not UtilClient.is_unset(request.rich_text_id):
            body['richTextId'] = request.rich_text_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRichText',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/rich/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateRichTextResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_rich_text(
        self,
        request: gemp20210413_models.UpdateRichTextRequest,
    ) -> gemp20210413_models.UpdateRichTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_rich_text_with_options(request, headers, runtime)

    async def update_rich_text_async(
        self,
        request: gemp20210413_models.UpdateRichTextRequest,
    ) -> gemp20210413_models.UpdateRichTextResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_rich_text_with_options_async(request, headers, runtime)

    def update_route_rule_with_options(
        self,
        request: gemp20210413_models.UpdateRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_object_id):
            body['assignObjectId'] = request.assign_object_id
        if not UtilClient.is_unset(request.assign_object_type):
            body['assignObjectType'] = request.assign_object_type
        if not UtilClient.is_unset(request.child_rule_relation):
            body['childRuleRelation'] = request.child_rule_relation
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.convergence_fields):
            body['convergenceFields'] = request.convergence_fields
        if not UtilClient.is_unset(request.convergence_type):
            body['convergenceType'] = request.convergence_type
        if not UtilClient.is_unset(request.coverage_problem_levels):
            body['coverageProblemLevels'] = request.coverage_problem_levels
        if not UtilClient.is_unset(request.effection):
            body['effection'] = request.effection
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.match_count):
            body['matchCount'] = request.match_count
        if not UtilClient.is_unset(request.notify_channels):
            body['notifyChannels'] = request.notify_channels
        if not UtilClient.is_unset(request.problem_effection_services):
            body['problemEffectionServices'] = request.problem_effection_services
        if not UtilClient.is_unset(request.problem_level_group):
            body['problemLevelGroup'] = request.problem_level_group
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.route_child_rules):
            body['routeChildRules'] = request.route_child_rules
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        if not UtilClient.is_unset(request.route_type):
            body['routeType'] = request.route_type
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.time_window):
            body['timeWindow'] = request.time_window
        if not UtilClient.is_unset(request.time_window_unit):
            body['timeWindowUnit'] = request.time_window_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/edit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_route_rule_with_options_async(
        self,
        request: gemp20210413_models.UpdateRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.assign_object_id):
            body['assignObjectId'] = request.assign_object_id
        if not UtilClient.is_unset(request.assign_object_type):
            body['assignObjectType'] = request.assign_object_type
        if not UtilClient.is_unset(request.child_rule_relation):
            body['childRuleRelation'] = request.child_rule_relation
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.convergence_fields):
            body['convergenceFields'] = request.convergence_fields
        if not UtilClient.is_unset(request.convergence_type):
            body['convergenceType'] = request.convergence_type
        if not UtilClient.is_unset(request.coverage_problem_levels):
            body['coverageProblemLevels'] = request.coverage_problem_levels
        if not UtilClient.is_unset(request.effection):
            body['effection'] = request.effection
        if not UtilClient.is_unset(request.incident_level):
            body['incidentLevel'] = request.incident_level
        if not UtilClient.is_unset(request.match_count):
            body['matchCount'] = request.match_count
        if not UtilClient.is_unset(request.notify_channels):
            body['notifyChannels'] = request.notify_channels
        if not UtilClient.is_unset(request.problem_effection_services):
            body['problemEffectionServices'] = request.problem_effection_services
        if not UtilClient.is_unset(request.problem_level_group):
            body['problemLevelGroup'] = request.problem_level_group
        if not UtilClient.is_unset(request.related_service_id):
            body['relatedServiceId'] = request.related_service_id
        if not UtilClient.is_unset(request.route_child_rules):
            body['routeChildRules'] = request.route_child_rules
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        if not UtilClient.is_unset(request.route_type):
            body['routeType'] = request.route_type
        if not UtilClient.is_unset(request.rule_name):
            body['ruleName'] = request.rule_name
        if not UtilClient.is_unset(request.time_window):
            body['timeWindow'] = request.time_window
        if not UtilClient.is_unset(request.time_window_unit):
            body['timeWindowUnit'] = request.time_window_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/edit',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_route_rule(
        self,
        request: gemp20210413_models.UpdateRouteRuleRequest,
    ) -> gemp20210413_models.UpdateRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_route_rule_with_options(request, headers, runtime)

    async def update_route_rule_async(
        self,
        request: gemp20210413_models.UpdateRouteRuleRequest,
    ) -> gemp20210413_models.UpdateRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_route_rule_with_options_async(request, headers, runtime)

    def update_service_with_options(
        self,
        request: gemp20210413_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_description):
            body['serviceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        request: gemp20210413_models.UpdateServiceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_description):
            body['serviceDescription'] = request.service_description
        if not UtilClient.is_unset(request.service_id):
            body['serviceId'] = request.service_id
        if not UtilClient.is_unset(request.service_name):
            body['serviceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        request: gemp20210413_models.UpdateServiceRequest,
    ) -> gemp20210413_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_with_options(request, headers, runtime)

    async def update_service_async(
        self,
        request: gemp20210413_models.UpdateServiceRequest,
    ) -> gemp20210413_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_with_options_async(request, headers, runtime)

    def update_service_group_with_options(
        self,
        request: gemp20210413_models.UpdateServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_webhook):
            body['enableWebhook'] = request.enable_webhook
        if not UtilClient.is_unset(request.monitor_source_templates):
            body['monitorSourceTemplates'] = request.monitor_source_templates
        if not UtilClient.is_unset(request.service_group_description):
            body['serviceGroupDescription'] = request.service_group_description
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.service_group_name):
            body['serviceGroupName'] = request.service_group_name
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.webhook_link):
            body['webhookLink'] = request.webhook_link
        if not UtilClient.is_unset(request.webhook_type):
            body['webhookType'] = request.webhook_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/modify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_group_with_options_async(
        self,
        request: gemp20210413_models.UpdateServiceGroupRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateServiceGroupResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_webhook):
            body['enableWebhook'] = request.enable_webhook
        if not UtilClient.is_unset(request.monitor_source_templates):
            body['monitorSourceTemplates'] = request.monitor_source_templates
        if not UtilClient.is_unset(request.service_group_description):
            body['serviceGroupDescription'] = request.service_group_description
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        if not UtilClient.is_unset(request.service_group_name):
            body['serviceGroupName'] = request.service_group_name
        if not UtilClient.is_unset(request.user_ids):
            body['userIds'] = request.user_ids
        if not UtilClient.is_unset(request.webhook_link):
            body['webhookLink'] = request.webhook_link
        if not UtilClient.is_unset(request.webhook_type):
            body['webhookType'] = request.webhook_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceGroup',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/modify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_group(
        self,
        request: gemp20210413_models.UpdateServiceGroupRequest,
    ) -> gemp20210413_models.UpdateServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_group_with_options(request, headers, runtime)

    async def update_service_group_async(
        self,
        request: gemp20210413_models.UpdateServiceGroupRequest,
    ) -> gemp20210413_models.UpdateServiceGroupResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_group_with_options_async(request, headers, runtime)

    def update_service_group_scheduling_with_options(
        self,
        request: gemp20210413_models.UpdateServiceGroupSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateServiceGroupSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.fast_scheduling):
            body['fastScheduling'] = request.fast_scheduling
        if not UtilClient.is_unset(request.fine_scheduling):
            body['fineScheduling'] = request.fine_scheduling
        if not UtilClient.is_unset(request.scheduling_way):
            body['schedulingWay'] = request.scheduling_way
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupSchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_group_scheduling_with_options_async(
        self,
        request: gemp20210413_models.UpdateServiceGroupSchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateServiceGroupSchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.fast_scheduling):
            body['fastScheduling'] = request.fast_scheduling
        if not UtilClient.is_unset(request.fine_scheduling):
            body['fineScheduling'] = request.fine_scheduling
        if not UtilClient.is_unset(request.scheduling_way):
            body['schedulingWay'] = request.scheduling_way
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceGroupScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupSchedulingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_group_scheduling(
        self,
        request: gemp20210413_models.UpdateServiceGroupSchedulingRequest,
    ) -> gemp20210413_models.UpdateServiceGroupSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_group_scheduling_with_options(request, headers, runtime)

    async def update_service_group_scheduling_async(
        self,
        request: gemp20210413_models.UpdateServiceGroupSchedulingRequest,
    ) -> gemp20210413_models.UpdateServiceGroupSchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_group_scheduling_with_options_async(request, headers, runtime)

    def update_service_group_special_day_scheduling_with_options(
        self,
        request: gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.scheduling_date):
            body['schedulingDate'] = request.scheduling_date
        if not UtilClient.is_unset(request.scheduling_special_days):
            body['schedulingSpecialDays'] = request.scheduling_special_days
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceGroupSpecialDayScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/updateSpecialDayScheduling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_group_special_day_scheduling_with_options_async(
        self,
        request: gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.scheduling_date):
            body['schedulingDate'] = request.scheduling_date
        if not UtilClient.is_unset(request.scheduling_special_days):
            body['schedulingSpecialDays'] = request.scheduling_special_days
        if not UtilClient.is_unset(request.service_group_id):
            body['serviceGroupId'] = request.service_group_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateServiceGroupSpecialDayScheduling',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/services/group/scheduling/updateSpecialDayScheduling',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_group_special_day_scheduling(
        self,
        request: gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingRequest,
    ) -> gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_service_group_special_day_scheduling_with_options(request, headers, runtime)

    async def update_service_group_special_day_scheduling_async(
        self,
        request: gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingRequest,
    ) -> gemp20210413_models.UpdateServiceGroupSpecialDaySchedulingResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_service_group_special_day_scheduling_with_options_async(request, headers, runtime)

    def update_subscription_with_options(
        self,
        request: gemp20210413_models.UpdateSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.expired_type):
            body['expiredType'] = request.expired_type
        if not UtilClient.is_unset(request.notify_object_list):
            body['notifyObjectList'] = request.notify_object_list
        if not UtilClient.is_unset(request.notify_object_type):
            body['notifyObjectType'] = request.notify_object_type
        if not UtilClient.is_unset(request.notify_strategy_list):
            body['notifyStrategyList'] = request.notify_strategy_list
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.scope_object_list):
            body['scopeObjectList'] = request.scope_object_list
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        if not UtilClient.is_unset(request.subscription_title):
            body['subscriptionTitle'] = request.subscription_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateSubscriptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_subscription_with_options_async(
        self,
        request: gemp20210413_models.UpdateSubscriptionRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateSubscriptionResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.end_time):
            body['endTime'] = request.end_time
        if not UtilClient.is_unset(request.expired_type):
            body['expiredType'] = request.expired_type
        if not UtilClient.is_unset(request.notify_object_list):
            body['notifyObjectList'] = request.notify_object_list
        if not UtilClient.is_unset(request.notify_object_type):
            body['notifyObjectType'] = request.notify_object_type
        if not UtilClient.is_unset(request.notify_strategy_list):
            body['notifyStrategyList'] = request.notify_strategy_list
        if not UtilClient.is_unset(request.period):
            body['period'] = request.period
        if not UtilClient.is_unset(request.scope):
            body['scope'] = request.scope
        if not UtilClient.is_unset(request.scope_object_list):
            body['scopeObjectList'] = request.scope_object_list
        if not UtilClient.is_unset(request.start_time):
            body['startTime'] = request.start_time
        if not UtilClient.is_unset(request.subscription_id):
            body['subscriptionId'] = request.subscription_id
        if not UtilClient.is_unset(request.subscription_title):
            body['subscriptionTitle'] = request.subscription_title
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSubscription',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/notify/subscription/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateSubscriptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_subscription(
        self,
        request: gemp20210413_models.UpdateSubscriptionRequest,
    ) -> gemp20210413_models.UpdateSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_subscription_with_options(request, headers, runtime)

    async def update_subscription_async(
        self,
        request: gemp20210413_models.UpdateSubscriptionRequest,
    ) -> gemp20210413_models.UpdateSubscriptionResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_subscription_with_options_async(request, headers, runtime)

    def update_user_with_options(
        self,
        request: gemp20210413_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.ram_id):
            body['ramId'] = request.ram_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_with_options_async(
        self,
        request: gemp20210413_models.UpdateUserRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateUserResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.email):
            body['email'] = request.email
        if not UtilClient.is_unset(request.phone):
            body['phone'] = request.phone
        if not UtilClient.is_unset(request.ram_id):
            body['ramId'] = request.ram_id
        if not UtilClient.is_unset(request.user_id):
            body['userId'] = request.user_id
        if not UtilClient.is_unset(request.username):
            body['username'] = request.username
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/update',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user(
        self,
        request: gemp20210413_models.UpdateUserRequest,
    ) -> gemp20210413_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_with_options(request, headers, runtime)

    async def update_user_async(
        self,
        request: gemp20210413_models.UpdateUserRequest,
    ) -> gemp20210413_models.UpdateUserResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_user_with_options_async(request, headers, runtime)

    def update_user_guide_status_with_options(
        self,
        request: gemp20210413_models.UpdateUserGuideStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateUserGuideStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.guide_action):
            body['guideAction'] = request.guide_action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGuideStatus',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/update/guide/status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateUserGuideStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_guide_status_with_options_async(
        self,
        request: gemp20210413_models.UpdateUserGuideStatusRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.UpdateUserGuideStatusResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['clientToken'] = request.client_token
        if not UtilClient.is_unset(request.guide_action):
            body['guideAction'] = request.guide_action
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGuideStatus',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/user/update/guide/status',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.UpdateUserGuideStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_guide_status(
        self,
        request: gemp20210413_models.UpdateUserGuideStatusRequest,
    ) -> gemp20210413_models.UpdateUserGuideStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_user_guide_status_with_options(request, headers, runtime)

    async def update_user_guide_status_async(
        self,
        request: gemp20210413_models.UpdateUserGuideStatusRequest,
    ) -> gemp20210413_models.UpdateUserGuideStatusResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_user_guide_status_with_options_async(request, headers, runtime)

    def verify_route_rule_with_options(
        self,
        request: gemp20210413_models.VerifyRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.VerifyRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        if not UtilClient.is_unset(request.test_source_events):
            body['testSourceEvents'] = request.test_source_events
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/verify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.VerifyRouteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    async def verify_route_rule_with_options_async(
        self,
        request: gemp20210413_models.VerifyRouteRuleRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> gemp20210413_models.VerifyRouteRuleResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.route_rule_id):
            body['routeRuleId'] = request.route_rule_id
        if not UtilClient.is_unset(request.test_source_events):
            body['testSourceEvents'] = request.test_source_events
        req = open_api_models.OpenApiRequest(
            headers=headers,
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyRouteRule',
            version='2021-04-13',
            protocol='HTTPS',
            pathname=f'/routeRule/verify',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            gemp20210413_models.VerifyRouteRuleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def verify_route_rule(
        self,
        request: gemp20210413_models.VerifyRouteRuleRequest,
    ) -> gemp20210413_models.VerifyRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.verify_route_rule_with_options(request, headers, runtime)

    async def verify_route_rule_async(
        self,
        request: gemp20210413_models.VerifyRouteRuleRequest,
    ) -> gemp20210413_models.VerifyRouteRuleResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.verify_route_rule_with_options_async(request, headers, runtime)
