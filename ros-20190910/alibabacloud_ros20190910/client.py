# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_ros20190910 import models as main_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('ros', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_stack_operation_with_options(
        self,
        request: main_models.CancelStackOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelStackOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allowed_stack_operations):
            query['AllowedStackOperations'] = request.allowed_stack_operations
        if not DaraCore.is_null(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelStackOperation',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelStackOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_stack_operation_with_options_async(
        self,
        request: main_models.CancelStackOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelStackOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.allowed_stack_operations):
            query['AllowedStackOperations'] = request.allowed_stack_operations
        if not DaraCore.is_null(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelStackOperation',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelStackOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_stack_operation(
        self,
        request: main_models.CancelStackOperationRequest,
    ) -> main_models.CancelStackOperationResponse:
        runtime = RuntimeOptions()
        return self.cancel_stack_operation_with_options(request, runtime)

    async def cancel_stack_operation_async(
        self,
        request: main_models.CancelStackOperationRequest,
    ) -> main_models.CancelStackOperationResponse:
        runtime = RuntimeOptions()
        return await self.cancel_stack_operation_with_options_async(request, runtime)

    def cancel_update_stack_with_options(
        self,
        request: main_models.CancelUpdateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUpdateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelUpdateStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUpdateStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_update_stack_with_options_async(
        self,
        request: main_models.CancelUpdateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelUpdateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelUpdateStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelUpdateStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_update_stack(
        self,
        request: main_models.CancelUpdateStackRequest,
    ) -> main_models.CancelUpdateStackResponse:
        runtime = RuntimeOptions()
        return self.cancel_update_stack_with_options(request, runtime)

    async def cancel_update_stack_async(
        self,
        request: main_models.CancelUpdateStackRequest,
    ) -> main_models.CancelUpdateStackResponse:
        runtime = RuntimeOptions()
        return await self.cancel_update_stack_with_options_async(request, runtime)

    def continue_create_stack_with_options(
        self,
        request: main_models.ContinueCreateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinueCreateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.recreating_options):
            query['RecreatingOptions'] = request.recreating_options
        if not DaraCore.is_null(request.recreating_resources):
            query['RecreatingResources'] = request.recreating_resources
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_body):
            query['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinueCreateStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueCreateStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_create_stack_with_options_async(
        self,
        request: main_models.ContinueCreateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinueCreateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.mode):
            query['Mode'] = request.mode
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.recreating_options):
            query['RecreatingOptions'] = request.recreating_options
        if not DaraCore.is_null(request.recreating_resources):
            query['RecreatingResources'] = request.recreating_resources
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_body):
            query['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinueCreateStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueCreateStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_create_stack(
        self,
        request: main_models.ContinueCreateStackRequest,
    ) -> main_models.ContinueCreateStackResponse:
        runtime = RuntimeOptions()
        return self.continue_create_stack_with_options(request, runtime)

    async def continue_create_stack_async(
        self,
        request: main_models.ContinueCreateStackRequest,
    ) -> main_models.ContinueCreateStackResponse:
        runtime = RuntimeOptions()
        return await self.continue_create_stack_with_options_async(request, runtime)

    def create_aitask_with_options(
        self,
        request: main_models.CreateAITaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAITaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        body = {}
        if not DaraCore.is_null(request.template):
            body['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAITask',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAITaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_aitask_with_options_async(
        self,
        request: main_models.CreateAITaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAITaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.prompt):
            query['Prompt'] = request.prompt
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        body = {}
        if not DaraCore.is_null(request.template):
            body['Template'] = request.template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAITask',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAITaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_aitask(
        self,
        request: main_models.CreateAITaskRequest,
    ) -> main_models.CreateAITaskResponse:
        runtime = RuntimeOptions()
        return self.create_aitask_with_options(request, runtime)

    async def create_aitask_async(
        self,
        request: main_models.CreateAITaskRequest,
    ) -> main_models.CreateAITaskResponse:
        runtime = RuntimeOptions()
        return await self.create_aitask_with_options_async(request, runtime)

    def create_change_set_with_options(
        self,
        request: main_models.CreateChangeSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChangeSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not DaraCore.is_null(request.change_set_type):
            query['ChangeSetType'] = request.change_set_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resources_to_import):
            query['ResourcesToImport'] = request.resources_to_import
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_name):
            query['StackName'] = request.stack_name
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not DaraCore.is_null(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.taint_resources):
            query['TaintResources'] = request.taint_resources
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not DaraCore.is_null(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChangeSet',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_change_set_with_options_async(
        self,
        request: main_models.CreateChangeSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateChangeSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not DaraCore.is_null(request.change_set_type):
            query['ChangeSetType'] = request.change_set_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.resources_to_import):
            query['ResourcesToImport'] = request.resources_to_import
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_name):
            query['StackName'] = request.stack_name
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not DaraCore.is_null(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.taint_resources):
            query['TaintResources'] = request.taint_resources
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not DaraCore.is_null(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateChangeSet',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateChangeSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_change_set(
        self,
        request: main_models.CreateChangeSetRequest,
    ) -> main_models.CreateChangeSetResponse:
        runtime = RuntimeOptions()
        return self.create_change_set_with_options(request, runtime)

    async def create_change_set_async(
        self,
        request: main_models.CreateChangeSetRequest,
    ) -> main_models.CreateChangeSetResponse:
        runtime = RuntimeOptions()
        return await self.create_change_set_with_options_async(request, runtime)

    def create_diagnostic_with_options(
        self,
        request: main_models.CreateDiagnosticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnosticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.diagnostic_key):
            query['DiagnosticKey'] = request.diagnostic_key
        if not DaraCore.is_null(request.diagnostic_type):
            query['DiagnosticType'] = request.diagnostic_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnostic',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnosticResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_diagnostic_with_options_async(
        self,
        request: main_models.CreateDiagnosticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDiagnosticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.diagnostic_key):
            query['DiagnosticKey'] = request.diagnostic_key
        if not DaraCore.is_null(request.diagnostic_type):
            query['DiagnosticType'] = request.diagnostic_type
        if not DaraCore.is_null(request.lang):
            query['Lang'] = request.lang
        if not DaraCore.is_null(request.product):
            query['Product'] = request.product
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDiagnostic',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDiagnosticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_diagnostic(
        self,
        request: main_models.CreateDiagnosticRequest,
    ) -> main_models.CreateDiagnosticResponse:
        runtime = RuntimeOptions()
        return self.create_diagnostic_with_options(request, runtime)

    async def create_diagnostic_async(
        self,
        request: main_models.CreateDiagnosticRequest,
    ) -> main_models.CreateDiagnosticResponse:
        runtime = RuntimeOptions()
        return await self.create_diagnostic_with_options_async(request, runtime)

    def create_stack_with_options(
        self,
        request: main_models.CreateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_option):
            query['CreateOption'] = request.create_option
        if not DaraCore.is_null(request.create_options):
            query['CreateOptions'] = request.create_options
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.stack_name):
            query['StackName'] = request.stack_name
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stack_with_options_async(
        self,
        request: main_models.CreateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.create_option):
            query['CreateOption'] = request.create_option
        if not DaraCore.is_null(request.create_options):
            query['CreateOptions'] = request.create_options
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.stack_name):
            query['StackName'] = request.stack_name
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stack(
        self,
        request: main_models.CreateStackRequest,
    ) -> main_models.CreateStackResponse:
        runtime = RuntimeOptions()
        return self.create_stack_with_options(request, runtime)

    async def create_stack_async(
        self,
        request: main_models.CreateStackRequest,
    ) -> main_models.CreateStackResponse:
        runtime = RuntimeOptions()
        return await self.create_stack_with_options_async(request, runtime)

    def create_stack_group_with_options(
        self,
        tmp_req: main_models.CreateStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStackGroupResponse:
        tmp_req.validate()
        request = main_models.CreateStackGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auto_deployment):
            request.auto_deployment_shrink = Utils.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        query = {}
        if not DaraCore.is_null(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not DaraCore.is_null(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not DaraCore.is_null(request.capabilities):
            query['Capabilities'] = request.capabilities
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.stack_arn):
            query['StackArn'] = request.stack_arn
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stack_group_with_options_async(
        self,
        tmp_req: main_models.CreateStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStackGroupResponse:
        tmp_req.validate()
        request = main_models.CreateStackGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.auto_deployment):
            request.auto_deployment_shrink = Utils.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        query = {}
        if not DaraCore.is_null(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not DaraCore.is_null(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not DaraCore.is_null(request.capabilities):
            query['Capabilities'] = request.capabilities
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.stack_arn):
            query['StackArn'] = request.stack_arn
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStackGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stack_group(
        self,
        request: main_models.CreateStackGroupRequest,
    ) -> main_models.CreateStackGroupResponse:
        runtime = RuntimeOptions()
        return self.create_stack_group_with_options(request, runtime)

    async def create_stack_group_async(
        self,
        request: main_models.CreateStackGroupRequest,
    ) -> main_models.CreateStackGroupResponse:
        runtime = RuntimeOptions()
        return await self.create_stack_group_with_options_async(request, runtime)

    def create_stack_instances_with_options(
        self,
        tmp_req: main_models.CreateStackInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStackInstancesResponse:
        tmp_req.validate()
        request = main_models.CreateStackInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not DaraCore.is_null(tmp_req.deployment_targets):
            request.deployment_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deployment_options):
            query['DeploymentOptions'] = request.deployment_options
        if not DaraCore.is_null(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStackInstances',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stack_instances_with_options_async(
        self,
        tmp_req: main_models.CreateStackInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateStackInstancesResponse:
        tmp_req.validate()
        request = main_models.CreateStackInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not DaraCore.is_null(tmp_req.deployment_targets):
            request.deployment_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deployment_options):
            query['DeploymentOptions'] = request.deployment_options
        if not DaraCore.is_null(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateStackInstances',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateStackInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stack_instances(
        self,
        request: main_models.CreateStackInstancesRequest,
    ) -> main_models.CreateStackInstancesResponse:
        runtime = RuntimeOptions()
        return self.create_stack_instances_with_options(request, runtime)

    async def create_stack_instances_async(
        self,
        request: main_models.CreateStackInstancesRequest,
    ) -> main_models.CreateStackInstancesResponse:
        runtime = RuntimeOptions()
        return await self.create_stack_instances_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.validation_options):
            query['ValidationOptions'] = request.validation_options
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.validation_options):
            query['ValidationOptions'] = request.validation_options
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def create_template_scratch_with_options(
        self,
        tmp_req: main_models.CreateTemplateScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateScratchResponse:
        tmp_req.validate()
        request = main_models.CreateTemplateScratchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.preference_parameters):
            request.preference_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_resource_group):
            request.source_resource_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not DaraCore.is_null(tmp_req.source_resources):
            request.source_resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not DaraCore.is_null(tmp_req.source_tag):
            request.source_tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not DaraCore.is_null(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not DaraCore.is_null(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not DaraCore.is_null(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplateScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_scratch_with_options_async(
        self,
        tmp_req: main_models.CreateTemplateScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateScratchResponse:
        tmp_req.validate()
        request = main_models.CreateTemplateScratchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.preference_parameters):
            request.preference_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_resource_group):
            request.source_resource_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not DaraCore.is_null(tmp_req.source_resources):
            request.source_resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not DaraCore.is_null(tmp_req.source_tag):
            request.source_tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not DaraCore.is_null(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not DaraCore.is_null(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not DaraCore.is_null(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplateScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template_scratch(
        self,
        request: main_models.CreateTemplateScratchRequest,
    ) -> main_models.CreateTemplateScratchResponse:
        runtime = RuntimeOptions()
        return self.create_template_scratch_with_options(request, runtime)

    async def create_template_scratch_async(
        self,
        request: main_models.CreateTemplateScratchRequest,
    ) -> main_models.CreateTemplateScratchResponse:
        runtime = RuntimeOptions()
        return await self.create_template_scratch_with_options_async(request, runtime)

    def delete_change_set_with_options(
        self,
        request: main_models.DeleteChangeSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChangeSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChangeSet',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_change_set_with_options_async(
        self,
        request: main_models.DeleteChangeSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteChangeSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteChangeSet',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteChangeSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_change_set(
        self,
        request: main_models.DeleteChangeSetRequest,
    ) -> main_models.DeleteChangeSetResponse:
        runtime = RuntimeOptions()
        return self.delete_change_set_with_options(request, runtime)

    async def delete_change_set_async(
        self,
        request: main_models.DeleteChangeSetRequest,
    ) -> main_models.DeleteChangeSetResponse:
        runtime = RuntimeOptions()
        return await self.delete_change_set_with_options_async(request, runtime)

    def delete_diagnostic_with_options(
        self,
        request: main_models.DeleteDiagnosticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDiagnosticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDiagnostic',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDiagnosticResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_diagnostic_with_options_async(
        self,
        request: main_models.DeleteDiagnosticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDiagnosticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDiagnostic',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDiagnosticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_diagnostic(
        self,
        request: main_models.DeleteDiagnosticRequest,
    ) -> main_models.DeleteDiagnosticResponse:
        runtime = RuntimeOptions()
        return self.delete_diagnostic_with_options(request, runtime)

    async def delete_diagnostic_async(
        self,
        request: main_models.DeleteDiagnosticRequest,
    ) -> main_models.DeleteDiagnosticResponse:
        runtime = RuntimeOptions()
        return await self.delete_diagnostic_with_options_async(request, runtime)

    def delete_stack_with_options(
        self,
        request: main_models.DeleteStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_options):
            query['DeleteOptions'] = request.delete_options
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not DaraCore.is_null(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stack_with_options_async(
        self,
        request: main_models.DeleteStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delete_options):
            query['DeleteOptions'] = request.delete_options
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not DaraCore.is_null(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stack(
        self,
        request: main_models.DeleteStackRequest,
    ) -> main_models.DeleteStackResponse:
        runtime = RuntimeOptions()
        return self.delete_stack_with_options(request, runtime)

    async def delete_stack_async(
        self,
        request: main_models.DeleteStackRequest,
    ) -> main_models.DeleteStackResponse:
        runtime = RuntimeOptions()
        return await self.delete_stack_with_options_async(request, runtime)

    def delete_stack_group_with_options(
        self,
        request: main_models.DeleteStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStackGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stack_group_with_options_async(
        self,
        request: main_models.DeleteStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStackGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStackGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stack_group(
        self,
        request: main_models.DeleteStackGroupRequest,
    ) -> main_models.DeleteStackGroupResponse:
        runtime = RuntimeOptions()
        return self.delete_stack_group_with_options(request, runtime)

    async def delete_stack_group_async(
        self,
        request: main_models.DeleteStackGroupRequest,
    ) -> main_models.DeleteStackGroupResponse:
        runtime = RuntimeOptions()
        return await self.delete_stack_group_with_options_async(request, runtime)

    def delete_stack_instances_with_options(
        self,
        tmp_req: main_models.DeleteStackInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStackInstancesResponse:
        tmp_req.validate()
        request = main_models.DeleteStackInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not DaraCore.is_null(tmp_req.deployment_targets):
            request.deployment_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.retain_stacks):
            query['RetainStacks'] = request.retain_stacks
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStackInstances',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stack_instances_with_options_async(
        self,
        tmp_req: main_models.DeleteStackInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteStackInstancesResponse:
        tmp_req.validate()
        request = main_models.DeleteStackInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not DaraCore.is_null(tmp_req.deployment_targets):
            request.deployment_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.retain_stacks):
            query['RetainStacks'] = request.retain_stacks
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteStackInstances',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteStackInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stack_instances(
        self,
        request: main_models.DeleteStackInstancesRequest,
    ) -> main_models.DeleteStackInstancesResponse:
        runtime = RuntimeOptions()
        return self.delete_stack_instances_with_options(request, runtime)

    async def delete_stack_instances_async(
        self,
        request: main_models.DeleteStackInstancesRequest,
    ) -> main_models.DeleteStackInstancesResponse:
        runtime = RuntimeOptions()
        return await self.delete_stack_instances_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: main_models.DeleteTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: main_models.DeleteTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: main_models.DeleteTemplateRequest,
    ) -> main_models.DeleteTemplateResponse:
        runtime = RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_template_scratch_with_options(
        self,
        request: main_models.DeleteTemplateScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateScratchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplateScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_scratch_with_options_async(
        self,
        request: main_models.DeleteTemplateScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTemplateScratchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTemplateScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTemplateScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template_scratch(
        self,
        request: main_models.DeleteTemplateScratchRequest,
    ) -> main_models.DeleteTemplateScratchResponse:
        runtime = RuntimeOptions()
        return self.delete_template_scratch_with_options(request, runtime)

    async def delete_template_scratch_async(
        self,
        request: main_models.DeleteTemplateScratchRequest,
    ) -> main_models.DeleteTemplateScratchResponse:
        runtime = RuntimeOptions()
        return await self.delete_template_scratch_with_options_async(request, runtime)

    def deregister_resource_type_with_options(
        self,
        request: main_models.DeregisterResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeregisterResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeregisterResourceType',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeregisterResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_resource_type_with_options_async(
        self,
        request: main_models.DeregisterResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeregisterResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeregisterResourceType',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeregisterResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_resource_type(
        self,
        request: main_models.DeregisterResourceTypeRequest,
    ) -> main_models.DeregisterResourceTypeResponse:
        runtime = RuntimeOptions()
        return self.deregister_resource_type_with_options(request, runtime)

    async def deregister_resource_type_async(
        self,
        request: main_models.DeregisterResourceTypeRequest,
    ) -> main_models.DeregisterResourceTypeResponse:
        runtime = RuntimeOptions()
        return await self.deregister_resource_type_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def detect_stack_drift_with_options(
        self,
        request: main_models.DetectStackDriftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectStackDriftResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectStackDrift',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectStackDriftResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_stack_drift_with_options_async(
        self,
        request: main_models.DetectStackDriftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectStackDriftResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectStackDrift',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectStackDriftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_stack_drift(
        self,
        request: main_models.DetectStackDriftRequest,
    ) -> main_models.DetectStackDriftResponse:
        runtime = RuntimeOptions()
        return self.detect_stack_drift_with_options(request, runtime)

    async def detect_stack_drift_async(
        self,
        request: main_models.DetectStackDriftRequest,
    ) -> main_models.DetectStackDriftResponse:
        runtime = RuntimeOptions()
        return await self.detect_stack_drift_with_options_async(request, runtime)

    def detect_stack_group_drift_with_options(
        self,
        tmp_req: main_models.DetectStackGroupDriftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectStackGroupDriftResponse:
        tmp_req.validate()
        request = main_models.DetectStackGroupDriftShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectStackGroupDrift',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectStackGroupDriftResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_stack_group_drift_with_options_async(
        self,
        tmp_req: main_models.DetectStackGroupDriftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectStackGroupDriftResponse:
        tmp_req.validate()
        request = main_models.DetectStackGroupDriftShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectStackGroupDrift',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectStackGroupDriftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_stack_group_drift(
        self,
        request: main_models.DetectStackGroupDriftRequest,
    ) -> main_models.DetectStackGroupDriftResponse:
        runtime = RuntimeOptions()
        return self.detect_stack_group_drift_with_options(request, runtime)

    async def detect_stack_group_drift_async(
        self,
        request: main_models.DetectStackGroupDriftRequest,
    ) -> main_models.DetectStackGroupDriftResponse:
        runtime = RuntimeOptions()
        return await self.detect_stack_group_drift_with_options_async(request, runtime)

    def detect_stack_resource_drift_with_options(
        self,
        request: main_models.DetectStackResourceDriftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectStackResourceDriftResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectStackResourceDrift',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectStackResourceDriftResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_stack_resource_drift_with_options_async(
        self,
        request: main_models.DetectStackResourceDriftRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetectStackResourceDriftResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetectStackResourceDrift',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetectStackResourceDriftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_stack_resource_drift(
        self,
        request: main_models.DetectStackResourceDriftRequest,
    ) -> main_models.DetectStackResourceDriftResponse:
        runtime = RuntimeOptions()
        return self.detect_stack_resource_drift_with_options(request, runtime)

    async def detect_stack_resource_drift_async(
        self,
        request: main_models.DetectStackResourceDriftRequest,
    ) -> main_models.DetectStackResourceDriftResponse:
        runtime = RuntimeOptions()
        return await self.detect_stack_resource_drift_with_options_async(request, runtime)

    def enable_service_access_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableServiceAccessResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableServiceAccess',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableServiceAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_service_access_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableServiceAccessResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableServiceAccess',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableServiceAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_service_access(self) -> main_models.EnableServiceAccessResponse:
        runtime = RuntimeOptions()
        return self.enable_service_access_with_options(runtime)

    async def enable_service_access_async(self) -> main_models.EnableServiceAccessResponse:
        runtime = RuntimeOptions()
        return await self.enable_service_access_with_options_async(runtime)

    def enable_services_with_options(
        self,
        tmp_req: main_models.EnableServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableServicesResponse:
        tmp_req.validate()
        request = main_models.EnableServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.service_names):
            request.service_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.service_names, 'ServiceNames', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_names_shrink):
            query['ServiceNames'] = request.service_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableServices',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_services_with_options_async(
        self,
        tmp_req: main_models.EnableServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnableServicesResponse:
        tmp_req.validate()
        request = main_models.EnableServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.service_names):
            request.service_names_shrink = Utils.array_to_string_with_specified_style(tmp_req.service_names, 'ServiceNames', 'json')
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_names_shrink):
            query['ServiceNames'] = request.service_names_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnableServices',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_services(
        self,
        request: main_models.EnableServicesRequest,
    ) -> main_models.EnableServicesResponse:
        runtime = RuntimeOptions()
        return self.enable_services_with_options(request, runtime)

    async def enable_services_async(
        self,
        request: main_models.EnableServicesRequest,
    ) -> main_models.EnableServicesResponse:
        runtime = RuntimeOptions()
        return await self.enable_services_with_options_async(request, runtime)

    def execute_change_set_with_options(
        self,
        request: main_models.ExecuteChangeSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteChangeSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteChangeSet',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_change_set_with_options_async(
        self,
        request: main_models.ExecuteChangeSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteChangeSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteChangeSet',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteChangeSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_change_set(
        self,
        request: main_models.ExecuteChangeSetRequest,
    ) -> main_models.ExecuteChangeSetResponse:
        runtime = RuntimeOptions()
        return self.execute_change_set_with_options(request, runtime)

    async def execute_change_set_async(
        self,
        request: main_models.ExecuteChangeSetRequest,
    ) -> main_models.ExecuteChangeSetResponse:
        runtime = RuntimeOptions()
        return await self.execute_change_set_with_options_async(request, runtime)

    def generate_template_by_scratch_with_options(
        self,
        request: main_models.GenerateTemplateByScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTemplateByScratchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.provision_region_id):
            query['ProvisionRegionId'] = request.provision_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTemplateByScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTemplateByScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_template_by_scratch_with_options_async(
        self,
        request: main_models.GenerateTemplateByScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTemplateByScratchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.provision_region_id):
            query['ProvisionRegionId'] = request.provision_region_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTemplateByScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTemplateByScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_template_by_scratch(
        self,
        request: main_models.GenerateTemplateByScratchRequest,
    ) -> main_models.GenerateTemplateByScratchResponse:
        runtime = RuntimeOptions()
        return self.generate_template_by_scratch_with_options(request, runtime)

    async def generate_template_by_scratch_async(
        self,
        request: main_models.GenerateTemplateByScratchRequest,
    ) -> main_models.GenerateTemplateByScratchResponse:
        runtime = RuntimeOptions()
        return await self.generate_template_by_scratch_with_options_async(request, runtime)

    def generate_template_policy_with_options(
        self,
        request: main_models.GenerateTemplatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTemplatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.generate_options):
            query['GenerateOptions'] = request.generate_options
        if not DaraCore.is_null(request.operation_types):
            query['OperationTypes'] = request.operation_types
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.template_body):
            query['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTemplatePolicy',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTemplatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_template_policy_with_options_async(
        self,
        request: main_models.GenerateTemplatePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateTemplatePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.generate_options):
            query['GenerateOptions'] = request.generate_options
        if not DaraCore.is_null(request.operation_types):
            query['OperationTypes'] = request.operation_types
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.template_body):
            query['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateTemplatePolicy',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateTemplatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_template_policy(
        self,
        request: main_models.GenerateTemplatePolicyRequest,
    ) -> main_models.GenerateTemplatePolicyResponse:
        runtime = RuntimeOptions()
        return self.generate_template_policy_with_options(request, runtime)

    async def generate_template_policy_async(
        self,
        request: main_models.GenerateTemplatePolicyRequest,
    ) -> main_models.GenerateTemplatePolicyResponse:
        runtime = RuntimeOptions()
        return await self.generate_template_policy_with_options_async(request, runtime)

    def get_aitask_with_options(
        self,
        request: main_models.GetAITaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAITaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output_option):
            query['OutputOption'] = request.output_option
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAITask',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAITaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_aitask_with_options_async(
        self,
        request: main_models.GetAITaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAITaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output_option):
            query['OutputOption'] = request.output_option
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAITask',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAITaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_aitask(
        self,
        request: main_models.GetAITaskRequest,
    ) -> main_models.GetAITaskResponse:
        runtime = RuntimeOptions()
        return self.get_aitask_with_options(request, runtime)

    async def get_aitask_async(
        self,
        request: main_models.GetAITaskRequest,
    ) -> main_models.GetAITaskResponse:
        runtime = RuntimeOptions()
        return await self.get_aitask_with_options_async(request, runtime)

    def get_change_set_with_options(
        self,
        request: main_models.GetChangeSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChangeSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_template):
            query['ShowTemplate'] = request.show_template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChangeSet',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_change_set_with_options_async(
        self,
        request: main_models.GetChangeSetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetChangeSetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_template):
            query['ShowTemplate'] = request.show_template
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetChangeSet',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetChangeSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_change_set(
        self,
        request: main_models.GetChangeSetRequest,
    ) -> main_models.GetChangeSetResponse:
        runtime = RuntimeOptions()
        return self.get_change_set_with_options(request, runtime)

    async def get_change_set_async(
        self,
        request: main_models.GetChangeSetRequest,
    ) -> main_models.GetChangeSetResponse:
        runtime = RuntimeOptions()
        return await self.get_change_set_with_options_async(request, runtime)

    def get_diagnostic_with_options(
        self,
        request: main_models.GetDiagnosticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDiagnosticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiagnostic',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiagnosticResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_diagnostic_with_options_async(
        self,
        request: main_models.GetDiagnosticRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDiagnosticResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.report_id):
            query['ReportId'] = request.report_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDiagnostic',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDiagnosticResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_diagnostic(
        self,
        request: main_models.GetDiagnosticRequest,
    ) -> main_models.GetDiagnosticResponse:
        runtime = RuntimeOptions()
        return self.get_diagnostic_with_options(request, runtime)

    async def get_diagnostic_async(
        self,
        request: main_models.GetDiagnosticRequest,
    ) -> main_models.GetDiagnosticResponse:
        runtime = RuntimeOptions()
        return await self.get_diagnostic_with_options_async(request, runtime)

    def get_feature_details_with_options(
        self,
        request: main_models.GetFeatureDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature):
            query['Feature'] = request.feature
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureDetails',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_details_with_options_async(
        self,
        request: main_models.GetFeatureDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetFeatureDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.feature):
            query['Feature'] = request.feature
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetFeatureDetails',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetFeatureDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_details(
        self,
        request: main_models.GetFeatureDetailsRequest,
    ) -> main_models.GetFeatureDetailsResponse:
        runtime = RuntimeOptions()
        return self.get_feature_details_with_options(request, runtime)

    async def get_feature_details_async(
        self,
        request: main_models.GetFeatureDetailsRequest,
    ) -> main_models.GetFeatureDetailsResponse:
        runtime = RuntimeOptions()
        return await self.get_feature_details_with_options_async(request, runtime)

    def get_resource_type_with_options(
        self,
        request: main_models.GetResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceType',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_type_with_options_async(
        self,
        request: main_models.GetResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceType',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_type(
        self,
        request: main_models.GetResourceTypeRequest,
    ) -> main_models.GetResourceTypeResponse:
        runtime = RuntimeOptions()
        return self.get_resource_type_with_options(request, runtime)

    async def get_resource_type_async(
        self,
        request: main_models.GetResourceTypeRequest,
    ) -> main_models.GetResourceTypeResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_type_with_options_async(request, runtime)

    def get_resource_type_template_with_options(
        self,
        request: main_models.GetResourceTypeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceTypeTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_type_template_with_options_async(
        self,
        request: main_models.GetResourceTypeTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceTypeTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceTypeTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceTypeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_type_template(
        self,
        request: main_models.GetResourceTypeTemplateRequest,
    ) -> main_models.GetResourceTypeTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_resource_type_template_with_options(request, runtime)

    async def get_resource_type_template_async(
        self,
        request: main_models.GetResourceTypeTemplateRequest,
    ) -> main_models.GetResourceTypeTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_type_template_with_options_async(request, runtime)

    def get_service_access_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceAccessResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetServiceAccess',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceAccessResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_access_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceAccessResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetServiceAccess',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceAccessResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_access(self) -> main_models.GetServiceAccessResponse:
        runtime = RuntimeOptions()
        return self.get_service_access_with_options(runtime)

    async def get_service_access_async(self) -> main_models.GetServiceAccessResponse:
        runtime = RuntimeOptions()
        return await self.get_service_access_with_options_async(runtime)

    def get_service_provisions_with_options(
        self,
        request: main_models.GetServiceProvisionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceProvisionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.services):
            query['Services'] = request.services
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceProvisions',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceProvisionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_provisions_with_options_async(
        self,
        request: main_models.GetServiceProvisionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceProvisionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.services):
            query['Services'] = request.services
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceProvisions',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceProvisionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_provisions(
        self,
        request: main_models.GetServiceProvisionsRequest,
    ) -> main_models.GetServiceProvisionsResponse:
        runtime = RuntimeOptions()
        return self.get_service_provisions_with_options(request, runtime)

    async def get_service_provisions_async(
        self,
        request: main_models.GetServiceProvisionsRequest,
    ) -> main_models.GetServiceProvisionsResponse:
        runtime = RuntimeOptions()
        return await self.get_service_provisions_with_options_async(request, runtime)

    def get_stack_with_options(
        self,
        request: main_models.GetStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.log_option):
            query['LogOption'] = request.log_option
        if not DaraCore.is_null(request.output_option):
            query['OutputOption'] = request.output_option
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_resource_progress):
            query['ShowResourceProgress'] = request.show_resource_progress
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_with_options_async(
        self,
        request: main_models.GetStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.log_option):
            query['LogOption'] = request.log_option
        if not DaraCore.is_null(request.output_option):
            query['OutputOption'] = request.output_option
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_resource_progress):
            query['ShowResourceProgress'] = request.show_resource_progress
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack(
        self,
        request: main_models.GetStackRequest,
    ) -> main_models.GetStackResponse:
        runtime = RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    async def get_stack_async(
        self,
        request: main_models.GetStackRequest,
    ) -> main_models.GetStackResponse:
        runtime = RuntimeOptions()
        return await self.get_stack_with_options_async(request, runtime)

    def get_stack_drift_detection_status_with_options(
        self,
        request: main_models.GetStackDriftDetectionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackDriftDetectionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drift_detection_id):
            query['DriftDetectionId'] = request.drift_detection_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackDriftDetectionStatus',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackDriftDetectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_drift_detection_status_with_options_async(
        self,
        request: main_models.GetStackDriftDetectionStatusRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackDriftDetectionStatusResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.drift_detection_id):
            query['DriftDetectionId'] = request.drift_detection_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackDriftDetectionStatus',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackDriftDetectionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_drift_detection_status(
        self,
        request: main_models.GetStackDriftDetectionStatusRequest,
    ) -> main_models.GetStackDriftDetectionStatusResponse:
        runtime = RuntimeOptions()
        return self.get_stack_drift_detection_status_with_options(request, runtime)

    async def get_stack_drift_detection_status_async(
        self,
        request: main_models.GetStackDriftDetectionStatusRequest,
    ) -> main_models.GetStackDriftDetectionStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_stack_drift_detection_status_with_options_async(request, runtime)

    def get_stack_group_with_options(
        self,
        request: main_models.GetStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_id):
            query['StackGroupId'] = request.stack_group_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_group_with_options_async(
        self,
        request: main_models.GetStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_id):
            query['StackGroupId'] = request.stack_group_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_group(
        self,
        request: main_models.GetStackGroupRequest,
    ) -> main_models.GetStackGroupResponse:
        runtime = RuntimeOptions()
        return self.get_stack_group_with_options(request, runtime)

    async def get_stack_group_async(
        self,
        request: main_models.GetStackGroupRequest,
    ) -> main_models.GetStackGroupResponse:
        runtime = RuntimeOptions()
        return await self.get_stack_group_with_options_async(request, runtime)

    def get_stack_group_operation_with_options(
        self,
        request: main_models.GetStackGroupOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackGroupOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackGroupOperation',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackGroupOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_group_operation_with_options_async(
        self,
        request: main_models.GetStackGroupOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackGroupOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackGroupOperation',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackGroupOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_group_operation(
        self,
        request: main_models.GetStackGroupOperationRequest,
    ) -> main_models.GetStackGroupOperationResponse:
        runtime = RuntimeOptions()
        return self.get_stack_group_operation_with_options(request, runtime)

    async def get_stack_group_operation_async(
        self,
        request: main_models.GetStackGroupOperationRequest,
    ) -> main_models.GetStackGroupOperationResponse:
        runtime = RuntimeOptions()
        return await self.get_stack_group_operation_with_options_async(request, runtime)

    def get_stack_instance_with_options(
        self,
        request: main_models.GetStackInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output_option):
            query['OutputOption'] = request.output_option
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not DaraCore.is_null(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackInstance',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_instance_with_options_async(
        self,
        request: main_models.GetStackInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.output_option):
            query['OutputOption'] = request.output_option
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not DaraCore.is_null(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackInstance',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_instance(
        self,
        request: main_models.GetStackInstanceRequest,
    ) -> main_models.GetStackInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_stack_instance_with_options(request, runtime)

    async def get_stack_instance_async(
        self,
        request: main_models.GetStackInstanceRequest,
    ) -> main_models.GetStackInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_stack_instance_with_options_async(request, runtime)

    def get_stack_policy_with_options(
        self,
        request: main_models.GetStackPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackPolicy',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_policy_with_options_async(
        self,
        request: main_models.GetStackPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackPolicy',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_policy(
        self,
        request: main_models.GetStackPolicyRequest,
    ) -> main_models.GetStackPolicyResponse:
        runtime = RuntimeOptions()
        return self.get_stack_policy_with_options(request, runtime)

    async def get_stack_policy_async(
        self,
        request: main_models.GetStackPolicyRequest,
    ) -> main_models.GetStackPolicyResponse:
        runtime = RuntimeOptions()
        return await self.get_stack_policy_with_options_async(request, runtime)

    def get_stack_resource_with_options(
        self,
        request: main_models.GetStackResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_attributes):
            query['ResourceAttributes'] = request.resource_attributes
        if not DaraCore.is_null(request.show_resource_attributes):
            query['ShowResourceAttributes'] = request.show_resource_attributes
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackResource',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_resource_with_options_async(
        self,
        request: main_models.GetStackResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetStackResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_attributes):
            query['ResourceAttributes'] = request.resource_attributes
        if not DaraCore.is_null(request.show_resource_attributes):
            query['ShowResourceAttributes'] = request.show_resource_attributes
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackResource',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_resource(
        self,
        request: main_models.GetStackResourceRequest,
    ) -> main_models.GetStackResourceResponse:
        runtime = RuntimeOptions()
        return self.get_stack_resource_with_options(request, runtime)

    async def get_stack_resource_async(
        self,
        request: main_models.GetStackResourceRequest,
    ) -> main_models.GetStackResourceResponse:
        runtime = RuntimeOptions()
        return await self.get_stack_resource_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: main_models.GetTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.include_permission):
            query['IncludePermission'] = request.include_permission
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_stage):
            query['TemplateStage'] = request.template_stage
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: main_models.GetTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.include_permission):
            query['IncludePermission'] = request.include_permission
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_stage):
            query['TemplateStage'] = request.template_stage
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_template_estimate_cost_with_options(
        self,
        request: main_models.GetTemplateEstimateCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateEstimateCostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateEstimateCost',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateEstimateCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_estimate_cost_with_options_async(
        self,
        request: main_models.GetTemplateEstimateCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateEstimateCostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateEstimateCost',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateEstimateCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_estimate_cost(
        self,
        request: main_models.GetTemplateEstimateCostRequest,
    ) -> main_models.GetTemplateEstimateCostResponse:
        runtime = RuntimeOptions()
        return self.get_template_estimate_cost_with_options(request, runtime)

    async def get_template_estimate_cost_async(
        self,
        request: main_models.GetTemplateEstimateCostRequest,
    ) -> main_models.GetTemplateEstimateCostResponse:
        runtime = RuntimeOptions()
        return await self.get_template_estimate_cost_with_options_async(request, runtime)

    def get_template_parameter_constraints_with_options(
        self,
        tmp_req: main_models.GetTemplateParameterConstraintsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateParameterConstraintsResponse:
        tmp_req.validate()
        request = main_models.GetTemplateParameterConstraintsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters_key_filter):
            request.parameters_key_filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters_key_filter, 'ParametersKeyFilter', 'json')
        if not DaraCore.is_null(tmp_req.parameters_order):
            request.parameters_order_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters_order, 'ParametersOrder', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.parameters_key_filter_shrink):
            query['ParametersKeyFilter'] = request.parameters_key_filter_shrink
        if not DaraCore.is_null(request.parameters_order_shrink):
            query['ParametersOrder'] = request.parameters_order_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateParameterConstraints',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateParameterConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_parameter_constraints_with_options_async(
        self,
        tmp_req: main_models.GetTemplateParameterConstraintsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateParameterConstraintsResponse:
        tmp_req.validate()
        request = main_models.GetTemplateParameterConstraintsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters_key_filter):
            request.parameters_key_filter_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters_key_filter, 'ParametersKeyFilter', 'json')
        if not DaraCore.is_null(tmp_req.parameters_order):
            request.parameters_order_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters_order, 'ParametersOrder', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.parameters_key_filter_shrink):
            query['ParametersKeyFilter'] = request.parameters_key_filter_shrink
        if not DaraCore.is_null(request.parameters_order_shrink):
            query['ParametersOrder'] = request.parameters_order_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateParameterConstraints',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateParameterConstraintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_parameter_constraints(
        self,
        request: main_models.GetTemplateParameterConstraintsRequest,
    ) -> main_models.GetTemplateParameterConstraintsResponse:
        runtime = RuntimeOptions()
        return self.get_template_parameter_constraints_with_options(request, runtime)

    async def get_template_parameter_constraints_async(
        self,
        request: main_models.GetTemplateParameterConstraintsRequest,
    ) -> main_models.GetTemplateParameterConstraintsResponse:
        runtime = RuntimeOptions()
        return await self.get_template_parameter_constraints_with_options_async(request, runtime)

    def get_template_recommend_parameters_with_options(
        self,
        request: main_models.GetTemplateRecommendParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateRecommendParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_body):
            query['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateRecommendParameters',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateRecommendParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_recommend_parameters_with_options_async(
        self,
        request: main_models.GetTemplateRecommendParametersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateRecommendParametersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_body):
            query['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateRecommendParameters',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateRecommendParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_recommend_parameters(
        self,
        request: main_models.GetTemplateRecommendParametersRequest,
    ) -> main_models.GetTemplateRecommendParametersResponse:
        runtime = RuntimeOptions()
        return self.get_template_recommend_parameters_with_options(request, runtime)

    async def get_template_recommend_parameters_async(
        self,
        request: main_models.GetTemplateRecommendParametersRequest,
    ) -> main_models.GetTemplateRecommendParametersResponse:
        runtime = RuntimeOptions()
        return await self.get_template_recommend_parameters_with_options_async(request, runtime)

    def get_template_scratch_with_options(
        self,
        request: main_models.GetTemplateScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateScratchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_data_option):
            query['ShowDataOption'] = request.show_data_option
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_scratch_with_options_async(
        self,
        request: main_models.GetTemplateScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateScratchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.show_data_option):
            query['ShowDataOption'] = request.show_data_option
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_scratch(
        self,
        request: main_models.GetTemplateScratchRequest,
    ) -> main_models.GetTemplateScratchResponse:
        runtime = RuntimeOptions()
        return self.get_template_scratch_with_options(request, runtime)

    async def get_template_scratch_async(
        self,
        request: main_models.GetTemplateScratchRequest,
    ) -> main_models.GetTemplateScratchResponse:
        runtime = RuntimeOptions()
        return await self.get_template_scratch_with_options_async(request, runtime)

    def get_template_summary_with_options(
        self,
        request: main_models.GetTemplateSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_body):
            query['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateSummary',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_summary_with_options_async(
        self,
        request: main_models.GetTemplateSummaryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_body):
            query['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplateSummary',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_summary(
        self,
        request: main_models.GetTemplateSummaryRequest,
    ) -> main_models.GetTemplateSummaryResponse:
        runtime = RuntimeOptions()
        return self.get_template_summary_with_options(request, runtime)

    async def get_template_summary_async(
        self,
        request: main_models.GetTemplateSummaryRequest,
    ) -> main_models.GetTemplateSummaryResponse:
        runtime = RuntimeOptions()
        return await self.get_template_summary_with_options_async(request, runtime)

    def import_stacks_to_stack_group_with_options(
        self,
        tmp_req: main_models.ImportStacksToStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportStacksToStackGroupResponse:
        tmp_req.validate()
        request = main_models.ImportStacksToStackGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.resource_directory_folder_ids):
            request.resource_directory_folder_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_directory_folder_ids, 'ResourceDirectoryFolderIds', 'json')
        if not DaraCore.is_null(tmp_req.stack_arns):
            request.stack_arns_shrink = Utils.array_to_string_with_specified_style(tmp_req.stack_arns, 'StackArns', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_directory_folder_ids_shrink):
            query['ResourceDirectoryFolderIds'] = request.resource_directory_folder_ids_shrink
        if not DaraCore.is_null(request.stack_arns_shrink):
            query['StackArns'] = request.stack_arns_shrink
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportStacksToStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportStacksToStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def import_stacks_to_stack_group_with_options_async(
        self,
        tmp_req: main_models.ImportStacksToStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ImportStacksToStackGroupResponse:
        tmp_req.validate()
        request = main_models.ImportStacksToStackGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.resource_directory_folder_ids):
            request.resource_directory_folder_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.resource_directory_folder_ids, 'ResourceDirectoryFolderIds', 'json')
        if not DaraCore.is_null(tmp_req.stack_arns):
            request.stack_arns_shrink = Utils.array_to_string_with_specified_style(tmp_req.stack_arns, 'StackArns', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_directory_folder_ids_shrink):
            query['ResourceDirectoryFolderIds'] = request.resource_directory_folder_ids_shrink
        if not DaraCore.is_null(request.stack_arns_shrink):
            query['StackArns'] = request.stack_arns_shrink
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ImportStacksToStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ImportStacksToStackGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def import_stacks_to_stack_group(
        self,
        request: main_models.ImportStacksToStackGroupRequest,
    ) -> main_models.ImportStacksToStackGroupResponse:
        runtime = RuntimeOptions()
        return self.import_stacks_to_stack_group_with_options(request, runtime)

    async def import_stacks_to_stack_group_async(
        self,
        request: main_models.ImportStacksToStackGroupRequest,
    ) -> main_models.ImportStacksToStackGroupResponse:
        runtime = RuntimeOptions()
        return await self.import_stacks_to_stack_group_with_options_async(request, runtime)

    def list_aitask_events_with_options(
        self,
        request: main_models.ListAITaskEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAITaskEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAITaskEvents',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAITaskEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aitask_events_with_options_async(
        self,
        request: main_models.ListAITaskEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAITaskEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAITaskEvents',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAITaskEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aitask_events(
        self,
        request: main_models.ListAITaskEventsRequest,
    ) -> main_models.ListAITaskEventsResponse:
        runtime = RuntimeOptions()
        return self.list_aitask_events_with_options(request, runtime)

    async def list_aitask_events_async(
        self,
        request: main_models.ListAITaskEventsRequest,
    ) -> main_models.ListAITaskEventsResponse:
        runtime = RuntimeOptions()
        return await self.list_aitask_events_with_options_async(request, runtime)

    def list_aitasks_with_options(
        self,
        request: main_models.ListAITasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAITasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAITasks',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAITasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_aitasks_with_options_async(
        self,
        request: main_models.ListAITasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAITasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        if not DaraCore.is_null(request.task_type):
            query['TaskType'] = request.task_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAITasks',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAITasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_aitasks(
        self,
        request: main_models.ListAITasksRequest,
    ) -> main_models.ListAITasksResponse:
        runtime = RuntimeOptions()
        return self.list_aitasks_with_options(request, runtime)

    async def list_aitasks_async(
        self,
        request: main_models.ListAITasksRequest,
    ) -> main_models.ListAITasksResponse:
        runtime = RuntimeOptions()
        return await self.list_aitasks_with_options_async(request, runtime)

    def list_change_sets_with_options(
        self,
        request: main_models.ListChangeSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChangeSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not DaraCore.is_null(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChangeSets',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChangeSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_change_sets_with_options_async(
        self,
        request: main_models.ListChangeSetsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListChangeSetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not DaraCore.is_null(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not DaraCore.is_null(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListChangeSets',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListChangeSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_change_sets(
        self,
        request: main_models.ListChangeSetsRequest,
    ) -> main_models.ListChangeSetsResponse:
        runtime = RuntimeOptions()
        return self.list_change_sets_with_options(request, runtime)

    async def list_change_sets_async(
        self,
        request: main_models.ListChangeSetsRequest,
    ) -> main_models.ListChangeSetsResponse:
        runtime = RuntimeOptions()
        return await self.list_change_sets_with_options_async(request, runtime)

    def list_diagnostics_with_options(
        self,
        request: main_models.ListDiagnosticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnosticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.diagnostic_key):
            query['DiagnosticKey'] = request.diagnostic_key
        if not DaraCore.is_null(request.diagnostic_product):
            query['DiagnosticProduct'] = request.diagnostic_product
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnostics',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnosticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_diagnostics_with_options_async(
        self,
        request: main_models.ListDiagnosticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDiagnosticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.diagnostic_key):
            query['DiagnosticKey'] = request.diagnostic_key
        if not DaraCore.is_null(request.diagnostic_product):
            query['DiagnosticProduct'] = request.diagnostic_product
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDiagnostics',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDiagnosticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_diagnostics(
        self,
        request: main_models.ListDiagnosticsRequest,
    ) -> main_models.ListDiagnosticsResponse:
        runtime = RuntimeOptions()
        return self.list_diagnostics_with_options(request, runtime)

    async def list_diagnostics_async(
        self,
        request: main_models.ListDiagnosticsRequest,
    ) -> main_models.ListDiagnosticsResponse:
        runtime = RuntimeOptions()
        return await self.list_diagnostics_with_options_async(request, runtime)

    def list_resource_type_registrations_with_options(
        self,
        request: main_models.ListResourceTypeRegistrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypeRegistrationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.registration_id):
            query['RegistrationId'] = request.registration_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypeRegistrations',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypeRegistrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_type_registrations_with_options_async(
        self,
        request: main_models.ListResourceTypeRegistrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypeRegistrationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.registration_id):
            query['RegistrationId'] = request.registration_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypeRegistrations',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypeRegistrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_type_registrations(
        self,
        request: main_models.ListResourceTypeRegistrationsRequest,
    ) -> main_models.ListResourceTypeRegistrationsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_type_registrations_with_options(request, runtime)

    async def list_resource_type_registrations_async(
        self,
        request: main_models.ListResourceTypeRegistrationsRequest,
    ) -> main_models.ListResourceTypeRegistrationsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_type_registrations_with_options_async(request, runtime)

    def list_resource_type_versions_with_options(
        self,
        request: main_models.ListResourceTypeVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypeVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypeVersions',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypeVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_type_versions_with_options_async(
        self,
        request: main_models.ListResourceTypeVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypeVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypeVersions',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypeVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_type_versions(
        self,
        request: main_models.ListResourceTypeVersionsRequest,
    ) -> main_models.ListResourceTypeVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_type_versions_with_options(request, runtime)

    async def list_resource_type_versions_async(
        self,
        request: main_models.ListResourceTypeVersionsRequest,
    ) -> main_models.ListResourceTypeVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_type_versions_with_options_async(request, runtime)

    def list_resource_types_with_options(
        self,
        request: main_models.ListResourceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypes',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        request: main_models.ListResourceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.provider):
            query['Provider'] = request.provider
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypes',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_types(
        self,
        request: main_models.ListResourceTypesRequest,
    ) -> main_models.ListResourceTypesResponse:
        runtime = RuntimeOptions()
        return self.list_resource_types_with_options(request, runtime)

    async def list_resource_types_async(
        self,
        request: main_models.ListResourceTypesRequest,
    ) -> main_models.ListResourceTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_types_with_options_async(request, runtime)

    def list_stack_events_with_options(
        self,
        request: main_models.ListStackEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackEvents',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_events_with_options_async(
        self,
        request: main_models.ListStackEventsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackEventsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackEvents',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_events(
        self,
        request: main_models.ListStackEventsRequest,
    ) -> main_models.ListStackEventsResponse:
        runtime = RuntimeOptions()
        return self.list_stack_events_with_options(request, runtime)

    async def list_stack_events_async(
        self,
        request: main_models.ListStackEventsRequest,
    ) -> main_models.ListStackEventsResponse:
        runtime = RuntimeOptions()
        return await self.list_stack_events_with_options_async(request, runtime)

    def list_stack_group_operation_results_with_options(
        self,
        request: main_models.ListStackGroupOperationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackGroupOperationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackGroupOperationResults',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackGroupOperationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_group_operation_results_with_options_async(
        self,
        request: main_models.ListStackGroupOperationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackGroupOperationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackGroupOperationResults',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackGroupOperationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_group_operation_results(
        self,
        request: main_models.ListStackGroupOperationResultsRequest,
    ) -> main_models.ListStackGroupOperationResultsResponse:
        runtime = RuntimeOptions()
        return self.list_stack_group_operation_results_with_options(request, runtime)

    async def list_stack_group_operation_results_async(
        self,
        request: main_models.ListStackGroupOperationResultsRequest,
    ) -> main_models.ListStackGroupOperationResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_stack_group_operation_results_with_options_async(request, runtime)

    def list_stack_group_operations_with_options(
        self,
        request: main_models.ListStackGroupOperationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackGroupOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackGroupOperations',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackGroupOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_group_operations_with_options_async(
        self,
        request: main_models.ListStackGroupOperationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackGroupOperationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackGroupOperations',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackGroupOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_group_operations(
        self,
        request: main_models.ListStackGroupOperationsRequest,
    ) -> main_models.ListStackGroupOperationsResponse:
        runtime = RuntimeOptions()
        return self.list_stack_group_operations_with_options(request, runtime)

    async def list_stack_group_operations_async(
        self,
        request: main_models.ListStackGroupOperationsRequest,
    ) -> main_models.ListStackGroupOperationsResponse:
        runtime = RuntimeOptions()
        return await self.list_stack_group_operations_with_options_async(request, runtime)

    def list_stack_groups_with_options(
        self,
        request: main_models.ListStackGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackGroups',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_groups_with_options_async(
        self,
        request: main_models.ListStackGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackGroups',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_groups(
        self,
        request: main_models.ListStackGroupsRequest,
    ) -> main_models.ListStackGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_stack_groups_with_options(request, runtime)

    async def list_stack_groups_async(
        self,
        request: main_models.ListStackGroupsRequest,
    ) -> main_models.ListStackGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_stack_groups_with_options_async(request, runtime)

    def list_stack_instances_with_options(
        self,
        request: main_models.ListStackInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not DaraCore.is_null(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackInstances',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_instances_with_options_async(
        self,
        request: main_models.ListStackInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not DaraCore.is_null(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackInstances',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_instances(
        self,
        request: main_models.ListStackInstancesRequest,
    ) -> main_models.ListStackInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_stack_instances_with_options(request, runtime)

    async def list_stack_instances_async(
        self,
        request: main_models.ListStackInstancesRequest,
    ) -> main_models.ListStackInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_stack_instances_with_options_async(request, runtime)

    def list_stack_operation_risks_with_options(
        self,
        request: main_models.ListStackOperationRisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackOperationRisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not DaraCore.is_null(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListStackOperationRisks',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackOperationRisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_operation_risks_with_options_async(
        self,
        request: main_models.ListStackOperationRisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackOperationRisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.operation_type):
            query['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not DaraCore.is_null(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ListStackOperationRisks',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackOperationRisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_operation_risks(
        self,
        request: main_models.ListStackOperationRisksRequest,
    ) -> main_models.ListStackOperationRisksResponse:
        runtime = RuntimeOptions()
        return self.list_stack_operation_risks_with_options(request, runtime)

    async def list_stack_operation_risks_async(
        self,
        request: main_models.ListStackOperationRisksRequest,
    ) -> main_models.ListStackOperationRisksResponse:
        runtime = RuntimeOptions()
        return await self.list_stack_operation_risks_with_options_async(request, runtime)

    def list_stack_resource_drifts_with_options(
        self,
        request: main_models.ListStackResourceDriftsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackResourceDriftsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_drift_status):
            query['ResourceDriftStatus'] = request.resource_drift_status
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackResourceDrifts',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackResourceDriftsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_resource_drifts_with_options_async(
        self,
        request: main_models.ListStackResourceDriftsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackResourceDriftsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_drift_status):
            query['ResourceDriftStatus'] = request.resource_drift_status
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackResourceDrifts',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackResourceDriftsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_resource_drifts(
        self,
        request: main_models.ListStackResourceDriftsRequest,
    ) -> main_models.ListStackResourceDriftsResponse:
        runtime = RuntimeOptions()
        return self.list_stack_resource_drifts_with_options(request, runtime)

    async def list_stack_resource_drifts_async(
        self,
        request: main_models.ListStackResourceDriftsRequest,
    ) -> main_models.ListStackResourceDriftsResponse:
        runtime = RuntimeOptions()
        return await self.list_stack_resource_drifts_with_options_async(request, runtime)

    def list_stack_resources_with_options(
        self,
        request: main_models.ListStackResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_resources_with_options_async(
        self,
        request: main_models.ListStackResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStackResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStackResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStackResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_resources(
        self,
        request: main_models.ListStackResourcesRequest,
    ) -> main_models.ListStackResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_stack_resources_with_options(request, runtime)

    async def list_stack_resources_async(
        self,
        request: main_models.ListStackResourcesRequest,
    ) -> main_models.ListStackResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_stack_resources_with_options_async(request, runtime)

    def list_stacks_with_options(
        self,
        request: main_models.ListStacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_stack_id):
            query['ParentStackId'] = request.parent_stack_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_nested_stack):
            query['ShowNestedStack'] = request.show_nested_stack
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_ids):
            query['StackIds'] = request.stack_ids
        if not DaraCore.is_null(request.stack_name):
            query['StackName'] = request.stack_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStacks',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stacks_with_options_async(
        self,
        request: main_models.ListStacksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListStacksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.parent_stack_id):
            query['ParentStackId'] = request.parent_stack_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.show_nested_stack):
            query['ShowNestedStack'] = request.show_nested_stack
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_ids):
            query['StackIds'] = request.stack_ids
        if not DaraCore.is_null(request.stack_name):
            query['StackName'] = request.stack_name
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListStacks',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListStacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stacks(
        self,
        request: main_models.ListStacksRequest,
    ) -> main_models.ListStacksResponse:
        runtime = RuntimeOptions()
        return self.list_stacks_with_options(request, runtime)

    async def list_stacks_async(
        self,
        request: main_models.ListStacksRequest,
    ) -> main_models.ListStacksResponse:
        runtime = RuntimeOptions()
        return await self.list_stacks_with_options_async(request, runtime)

    def list_summaries_with_options(
        self,
        request: main_models.ListSummariesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSummariesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSummaries',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_summaries_with_options_async(
        self,
        request: main_models.ListSummariesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSummariesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSummaries',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_summaries(
        self,
        request: main_models.ListSummariesRequest,
    ) -> main_models.ListSummariesResponse:
        runtime = RuntimeOptions()
        return self.list_summaries_with_options(request, runtime)

    async def list_summaries_async(
        self,
        request: main_models.ListSummariesRequest,
    ) -> main_models.ListSummariesResponse:
        runtime = RuntimeOptions()
        return await self.list_summaries_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: main_models.ListTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: main_models.ListTagResourcesRequest,
    ) -> main_models.ListTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.key):
            query['Key'] = request.key
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_template_scratches_with_options(
        self,
        request: main_models.ListTemplateScratchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateScratchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateScratches',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateScratchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_scratches_with_options_async(
        self,
        request: main_models.ListTemplateScratchesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateScratchesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateScratches',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateScratchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_scratches(
        self,
        request: main_models.ListTemplateScratchesRequest,
    ) -> main_models.ListTemplateScratchesResponse:
        runtime = RuntimeOptions()
        return self.list_template_scratches_with_options(request, runtime)

    async def list_template_scratches_async(
        self,
        request: main_models.ListTemplateScratchesRequest,
    ) -> main_models.ListTemplateScratchesResponse:
        runtime = RuntimeOptions()
        return await self.list_template_scratches_with_options_async(request, runtime)

    def list_template_versions_with_options(
        self,
        request: main_models.ListTemplateVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateVersions',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_versions_with_options_async(
        self,
        request: main_models.ListTemplateVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplateVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplateVersions',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplateVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_versions(
        self,
        request: main_models.ListTemplateVersionsRequest,
    ) -> main_models.ListTemplateVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    async def list_template_versions_async(
        self,
        request: main_models.ListTemplateVersionsRequest,
    ) -> main_models.ListTemplateVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_template_versions_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: main_models.ListTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: main_models.ListTemplatesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTemplates',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: main_models.ListTemplatesRequest,
    ) -> main_models.ListTemplatesResponse:
        runtime = RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: main_models.MoveResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.MoveResourceGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'MoveResourceGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: main_models.MoveResourceGroupRequest,
    ) -> main_models.MoveResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def preview_stack_with_options(
        self,
        request: main_models.PreviewStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.enable_pre_config):
            query['EnablePreConfig'] = request.enable_pre_config
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_name):
            query['StackName'] = request.stack_name
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not DaraCore.is_null(request.taint_resources):
            query['TaintResources'] = request.taint_resources
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not DaraCore.is_null(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_stack_with_options_async(
        self,
        request: main_models.PreviewStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreviewStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.enable_pre_config):
            query['EnablePreConfig'] = request.enable_pre_config
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_name):
            query['StackName'] = request.stack_name
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not DaraCore.is_null(request.taint_resources):
            query['TaintResources'] = request.taint_resources
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not DaraCore.is_null(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not DaraCore.is_null(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_stack(
        self,
        request: main_models.PreviewStackRequest,
    ) -> main_models.PreviewStackResponse:
        runtime = RuntimeOptions()
        return self.preview_stack_with_options(request, runtime)

    async def preview_stack_async(
        self,
        request: main_models.PreviewStackRequest,
    ) -> main_models.PreviewStackResponse:
        runtime = RuntimeOptions()
        return await self.preview_stack_with_options_async(request, runtime)

    def register_resource_type_with_options(
        self,
        request: main_models.RegisterResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RegisterResourceType',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_resource_type_with_options_async(
        self,
        request: main_models.RegisterResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.entity_type):
            query['EntityType'] = request.entity_type
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RegisterResourceType',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_resource_type(
        self,
        request: main_models.RegisterResourceTypeRequest,
    ) -> main_models.RegisterResourceTypeResponse:
        runtime = RuntimeOptions()
        return self.register_resource_type_with_options(request, runtime)

    async def register_resource_type_async(
        self,
        request: main_models.RegisterResourceTypeRequest,
    ) -> main_models.RegisterResourceTypeResponse:
        runtime = RuntimeOptions()
        return await self.register_resource_type_with_options_async(request, runtime)

    def set_deletion_protection_with_options(
        self,
        request: main_models.SetDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDeletionProtection',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_deletion_protection_with_options_async(
        self,
        request: main_models.SetDeletionProtectionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetDeletionProtectionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetDeletionProtection',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_deletion_protection(
        self,
        request: main_models.SetDeletionProtectionRequest,
    ) -> main_models.SetDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    async def set_deletion_protection_async(
        self,
        request: main_models.SetDeletionProtectionRequest,
    ) -> main_models.SetDeletionProtectionResponse:
        runtime = RuntimeOptions()
        return await self.set_deletion_protection_with_options_async(request, runtime)

    def set_resource_type_with_options(
        self,
        request: main_models.SetResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_version_id):
            query['DefaultVersionId'] = request.default_version_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetResourceType',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_resource_type_with_options_async(
        self,
        request: main_models.SetResourceTypeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetResourceTypeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.default_version_id):
            query['DefaultVersionId'] = request.default_version_id
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetResourceType',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_resource_type(
        self,
        request: main_models.SetResourceTypeRequest,
    ) -> main_models.SetResourceTypeResponse:
        runtime = RuntimeOptions()
        return self.set_resource_type_with_options(request, runtime)

    async def set_resource_type_async(
        self,
        request: main_models.SetResourceTypeRequest,
    ) -> main_models.SetResourceTypeResponse:
        runtime = RuntimeOptions()
        return await self.set_resource_type_with_options_async(request, runtime)

    def set_stack_policy_with_options(
        self,
        request: main_models.SetStackPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetStackPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetStackPolicy',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetStackPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_stack_policy_with_options_async(
        self,
        request: main_models.SetStackPolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetStackPolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetStackPolicy',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetStackPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_stack_policy(
        self,
        request: main_models.SetStackPolicyRequest,
    ) -> main_models.SetStackPolicyResponse:
        runtime = RuntimeOptions()
        return self.set_stack_policy_with_options(request, runtime)

    async def set_stack_policy_async(
        self,
        request: main_models.SetStackPolicyRequest,
    ) -> main_models.SetStackPolicyResponse:
        runtime = RuntimeOptions()
        return await self.set_stack_policy_with_options_async(request, runtime)

    def set_template_permission_with_options(
        self,
        request: main_models.SetTemplatePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTemplatePermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.share_option):
            query['ShareOption'] = request.share_option
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.version_option):
            query['VersionOption'] = request.version_option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTemplatePermission',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTemplatePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_template_permission_with_options_async(
        self,
        request: main_models.SetTemplatePermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SetTemplatePermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not DaraCore.is_null(request.share_option):
            query['ShareOption'] = request.share_option
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.version_option):
            query['VersionOption'] = request.version_option
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SetTemplatePermission',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SetTemplatePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_template_permission(
        self,
        request: main_models.SetTemplatePermissionRequest,
    ) -> main_models.SetTemplatePermissionResponse:
        runtime = RuntimeOptions()
        return self.set_template_permission_with_options(request, runtime)

    async def set_template_permission_async(
        self,
        request: main_models.SetTemplatePermissionRequest,
    ) -> main_models.SetTemplatePermissionResponse:
        runtime = RuntimeOptions()
        return await self.set_template_permission_with_options_async(request, runtime)

    def signal_resource_with_options(
        self,
        request: main_models.SignalResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignalResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SignalResource',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignalResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def signal_resource_with_options_async(
        self,
        request: main_models.SignalResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SignalResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SignalResource',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SignalResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def signal_resource(
        self,
        request: main_models.SignalResourceRequest,
    ) -> main_models.SignalResourceResponse:
        runtime = RuntimeOptions()
        return self.signal_resource_with_options(request, runtime)

    async def signal_resource_async(
        self,
        request: main_models.SignalResourceRequest,
    ) -> main_models.SignalResourceResponse:
        runtime = RuntimeOptions()
        return await self.signal_resource_with_options_async(request, runtime)

    def stop_stack_group_operation_with_options(
        self,
        request: main_models.StopStackGroupOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopStackGroupOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopStackGroupOperation',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopStackGroupOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_stack_group_operation_with_options_async(
        self,
        request: main_models.StopStackGroupOperationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopStackGroupOperationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_id):
            query['OperationId'] = request.operation_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopStackGroupOperation',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopStackGroupOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_stack_group_operation(
        self,
        request: main_models.StopStackGroupOperationRequest,
    ) -> main_models.StopStackGroupOperationResponse:
        runtime = RuntimeOptions()
        return self.stop_stack_group_operation_with_options(request, runtime)

    async def stop_stack_group_operation_async(
        self,
        request: main_models.StopStackGroupOperationRequest,
    ) -> main_models.StopStackGroupOperationResponse:
        runtime = RuntimeOptions()
        return await self.stop_stack_group_operation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: main_models.TagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'TagResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: main_models.TagResourcesRequest,
    ) -> main_models.TagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: main_models.UntagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UntagResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.all):
            query['All'] = request.all
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UntagResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: main_models.UntagResourcesRequest,
    ) -> main_models.UntagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_stack_with_options(
        self,
        request: main_models.UpdateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dry_run_options):
            query['DryRunOptions'] = request.dry_run_options
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not DaraCore.is_null(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.taint_resources):
            query['TaintResources'] = request.taint_resources
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not DaraCore.is_null(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_stack_with_options_async(
        self,
        request: main_models.UpdateStackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.dry_run_options):
            query['DryRunOptions'] = request.dry_run_options
        if not DaraCore.is_null(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not DaraCore.is_null(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not DaraCore.is_null(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not DaraCore.is_null(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not DaraCore.is_null(request.tags):
            query['Tags'] = request.tags
        if not DaraCore.is_null(request.taint_resources):
            query['TaintResources'] = request.taint_resources
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not DaraCore.is_null(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStack',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_stack(
        self,
        request: main_models.UpdateStackRequest,
    ) -> main_models.UpdateStackResponse:
        runtime = RuntimeOptions()
        return self.update_stack_with_options(request, runtime)

    async def update_stack_async(
        self,
        request: main_models.UpdateStackRequest,
    ) -> main_models.UpdateStackResponse:
        runtime = RuntimeOptions()
        return await self.update_stack_with_options_async(request, runtime)

    def update_stack_group_with_options(
        self,
        tmp_req: main_models.UpdateStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStackGroupResponse:
        tmp_req.validate()
        request = main_models.UpdateStackGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not DaraCore.is_null(tmp_req.auto_deployment):
            request.auto_deployment_shrink = Utils.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        if not DaraCore.is_null(tmp_req.deployment_targets):
            request.deployment_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not DaraCore.is_null(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not DaraCore.is_null(request.capabilities):
            query['Capabilities'] = request.capabilities
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deployment_options):
            query['DeploymentOptions'] = request.deployment_options
        if not DaraCore.is_null(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_stack_group_with_options_async(
        self,
        tmp_req: main_models.UpdateStackGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStackGroupResponse:
        tmp_req.validate()
        request = main_models.UpdateStackGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not DaraCore.is_null(tmp_req.auto_deployment):
            request.auto_deployment_shrink = Utils.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        if not DaraCore.is_null(tmp_req.deployment_targets):
            request.deployment_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not DaraCore.is_null(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not DaraCore.is_null(request.capabilities):
            query['Capabilities'] = request.capabilities
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deployment_options):
            query['DeploymentOptions'] = request.deployment_options
        if not DaraCore.is_null(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStackGroup',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStackGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_stack_group(
        self,
        request: main_models.UpdateStackGroupRequest,
    ) -> main_models.UpdateStackGroupResponse:
        runtime = RuntimeOptions()
        return self.update_stack_group_with_options(request, runtime)

    async def update_stack_group_async(
        self,
        request: main_models.UpdateStackGroupRequest,
    ) -> main_models.UpdateStackGroupResponse:
        runtime = RuntimeOptions()
        return await self.update_stack_group_with_options_async(request, runtime)

    def update_stack_instances_with_options(
        self,
        tmp_req: main_models.UpdateStackInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStackInstancesResponse:
        tmp_req.validate()
        request = main_models.UpdateStackInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not DaraCore.is_null(tmp_req.deployment_targets):
            request.deployment_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStackInstances',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_stack_instances_with_options_async(
        self,
        tmp_req: main_models.UpdateStackInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStackInstancesResponse:
        tmp_req.validate()
        request = main_models.UpdateStackInstancesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not DaraCore.is_null(tmp_req.deployment_targets):
            request.deployment_targets_shrink = Utils.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not DaraCore.is_null(tmp_req.operation_preferences):
            request.operation_preferences_shrink = Utils.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not DaraCore.is_null(tmp_req.region_ids):
            request.region_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not DaraCore.is_null(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not DaraCore.is_null(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not DaraCore.is_null(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not DaraCore.is_null(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not DaraCore.is_null(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStackInstances',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStackInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_stack_instances(
        self,
        request: main_models.UpdateStackInstancesRequest,
    ) -> main_models.UpdateStackInstancesResponse:
        runtime = RuntimeOptions()
        return self.update_stack_instances_with_options(request, runtime)

    async def update_stack_instances_async(
        self,
        request: main_models.UpdateStackInstancesRequest,
    ) -> main_models.UpdateStackInstancesResponse:
        runtime = RuntimeOptions()
        return await self.update_stack_instances_with_options_async(request, runtime)

    def update_stack_template_by_resources_with_options(
        self,
        request: main_models.UpdateStackTemplateByResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStackTemplateByResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_format):
            query['TemplateFormat'] = request.template_format
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStackTemplateByResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStackTemplateByResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_stack_template_by_resources_with_options_async(
        self,
        request: main_models.UpdateStackTemplateByResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateStackTemplateByResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.stack_id):
            query['StackId'] = request.stack_id
        if not DaraCore.is_null(request.template_format):
            query['TemplateFormat'] = request.template_format
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateStackTemplateByResources',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateStackTemplateByResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_stack_template_by_resources(
        self,
        request: main_models.UpdateStackTemplateByResourcesRequest,
    ) -> main_models.UpdateStackTemplateByResourcesResponse:
        runtime = RuntimeOptions()
        return self.update_stack_template_by_resources_with_options(request, runtime)

    async def update_stack_template_by_resources_async(
        self,
        request: main_models.UpdateStackTemplateByResourcesRequest,
    ) -> main_models.UpdateStackTemplateByResourcesResponse:
        runtime = RuntimeOptions()
        return await self.update_stack_template_by_resources_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: main_models.UpdateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.is_draft):
            query['IsDraft'] = request.is_draft
        if not DaraCore.is_null(request.rotate_strategy):
            query['RotateStrategy'] = request.rotate_strategy
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.validation_options):
            query['ValidationOptions'] = request.validation_options
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: main_models.UpdateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.is_draft):
            query['IsDraft'] = request.is_draft
        if not DaraCore.is_null(request.rotate_strategy):
            query['RotateStrategy'] = request.rotate_strategy
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.validation_options):
            query['ValidationOptions'] = request.validation_options
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: main_models.UpdateTemplateRequest,
    ) -> main_models.UpdateTemplateResponse:
        runtime = RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def update_template_scratch_with_options(
        self,
        tmp_req: main_models.UpdateTemplateScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateScratchResponse:
        tmp_req.validate()
        request = main_models.UpdateTemplateScratchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.preference_parameters):
            request.preference_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_resource_group):
            request.source_resource_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not DaraCore.is_null(tmp_req.source_resources):
            request.source_resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not DaraCore.is_null(tmp_req.source_tag):
            request.source_tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not DaraCore.is_null(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not DaraCore.is_null(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not DaraCore.is_null(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplateScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_scratch_with_options_async(
        self,
        tmp_req: main_models.UpdateTemplateScratchRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTemplateScratchResponse:
        tmp_req.validate()
        request = main_models.UpdateTemplateScratchShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.preference_parameters):
            request.preference_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not DaraCore.is_null(tmp_req.source_resource_group):
            request.source_resource_group_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not DaraCore.is_null(tmp_req.source_resources):
            request.source_resources_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not DaraCore.is_null(tmp_req.source_tag):
            request.source_tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not DaraCore.is_null(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not DaraCore.is_null(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not DaraCore.is_null(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not DaraCore.is_null(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not DaraCore.is_null(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTemplateScratch',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTemplateScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template_scratch(
        self,
        request: main_models.UpdateTemplateScratchRequest,
    ) -> main_models.UpdateTemplateScratchResponse:
        runtime = RuntimeOptions()
        return self.update_template_scratch_with_options(request, runtime)

    async def update_template_scratch_async(
        self,
        request: main_models.UpdateTemplateScratchRequest,
    ) -> main_models.UpdateTemplateScratchResponse:
        runtime = RuntimeOptions()
        return await self.update_template_scratch_with_options_async(request, runtime)

    def validate_template_with_options(
        self,
        request: main_models.ValidateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.update_info_options):
            query['UpdateInfoOptions'] = request.update_info_options
        if not DaraCore.is_null(request.validation_option):
            query['ValidationOption'] = request.validation_option
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_template_with_options_async(
        self,
        request: main_models.ValidateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.template_url):
            query['TemplateURL'] = request.template_url
        if not DaraCore.is_null(request.update_info_options):
            query['UpdateInfoOptions'] = request.update_info_options
        if not DaraCore.is_null(request.validation_option):
            query['ValidationOption'] = request.validation_option
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query),
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ValidateTemplate',
            version = '2019-09-10',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_template(
        self,
        request: main_models.ValidateTemplateRequest,
    ) -> main_models.ValidateTemplateResponse:
        runtime = RuntimeOptions()
        return self.validate_template_with_options(request, runtime)

    async def validate_template_async(
        self,
        request: main_models.ValidateTemplateRequest,
    ) -> main_models.ValidateTemplateResponse:
        runtime = RuntimeOptions()
        return await self.validate_template_with_options_async(request, runtime)
