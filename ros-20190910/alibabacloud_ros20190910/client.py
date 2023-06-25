# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_ros20190910 import models as ros20190910_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_stack_operation_with_options(
        self,
        request: ros20190910_models.CancelStackOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CancelStackOperationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allowed_stack_operations):
            query['AllowedStackOperations'] = request.allowed_stack_operations
        if not UtilClient.is_unset(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelStackOperation',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CancelStackOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_stack_operation_with_options_async(
        self,
        request: ros20190910_models.CancelStackOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CancelStackOperationResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allowed_stack_operations):
            query['AllowedStackOperations'] = request.allowed_stack_operations
        if not UtilClient.is_unset(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelStackOperation',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CancelStackOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_stack_operation(
        self,
        request: ros20190910_models.CancelStackOperationRequest,
    ) -> ros20190910_models.CancelStackOperationResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_stack_operation_with_options(request, runtime)

    async def cancel_stack_operation_async(
        self,
        request: ros20190910_models.CancelStackOperationRequest,
    ) -> ros20190910_models.CancelStackOperationResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_stack_operation_with_options_async(request, runtime)

    def cancel_update_stack_with_options(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelUpdateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CancelUpdateStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_update_stack_with_options_async(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cancel_type):
            query['CancelType'] = request.cancel_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelUpdateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CancelUpdateStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_update_stack(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.cancel_update_stack_with_options(request, runtime)

    async def cancel_update_stack_async(
        self,
        request: ros20190910_models.CancelUpdateStackRequest,
    ) -> ros20190910_models.CancelUpdateStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.cancel_update_stack_with_options_async(request, runtime)

    def continue_create_stack_with_options(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        """
        This topic provides an example on how to continue to create a stack that failed to be created. In this example, the stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***` failed to be created in the China (Hangzhou) region.
        
        @param request: ContinueCreateStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinueCreateStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.recreating_options):
            query['RecreatingOptions'] = request.recreating_options
        if not UtilClient.is_unset(request.recreating_resources):
            query['RecreatingResources'] = request.recreating_resources
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinueCreateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ContinueCreateStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_create_stack_with_options_async(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        """
        This topic provides an example on how to continue to create a stack that failed to be created. In this example, the stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***` failed to be created in the China (Hangzhou) region.
        
        @param request: ContinueCreateStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinueCreateStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.recreating_options):
            query['RecreatingOptions'] = request.recreating_options
        if not UtilClient.is_unset(request.recreating_resources):
            query['RecreatingResources'] = request.recreating_resources
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinueCreateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ContinueCreateStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_create_stack(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        """
        This topic provides an example on how to continue to create a stack that failed to be created. In this example, the stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***` failed to be created in the China (Hangzhou) region.
        
        @param request: ContinueCreateStackRequest
        @return: ContinueCreateStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.continue_create_stack_with_options(request, runtime)

    async def continue_create_stack_async(
        self,
        request: ros20190910_models.ContinueCreateStackRequest,
    ) -> ros20190910_models.ContinueCreateStackResponse:
        """
        This topic provides an example on how to continue to create a stack that failed to be created. In this example, the stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***` failed to be created in the China (Hangzhou) region.
        
        @param request: ContinueCreateStackRequest
        @return: ContinueCreateStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.continue_create_stack_with_options_async(request, runtime)

    def create_change_set_with_options(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateChangeSetResponse:
        """
        You can create and execute change sets to update running stacks. For more information about change sets, see [Overview](~~156038~~).
        ## Limits
        - A stack can contain up to 20 change sets.
        - Change sets reflect only the changes of stacks. Change sets do not reflect whether stacks are updated.
        - You cannot use change sets to check the following items: whether the upper limit of your account is reached, whether to update resources that cannot be updated, and whether your account is not granted the required permissions to modify resources. These items may cause stack updates to fail. If stacks fail to be updated, Resource Orchestration Service (ROS) attempts to roll back the resources to the original status.
        This topic provides an example on how to create a change set. In this example, a change set named `MyChangeSet` is created in the `China (Hangzhou)` region. The change set is used to change the template body of a stack to `{"ROSTemplateFormatVersion":"2015-09-01"}`. The ID of the stack is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****`.
        
        @param request: CreateChangeSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChangeSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not UtilClient.is_unset(request.change_set_type):
            query['ChangeSetType'] = request.change_set_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not UtilClient.is_unset(request.resources_to_import):
            query['ResourcesToImport'] = request.resources_to_import
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not UtilClient.is_unset(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not UtilClient.is_unset(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_change_set_with_options_async(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateChangeSetResponse:
        """
        You can create and execute change sets to update running stacks. For more information about change sets, see [Overview](~~156038~~).
        ## Limits
        - A stack can contain up to 20 change sets.
        - Change sets reflect only the changes of stacks. Change sets do not reflect whether stacks are updated.
        - You cannot use change sets to check the following items: whether the upper limit of your account is reached, whether to update resources that cannot be updated, and whether your account is not granted the required permissions to modify resources. These items may cause stack updates to fail. If stacks fail to be updated, Resource Orchestration Service (ROS) attempts to roll back the resources to the original status.
        This topic provides an example on how to create a change set. In this example, a change set named `MyChangeSet` is created in the `China (Hangzhou)` region. The change set is used to change the template body of a stack to `{"ROSTemplateFormatVersion":"2015-09-01"}`. The ID of the stack is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****`.
        
        @param request: CreateChangeSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateChangeSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not UtilClient.is_unset(request.change_set_type):
            query['ChangeSetType'] = request.change_set_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not UtilClient.is_unset(request.resources_to_import):
            query['ResourcesToImport'] = request.resources_to_import
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not UtilClient.is_unset(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not UtilClient.is_unset(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateChangeSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_change_set(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
    ) -> ros20190910_models.CreateChangeSetResponse:
        """
        You can create and execute change sets to update running stacks. For more information about change sets, see [Overview](~~156038~~).
        ## Limits
        - A stack can contain up to 20 change sets.
        - Change sets reflect only the changes of stacks. Change sets do not reflect whether stacks are updated.
        - You cannot use change sets to check the following items: whether the upper limit of your account is reached, whether to update resources that cannot be updated, and whether your account is not granted the required permissions to modify resources. These items may cause stack updates to fail. If stacks fail to be updated, Resource Orchestration Service (ROS) attempts to roll back the resources to the original status.
        This topic provides an example on how to create a change set. In this example, a change set named `MyChangeSet` is created in the `China (Hangzhou)` region. The change set is used to change the template body of a stack to `{"ROSTemplateFormatVersion":"2015-09-01"}`. The ID of the stack is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****`.
        
        @param request: CreateChangeSetRequest
        @return: CreateChangeSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_change_set_with_options(request, runtime)

    async def create_change_set_async(
        self,
        request: ros20190910_models.CreateChangeSetRequest,
    ) -> ros20190910_models.CreateChangeSetResponse:
        """
        You can create and execute change sets to update running stacks. For more information about change sets, see [Overview](~~156038~~).
        ## Limits
        - A stack can contain up to 20 change sets.
        - Change sets reflect only the changes of stacks. Change sets do not reflect whether stacks are updated.
        - You cannot use change sets to check the following items: whether the upper limit of your account is reached, whether to update resources that cannot be updated, and whether your account is not granted the required permissions to modify resources. These items may cause stack updates to fail. If stacks fail to be updated, Resource Orchestration Service (ROS) attempts to roll back the resources to the original status.
        This topic provides an example on how to create a change set. In this example, a change set named `MyChangeSet` is created in the `China (Hangzhou)` region. The change set is used to change the template body of a stack to `{"ROSTemplateFormatVersion":"2015-09-01"}`. The ID of the stack is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****`.
        
        @param request: CreateChangeSetRequest
        @return: CreateChangeSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_change_set_with_options_async(request, runtime)

    def create_stack_with_options(
        self,
        request: ros20190910_models.CreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackResponse:
        """
        | Error code | Error message | HTTPS status code | Description |
        | ---------- | ------------- | ----------------- | ----------- |
        | CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains circular dependencies. reason indicates the cause of the error. |
        | InvalidSchema | {reason}. | 400 | The error message returned because the format of the template is invalid. reason indicates the cause of the error. |
        | InvalidTemplateAttribute | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource property that is referenced in the Outputs section of the template is invalid. resource indicates the resource name. name indicates the property name. |
        | InvalidTemplatePropertyType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the resource property that is defined in a section of the template is invalid. resource indicates the resource name. section indicates the section name. |
        | InvalidTemplateReference | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name. referencer indicates the referencer name. |
        | InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
        | InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is invalid. reason indicates the cause of the error. |
        | StackValidationFailed | {reason}. | 400 | The error message returned because the stack failed to be validated. reason indicates the cause of the error. |
        | UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter name. |
        | UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is specified for the specified parameter that is defined in the template. name indicates the parameter name. |
        | ActionInProgress | Stack {name} already has an action ({action}) in progress. | 409 | The error message returned because the stack is being changed. name indicates the name or ID of the stack. action indicates the change operation. |
        | StackExists | The Stack ({name}) already exists. | 409 | The error message returned because a stack that has the same name already exists. name indicates the stack name. |
        | TemplateNotFound | The Template ({ ID }) could not be found. | 404 | The error message returned because the specified template does not exist. ID indicates the template ID. |
        | TemplateNotFound | The Template { ID } with version { version } could not be found. | 404 | The error message returned because the specified template or template version does not exist. ID indicates the template ID. version indicates the template version. |
        
        @param request: CreateStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_option):
            query['CreateOption'] = request.create_option
        if not UtilClient.is_unset(request.create_options):
            query['CreateOptions'] = request.create_options
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stack_with_options_async(
        self,
        request: ros20190910_models.CreateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackResponse:
        """
        | Error code | Error message | HTTPS status code | Description |
        | ---------- | ------------- | ----------------- | ----------- |
        | CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains circular dependencies. reason indicates the cause of the error. |
        | InvalidSchema | {reason}. | 400 | The error message returned because the format of the template is invalid. reason indicates the cause of the error. |
        | InvalidTemplateAttribute | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource property that is referenced in the Outputs section of the template is invalid. resource indicates the resource name. name indicates the property name. |
        | InvalidTemplatePropertyType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the resource property that is defined in a section of the template is invalid. resource indicates the resource name. section indicates the section name. |
        | InvalidTemplateReference | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name. referencer indicates the referencer name. |
        | InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
        | InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is invalid. reason indicates the cause of the error. |
        | StackValidationFailed | {reason}. | 400 | The error message returned because the stack failed to be validated. reason indicates the cause of the error. |
        | UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter name. |
        | UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is specified for the specified parameter that is defined in the template. name indicates the parameter name. |
        | ActionInProgress | Stack {name} already has an action ({action}) in progress. | 409 | The error message returned because the stack is being changed. name indicates the name or ID of the stack. action indicates the change operation. |
        | StackExists | The Stack ({name}) already exists. | 409 | The error message returned because a stack that has the same name already exists. name indicates the stack name. |
        | TemplateNotFound | The Template ({ ID }) could not be found. | 404 | The error message returned because the specified template does not exist. ID indicates the template ID. |
        | TemplateNotFound | The Template { ID } with version { version } could not be found. | 404 | The error message returned because the specified template or template version does not exist. ID indicates the template ID. version indicates the template version. |
        
        @param request: CreateStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.create_option):
            query['CreateOption'] = request.create_option
        if not UtilClient.is_unset(request.create_options):
            query['CreateOptions'] = request.create_options
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.notification_urls):
            query['NotificationURLs'] = request.notification_urls
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stack(
        self,
        request: ros20190910_models.CreateStackRequest,
    ) -> ros20190910_models.CreateStackResponse:
        """
        | Error code | Error message | HTTPS status code | Description |
        | ---------- | ------------- | ----------------- | ----------- |
        | CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains circular dependencies. reason indicates the cause of the error. |
        | InvalidSchema | {reason}. | 400 | The error message returned because the format of the template is invalid. reason indicates the cause of the error. |
        | InvalidTemplateAttribute | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource property that is referenced in the Outputs section of the template is invalid. resource indicates the resource name. name indicates the property name. |
        | InvalidTemplatePropertyType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the resource property that is defined in a section of the template is invalid. resource indicates the resource name. section indicates the section name. |
        | InvalidTemplateReference | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name. referencer indicates the referencer name. |
        | InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
        | InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is invalid. reason indicates the cause of the error. |
        | StackValidationFailed | {reason}. | 400 | The error message returned because the stack failed to be validated. reason indicates the cause of the error. |
        | UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter name. |
        | UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is specified for the specified parameter that is defined in the template. name indicates the parameter name. |
        | ActionInProgress | Stack {name} already has an action ({action}) in progress. | 409 | The error message returned because the stack is being changed. name indicates the name or ID of the stack. action indicates the change operation. |
        | StackExists | The Stack ({name}) already exists. | 409 | The error message returned because a stack that has the same name already exists. name indicates the stack name. |
        | TemplateNotFound | The Template ({ ID }) could not be found. | 404 | The error message returned because the specified template does not exist. ID indicates the template ID. |
        | TemplateNotFound | The Template { ID } with version { version } could not be found. | 404 | The error message returned because the specified template or template version does not exist. ID indicates the template ID. version indicates the template version. |
        
        @param request: CreateStackRequest
        @return: CreateStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_stack_with_options(request, runtime)

    async def create_stack_async(
        self,
        request: ros20190910_models.CreateStackRequest,
    ) -> ros20190910_models.CreateStackResponse:
        """
        | Error code | Error message | HTTPS status code | Description |
        | ---------- | ------------- | ----------------- | ----------- |
        | CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains circular dependencies. reason indicates the cause of the error. |
        | InvalidSchema | {reason}. | 400 | The error message returned because the format of the template is invalid. reason indicates the cause of the error. |
        | InvalidTemplateAttribute | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource property that is referenced in the Outputs section of the template is invalid. resource indicates the resource name. name indicates the property name. |
        | InvalidTemplatePropertyType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the resource property that is defined in a section of the template is invalid. resource indicates the resource name. section indicates the section name. |
        | InvalidTemplateReference | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name. referencer indicates the referencer name. |
        | InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
        | InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is invalid. reason indicates the cause of the error. |
        | StackValidationFailed | {reason}. | 400 | The error message returned because the stack failed to be validated. reason indicates the cause of the error. |
        | UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter name. |
        | UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is specified for the specified parameter that is defined in the template. name indicates the parameter name. |
        | ActionInProgress | Stack {name} already has an action ({action}) in progress. | 409 | The error message returned because the stack is being changed. name indicates the name or ID of the stack. action indicates the change operation. |
        | StackExists | The Stack ({name}) already exists. | 409 | The error message returned because a stack that has the same name already exists. name indicates the stack name. |
        | TemplateNotFound | The Template ({ ID }) could not be found. | 404 | The error message returned because the specified template does not exist. ID indicates the template ID. |
        | TemplateNotFound | The Template { ID } with version { version } could not be found. | 404 | The error message returned because the specified template or template version does not exist. ID indicates the template ID. version indicates the template version. |
        
        @param request: CreateStackRequest
        @return: CreateStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_with_options_async(request, runtime)

    def create_stack_group_with_options(
        self,
        tmp_req: ros20190910_models.CreateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackGroupResponse:
        """
        | Error code | Error message | HTTP status code | Description |
        | ---------- | ------------- | ---------------- | ----------- |
        | CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains circular dependencies. reason indicates the cause of the error. |
        | InvalidSchema | {reason}. | 400 | The error message returned because the template format is invalid. reason indicates the cause of the error. |
        | InvalidTemplateAttribute | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource property that is referenced in the Outputs section of the template is invalid. resource indicates the resource name. name indicates the property name. |
        | InvalidTemplatePropertyType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the resource property that is defined in a template section is invalid. resource indicates the resource name. section indicates the section name. |
        | InvalidTemplateReference | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name. referencer indicates the referencer name. |
        | InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
        | InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is invalid. reason indicates the cause of the error. |
        | UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter name. |
        | UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is specified for a parameter in the template. name indicates the parameter name. |
        | StackGroupExists | The StackGroup ({name}) already exists. | 409 | The error message returned because a stack group that has the same name already exists. name indicates the name of the stack group. |
        | TemplateNotFound | The Tempalte ({ ID }) could not be found. | 404 | The error message returned because the template does not exist. ID indicates the ID of the template. |
        | TemplateNotFound | The Template { ID } with version { version } could not be found. | 404 | The error message returned because the specified template or template version does not exist. ID indicates the ID of the template. version indicates the version of the template. |
        
        @param tmp_req: CreateStackGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStackGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateStackGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auto_deployment):
            request.auto_deployment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        query = {}
        if not UtilClient.is_unset(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not UtilClient.is_unset(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not UtilClient.is_unset(request.capabilities):
            query['Capabilities'] = request.capabilities
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stack_group_with_options_async(
        self,
        tmp_req: ros20190910_models.CreateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackGroupResponse:
        """
        | Error code | Error message | HTTP status code | Description |
        | ---------- | ------------- | ---------------- | ----------- |
        | CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains circular dependencies. reason indicates the cause of the error. |
        | InvalidSchema | {reason}. | 400 | The error message returned because the template format is invalid. reason indicates the cause of the error. |
        | InvalidTemplateAttribute | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource property that is referenced in the Outputs section of the template is invalid. resource indicates the resource name. name indicates the property name. |
        | InvalidTemplatePropertyType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the resource property that is defined in a template section is invalid. resource indicates the resource name. section indicates the section name. |
        | InvalidTemplateReference | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name. referencer indicates the referencer name. |
        | InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
        | InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is invalid. reason indicates the cause of the error. |
        | UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter name. |
        | UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is specified for a parameter in the template. name indicates the parameter name. |
        | StackGroupExists | The StackGroup ({name}) already exists. | 409 | The error message returned because a stack group that has the same name already exists. name indicates the name of the stack group. |
        | TemplateNotFound | The Tempalte ({ ID }) could not be found. | 404 | The error message returned because the template does not exist. ID indicates the ID of the template. |
        | TemplateNotFound | The Template { ID } with version { version } could not be found. | 404 | The error message returned because the specified template or template version does not exist. ID indicates the ID of the template. version indicates the version of the template. |
        
        @param tmp_req: CreateStackGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStackGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateStackGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.auto_deployment):
            request.auto_deployment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        query = {}
        if not UtilClient.is_unset(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not UtilClient.is_unset(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not UtilClient.is_unset(request.capabilities):
            query['Capabilities'] = request.capabilities
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stack_group(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
    ) -> ros20190910_models.CreateStackGroupResponse:
        """
        | Error code | Error message | HTTP status code | Description |
        | ---------- | ------------- | ---------------- | ----------- |
        | CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains circular dependencies. reason indicates the cause of the error. |
        | InvalidSchema | {reason}. | 400 | The error message returned because the template format is invalid. reason indicates the cause of the error. |
        | InvalidTemplateAttribute | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource property that is referenced in the Outputs section of the template is invalid. resource indicates the resource name. name indicates the property name. |
        | InvalidTemplatePropertyType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the resource property that is defined in a template section is invalid. resource indicates the resource name. section indicates the section name. |
        | InvalidTemplateReference | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name. referencer indicates the referencer name. |
        | InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
        | InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is invalid. reason indicates the cause of the error. |
        | UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter name. |
        | UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is specified for a parameter in the template. name indicates the parameter name. |
        | StackGroupExists | The StackGroup ({name}) already exists. | 409 | The error message returned because a stack group that has the same name already exists. name indicates the name of the stack group. |
        | TemplateNotFound | The Tempalte ({ ID }) could not be found. | 404 | The error message returned because the template does not exist. ID indicates the ID of the template. |
        | TemplateNotFound | The Template { ID } with version { version } could not be found. | 404 | The error message returned because the specified template or template version does not exist. ID indicates the ID of the template. version indicates the version of the template. |
        
        @param request: CreateStackGroupRequest
        @return: CreateStackGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_stack_group_with_options(request, runtime)

    async def create_stack_group_async(
        self,
        request: ros20190910_models.CreateStackGroupRequest,
    ) -> ros20190910_models.CreateStackGroupResponse:
        """
        | Error code | Error message | HTTP status code | Description |
        | ---------- | ------------- | ---------------- | ----------- |
        | CircularDependency | Circular Dependency Found: {reason}. | 400 | The error message returned because the template contains circular dependencies. reason indicates the cause of the error. |
        | InvalidSchema | {reason}. | 400 | The error message returned because the template format is invalid. reason indicates the cause of the error. |
        | InvalidTemplateAttribute | The Referenced Attribute ({resource} {name}) is incorrect. | 400 | The error message returned because the resource property that is referenced in the Outputs section of the template is invalid. resource indicates the resource name. name indicates the property name. |
        | InvalidTemplatePropertyType | The specified value type of ({resource} {section}) is incorrect. | 400 | The error message returned because the type of the resource property that is defined in a template section is invalid. resource indicates the resource name. section indicates the section name. |
        | InvalidTemplateReference | The specified reference "{name}" (in {referencer}) is incorrect. | 400 | The error message returned because the template contains an invalid reference. name indicates the reference name. referencer indicates the referencer name. |
        | InvalidTemplateSection | The template section is invalid: {section}. | 400 | The error message returned because the template contains an invalid section. section indicates the section name. |
        | InvalidTemplateVersion | The template version is invalid: {reason}. | 400 | The error message returned because the template version is invalid. reason indicates the cause of the error. |
        | UnknownUserParameter | The Parameter ({name}) was not defined in template. | 400 | The error message returned because the specified parameter is not defined in the template. name indicates the parameter name. |
        | UserParameterMissing | The Parameter {name} was not provided. | 400 | The error message returned because no value is specified for a parameter in the template. name indicates the parameter name. |
        | StackGroupExists | The StackGroup ({name}) already exists. | 409 | The error message returned because a stack group that has the same name already exists. name indicates the name of the stack group. |
        | TemplateNotFound | The Tempalte ({ ID }) could not be found. | 404 | The error message returned because the template does not exist. ID indicates the ID of the template. |
        | TemplateNotFound | The Template { ID } with version { version } could not be found. | 404 | The error message returned because the specified template or template version does not exist. ID indicates the ID of the template. version indicates the version of the template. |
        
        @param request: CreateStackGroupRequest
        @return: CreateStackGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_group_with_options_async(request, runtime)

    def create_stack_instances_with_options(
        self,
        tmp_req: ros20190910_models.CreateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        """
        Before you call this operation, make sure that a stack group is created. For more information, see [CreateStackGroup](~~151333~~).
        This topic provides an example on how to create stacks in a stack group. In this example, stacks are created in a stack group named `MyStackGroup`. The stacks are created within the `151266687691****` and `141261387191****` Alibaba Cloud accounts in the China (Hangzhou) and China (Beijing) regions. The stack group is granted self-managed permissions and created in the China (Hangzhou) region.
        
        @param tmp_req: CreateStackInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStackInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_stack_instances_with_options_async(
        self,
        tmp_req: ros20190910_models.CreateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        """
        Before you call this operation, make sure that a stack group is created. For more information, see [CreateStackGroup](~~151333~~).
        This topic provides an example on how to create stacks in a stack group. In this example, stacks are created in a stack group named `MyStackGroup`. The stacks are created within the `151266687691****` and `141261387191****` Alibaba Cloud accounts in the China (Hangzhou) and China (Beijing) regions. The stack group is granted self-managed permissions and created in the China (Hangzhou) region.
        
        @param tmp_req: CreateStackInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateStackInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateStackInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_stack_instances(
        self,
        request: ros20190910_models.CreateStackInstancesRequest,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        """
        Before you call this operation, make sure that a stack group is created. For more information, see [CreateStackGroup](~~151333~~).
        This topic provides an example on how to create stacks in a stack group. In this example, stacks are created in a stack group named `MyStackGroup`. The stacks are created within the `151266687691****` and `141261387191****` Alibaba Cloud accounts in the China (Hangzhou) and China (Beijing) regions. The stack group is granted self-managed permissions and created in the China (Hangzhou) region.
        
        @param request: CreateStackInstancesRequest
        @return: CreateStackInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_stack_instances_with_options(request, runtime)

    async def create_stack_instances_async(
        self,
        request: ros20190910_models.CreateStackInstancesRequest,
    ) -> ros20190910_models.CreateStackInstancesResponse:
        """
        Before you call this operation, make sure that a stack group is created. For more information, see [CreateStackGroup](~~151333~~).
        This topic provides an example on how to create stacks in a stack group. In this example, stacks are created in a stack group named `MyStackGroup`. The stacks are created within the `151266687691****` and `141261387191****` Alibaba Cloud accounts in the China (Hangzhou) and China (Beijing) regions. The stack group is granted self-managed permissions and created in the China (Hangzhou) region.
        
        @param request: CreateStackInstancesRequest
        @return: CreateStackInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_stack_instances_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: ros20190910_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateTemplateResponse:
        """
        This topic provides an example on how to create a template. In this example, a template named `MyTemplate` is created in the `China (Hangzhou)` region. The `TemplateBody` parameter is set to `{"ROSTemplateFormatVersion": "2015-09-01"}`.
        
        @param request: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: ros20190910_models.CreateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateTemplateResponse:
        """
        This topic provides an example on how to create a template. In this example, a template named `MyTemplate` is created in the `China (Hangzhou)` region. The `TemplateBody` parameter is set to `{"ROSTemplateFormatVersion": "2015-09-01"}`.
        
        @param request: CreateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: ros20190910_models.CreateTemplateRequest,
    ) -> ros20190910_models.CreateTemplateResponse:
        """
        This topic provides an example on how to create a template. In this example, a template named `MyTemplate` is created in the `China (Hangzhou)` region. The `TemplateBody` parameter is set to `{"ROSTemplateFormatVersion": "2015-09-01"}`.
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: ros20190910_models.CreateTemplateRequest,
    ) -> ros20190910_models.CreateTemplateResponse:
        """
        This topic provides an example on how to create a template. In this example, a template named `MyTemplate` is created in the `China (Hangzhou)` region. The `TemplateBody` parameter is set to `{"ROSTemplateFormatVersion": "2015-09-01"}`.
        
        @param request: CreateTemplateRequest
        @return: CreateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def create_template_scratch_with_options(
        self,
        tmp_req: ros20190910_models.CreateTemplateScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateTemplateScratchResponse:
        """
        You can call this operation to create a scenario that allows you to specify a resource scope on a visualized interface and easily replicate and manage the resources that you specify. For more information about scenarios, see [Overview](~~352074~~).
        This topic provides an example on how to create a scenario of the resource replication type in the China (Hangzhou) region. In this example, a virtual private cloud (VPC) named `vpc-bp1m6fww66xbntjyc****` is replicated by using the scenario.
        
        @param tmp_req: CreateTemplateScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateScratchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateTemplateScratchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.preference_parameters):
            request.preference_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_resource_group):
            request.source_resource_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not UtilClient.is_unset(tmp_req.source_resources):
            request.source_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not UtilClient.is_unset(tmp_req.source_tag):
            request.source_tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not UtilClient.is_unset(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not UtilClient.is_unset(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not UtilClient.is_unset(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_scratch_with_options_async(
        self,
        tmp_req: ros20190910_models.CreateTemplateScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.CreateTemplateScratchResponse:
        """
        You can call this operation to create a scenario that allows you to specify a resource scope on a visualized interface and easily replicate and manage the resources that you specify. For more information about scenarios, see [Overview](~~352074~~).
        This topic provides an example on how to create a scenario of the resource replication type in the China (Hangzhou) region. In this example, a virtual private cloud (VPC) named `vpc-bp1m6fww66xbntjyc****` is replicated by using the scenario.
        
        @param tmp_req: CreateTemplateScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateTemplateScratchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.CreateTemplateScratchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.preference_parameters):
            request.preference_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_resource_group):
            request.source_resource_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not UtilClient.is_unset(tmp_req.source_resources):
            request.source_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not UtilClient.is_unset(tmp_req.source_tag):
            request.source_tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not UtilClient.is_unset(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not UtilClient.is_unset(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not UtilClient.is_unset(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.CreateTemplateScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template_scratch(
        self,
        request: ros20190910_models.CreateTemplateScratchRequest,
    ) -> ros20190910_models.CreateTemplateScratchResponse:
        """
        You can call this operation to create a scenario that allows you to specify a resource scope on a visualized interface and easily replicate and manage the resources that you specify. For more information about scenarios, see [Overview](~~352074~~).
        This topic provides an example on how to create a scenario of the resource replication type in the China (Hangzhou) region. In this example, a virtual private cloud (VPC) named `vpc-bp1m6fww66xbntjyc****` is replicated by using the scenario.
        
        @param request: CreateTemplateScratchRequest
        @return: CreateTemplateScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_template_scratch_with_options(request, runtime)

    async def create_template_scratch_async(
        self,
        request: ros20190910_models.CreateTemplateScratchRequest,
    ) -> ros20190910_models.CreateTemplateScratchResponse:
        """
        You can call this operation to create a scenario that allows you to specify a resource scope on a visualized interface and easily replicate and manage the resources that you specify. For more information about scenarios, see [Overview](~~352074~~).
        This topic provides an example on how to create a scenario of the resource replication type in the China (Hangzhou) region. In this example, a virtual private cloud (VPC) named `vpc-bp1m6fww66xbntjyc****` is replicated by using the scenario.
        
        @param request: CreateTemplateScratchRequest
        @return: CreateTemplateScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_template_scratch_with_options_async(request, runtime)

    def delete_change_set_with_options(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        """
        Limits:
        *   Before you call this operation, make sure that the following requirements are met:
        *   The status of the change set is CREATE_COMPLETE, CREATE_FAILED, or DELETE_FAILED.
        *   The execution status is UNAVAILABLE or AVAILABLE.
        *   After a change set is executed, other change sets associated with the same stack as this change set are deleted.
        *   After a stack is deleted, change sets associated with the stack are deleted.
        *   If a change set of the CREATE type is deleted, you must delete stacks associated with the change set.
        In this example, a change set in the China (Hangzhou) region whose ID is `1f6521a4-05af-4975-afe9-bc4b45ad****` is deleted.
        
        @param request: DeleteChangeSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChangeSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_change_set_with_options_async(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        """
        Limits:
        *   Before you call this operation, make sure that the following requirements are met:
        *   The status of the change set is CREATE_COMPLETE, CREATE_FAILED, or DELETE_FAILED.
        *   The execution status is UNAVAILABLE or AVAILABLE.
        *   After a change set is executed, other change sets associated with the same stack as this change set are deleted.
        *   After a stack is deleted, change sets associated with the stack are deleted.
        *   If a change set of the CREATE type is deleted, you must delete stacks associated with the change set.
        In this example, a change set in the China (Hangzhou) region whose ID is `1f6521a4-05af-4975-afe9-bc4b45ad****` is deleted.
        
        @param request: DeleteChangeSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteChangeSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteChangeSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_change_set(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        """
        Limits:
        *   Before you call this operation, make sure that the following requirements are met:
        *   The status of the change set is CREATE_COMPLETE, CREATE_FAILED, or DELETE_FAILED.
        *   The execution status is UNAVAILABLE or AVAILABLE.
        *   After a change set is executed, other change sets associated with the same stack as this change set are deleted.
        *   After a stack is deleted, change sets associated with the stack are deleted.
        *   If a change set of the CREATE type is deleted, you must delete stacks associated with the change set.
        In this example, a change set in the China (Hangzhou) region whose ID is `1f6521a4-05af-4975-afe9-bc4b45ad****` is deleted.
        
        @param request: DeleteChangeSetRequest
        @return: DeleteChangeSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_change_set_with_options(request, runtime)

    async def delete_change_set_async(
        self,
        request: ros20190910_models.DeleteChangeSetRequest,
    ) -> ros20190910_models.DeleteChangeSetResponse:
        """
        Limits:
        *   Before you call this operation, make sure that the following requirements are met:
        *   The status of the change set is CREATE_COMPLETE, CREATE_FAILED, or DELETE_FAILED.
        *   The execution status is UNAVAILABLE or AVAILABLE.
        *   After a change set is executed, other change sets associated with the same stack as this change set are deleted.
        *   After a stack is deleted, change sets associated with the stack are deleted.
        *   If a change set of the CREATE type is deleted, you must delete stacks associated with the change set.
        In this example, a change set in the China (Hangzhou) region whose ID is `1f6521a4-05af-4975-afe9-bc4b45ad****` is deleted.
        
        @param request: DeleteChangeSetRequest
        @return: DeleteChangeSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_change_set_with_options_async(request, runtime)

    def delete_stack_with_options(
        self,
        request: ros20190910_models.DeleteStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_options):
            query['DeleteOptions'] = request.delete_options
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stack_with_options_async(
        self,
        request: ros20190910_models.DeleteStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_options):
            query['DeleteOptions'] = request.delete_options
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stack(
        self,
        request: ros20190910_models.DeleteStackRequest,
    ) -> ros20190910_models.DeleteStackResponse:
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_with_options(request, runtime)

    async def delete_stack_async(
        self,
        request: ros20190910_models.DeleteStackRequest,
    ) -> ros20190910_models.DeleteStackResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_with_options_async(request, runtime)

    def delete_stack_group_with_options(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        """
        A stack group can be deleted only when the stack group does not contain stacks. You can call the [DeleteStackInstances](~~151715~~) operation to delete stacks.
        This topic provides an example on how to delete a stack group. In this example, a stack group named `MyStackGroup` in the China (Hangzhou) region is deleted.
        
        @param request: DeleteStackGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStackGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stack_group_with_options_async(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        """
        A stack group can be deleted only when the stack group does not contain stacks. You can call the [DeleteStackInstances](~~151715~~) operation to delete stacks.
        This topic provides an example on how to delete a stack group. In this example, a stack group named `MyStackGroup` in the China (Hangzhou) region is deleted.
        
        @param request: DeleteStackGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStackGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stack_group(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        """
        A stack group can be deleted only when the stack group does not contain stacks. You can call the [DeleteStackInstances](~~151715~~) operation to delete stacks.
        This topic provides an example on how to delete a stack group. In this example, a stack group named `MyStackGroup` in the China (Hangzhou) region is deleted.
        
        @param request: DeleteStackGroupRequest
        @return: DeleteStackGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_group_with_options(request, runtime)

    async def delete_stack_group_async(
        self,
        request: ros20190910_models.DeleteStackGroupRequest,
    ) -> ros20190910_models.DeleteStackGroupResponse:
        """
        A stack group can be deleted only when the stack group does not contain stacks. You can call the [DeleteStackInstances](~~151715~~) operation to delete stacks.
        This topic provides an example on how to delete a stack group. In this example, a stack group named `MyStackGroup` in the China (Hangzhou) region is deleted.
        
        @param request: DeleteStackGroupRequest
        @return: DeleteStackGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_group_with_options_async(request, runtime)

    def delete_stack_instances_with_options(
        self,
        tmp_req: ros20190910_models.DeleteStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        """
        This topic provides an example on how to delete stacks from a stack group. In this example, the stacks that are deployed within the `151266687691***` Alibaba Cloud account in the China (Beijing) region are deleted from a stack group named `MyStackGroup`. The stack group is deployed in the China (Hangzhou) region and granted self-managed permissions.
        
        @param tmp_req: DeleteStackInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStackInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DeleteStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.retain_stacks):
            query['RetainStacks'] = request.retain_stacks
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_stack_instances_with_options_async(
        self,
        tmp_req: ros20190910_models.DeleteStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        """
        This topic provides an example on how to delete stacks from a stack group. In this example, the stacks that are deployed within the `151266687691***` Alibaba Cloud account in the China (Beijing) region are deleted from a stack group named `MyStackGroup`. The stack group is deployed in the China (Hangzhou) region and granted self-managed permissions.
        
        @param tmp_req: DeleteStackInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteStackInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DeleteStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.retain_stacks):
            query['RetainStacks'] = request.retain_stacks
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteStackInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_stack_instances(
        self,
        request: ros20190910_models.DeleteStackInstancesRequest,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        """
        This topic provides an example on how to delete stacks from a stack group. In this example, the stacks that are deployed within the `151266687691***` Alibaba Cloud account in the China (Beijing) region are deleted from a stack group named `MyStackGroup`. The stack group is deployed in the China (Hangzhou) region and granted self-managed permissions.
        
        @param request: DeleteStackInstancesRequest
        @return: DeleteStackInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_stack_instances_with_options(request, runtime)

    async def delete_stack_instances_async(
        self,
        request: ros20190910_models.DeleteStackInstancesRequest,
    ) -> ros20190910_models.DeleteStackInstancesResponse:
        """
        This topic provides an example on how to delete stacks from a stack group. In this example, the stacks that are deployed within the `151266687691***` Alibaba Cloud account in the China (Beijing) region are deleted from a stack group named `MyStackGroup`. The stack group is deployed in the China (Hangzhou) region and granted self-managed permissions.
        
        @param request: DeleteStackInstancesRequest
        @return: DeleteStackInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_stack_instances_with_options_async(request, runtime)

    def delete_template_with_options(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteTemplateResponse:
        """
        If the template is shared with other Alibaba Cloud accounts, you must unshare the template before you delete it.
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_with_options_async(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteTemplateResponse:
        """
        If the template is shared with other Alibaba Cloud accounts, you must unshare the template before you delete it.
        
        @param request: DeleteTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
    ) -> ros20190910_models.DeleteTemplateResponse:
        """
        If the template is shared with other Alibaba Cloud accounts, you must unshare the template before you delete it.
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    async def delete_template_async(
        self,
        request: ros20190910_models.DeleteTemplateRequest,
    ) -> ros20190910_models.DeleteTemplateResponse:
        """
        If the template is shared with other Alibaba Cloud accounts, you must unshare the template before you delete it.
        
        @param request: DeleteTemplateRequest
        @return: DeleteTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_with_options_async(request, runtime)

    def delete_template_scratch_with_options(
        self,
        request: ros20190910_models.DeleteTemplateScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteTemplateScratchResponse:
        """
        This topic describes how to delete a scenario. In this topic, the `ts-4f83704400994409***` scenario in the China (Hangzhou) region is deleted.
        
        @param request: DeleteTemplateScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateScratchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_template_scratch_with_options_async(
        self,
        request: ros20190910_models.DeleteTemplateScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeleteTemplateScratchResponse:
        """
        This topic describes how to delete a scenario. In this topic, the `ts-4f83704400994409***` scenario in the China (Hangzhou) region is deleted.
        
        @param request: DeleteTemplateScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteTemplateScratchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeleteTemplateScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_template_scratch(
        self,
        request: ros20190910_models.DeleteTemplateScratchRequest,
    ) -> ros20190910_models.DeleteTemplateScratchResponse:
        """
        This topic describes how to delete a scenario. In this topic, the `ts-4f83704400994409***` scenario in the China (Hangzhou) region is deleted.
        
        @param request: DeleteTemplateScratchRequest
        @return: DeleteTemplateScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_template_scratch_with_options(request, runtime)

    async def delete_template_scratch_async(
        self,
        request: ros20190910_models.DeleteTemplateScratchRequest,
    ) -> ros20190910_models.DeleteTemplateScratchResponse:
        """
        This topic describes how to delete a scenario. In this topic, the `ts-4f83704400994409***` scenario in the China (Hangzhou) region is deleted.
        
        @param request: DeleteTemplateScratchRequest
        @return: DeleteTemplateScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_template_scratch_with_options_async(request, runtime)

    def deregister_resource_type_with_options(
        self,
        request: ros20190910_models.DeregisterResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeregisterResourceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterResourceType',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeregisterResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def deregister_resource_type_with_options_async(
        self,
        request: ros20190910_models.DeregisterResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DeregisterResourceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterResourceType',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DeregisterResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deregister_resource_type(
        self,
        request: ros20190910_models.DeregisterResourceTypeRequest,
    ) -> ros20190910_models.DeregisterResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.deregister_resource_type_with_options(request, runtime)

    async def deregister_resource_type_async(
        self,
        request: ros20190910_models.DeregisterResourceTypeRequest,
    ) -> ros20190910_models.DeregisterResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.deregister_resource_type_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DescribeRegionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
    ) -> ros20190910_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: ros20190910_models.DescribeRegionsRequest,
    ) -> ros20190910_models.DescribeRegionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def detect_stack_drift_with_options(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackDriftResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectStackDrift',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackDriftResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_stack_drift_with_options_async(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackDriftResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectStackDrift',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackDriftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_stack_drift(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
    ) -> ros20190910_models.DetectStackDriftResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_drift_with_options(request, runtime)

    async def detect_stack_drift_async(
        self,
        request: ros20190910_models.DetectStackDriftRequest,
    ) -> ros20190910_models.DetectStackDriftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_stack_drift_with_options_async(request, runtime)

    def detect_stack_group_drift_with_options(
        self,
        tmp_req: ros20190910_models.DetectStackGroupDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DetectStackGroupDriftShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectStackGroupDrift',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackGroupDriftResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_stack_group_drift_with_options_async(
        self,
        tmp_req: ros20190910_models.DetectStackGroupDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.DetectStackGroupDriftShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectStackGroupDrift',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackGroupDriftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_stack_group_drift(
        self,
        request: ros20190910_models.DetectStackGroupDriftRequest,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_group_drift_with_options(request, runtime)

    async def detect_stack_group_drift_async(
        self,
        request: ros20190910_models.DetectStackGroupDriftRequest,
    ) -> ros20190910_models.DetectStackGroupDriftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_stack_group_drift_with_options_async(request, runtime)

    def detect_stack_resource_drift_with_options(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectStackResourceDrift',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackResourceDriftResponse(),
            self.call_api(params, req, runtime)
        )

    async def detect_stack_resource_drift_with_options_async(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectStackResourceDrift',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.DetectStackResourceDriftResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detect_stack_resource_drift(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        runtime = util_models.RuntimeOptions()
        return self.detect_stack_resource_drift_with_options(request, runtime)

    async def detect_stack_resource_drift_async(
        self,
        request: ros20190910_models.DetectStackResourceDriftRequest,
    ) -> ros20190910_models.DetectStackResourceDriftResponse:
        runtime = util_models.RuntimeOptions()
        return await self.detect_stack_resource_drift_with_options_async(request, runtime)

    def execute_change_set_with_options(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        """
        In this example, a change set in the `China (Hangzhou)` region whose ID is `1f6521a4-05af-4975-afe9-bc4b45ad***` is executed.
        
        @param request: ExecuteChangeSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteChangeSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ExecuteChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_change_set_with_options_async(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        """
        In this example, a change set in the `China (Hangzhou)` region whose ID is `1f6521a4-05af-4975-afe9-bc4b45ad***` is executed.
        
        @param request: ExecuteChangeSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ExecuteChangeSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExecuteChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ExecuteChangeSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_change_set(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        """
        In this example, a change set in the `China (Hangzhou)` region whose ID is `1f6521a4-05af-4975-afe9-bc4b45ad***` is executed.
        
        @param request: ExecuteChangeSetRequest
        @return: ExecuteChangeSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.execute_change_set_with_options(request, runtime)

    async def execute_change_set_async(
        self,
        request: ros20190910_models.ExecuteChangeSetRequest,
    ) -> ros20190910_models.ExecuteChangeSetResponse:
        """
        In this example, a change set in the `China (Hangzhou)` region whose ID is `1f6521a4-05af-4975-afe9-bc4b45ad***` is executed.
        
        @param request: ExecuteChangeSetRequest
        @return: ExecuteChangeSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.execute_change_set_with_options_async(request, runtime)

    def generate_template_by_scratch_with_options(
        self,
        request: ros20190910_models.GenerateTemplateByScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GenerateTemplateByScratchResponse:
        """
        This topic describes how to create a template for a scenario. In this topic, the `ts-aa9c62feab844a6b***` scenario of the Resource Management type in the China (Hangzhou) region is used.
        
        @param request: GenerateTemplateByScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTemplateByScratchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provision_region_id):
            query['ProvisionRegionId'] = request.provision_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateTemplateByScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GenerateTemplateByScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_template_by_scratch_with_options_async(
        self,
        request: ros20190910_models.GenerateTemplateByScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GenerateTemplateByScratchResponse:
        """
        This topic describes how to create a template for a scenario. In this topic, the `ts-aa9c62feab844a6b***` scenario of the Resource Management type in the China (Hangzhou) region is used.
        
        @param request: GenerateTemplateByScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTemplateByScratchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.provision_region_id):
            query['ProvisionRegionId'] = request.provision_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateTemplateByScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GenerateTemplateByScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_template_by_scratch(
        self,
        request: ros20190910_models.GenerateTemplateByScratchRequest,
    ) -> ros20190910_models.GenerateTemplateByScratchResponse:
        """
        This topic describes how to create a template for a scenario. In this topic, the `ts-aa9c62feab844a6b***` scenario of the Resource Management type in the China (Hangzhou) region is used.
        
        @param request: GenerateTemplateByScratchRequest
        @return: GenerateTemplateByScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_template_by_scratch_with_options(request, runtime)

    async def generate_template_by_scratch_async(
        self,
        request: ros20190910_models.GenerateTemplateByScratchRequest,
    ) -> ros20190910_models.GenerateTemplateByScratchResponse:
        """
        This topic describes how to create a template for a scenario. In this topic, the `ts-aa9c62feab844a6b***` scenario of the Resource Management type in the China (Hangzhou) region is used.
        
        @param request: GenerateTemplateByScratchRequest
        @return: GenerateTemplateByScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_template_by_scratch_with_options_async(request, runtime)

    def generate_template_policy_with_options(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        """
        If the policy information is related to Enterprise Distributed Application Service (EDAS), you must log on to your Alibaba Cloud account and grant the required permissions to the relevant RAM users.
        In this example, a policy is generated for a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc****`.
        
        @param request: GenerateTemplatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTemplatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_types):
            query['OperationTypes'] = request.operation_types
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateTemplatePolicy',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GenerateTemplatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_template_policy_with_options_async(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        """
        If the policy information is related to Enterprise Distributed Application Service (EDAS), you must log on to your Alibaba Cloud account and grant the required permissions to the relevant RAM users.
        In this example, a policy is generated for a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc****`.
        
        @param request: GenerateTemplatePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateTemplatePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_types):
            query['OperationTypes'] = request.operation_types
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateTemplatePolicy',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GenerateTemplatePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_template_policy(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        """
        If the policy information is related to Enterprise Distributed Application Service (EDAS), you must log on to your Alibaba Cloud account and grant the required permissions to the relevant RAM users.
        In this example, a policy is generated for a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc****`.
        
        @param request: GenerateTemplatePolicyRequest
        @return: GenerateTemplatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_template_policy_with_options(request, runtime)

    async def generate_template_policy_async(
        self,
        request: ros20190910_models.GenerateTemplatePolicyRequest,
    ) -> ros20190910_models.GenerateTemplatePolicyResponse:
        """
        If the policy information is related to Enterprise Distributed Application Service (EDAS), you must log on to your Alibaba Cloud account and grant the required permissions to the relevant RAM users.
        In this example, a policy is generated for a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc****`.
        
        @param request: GenerateTemplatePolicyRequest
        @return: GenerateTemplatePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_template_policy_with_options_async(request, runtime)

    def get_change_set_with_options(
        self,
        request: ros20190910_models.GetChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetChangeSetResponse:
        """
        In this example, the information of the change set whose ID is `4c11658d-bd47-4dd0-ba64-727edc62***` is queried.
        
        @param request: GetChangeSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChangeSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_template):
            query['ShowTemplate'] = request.show_template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetChangeSetResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_change_set_with_options_async(
        self,
        request: ros20190910_models.GetChangeSetRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetChangeSetResponse:
        """
        In this example, the information of the change set whose ID is `4c11658d-bd47-4dd0-ba64-727edc62***` is queried.
        
        @param request: GetChangeSetRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetChangeSetResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_template):
            query['ShowTemplate'] = request.show_template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChangeSet',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetChangeSetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_change_set(
        self,
        request: ros20190910_models.GetChangeSetRequest,
    ) -> ros20190910_models.GetChangeSetResponse:
        """
        In this example, the information of the change set whose ID is `4c11658d-bd47-4dd0-ba64-727edc62***` is queried.
        
        @param request: GetChangeSetRequest
        @return: GetChangeSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_change_set_with_options(request, runtime)

    async def get_change_set_async(
        self,
        request: ros20190910_models.GetChangeSetRequest,
    ) -> ros20190910_models.GetChangeSetResponse:
        """
        In this example, the information of the change set whose ID is `4c11658d-bd47-4dd0-ba64-727edc62***` is queried.
        
        @param request: GetChangeSetRequest
        @return: GetChangeSetResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_change_set_with_options_async(request, runtime)

    def get_feature_details_with_options(
        self,
        request: ros20190910_models.GetFeatureDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetFeatureDetailsResponse:
        """
        You can call this operation to query the Terraform hosting, resource cleaner, and scenario features.
        This topic provides an example on how to query the details of features supported by ROS in the China (Hangzhou) region. The details include Terraform versions, provider versions, and supported resource types.
        >  In the Examples section, only part of the sample code is provided.
        
        @param request: GetFeatureDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature):
            query['Feature'] = request.feature
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFeatureDetails',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetFeatureDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_feature_details_with_options_async(
        self,
        request: ros20190910_models.GetFeatureDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetFeatureDetailsResponse:
        """
        You can call this operation to query the Terraform hosting, resource cleaner, and scenario features.
        This topic provides an example on how to query the details of features supported by ROS in the China (Hangzhou) region. The details include Terraform versions, provider versions, and supported resource types.
        >  In the Examples section, only part of the sample code is provided.
        
        @param request: GetFeatureDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetFeatureDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.feature):
            query['Feature'] = request.feature
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFeatureDetails',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetFeatureDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_feature_details(
        self,
        request: ros20190910_models.GetFeatureDetailsRequest,
    ) -> ros20190910_models.GetFeatureDetailsResponse:
        """
        You can call this operation to query the Terraform hosting, resource cleaner, and scenario features.
        This topic provides an example on how to query the details of features supported by ROS in the China (Hangzhou) region. The details include Terraform versions, provider versions, and supported resource types.
        >  In the Examples section, only part of the sample code is provided.
        
        @param request: GetFeatureDetailsRequest
        @return: GetFeatureDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_feature_details_with_options(request, runtime)

    async def get_feature_details_async(
        self,
        request: ros20190910_models.GetFeatureDetailsRequest,
    ) -> ros20190910_models.GetFeatureDetailsResponse:
        """
        You can call this operation to query the Terraform hosting, resource cleaner, and scenario features.
        This topic provides an example on how to query the details of features supported by ROS in the China (Hangzhou) region. The details include Terraform versions, provider versions, and supported resource types.
        >  In the Examples section, only part of the sample code is provided.
        
        @param request: GetFeatureDetailsRequest
        @return: GetFeatureDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_feature_details_with_options_async(request, runtime)

    def get_resource_type_with_options(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: GetResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_type_with_options_async(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: GetResourceTypeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceType',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_type(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
    ) -> ros20190910_models.GetResourceTypeResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: GetResourceTypeRequest
        @return: GetResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_with_options(request, runtime)

    async def get_resource_type_async(
        self,
        request: ros20190910_models.GetResourceTypeRequest,
    ) -> ros20190910_models.GetResourceTypeResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: GetResourceTypeRequest
        @return: GetResourceTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_type_with_options_async(request, runtime)

    def get_resource_type_template_with_options(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTypeTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetResourceTypeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_type_template_with_options_async(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceTypeTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetResourceTypeTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_type_template(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_resource_type_template_with_options(request, runtime)

    async def get_resource_type_template_async(
        self,
        request: ros20190910_models.GetResourceTypeTemplateRequest,
    ) -> ros20190910_models.GetResourceTypeTemplateResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_type_template_with_options_async(request, runtime)

    def get_service_provisions_with_options(
        self,
        request: ros20190910_models.GetServiceProvisionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetServiceProvisionsResponse:
        """
        This topic describes how to query the activation status and the RAM roles of an Alibaba Cloud service. In this example, the Elastic High Performance Computing (E-HPC) service that is deployed in the China (Hangzhou) region is queried.
        >  Make sure that you have obtained the permissions on the [GetRole](~~28711~~) operation.
        
        @param request: GetServiceProvisionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceProvisionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.services):
            query['Services'] = request.services
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceProvisions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetServiceProvisionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_provisions_with_options_async(
        self,
        request: ros20190910_models.GetServiceProvisionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetServiceProvisionsResponse:
        """
        This topic describes how to query the activation status and the RAM roles of an Alibaba Cloud service. In this example, the Elastic High Performance Computing (E-HPC) service that is deployed in the China (Hangzhou) region is queried.
        >  Make sure that you have obtained the permissions on the [GetRole](~~28711~~) operation.
        
        @param request: GetServiceProvisionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceProvisionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.services):
            query['Services'] = request.services
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceProvisions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetServiceProvisionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_provisions(
        self,
        request: ros20190910_models.GetServiceProvisionsRequest,
    ) -> ros20190910_models.GetServiceProvisionsResponse:
        """
        This topic describes how to query the activation status and the RAM roles of an Alibaba Cloud service. In this example, the Elastic High Performance Computing (E-HPC) service that is deployed in the China (Hangzhou) region is queried.
        >  Make sure that you have obtained the permissions on the [GetRole](~~28711~~) operation.
        
        @param request: GetServiceProvisionsRequest
        @return: GetServiceProvisionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_provisions_with_options(request, runtime)

    async def get_service_provisions_async(
        self,
        request: ros20190910_models.GetServiceProvisionsRequest,
    ) -> ros20190910_models.GetServiceProvisionsResponse:
        """
        This topic describes how to query the activation status and the RAM roles of an Alibaba Cloud service. In this example, the Elastic High Performance Computing (E-HPC) service that is deployed in the China (Hangzhou) region is queried.
        >  Make sure that you have obtained the permissions on the [GetRole](~~28711~~) operation.
        
        @param request: GetServiceProvisionsRequest
        @return: GetServiceProvisionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_provisions_with_options_async(request, runtime)

    def get_stack_with_options(
        self,
        request: ros20190910_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResponse:
        """
        In this topic, the information about a stack whose ID is `c754d2a4-28f1-46df-b557-9586173a***` is queried. The stack is deployed in the China (Hangzhou) region.
        
        @param request: GetStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.log_option):
            query['LogOption'] = request.log_option
        if not UtilClient.is_unset(request.output_option):
            query['OutputOption'] = request.output_option
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_resource_progress):
            query['ShowResourceProgress'] = request.show_resource_progress
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_with_options_async(
        self,
        request: ros20190910_models.GetStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResponse:
        """
        In this topic, the information about a stack whose ID is `c754d2a4-28f1-46df-b557-9586173a***` is queried. The stack is deployed in the China (Hangzhou) region.
        
        @param request: GetStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.log_option):
            query['LogOption'] = request.log_option
        if not UtilClient.is_unset(request.output_option):
            query['OutputOption'] = request.output_option
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_resource_progress):
            query['ShowResourceProgress'] = request.show_resource_progress
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack(
        self,
        request: ros20190910_models.GetStackRequest,
    ) -> ros20190910_models.GetStackResponse:
        """
        In this topic, the information about a stack whose ID is `c754d2a4-28f1-46df-b557-9586173a***` is queried. The stack is deployed in the China (Hangzhou) region.
        
        @param request: GetStackRequest
        @return: GetStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    async def get_stack_async(
        self,
        request: ros20190910_models.GetStackRequest,
    ) -> ros20190910_models.GetStackResponse:
        """
        In this topic, the information about a stack whose ID is `c754d2a4-28f1-46df-b557-9586173a***` is queried. The stack is deployed in the China (Hangzhou) region.
        
        @param request: GetStackRequest
        @return: GetStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_with_options_async(request, runtime)

    def get_stack_drift_detection_status_with_options(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        """
        In this topic, the status of a drift detection operation whose ID is `a7044f0d-6f2e-4128-a307-4524ef88***` is queried. The operation is performed in the China (Hangzhou) region.
        
        @param request: GetStackDriftDetectionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackDriftDetectionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drift_detection_id):
            query['DriftDetectionId'] = request.drift_detection_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackDriftDetectionStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackDriftDetectionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_drift_detection_status_with_options_async(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        """
        In this topic, the status of a drift detection operation whose ID is `a7044f0d-6f2e-4128-a307-4524ef88***` is queried. The operation is performed in the China (Hangzhou) region.
        
        @param request: GetStackDriftDetectionStatusRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackDriftDetectionStatusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.drift_detection_id):
            query['DriftDetectionId'] = request.drift_detection_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackDriftDetectionStatus',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackDriftDetectionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_drift_detection_status(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        """
        In this topic, the status of a drift detection operation whose ID is `a7044f0d-6f2e-4128-a307-4524ef88***` is queried. The operation is performed in the China (Hangzhou) region.
        
        @param request: GetStackDriftDetectionStatusRequest
        @return: GetStackDriftDetectionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_stack_drift_detection_status_with_options(request, runtime)

    async def get_stack_drift_detection_status_async(
        self,
        request: ros20190910_models.GetStackDriftDetectionStatusRequest,
    ) -> ros20190910_models.GetStackDriftDetectionStatusResponse:
        """
        In this topic, the status of a drift detection operation whose ID is `a7044f0d-6f2e-4128-a307-4524ef88***` is queried. The operation is performed in the China (Hangzhou) region.
        
        @param request: GetStackDriftDetectionStatusRequest
        @return: GetStackDriftDetectionStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_drift_detection_status_with_options_async(request, runtime)

    def get_stack_group_with_options(
        self,
        request: ros20190910_models.GetStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: GetStackGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_id):
            query['StackGroupId'] = request.stack_group_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_group_with_options_async(
        self,
        request: ros20190910_models.GetStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: GetStackGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_id):
            query['StackGroupId'] = request.stack_group_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_group(
        self,
        request: ros20190910_models.GetStackGroupRequest,
    ) -> ros20190910_models.GetStackGroupResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: GetStackGroupRequest
        @return: GetStackGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_with_options(request, runtime)

    async def get_stack_group_async(
        self,
        request: ros20190910_models.GetStackGroupRequest,
    ) -> ros20190910_models.GetStackGroupResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: GetStackGroupRequest
        @return: GetStackGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_group_with_options_async(request, runtime)

    def get_stack_group_operation_with_options(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        """
        In this example, the operation ID `6da106ca-1784-4a6f-a7e1-e723863d∗∗∗∗` is set to query the details of an operation that you perform on a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: GetStackGroupOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackGroupOperationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackGroupOperation',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackGroupOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_group_operation_with_options_async(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        """
        In this example, the operation ID `6da106ca-1784-4a6f-a7e1-e723863d∗∗∗∗` is set to query the details of an operation that you perform on a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: GetStackGroupOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackGroupOperationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackGroupOperation',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackGroupOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_group_operation(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        """
        In this example, the operation ID `6da106ca-1784-4a6f-a7e1-e723863d∗∗∗∗` is set to query the details of an operation that you perform on a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: GetStackGroupOperationRequest
        @return: GetStackGroupOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_stack_group_operation_with_options(request, runtime)

    async def get_stack_group_operation_async(
        self,
        request: ros20190910_models.GetStackGroupOperationRequest,
    ) -> ros20190910_models.GetStackGroupOperationResponse:
        """
        In this example, the operation ID `6da106ca-1784-4a6f-a7e1-e723863d∗∗∗∗` is set to query the details of an operation that you perform on a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: GetStackGroupOperationRequest
        @return: GetStackGroupOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_group_operation_with_options_async(request, runtime)

    def get_stack_instance_with_options(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackInstanceResponse:
        """
        In this example, the details of a stack that is deployed in the China (Beijing) region within the `151266687691***` Alibaba Cloud account are queried. The stack is deployed in a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: GetStackInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not UtilClient.is_unset(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackInstance',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_instance_with_options_async(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackInstanceResponse:
        """
        In this example, the details of a stack that is deployed in the China (Beijing) region within the `151266687691***` Alibaba Cloud account are queried. The stack is deployed in a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: GetStackInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not UtilClient.is_unset(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackInstance',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_instance(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
    ) -> ros20190910_models.GetStackInstanceResponse:
        """
        In this example, the details of a stack that is deployed in the China (Beijing) region within the `151266687691***` Alibaba Cloud account are queried. The stack is deployed in a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: GetStackInstanceRequest
        @return: GetStackInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_stack_instance_with_options(request, runtime)

    async def get_stack_instance_async(
        self,
        request: ros20190910_models.GetStackInstanceRequest,
    ) -> ros20190910_models.GetStackInstanceResponse:
        """
        In this example, the details of a stack that is deployed in the China (Beijing) region within the `151266687691***` Alibaba Cloud account are queried. The stack is deployed in a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: GetStackInstanceRequest
        @return: GetStackInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_instance_with_options_async(request, runtime)

    def get_stack_policy_with_options(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackPolicyResponse:
        """
        In this example, the stack policy of a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***` is queried. The stack is deployed in the China (Hangzhou) region.
        
        @param request: GetStackPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackPolicy',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_policy_with_options_async(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackPolicyResponse:
        """
        In this example, the stack policy of a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***` is queried. The stack is deployed in the China (Hangzhou) region.
        
        @param request: GetStackPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackPolicy',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_policy(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
    ) -> ros20190910_models.GetStackPolicyResponse:
        """
        In this example, the stack policy of a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***` is queried. The stack is deployed in the China (Hangzhou) region.
        
        @param request: GetStackPolicyRequest
        @return: GetStackPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_stack_policy_with_options(request, runtime)

    async def get_stack_policy_async(
        self,
        request: ros20190910_models.GetStackPolicyRequest,
    ) -> ros20190910_models.GetStackPolicyResponse:
        """
        In this example, the stack policy of a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***` is queried. The stack is deployed in the China (Hangzhou) region.
        
        @param request: GetStackPolicyRequest
        @return: GetStackPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_policy_with_options_async(request, runtime)

    def get_stack_resource_with_options(
        self,
        request: ros20190910_models.GetStackResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResourceResponse:
        """
        | Http status code | Error code | Error message | Description |
        | ---------------- | ---------- | ------------- | ----------- |
        | 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the stack. name indicates the resource name. stack indicates the stack name or ID. |
        | 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the stack does not exist. name indicates the name or ID of the stack. |
        
        @param request: GetStackResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_attributes):
            query['ResourceAttributes'] = request.resource_attributes
        if not UtilClient.is_unset(request.show_resource_attributes):
            query['ShowResourceAttributes'] = request.show_resource_attributes
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackResource',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_resource_with_options_async(
        self,
        request: ros20190910_models.GetStackResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetStackResourceResponse:
        """
        | Http status code | Error code | Error message | Description |
        | ---------------- | ---------- | ------------- | ----------- |
        | 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the stack. name indicates the resource name. stack indicates the stack name or ID. |
        | 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the stack does not exist. name indicates the name or ID of the stack. |
        
        @param request: GetStackResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetStackResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_attributes):
            query['ResourceAttributes'] = request.resource_attributes
        if not UtilClient.is_unset(request.show_resource_attributes):
            query['ShowResourceAttributes'] = request.show_resource_attributes
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStackResource',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetStackResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_resource(
        self,
        request: ros20190910_models.GetStackResourceRequest,
    ) -> ros20190910_models.GetStackResourceResponse:
        """
        | Http status code | Error code | Error message | Description |
        | ---------------- | ---------- | ------------- | ----------- |
        | 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the stack. name indicates the resource name. stack indicates the stack name or ID. |
        | 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the stack does not exist. name indicates the name or ID of the stack. |
        
        @param request: GetStackResourceRequest
        @return: GetStackResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_stack_resource_with_options(request, runtime)

    async def get_stack_resource_async(
        self,
        request: ros20190910_models.GetStackResourceRequest,
    ) -> ros20190910_models.GetStackResourceResponse:
        """
        | Http status code | Error code | Error message | Description |
        | ---------------- | ---------- | ------------- | ----------- |
        | 404 | ResourceNotFound | The Resource ({name}) could not be found in Stack {stack}. | The error message returned because the specified resource does not exist in the stack. name indicates the resource name. stack indicates the stack name or ID. |
        | 404 | StackNotFound | The Stack ({name}) could not be found. | The error message returned because the stack does not exist. name indicates the name or ID of the stack. |
        
        @param request: GetStackResourceRequest
        @return: GetStackResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_stack_resource_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: ros20190910_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateResponse:
        """
        In this example, the details of a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc***` and region ID is `cn-hangzhou` are queried.
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.include_permission):
            query['IncludePermission'] = request.include_permission
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_stage):
            query['TemplateStage'] = request.template_stage
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: ros20190910_models.GetTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateResponse:
        """
        In this example, the details of a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc***` and region ID is `cn-hangzhou` are queried.
        
        @param request: GetTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.include_permission):
            query['IncludePermission'] = request.include_permission
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_stage):
            query['TemplateStage'] = request.template_stage
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: ros20190910_models.GetTemplateRequest,
    ) -> ros20190910_models.GetTemplateResponse:
        """
        In this example, the details of a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc***` and region ID is `cn-hangzhou` are queried.
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: ros20190910_models.GetTemplateRequest,
    ) -> ros20190910_models.GetTemplateResponse:
        """
        In this example, the details of a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc***` and region ID is `cn-hangzhou` are queried.
        
        @param request: GetTemplateRequest
        @return: GetTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def get_template_estimate_cost_with_options(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        """
        The operation that you want to perform. Set the value to GetTemplateEstimateCost.
        
        @param request: GetTemplateEstimateCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateEstimateCostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplateEstimateCost',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateEstimateCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_estimate_cost_with_options_async(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        """
        The operation that you want to perform. Set the value to GetTemplateEstimateCost.
        
        @param request: GetTemplateEstimateCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateEstimateCostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplateEstimateCost',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateEstimateCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_estimate_cost(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        """
        The operation that you want to perform. Set the value to GetTemplateEstimateCost.
        
        @param request: GetTemplateEstimateCostRequest
        @return: GetTemplateEstimateCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_template_estimate_cost_with_options(request, runtime)

    async def get_template_estimate_cost_async(
        self,
        request: ros20190910_models.GetTemplateEstimateCostRequest,
    ) -> ros20190910_models.GetTemplateEstimateCostResponse:
        """
        The operation that you want to perform. Set the value to GetTemplateEstimateCost.
        
        @param request: GetTemplateEstimateCostRequest
        @return: GetTemplateEstimateCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_template_estimate_cost_with_options_async(request, runtime)

    def get_template_parameter_constraints_with_options(
        self,
        tmp_req: ros20190910_models.GetTemplateParameterConstraintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateParameterConstraintsResponse:
        """
        This topic provides an example on how to query the values of a parameter. In this example, the values of the `ZoneInfo` parameter in a template that is created in the China (Hangzhou) region are queried. The template body is `{"Parameters":{"ZoneInfo":{"Type": "String"},"InstanceType": {"Type": "String"}},"ROSTemplateFormatVersion": "2015-09-01","Resources":{"ECS":{"Properties":{"ZoneId":{"Ref": "ZoneInfo"},"InstanceType": {"Ref": "InstanceType"}},"Type": "ALIYUN::ECS::Instance"}}}`.
        For more information about the template parameters whose values you can query by calling this operation and the sample code of the template, see [Query the constraints of parameters](~~432820~~).
        
        @param tmp_req: GetTemplateParameterConstraintsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateParameterConstraintsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.GetTemplateParameterConstraintsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters_key_filter):
            request.parameters_key_filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters_key_filter, 'ParametersKeyFilter', 'json')
        if not UtilClient.is_unset(tmp_req.parameters_order):
            request.parameters_order_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters_order, 'ParametersOrder', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.parameters_key_filter_shrink):
            query['ParametersKeyFilter'] = request.parameters_key_filter_shrink
        if not UtilClient.is_unset(request.parameters_order_shrink):
            query['ParametersOrder'] = request.parameters_order_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplateParameterConstraints',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateParameterConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_parameter_constraints_with_options_async(
        self,
        tmp_req: ros20190910_models.GetTemplateParameterConstraintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateParameterConstraintsResponse:
        """
        This topic provides an example on how to query the values of a parameter. In this example, the values of the `ZoneInfo` parameter in a template that is created in the China (Hangzhou) region are queried. The template body is `{"Parameters":{"ZoneInfo":{"Type": "String"},"InstanceType": {"Type": "String"}},"ROSTemplateFormatVersion": "2015-09-01","Resources":{"ECS":{"Properties":{"ZoneId":{"Ref": "ZoneInfo"},"InstanceType": {"Ref": "InstanceType"}},"Type": "ALIYUN::ECS::Instance"}}}`.
        For more information about the template parameters whose values you can query by calling this operation and the sample code of the template, see [Query the constraints of parameters](~~432820~~).
        
        @param tmp_req: GetTemplateParameterConstraintsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateParameterConstraintsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.GetTemplateParameterConstraintsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters_key_filter):
            request.parameters_key_filter_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters_key_filter, 'ParametersKeyFilter', 'json')
        if not UtilClient.is_unset(tmp_req.parameters_order):
            request.parameters_order_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters_order, 'ParametersOrder', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.parameters_key_filter_shrink):
            query['ParametersKeyFilter'] = request.parameters_key_filter_shrink
        if not UtilClient.is_unset(request.parameters_order_shrink):
            query['ParametersOrder'] = request.parameters_order_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetTemplateParameterConstraints',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateParameterConstraintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_parameter_constraints(
        self,
        request: ros20190910_models.GetTemplateParameterConstraintsRequest,
    ) -> ros20190910_models.GetTemplateParameterConstraintsResponse:
        """
        This topic provides an example on how to query the values of a parameter. In this example, the values of the `ZoneInfo` parameter in a template that is created in the China (Hangzhou) region are queried. The template body is `{"Parameters":{"ZoneInfo":{"Type": "String"},"InstanceType": {"Type": "String"}},"ROSTemplateFormatVersion": "2015-09-01","Resources":{"ECS":{"Properties":{"ZoneId":{"Ref": "ZoneInfo"},"InstanceType": {"Ref": "InstanceType"}},"Type": "ALIYUN::ECS::Instance"}}}`.
        For more information about the template parameters whose values you can query by calling this operation and the sample code of the template, see [Query the constraints of parameters](~~432820~~).
        
        @param request: GetTemplateParameterConstraintsRequest
        @return: GetTemplateParameterConstraintsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_template_parameter_constraints_with_options(request, runtime)

    async def get_template_parameter_constraints_async(
        self,
        request: ros20190910_models.GetTemplateParameterConstraintsRequest,
    ) -> ros20190910_models.GetTemplateParameterConstraintsResponse:
        """
        This topic provides an example on how to query the values of a parameter. In this example, the values of the `ZoneInfo` parameter in a template that is created in the China (Hangzhou) region are queried. The template body is `{"Parameters":{"ZoneInfo":{"Type": "String"},"InstanceType": {"Type": "String"}},"ROSTemplateFormatVersion": "2015-09-01","Resources":{"ECS":{"Properties":{"ZoneId":{"Ref": "ZoneInfo"},"InstanceType": {"Ref": "InstanceType"}},"Type": "ALIYUN::ECS::Instance"}}}`.
        For more information about the template parameters whose values you can query by calling this operation and the sample code of the template, see [Query the constraints of parameters](~~432820~~).
        
        @param request: GetTemplateParameterConstraintsRequest
        @return: GetTemplateParameterConstraintsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_template_parameter_constraints_with_options_async(request, runtime)

    def get_template_recommend_parameters_with_options(
        self,
        request: ros20190910_models.GetTemplateRecommendParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateRecommendParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateRecommendParameters',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateRecommendParametersResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_recommend_parameters_with_options_async(
        self,
        request: ros20190910_models.GetTemplateRecommendParametersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateRecommendParametersResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateRecommendParameters',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateRecommendParametersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_recommend_parameters(
        self,
        request: ros20190910_models.GetTemplateRecommendParametersRequest,
    ) -> ros20190910_models.GetTemplateRecommendParametersResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_recommend_parameters_with_options(request, runtime)

    async def get_template_recommend_parameters_async(
        self,
        request: ros20190910_models.GetTemplateRecommendParametersRequest,
    ) -> ros20190910_models.GetTemplateRecommendParametersResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_recommend_parameters_with_options_async(request, runtime)

    def get_template_scratch_with_options(
        self,
        request: ros20190910_models.GetTemplateScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateScratchResponse:
        """
        In this topic, the details about the `ts-7f7a704cf71c49a6***` scenario in the China (Hangzhou) region are queried. The source node data is displayed.
        
        @param request: GetTemplateScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateScratchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_data_option):
            query['ShowDataOption'] = request.show_data_option
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_scratch_with_options_async(
        self,
        request: ros20190910_models.GetTemplateScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateScratchResponse:
        """
        In this topic, the details about the `ts-7f7a704cf71c49a6***` scenario in the China (Hangzhou) region are queried. The source node data is displayed.
        
        @param request: GetTemplateScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetTemplateScratchResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_data_option):
            query['ShowDataOption'] = request.show_data_option
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_scratch(
        self,
        request: ros20190910_models.GetTemplateScratchRequest,
    ) -> ros20190910_models.GetTemplateScratchResponse:
        """
        In this topic, the details about the `ts-7f7a704cf71c49a6***` scenario in the China (Hangzhou) region are queried. The source node data is displayed.
        
        @param request: GetTemplateScratchRequest
        @return: GetTemplateScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_template_scratch_with_options(request, runtime)

    async def get_template_scratch_async(
        self,
        request: ros20190910_models.GetTemplateScratchRequest,
    ) -> ros20190910_models.GetTemplateScratchResponse:
        """
        In this topic, the details about the `ts-7f7a704cf71c49a6***` scenario in the China (Hangzhou) region are queried. The source node data is displayed.
        
        @param request: GetTemplateScratchRequest
        @return: GetTemplateScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_template_scratch_with_options_async(request, runtime)

    def get_template_summary_with_options(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateSummary',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_summary_with_options_async(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTemplateSummary',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.GetTemplateSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template_summary(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_template_summary_with_options(request, runtime)

    async def get_template_summary_async(
        self,
        request: ros20190910_models.GetTemplateSummaryRequest,
    ) -> ros20190910_models.GetTemplateSummaryResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_template_summary_with_options_async(request, runtime)

    def list_change_sets_with_options(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListChangeSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not UtilClient.is_unset(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChangeSets',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListChangeSetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_change_sets_with_options_async(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListChangeSetsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_set_id):
            query['ChangeSetId'] = request.change_set_id
        if not UtilClient.is_unset(request.change_set_name):
            query['ChangeSetName'] = request.change_set_name
        if not UtilClient.is_unset(request.execution_status):
            query['ExecutionStatus'] = request.execution_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChangeSets',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListChangeSetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_change_sets(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
    ) -> ros20190910_models.ListChangeSetsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_change_sets_with_options(request, runtime)

    async def list_change_sets_async(
        self,
        request: ros20190910_models.ListChangeSetsRequest,
    ) -> ros20190910_models.ListChangeSetsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_change_sets_with_options_async(request, runtime)

    def list_resource_type_registrations_with_options(
        self,
        request: ros20190910_models.ListResourceTypeRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypeRegistrationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypeRegistrations',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListResourceTypeRegistrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_type_registrations_with_options_async(
        self,
        request: ros20190910_models.ListResourceTypeRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypeRegistrationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypeRegistrations',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListResourceTypeRegistrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_type_registrations(
        self,
        request: ros20190910_models.ListResourceTypeRegistrationsRequest,
    ) -> ros20190910_models.ListResourceTypeRegistrationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_type_registrations_with_options(request, runtime)

    async def list_resource_type_registrations_async(
        self,
        request: ros20190910_models.ListResourceTypeRegistrationsRequest,
    ) -> ros20190910_models.ListResourceTypeRegistrationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_type_registrations_with_options_async(request, runtime)

    def list_resource_type_versions_with_options(
        self,
        request: ros20190910_models.ListResourceTypeVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypeVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypeVersions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListResourceTypeVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_type_versions_with_options_async(
        self,
        request: ros20190910_models.ListResourceTypeVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypeVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypeVersions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListResourceTypeVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_type_versions(
        self,
        request: ros20190910_models.ListResourceTypeVersionsRequest,
    ) -> ros20190910_models.ListResourceTypeVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_resource_type_versions_with_options(request, runtime)

    async def list_resource_type_versions_async(
        self,
        request: ros20190910_models.ListResourceTypeVersionsRequest,
    ) -> ros20190910_models.ListResourceTypeVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_type_versions_with_options_async(request, runtime)

    def list_resource_types_with_options(
        self,
        request: ros20190910_models.ListResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypesResponse:
        """
        For more information about errors common to all operations, see [Common error codes](/help/en/resource-orchestration-service/latest/common-error-codes).
        
        @param request: ListResourceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        request: ros20190910_models.ListResourceTypesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListResourceTypesResponse:
        """
        For more information about errors common to all operations, see [Common error codes](/help/en/resource-orchestration-service/latest/common-error-codes).
        
        @param request: ListResourceTypesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResourceTypesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.provider):
            query['Provider'] = request.provider
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceTypes',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_types(
        self,
        request: ros20190910_models.ListResourceTypesRequest,
    ) -> ros20190910_models.ListResourceTypesResponse:
        """
        For more information about errors common to all operations, see [Common error codes](/help/en/resource-orchestration-service/latest/common-error-codes).
        
        @param request: ListResourceTypesRequest
        @return: ListResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_types_with_options(request, runtime)

    async def list_resource_types_async(
        self,
        request: ros20190910_models.ListResourceTypesRequest,
    ) -> ros20190910_models.ListResourceTypesResponse:
        """
        For more information about errors common to all operations, see [Common error codes](/help/en/resource-orchestration-service/latest/common-error-codes).
        
        @param request: ListResourceTypesRequest
        @return: ListResourceTypesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resource_types_with_options_async(request, runtime)

    def list_stack_events_with_options(
        self,
        request: ros20190910_models.ListStackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackEvents',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackEventsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_events_with_options_async(
        self,
        request: ros20190910_models.ListStackEventsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackEventsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackEvents',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackEventsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_events(
        self,
        request: ros20190910_models.ListStackEventsRequest,
    ) -> ros20190910_models.ListStackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_events_with_options(request, runtime)

    async def list_stack_events_async(
        self,
        request: ros20190910_models.ListStackEventsRequest,
    ) -> ros20190910_models.ListStackEventsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_events_with_options_async(request, runtime)

    def list_stack_group_operation_results_with_options(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        """
        In this example, the operation ID `6da106ca-1784-4a6f-a7e1-e723863d∗∗∗∗` is set to query the results of an operation on a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and created in the China (Hangzhou) region.
        
        @param request: ListStackGroupOperationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackGroupOperationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackGroupOperationResults',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupOperationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_group_operation_results_with_options_async(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        """
        In this example, the operation ID `6da106ca-1784-4a6f-a7e1-e723863d∗∗∗∗` is set to query the results of an operation on a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and created in the China (Hangzhou) region.
        
        @param request: ListStackGroupOperationResultsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackGroupOperationResultsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackGroupOperationResults',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupOperationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_group_operation_results(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        """
        In this example, the operation ID `6da106ca-1784-4a6f-a7e1-e723863d∗∗∗∗` is set to query the results of an operation on a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and created in the China (Hangzhou) region.
        
        @param request: ListStackGroupOperationResultsRequest
        @return: ListStackGroupOperationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operation_results_with_options(request, runtime)

    async def list_stack_group_operation_results_async(
        self,
        request: ros20190910_models.ListStackGroupOperationResultsRequest,
    ) -> ros20190910_models.ListStackGroupOperationResultsResponse:
        """
        In this example, the operation ID `6da106ca-1784-4a6f-a7e1-e723863d∗∗∗∗` is set to query the results of an operation on a stack group named `MyStackGroup`. The stack group is granted self-managed permissions and created in the China (Hangzhou) region.
        
        @param request: ListStackGroupOperationResultsRequest
        @return: ListStackGroupOperationResultsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_group_operation_results_with_options_async(request, runtime)

    def list_stack_group_operations_with_options(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackGroupOperations',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupOperationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_group_operations_with_options_async(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackGroupOperations',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupOperationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_group_operations(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_group_operations_with_options(request, runtime)

    async def list_stack_group_operations_async(
        self,
        request: ros20190910_models.ListStackGroupOperationsRequest,
    ) -> ros20190910_models.ListStackGroupOperationsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_group_operations_with_options_async(request, runtime)

    def list_stack_groups_with_options(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupsResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: ListStackGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackGroups',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_groups_with_options_async(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackGroupsResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: ListStackGroupsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackGroups',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_groups(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
    ) -> ros20190910_models.ListStackGroupsResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: ListStackGroupsRequest
        @return: ListStackGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_stack_groups_with_options(request, runtime)

    async def list_stack_groups_async(
        self,
        request: ros20190910_models.ListStackGroupsRequest,
    ) -> ros20190910_models.ListStackGroupsResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: ListStackGroupsRequest
        @return: ListStackGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_groups_with_options_async(request, runtime)

    def list_stack_instances_with_options(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackInstancesResponse:
        """
        In this example, the stacks that are deployed in a stack group named `MyStackGroup` are queried. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: ListStackInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not UtilClient.is_unset(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_instances_with_options_async(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackInstancesResponse:
        """
        In this example, the stacks that are deployed in a stack group named `MyStackGroup` are queried. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: ListStackInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.stack_instance_account_id):
            query['StackInstanceAccountId'] = request.stack_instance_account_id
        if not UtilClient.is_unset(request.stack_instance_region_id):
            query['StackInstanceRegionId'] = request.stack_instance_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_instances(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
    ) -> ros20190910_models.ListStackInstancesResponse:
        """
        In this example, the stacks that are deployed in a stack group named `MyStackGroup` are queried. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: ListStackInstancesRequest
        @return: ListStackInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_stack_instances_with_options(request, runtime)

    async def list_stack_instances_async(
        self,
        request: ros20190910_models.ListStackInstancesRequest,
    ) -> ros20190910_models.ListStackInstancesResponse:
        """
        In this example, the stacks that are deployed in a stack group named `MyStackGroup` are queried. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: ListStackInstancesRequest
        @return: ListStackInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_instances_with_options_async(request, runtime)

    def list_stack_operation_risks_with_options(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        """
        The ListStackOperationRisks operation is suitable for the following scenarios:
        *   You want to detect high risks that may arise in resources when you delete a stack that contains the resources, and query the cause of each risk in a resource.
        *   When you create a stack, the creation may fail. In this case, you can call this operation to check which types of permissions that are required to create stacks are missing.
        
        @param request: ListStackOperationRisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackOperationRisksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackOperationRisks',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackOperationRisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_operation_risks_with_options_async(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        """
        The ListStackOperationRisks operation is suitable for the following scenarios:
        *   You want to detect high risks that may arise in resources when you delete a stack that contains the resources, and query the cause of each risk in a resource.
        *   When you create a stack, the creation may fail. In this case, you can call this operation to check which types of permissions that are required to create stacks are missing.
        
        @param request: ListStackOperationRisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackOperationRisksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.operation_type):
            query['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retain_all_resources):
            query['RetainAllResources'] = request.retain_all_resources
        if not UtilClient.is_unset(request.retain_resources):
            query['RetainResources'] = request.retain_resources
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackOperationRisks',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackOperationRisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_operation_risks(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        """
        The ListStackOperationRisks operation is suitable for the following scenarios:
        *   You want to detect high risks that may arise in resources when you delete a stack that contains the resources, and query the cause of each risk in a resource.
        *   When you create a stack, the creation may fail. In this case, you can call this operation to check which types of permissions that are required to create stacks are missing.
        
        @param request: ListStackOperationRisksRequest
        @return: ListStackOperationRisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_stack_operation_risks_with_options(request, runtime)

    async def list_stack_operation_risks_async(
        self,
        request: ros20190910_models.ListStackOperationRisksRequest,
    ) -> ros20190910_models.ListStackOperationRisksResponse:
        """
        The ListStackOperationRisks operation is suitable for the following scenarios:
        *   You want to detect high risks that may arise in resources when you delete a stack that contains the resources, and query the cause of each risk in a resource.
        *   When you create a stack, the creation may fail. In this case, you can call this operation to check which types of permissions that are required to create stacks are missing.
        
        @param request: ListStackOperationRisksRequest
        @return: ListStackOperationRisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_operation_risks_with_options_async(request, runtime)

    def list_stack_resource_drifts_with_options(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_drift_status):
            query['ResourceDriftStatus'] = request.resource_drift_status
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackResourceDrifts',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackResourceDriftsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_resource_drifts_with_options_async(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_drift_status):
            query['ResourceDriftStatus'] = request.resource_drift_status
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackResourceDrifts',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackResourceDriftsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_resource_drifts(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resource_drifts_with_options(request, runtime)

    async def list_stack_resource_drifts_async(
        self,
        request: ros20190910_models.ListStackResourceDriftsRequest,
    ) -> ros20190910_models.ListStackResourceDriftsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_resource_drifts_with_options_async(request, runtime)

    def list_stack_resources_with_options(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourcesResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: ListStackResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stack_resources_with_options_async(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStackResourcesResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: ListStackResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStackResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStackResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStackResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stack_resources(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
    ) -> ros20190910_models.ListStackResourcesResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: ListStackResourcesRequest
        @return: ListStackResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_stack_resources_with_options(request, runtime)

    async def list_stack_resources_async(
        self,
        request: ros20190910_models.ListStackResourcesRequest,
    ) -> ros20190910_models.ListStackResourcesResponse:
        """
        For more information about common request parameters, see [Common parameters](~~131957~~).
        
        @param request: ListStackResourcesRequest
        @return: ListStackResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_stack_resources_with_options_async(request, runtime)

    def list_stacks_with_options(
        self,
        request: ros20190910_models.ListStacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStacksResponse:
        """
        Specifies whether to return nested stacks. Default value: false. Valid values:
        *   true
        *   false
        > If the ParentStackId parameter is specified, you must set the ShowNestedStack parameter to true.
        
        @param request: ListStacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_stack_id):
            query['ParentStackId'] = request.parent_stack_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.show_nested_stack):
            query['ShowNestedStack'] = request.show_nested_stack
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_ids):
            query['StackIds'] = request.stack_ids
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStacks',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStacksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_stacks_with_options_async(
        self,
        request: ros20190910_models.ListStacksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListStacksResponse:
        """
        Specifies whether to return nested stacks. Default value: false. Valid values:
        *   true
        *   false
        > If the ParentStackId parameter is specified, you must set the ShowNestedStack parameter to true.
        
        @param request: ListStacksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListStacksResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_stack_id):
            query['ParentStackId'] = request.parent_stack_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.show_nested_stack):
            query['ShowNestedStack'] = request.show_nested_stack
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_ids):
            query['StackIds'] = request.stack_ids
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListStacks',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListStacksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_stacks(
        self,
        request: ros20190910_models.ListStacksRequest,
    ) -> ros20190910_models.ListStacksResponse:
        """
        Specifies whether to return nested stacks. Default value: false. Valid values:
        *   true
        *   false
        > If the ParentStackId parameter is specified, you must set the ShowNestedStack parameter to true.
        
        @param request: ListStacksRequest
        @return: ListStacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_stacks_with_options(request, runtime)

    async def list_stacks_async(
        self,
        request: ros20190910_models.ListStacksRequest,
    ) -> ros20190910_models.ListStacksResponse:
        """
        Specifies whether to return nested stacks. Default value: false. Valid values:
        *   true
        *   false
        > If the ParentStackId parameter is specified, you must set the ShowNestedStack parameter to true.
        
        @param request: ListStacksRequest
        @return: ListStacksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_stacks_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: ros20190910_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagKeysResponse:
        """
        In this example, the tag keys that are added to a stack in the China (Hangzhou) region are queried.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: ros20190910_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagKeysResponse:
        """
        In this example, the tag keys that are added to a stack in the China (Hangzhou) region are queried.
        
        @param request: ListTagKeysRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: ros20190910_models.ListTagKeysRequest,
    ) -> ros20190910_models.ListTagKeysResponse:
        """
        In this example, the tag keys that are added to a stack in the China (Hangzhou) region are queried.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: ros20190910_models.ListTagKeysRequest,
    ) -> ros20190910_models.ListTagKeysResponse:
        """
        In this example, the tag keys that are added to a stack in the China (Hangzhou) region are queried.
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagResourcesResponse:
        """
        To specify the query object, you must specify the ResourceId.N or Tag.N parameter in the request. Tag.N consists of Tag.N.Key and Tag.N.Value.
        *   If you specify the Tag.N and ResourceId.N parameters, ROS resources that match both the parameters are returned.
        This topic provides an example on how to query the tags that are added to a resource in a stack. In this example, the resource ID is `6bc589b5-9c02-4944-8fc3-f3624234****`. The stack is deployed in the China (Hangzhou) region.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagResourcesResponse:
        """
        To specify the query object, you must specify the ResourceId.N or Tag.N parameter in the request. Tag.N consists of Tag.N.Key and Tag.N.Value.
        *   If you specify the Tag.N and ResourceId.N parameters, ROS resources that match both the parameters are returned.
        This topic provides an example on how to query the tags that are added to a resource in a stack. In this example, the resource ID is `6bc589b5-9c02-4944-8fc3-f3624234****`. The stack is deployed in the China (Hangzhou) region.
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
    ) -> ros20190910_models.ListTagResourcesResponse:
        """
        To specify the query object, you must specify the ResourceId.N or Tag.N parameter in the request. Tag.N consists of Tag.N.Key and Tag.N.Value.
        *   If you specify the Tag.N and ResourceId.N parameters, ROS resources that match both the parameters are returned.
        This topic provides an example on how to query the tags that are added to a resource in a stack. In this example, the resource ID is `6bc589b5-9c02-4944-8fc3-f3624234****`. The stack is deployed in the China (Hangzhou) region.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: ros20190910_models.ListTagResourcesRequest,
    ) -> ros20190910_models.ListTagResourcesResponse:
        """
        To specify the query object, you must specify the ResourceId.N or Tag.N parameter in the request. Tag.N consists of Tag.N.Key and Tag.N.Value.
        *   If you specify the Tag.N and ResourceId.N parameters, ROS resources that match both the parameters are returned.
        This topic provides an example on how to query the tags that are added to a resource in a stack. In this example, the resource ID is `6bc589b5-9c02-4944-8fc3-f3624234****`. The stack is deployed in the China (Hangzhou) region.
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: ros20190910_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagValuesResponse:
        """
        In this example, the tag values of `TagKey1` that is added to a stack in the China (Hangzhou) region are queried.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: ros20190910_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTagValuesResponse:
        """
        In this example, the tag values of `TagKey1` that is added to a stack in the China (Hangzhou) region are queried.
        
        @param request: ListTagValuesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key):
            query['Key'] = request.key
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: ros20190910_models.ListTagValuesRequest,
    ) -> ros20190910_models.ListTagValuesResponse:
        """
        In this example, the tag values of `TagKey1` that is added to a stack in the China (Hangzhou) region are queried.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: ros20190910_models.ListTagValuesRequest,
    ) -> ros20190910_models.ListTagValuesResponse:
        """
        In this example, the tag values of `TagKey1` that is added to a stack in the China (Hangzhou) region are queried.
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def list_template_scratches_with_options(
        self,
        request: ros20190910_models.ListTemplateScratchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplateScratchesResponse:
        """
        This topic provides an example on how to query the list of scenarios. In this example, the scenarios that are created in the China (Hangzhou) region are queried. The following scenarios are returned: resource management and resource replication scenarios.
        
        @param request: ListTemplateScratchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplateScratchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateScratches',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplateScratchesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_scratches_with_options_async(
        self,
        request: ros20190910_models.ListTemplateScratchesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplateScratchesResponse:
        """
        This topic provides an example on how to query the list of scenarios. In this example, the scenarios that are created in the China (Hangzhou) region are queried. The following scenarios are returned: resource management and resource replication scenarios.
        
        @param request: ListTemplateScratchesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTemplateScratchesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_type):
            query['TemplateScratchType'] = request.template_scratch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateScratches',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplateScratchesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_scratches(
        self,
        request: ros20190910_models.ListTemplateScratchesRequest,
    ) -> ros20190910_models.ListTemplateScratchesResponse:
        """
        This topic provides an example on how to query the list of scenarios. In this example, the scenarios that are created in the China (Hangzhou) region are queried. The following scenarios are returned: resource management and resource replication scenarios.
        
        @param request: ListTemplateScratchesRequest
        @return: ListTemplateScratchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_template_scratches_with_options(request, runtime)

    async def list_template_scratches_async(
        self,
        request: ros20190910_models.ListTemplateScratchesRequest,
    ) -> ros20190910_models.ListTemplateScratchesResponse:
        """
        This topic provides an example on how to query the list of scenarios. In this example, the scenarios that are created in the China (Hangzhou) region are queried. The following scenarios are returned: resource management and resource replication scenarios.
        
        @param request: ListTemplateScratchesRequest
        @return: ListTemplateScratchesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_template_scratches_with_options_async(request, runtime)

    def list_template_versions_with_options(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateVersions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplateVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_template_versions_with_options_async(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplateVersions',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplateVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_template_versions(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_template_versions_with_options(request, runtime)

    async def list_template_versions_async(
        self,
        request: ros20190910_models.ListTemplateVersionsRequest,
    ) -> ros20190910_models.ListTemplateVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_template_versions_with_options_async(request, runtime)

    def list_templates_with_options(
        self,
        request: ros20190910_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_templates_with_options_async(
        self,
        request: ros20190910_models.ListTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ListTemplatesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTemplates',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ListTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_templates(
        self,
        request: ros20190910_models.ListTemplatesRequest,
    ) -> ros20190910_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_templates_with_options(request, runtime)

    async def list_templates_async(
        self,
        request: ros20190910_models.ListTemplatesRequest,
    ) -> ros20190910_models.ListTemplatesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_templates_with_options_async(request, runtime)

    def move_resource_group_with_options(
        self,
        request: ros20190910_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.MoveResourceGroupResponse:
        """
        In this example, a stack deployed in the `China (Hangzhou)` region is moved to a specific resource group. The ID of the stack is `4e8611cb-251e-42b7-b9cb-3496362c***` and the ID of the resource group is `rg-acfm3peow3k****`.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def move_resource_group_with_options_async(
        self,
        request: ros20190910_models.MoveResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.MoveResourceGroupResponse:
        """
        In this example, a stack deployed in the `China (Hangzhou)` region is moved to a specific resource group. The ID of the stack is `4e8611cb-251e-42b7-b9cb-3496362c***` and the ID of the resource group is `rg-acfm3peow3k****`.
        
        @param request: MoveResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: MoveResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.MoveResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def move_resource_group(
        self,
        request: ros20190910_models.MoveResourceGroupRequest,
    ) -> ros20190910_models.MoveResourceGroupResponse:
        """
        In this example, a stack deployed in the `China (Hangzhou)` region is moved to a specific resource group. The ID of the stack is `4e8611cb-251e-42b7-b9cb-3496362c***` and the ID of the resource group is `rg-acfm3peow3k****`.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    async def move_resource_group_async(
        self,
        request: ros20190910_models.MoveResourceGroupRequest,
    ) -> ros20190910_models.MoveResourceGroupResponse:
        """
        In this example, a stack deployed in the `China (Hangzhou)` region is moved to a specific resource group. The ID of the stack is `4e8611cb-251e-42b7-b9cb-3496362c***` and the ID of the resource group is `rg-acfm3peow3k****`.
        
        @param request: MoveResourceGroupRequest
        @return: MoveResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.move_resource_group_with_options_async(request, runtime)

    def preview_stack_with_options(
        self,
        request: ros20190910_models.PreviewStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.PreviewStackResponse:
        """
        This topic provides an example on how to create a stack named `MyStack` in the China (Hangzhou) region and preview the information about the stack. In this example, the template body of the stack is `{"ROSTemplateFormatVersion":"2015-09-01"}`.
        
        @param request: PreviewStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreviewStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.enable_pre_config):
            query['EnablePreConfig'] = request.enable_pre_config
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreviewStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.PreviewStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_stack_with_options_async(
        self,
        request: ros20190910_models.PreviewStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.PreviewStackResponse:
        """
        This topic provides an example on how to create a stack named `MyStack` in the China (Hangzhou) region and preview the information about the stack. In this example, the template body of the stack is `{"ROSTemplateFormatVersion":"2015-09-01"}`.
        
        @param request: PreviewStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreviewStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.enable_pre_config):
            query['EnablePreConfig'] = request.enable_pre_config
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_name):
            query['StackName'] = request.stack_name
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        if not UtilClient.is_unset(request.template_scratch_region_id):
            query['TemplateScratchRegionId'] = request.template_scratch_region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PreviewStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.PreviewStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_stack(
        self,
        request: ros20190910_models.PreviewStackRequest,
    ) -> ros20190910_models.PreviewStackResponse:
        """
        This topic provides an example on how to create a stack named `MyStack` in the China (Hangzhou) region and preview the information about the stack. In this example, the template body of the stack is `{"ROSTemplateFormatVersion":"2015-09-01"}`.
        
        @param request: PreviewStackRequest
        @return: PreviewStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.preview_stack_with_options(request, runtime)

    async def preview_stack_async(
        self,
        request: ros20190910_models.PreviewStackRequest,
    ) -> ros20190910_models.PreviewStackResponse:
        """
        This topic provides an example on how to create a stack named `MyStack` in the China (Hangzhou) region and preview the information about the stack. In this example, the template body of the stack is `{"ROSTemplateFormatVersion":"2015-09-01"}`.
        
        @param request: PreviewStackRequest
        @return: PreviewStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.preview_stack_with_options_async(request, runtime)

    def register_resource_type_with_options(
        self,
        request: ros20190910_models.RegisterResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.RegisterResourceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterResourceType',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.RegisterResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_resource_type_with_options_async(
        self,
        request: ros20190910_models.RegisterResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.RegisterResourceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterResourceType',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.RegisterResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_resource_type(
        self,
        request: ros20190910_models.RegisterResourceTypeRequest,
    ) -> ros20190910_models.RegisterResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.register_resource_type_with_options(request, runtime)

    async def register_resource_type_async(
        self,
        request: ros20190910_models.RegisterResourceTypeRequest,
    ) -> ros20190910_models.RegisterResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.register_resource_type_with_options_async(request, runtime)

    def set_deletion_protection_with_options(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeletionProtection',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetDeletionProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_deletion_protection_with_options_async(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_protection):
            query['DeletionProtection'] = request.deletion_protection
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeletionProtection',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetDeletionProtectionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_deletion_protection(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_deletion_protection_with_options(request, runtime)

    async def set_deletion_protection_async(
        self,
        request: ros20190910_models.SetDeletionProtectionRequest,
    ) -> ros20190910_models.SetDeletionProtectionResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_deletion_protection_with_options_async(request, runtime)

    def set_resource_type_with_options(
        self,
        request: ros20190910_models.SetResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetResourceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_version_id):
            query['DefaultVersionId'] = request.default_version_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResourceType',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetResourceTypeResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_resource_type_with_options_async(
        self,
        request: ros20190910_models.SetResourceTypeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetResourceTypeResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.default_version_id):
            query['DefaultVersionId'] = request.default_version_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetResourceType',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetResourceTypeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_resource_type(
        self,
        request: ros20190910_models.SetResourceTypeRequest,
    ) -> ros20190910_models.SetResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return self.set_resource_type_with_options(request, runtime)

    async def set_resource_type_async(
        self,
        request: ros20190910_models.SetResourceTypeRequest,
    ) -> ros20190910_models.SetResourceTypeResponse:
        runtime = util_models.RuntimeOptions()
        return await self.set_resource_type_with_options_async(request, runtime)

    def set_stack_policy_with_options(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetStackPolicyResponse:
        """
        In this example, a stack policy is configured for a stack deployed in the `China (Hangzhou)` region whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***`. The URL to the stack policy body is `oss://ros/stack-policy/demo`.
        
        @param request: SetStackPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetStackPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetStackPolicy',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetStackPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_stack_policy_with_options_async(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetStackPolicyResponse:
        """
        In this example, a stack policy is configured for a stack deployed in the `China (Hangzhou)` region whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***`. The URL to the stack policy body is `oss://ros/stack-policy/demo`.
        
        @param request: SetStackPolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetStackPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetStackPolicy',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetStackPolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_stack_policy(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
    ) -> ros20190910_models.SetStackPolicyResponse:
        """
        In this example, a stack policy is configured for a stack deployed in the `China (Hangzhou)` region whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***`. The URL to the stack policy body is `oss://ros/stack-policy/demo`.
        
        @param request: SetStackPolicyRequest
        @return: SetStackPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_stack_policy_with_options(request, runtime)

    async def set_stack_policy_async(
        self,
        request: ros20190910_models.SetStackPolicyRequest,
    ) -> ros20190910_models.SetStackPolicyResponse:
        """
        In this example, a stack policy is configured for a stack deployed in the `China (Hangzhou)` region whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691***`. The URL to the stack policy body is `oss://ros/stack-policy/demo`.
        
        @param request: SetStackPolicyRequest
        @return: SetStackPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_stack_policy_with_options_async(request, runtime)

    def set_template_permission_with_options(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        """
        In this example, a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc***` is shared with an Alibaba Cloud account whose ID is `151266687691****`.
        >  The account can authorize an RAM user to use the shared template.``
        
        @param request: SetTemplatePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetTemplatePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.share_option):
            query['ShareOption'] = request.share_option
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.version_option):
            query['VersionOption'] = request.version_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTemplatePermission',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetTemplatePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def set_template_permission_with_options_async(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        """
        In this example, a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc***` is shared with an Alibaba Cloud account whose ID is `151266687691****`.
        >  The account can authorize an RAM user to use the shared template.``
        
        @param request: SetTemplatePermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: SetTemplatePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_ids):
            query['AccountIds'] = request.account_ids
        if not UtilClient.is_unset(request.share_option):
            query['ShareOption'] = request.share_option
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.version_option):
            query['VersionOption'] = request.version_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTemplatePermission',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SetTemplatePermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def set_template_permission(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        """
        In this example, a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc***` is shared with an Alibaba Cloud account whose ID is `151266687691****`.
        >  The account can authorize an RAM user to use the shared template.``
        
        @param request: SetTemplatePermissionRequest
        @return: SetTemplatePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_template_permission_with_options(request, runtime)

    async def set_template_permission_async(
        self,
        request: ros20190910_models.SetTemplatePermissionRequest,
    ) -> ros20190910_models.SetTemplatePermissionResponse:
        """
        In this example, a template whose ID is `5ecd1e10-b0e9-4389-a565-e4c15efc***` is shared with an Alibaba Cloud account whose ID is `151266687691****`.
        >  The account can authorize an RAM user to use the shared template.``
        
        @param request: SetTemplatePermissionRequest
        @return: SetTemplatePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.set_template_permission_with_options_async(request, runtime)

    def signal_resource_with_options(
        self,
        request: ros20190910_models.SignalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SignalResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignalResource',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SignalResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def signal_resource_with_options_async(
        self,
        request: ros20190910_models.SignalResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.SignalResourceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SignalResource',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.SignalResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def signal_resource(
        self,
        request: ros20190910_models.SignalResourceRequest,
    ) -> ros20190910_models.SignalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return self.signal_resource_with_options(request, runtime)

    async def signal_resource_async(
        self,
        request: ros20190910_models.SignalResourceRequest,
    ) -> ros20190910_models.SignalResourceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.signal_resource_with_options_async(request, runtime)

    def stop_stack_group_operation_with_options(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        """
        This topic provides an example on how to stop a stack group operation whose ID is `6da106ca-1784-4a6f-a7e1-e723863***` in the China (Hangzhou) region.
        
        @param request: StopStackGroupOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopStackGroupOperationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStackGroupOperation',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.StopStackGroupOperationResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_stack_group_operation_with_options_async(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        """
        This topic provides an example on how to stop a stack group operation whose ID is `6da106ca-1784-4a6f-a7e1-e723863***` in the China (Hangzhou) region.
        
        @param request: StopStackGroupOperationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopStackGroupOperationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStackGroupOperation',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.StopStackGroupOperationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_stack_group_operation(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        """
        This topic provides an example on how to stop a stack group operation whose ID is `6da106ca-1784-4a6f-a7e1-e723863***` in the China (Hangzhou) region.
        
        @param request: StopStackGroupOperationRequest
        @return: StopStackGroupOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_stack_group_operation_with_options(request, runtime)

    async def stop_stack_group_operation_async(
        self,
        request: ros20190910_models.StopStackGroupOperationRequest,
    ) -> ros20190910_models.StopStackGroupOperationResponse:
        """
        This topic provides an example on how to stop a stack group operation whose ID is `6da106ca-1784-4a6f-a7e1-e723863***` in the China (Hangzhou) region.
        
        @param request: StopStackGroupOperationRequest
        @return: StopStackGroupOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_stack_group_operation_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: ros20190910_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.TagResourcesResponse:
        """
        This topic provides an example on how to create a tag and add the tag to a resource in a stack. In this example, the resource ID is `7fee80e1-8c48-4c2f-8300-0f6dc40b***`, the tag key is `FinanceDept`, and the tag value is `FinanceJoshua`.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: ros20190910_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.TagResourcesResponse:
        """
        This topic provides an example on how to create a tag and add the tag to a resource in a stack. In this example, the resource ID is `7fee80e1-8c48-4c2f-8300-0f6dc40b***`, the tag key is `FinanceDept`, and the tag value is `FinanceJoshua`.
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: ros20190910_models.TagResourcesRequest,
    ) -> ros20190910_models.TagResourcesResponse:
        """
        This topic provides an example on how to create a tag and add the tag to a resource in a stack. In this example, the resource ID is `7fee80e1-8c48-4c2f-8300-0f6dc40b***`, the tag key is `FinanceDept`, and the tag value is `FinanceJoshua`.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: ros20190910_models.TagResourcesRequest,
    ) -> ros20190910_models.TagResourcesResponse:
        """
        This topic provides an example on how to create a tag and add the tag to a resource in a stack. In this example, the resource ID is `7fee80e1-8c48-4c2f-8300-0f6dc40b***`, the tag key is `FinanceDept`, and the tag value is `FinanceJoshua`.
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: ros20190910_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UntagResourcesResponse:
        """
        This topic provides an example on how to remove all tags from a stack that is deployed in the China (Hangzhou) region. In this example, the ID of the stack is `46ec7b78-9d5e-4b21-aefd-448c90aa***`.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: ros20190910_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UntagResourcesResponse:
        """
        This topic provides an example on how to remove all tags from a stack that is deployed in the China (Hangzhou) region. In this example, the ID of the stack is `46ec7b78-9d5e-4b21-aefd-448c90aa***`.
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: ros20190910_models.UntagResourcesRequest,
    ) -> ros20190910_models.UntagResourcesResponse:
        """
        This topic provides an example on how to remove all tags from a stack that is deployed in the China (Hangzhou) region. In this example, the ID of the stack is `46ec7b78-9d5e-4b21-aefd-448c90aa***`.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: ros20190910_models.UntagResourcesRequest,
    ) -> ros20190910_models.UntagResourcesResponse:
        """
        This topic provides an example on how to remove all tags from a stack that is deployed in the China (Hangzhou) region. In this example, the ID of the stack is `46ec7b78-9d5e-4b21-aefd-448c90aa***`.
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_stack_with_options(
        self,
        request: ros20190910_models.UpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackResponse:
        """
        The values of parameters in the Parameters section vary based on the value that you specify for the UsePreviousParameters parameter in the request. If you do not add the parameters that are defined in the template to the Parameters section, take note of the following items:
        *   UsePreviousParameters is set to false: If the template parameters have default values, the default values are used. Otherwise, you must specify values for the template parameters in the Parameters section.
        *   UsePreviousParameters is set to true: If you specify values for the template parameters when you create a stack, the values are used. If you leave the template parameters empty when you create a stack but the template parameters have default values, the default values are used.
        This topic describes how to update a stack. In this example, the template body of a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****` in the China (Beijing) region is updated to `{"ROSTemplateFormatVersion": "2015-09-01"}`.
        
        @param request: UpdateStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not UtilClient.is_unset(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not UtilClient.is_unset(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_stack_with_options_async(
        self,
        request: ros20190910_models.UpdateStackRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackResponse:
        """
        The values of parameters in the Parameters section vary based on the value that you specify for the UsePreviousParameters parameter in the request. If you do not add the parameters that are defined in the template to the Parameters section, take note of the following items:
        *   UsePreviousParameters is set to false: If the template parameters have default values, the default values are used. Otherwise, you must specify values for the template parameters in the Parameters section.
        *   UsePreviousParameters is set to true: If you specify values for the template parameters when you create a stack, the values are used. If you leave the template parameters empty when you create a stack but the template parameters have default values, the default values are used.
        This topic describes how to update a stack. In this example, the template body of a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****` in the China (Beijing) region is updated to `{"ROSTemplateFormatVersion": "2015-09-01"}`.
        
        @param request: UpdateStackRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStackResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.disable_rollback):
            query['DisableRollback'] = request.disable_rollback
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.parallelism):
            query['Parallelism'] = request.parallelism
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.ram_role_name):
            query['RamRoleName'] = request.ram_role_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.replacement_option):
            query['ReplacementOption'] = request.replacement_option
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.stack_policy_body):
            query['StackPolicyBody'] = request.stack_policy_body
        if not UtilClient.is_unset(request.stack_policy_during_update_body):
            query['StackPolicyDuringUpdateBody'] = request.stack_policy_during_update_body
        if not UtilClient.is_unset(request.stack_policy_during_update_url):
            query['StackPolicyDuringUpdateURL'] = request.stack_policy_during_update_url
        if not UtilClient.is_unset(request.stack_policy_url):
            query['StackPolicyURL'] = request.stack_policy_url
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        if not UtilClient.is_unset(request.use_previous_parameters):
            query['UsePreviousParameters'] = request.use_previous_parameters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStack',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_stack(
        self,
        request: ros20190910_models.UpdateStackRequest,
    ) -> ros20190910_models.UpdateStackResponse:
        """
        The values of parameters in the Parameters section vary based on the value that you specify for the UsePreviousParameters parameter in the request. If you do not add the parameters that are defined in the template to the Parameters section, take note of the following items:
        *   UsePreviousParameters is set to false: If the template parameters have default values, the default values are used. Otherwise, you must specify values for the template parameters in the Parameters section.
        *   UsePreviousParameters is set to true: If you specify values for the template parameters when you create a stack, the values are used. If you leave the template parameters empty when you create a stack but the template parameters have default values, the default values are used.
        This topic describes how to update a stack. In this example, the template body of a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****` in the China (Beijing) region is updated to `{"ROSTemplateFormatVersion": "2015-09-01"}`.
        
        @param request: UpdateStackRequest
        @return: UpdateStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_stack_with_options(request, runtime)

    async def update_stack_async(
        self,
        request: ros20190910_models.UpdateStackRequest,
    ) -> ros20190910_models.UpdateStackResponse:
        """
        The values of parameters in the Parameters section vary based on the value that you specify for the UsePreviousParameters parameter in the request. If you do not add the parameters that are defined in the template to the Parameters section, take note of the following items:
        *   UsePreviousParameters is set to false: If the template parameters have default values, the default values are used. Otherwise, you must specify values for the template parameters in the Parameters section.
        *   UsePreviousParameters is set to true: If you specify values for the template parameters when you create a stack, the values are used. If you leave the template parameters empty when you create a stack but the template parameters have default values, the default values are used.
        This topic describes how to update a stack. In this example, the template body of a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****` in the China (Beijing) region is updated to `{"ROSTemplateFormatVersion": "2015-09-01"}`.
        
        @param request: UpdateStackRequest
        @return: UpdateStackResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_with_options_async(request, runtime)

    def update_stack_group_with_options(
        self,
        tmp_req: ros20190910_models.UpdateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        """
        The name of the stack group. The name must be unique within a region.
        The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\\_). The name must start with a digit or a letter.
        
        @param tmp_req: UpdateStackGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStackGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.auto_deployment):
            request.auto_deployment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not UtilClient.is_unset(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not UtilClient.is_unset(request.capabilities):
            query['Capabilities'] = request.capabilities
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_stack_group_with_options_async(
        self,
        tmp_req: ros20190910_models.UpdateStackGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        """
        The name of the stack group. The name must be unique within a region.
        The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\\_). The name must start with a digit or a letter.
        
        @param tmp_req: UpdateStackGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStackGroupResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.auto_deployment):
            request.auto_deployment_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.auto_deployment, 'AutoDeployment', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.administration_role_name):
            query['AdministrationRoleName'] = request.administration_role_name
        if not UtilClient.is_unset(request.auto_deployment_shrink):
            query['AutoDeployment'] = request.auto_deployment_shrink
        if not UtilClient.is_unset(request.capabilities):
            query['Capabilities'] = request.capabilities
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_role_name):
            query['ExecutionRoleName'] = request.execution_role_name
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.permission_model):
            query['PermissionModel'] = request.permission_model
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.template_version):
            query['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStackGroup',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_stack_group(
        self,
        request: ros20190910_models.UpdateStackGroupRequest,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        """
        The name of the stack group. The name must be unique within a region.
        The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\\_). The name must start with a digit or a letter.
        
        @param request: UpdateStackGroupRequest
        @return: UpdateStackGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_stack_group_with_options(request, runtime)

    async def update_stack_group_async(
        self,
        request: ros20190910_models.UpdateStackGroupRequest,
    ) -> ros20190910_models.UpdateStackGroupResponse:
        """
        The name of the stack group. The name must be unique within a region.
        The name can be up to 255 characters in length and can contain digits, letters, hyphens (-), and underscores (\\_). The name must start with a digit or a letter.
        
        @param request: UpdateStackGroupRequest
        @return: UpdateStackGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_group_with_options_async(request, runtime)

    def update_stack_instances_with_options(
        self,
        tmp_req: ros20190910_models.UpdateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        """
        This topic provides an example on how to update stacks in a stack group. In this example, the stacks that are deployed in a stack group named `MyStackGroup` are updated. The stacks are deployed within the `151266687691***` and `141261387191****` Alibaba Cloud accounts in the China (Hangzhou) and China (Beijing) regions. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param tmp_req: UpdateStackInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStackInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_stack_instances_with_options_async(
        self,
        tmp_req: ros20190910_models.UpdateStackInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        """
        This topic provides an example on how to update stacks in a stack group. In this example, the stacks that are deployed in a stack group named `MyStackGroup` are updated. The stacks are deployed within the `151266687691***` and `141261387191****` Alibaba Cloud accounts in the China (Hangzhou) and China (Beijing) regions. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param tmp_req: UpdateStackInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStackInstancesResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateStackInstancesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.account_ids):
            request.account_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        if not UtilClient.is_unset(tmp_req.deployment_targets):
            request.deployment_targets_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.deployment_targets, 'DeploymentTargets', 'json')
        if not UtilClient.is_unset(tmp_req.operation_preferences):
            request.operation_preferences_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.operation_preferences, 'OperationPreferences', 'json')
        if not UtilClient.is_unset(tmp_req.region_ids):
            request.region_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.region_ids, 'RegionIds', 'json')
        query = {}
        if not UtilClient.is_unset(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deployment_targets_shrink):
            query['DeploymentTargets'] = request.deployment_targets_shrink
        if not UtilClient.is_unset(request.operation_description):
            query['OperationDescription'] = request.operation_description
        if not UtilClient.is_unset(request.operation_preferences_shrink):
            query['OperationPreferences'] = request.operation_preferences_shrink
        if not UtilClient.is_unset(request.parameter_overrides):
            query['ParameterOverrides'] = request.parameter_overrides
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_ids_shrink):
            query['RegionIds'] = request.region_ids_shrink
        if not UtilClient.is_unset(request.stack_group_name):
            query['StackGroupName'] = request.stack_group_name
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStackInstances',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_stack_instances(
        self,
        request: ros20190910_models.UpdateStackInstancesRequest,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        """
        This topic provides an example on how to update stacks in a stack group. In this example, the stacks that are deployed in a stack group named `MyStackGroup` are updated. The stacks are deployed within the `151266687691***` and `141261387191****` Alibaba Cloud accounts in the China (Hangzhou) and China (Beijing) regions. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: UpdateStackInstancesRequest
        @return: UpdateStackInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_stack_instances_with_options(request, runtime)

    async def update_stack_instances_async(
        self,
        request: ros20190910_models.UpdateStackInstancesRequest,
    ) -> ros20190910_models.UpdateStackInstancesResponse:
        """
        This topic provides an example on how to update stacks in a stack group. In this example, the stacks that are deployed in a stack group named `MyStackGroup` are updated. The stacks are deployed within the `151266687691***` and `141261387191****` Alibaba Cloud accounts in the China (Hangzhou) and China (Beijing) regions. The stack group is granted self-managed permissions and deployed in the China (Hangzhou) region.
        
        @param request: UpdateStackInstancesRequest
        @return: UpdateStackInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_instances_with_options_async(request, runtime)

    def update_stack_template_by_resources_with_options(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        """
        Limits: You can eliminate only drift on stacks that have drifted. You must call the [DetectStackDrift](~~155094~~) operation to perform drift detection on a stack, call the [GetStackDriftDetectionStatus](~~155097~~) operation to query the drift status of the stack to make sure that the stack has drifted, and then call the UpdateStackTemplateByResources operation to eliminate drift.
        In this topic, drift is eliminated for a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****`. The stack is deployed in the China (Hangzhou) region.
        
        @param request: UpdateStackTemplateByResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStackTemplateByResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_format):
            query['TemplateFormat'] = request.template_format
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStackTemplateByResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackTemplateByResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_stack_template_by_resources_with_options_async(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        """
        Limits: You can eliminate only drift on stacks that have drifted. You must call the [DetectStackDrift](~~155094~~) operation to perform drift detection on a stack, call the [GetStackDriftDetectionStatus](~~155097~~) operation to query the drift status of the stack to make sure that the stack has drifted, and then call the UpdateStackTemplateByResources operation to eliminate drift.
        In this topic, drift is eliminated for a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****`. The stack is deployed in the China (Hangzhou) region.
        
        @param request: UpdateStackTemplateByResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateStackTemplateByResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.logical_resource_id):
            query['LogicalResourceId'] = request.logical_resource_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.stack_id):
            query['StackId'] = request.stack_id
        if not UtilClient.is_unset(request.template_format):
            query['TemplateFormat'] = request.template_format
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateStackTemplateByResources',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateStackTemplateByResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_stack_template_by_resources(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        """
        Limits: You can eliminate only drift on stacks that have drifted. You must call the [DetectStackDrift](~~155094~~) operation to perform drift detection on a stack, call the [GetStackDriftDetectionStatus](~~155097~~) operation to query the drift status of the stack to make sure that the stack has drifted, and then call the UpdateStackTemplateByResources operation to eliminate drift.
        In this topic, drift is eliminated for a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****`. The stack is deployed in the China (Hangzhou) region.
        
        @param request: UpdateStackTemplateByResourcesRequest
        @return: UpdateStackTemplateByResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_stack_template_by_resources_with_options(request, runtime)

    async def update_stack_template_by_resources_async(
        self,
        request: ros20190910_models.UpdateStackTemplateByResourcesRequest,
    ) -> ros20190910_models.UpdateStackTemplateByResourcesResponse:
        """
        Limits: You can eliminate only drift on stacks that have drifted. You must call the [DetectStackDrift](~~155094~~) operation to perform drift detection on a stack, call the [GetStackDriftDetectionStatus](~~155097~~) operation to query the drift status of the stack to make sure that the stack has drifted, and then call the UpdateStackTemplateByResources operation to eliminate drift.
        In this topic, drift is eliminated for a stack whose ID is `4a6c9851-3b0f-4f5f-b4ca-a14bf691****`. The stack is deployed in the China (Hangzhou) region.
        
        @param request: UpdateStackTemplateByResourcesRequest
        @return: UpdateStackTemplateByResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_stack_template_by_resources_with_options_async(request, runtime)

    def update_template_with_options(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateTemplateResponse:
        """
        Take note of the following items:
        *   If you specify the TemplateBody or TemplateURL parameter, the existing version number is automatically incremented by 1 after the template is updated. For example, the version is changed from v1 to V2.
        *   If you do not specify the TemplateBody or TemplateURL parameter, the version number remains unchanged.
        *   A template can have up to 100 versions. If the number of templates reaches the upper limit, the template fails to be updated. You must create another template.
        
        @param request: UpdateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_with_options_async(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateTemplateResponse:
        """
        Take note of the following items:
        *   If you specify the TemplateBody or TemplateURL parameter, the existing version number is automatically incremented by 1 after the template is updated. For example, the version is changed from v1 to V2.
        *   If you do not specify the TemplateBody or TemplateURL parameter, the version number remains unchanged.
        *   A template can have up to 100 versions. If the number of templates reaches the upper limit, the template fails to be updated. You must create another template.
        
        @param request: UpdateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.template_body):
            query['TemplateBody'] = request.template_body
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
    ) -> ros20190910_models.UpdateTemplateResponse:
        """
        Take note of the following items:
        *   If you specify the TemplateBody or TemplateURL parameter, the existing version number is automatically incremented by 1 after the template is updated. For example, the version is changed from v1 to V2.
        *   If you do not specify the TemplateBody or TemplateURL parameter, the version number remains unchanged.
        *   A template can have up to 100 versions. If the number of templates reaches the upper limit, the template fails to be updated. You must create another template.
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_template_with_options(request, runtime)

    async def update_template_async(
        self,
        request: ros20190910_models.UpdateTemplateRequest,
    ) -> ros20190910_models.UpdateTemplateResponse:
        """
        Take note of the following items:
        *   If you specify the TemplateBody or TemplateURL parameter, the existing version number is automatically incremented by 1 after the template is updated. For example, the version is changed from v1 to V2.
        *   If you do not specify the TemplateBody or TemplateURL parameter, the version number remains unchanged.
        *   A template can have up to 100 versions. If the number of templates reaches the upper limit, the template fails to be updated. You must create another template.
        
        @param request: UpdateTemplateRequest
        @return: UpdateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_template_with_options_async(request, runtime)

    def update_template_scratch_with_options(
        self,
        tmp_req: ros20190910_models.UpdateTemplateScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateTemplateScratchResponse:
        """
        In this topic, the `ts-7f7a704cf71c49a6***` scenario that is created in the China (Hangzhou) region is updated. In this scenario, the ID of the virtual private cloud (VPC) is updated to `ts-7f7a704cf71c49a6****`.
        
        @param tmp_req: UpdateTemplateScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateScratchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateTemplateScratchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.preference_parameters):
            request.preference_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_resource_group):
            request.source_resource_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not UtilClient.is_unset(tmp_req.source_resources):
            request.source_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not UtilClient.is_unset(tmp_req.source_tag):
            request.source_tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not UtilClient.is_unset(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not UtilClient.is_unset(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not UtilClient.is_unset(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateTemplateScratchResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_template_scratch_with_options_async(
        self,
        tmp_req: ros20190910_models.UpdateTemplateScratchRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.UpdateTemplateScratchResponse:
        """
        In this topic, the `ts-7f7a704cf71c49a6***` scenario that is created in the China (Hangzhou) region is updated. In this scenario, the ID of the virtual private cloud (VPC) is updated to `ts-7f7a704cf71c49a6****`.
        
        @param tmp_req: UpdateTemplateScratchRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateTemplateScratchResponse
        """
        UtilClient.validate_model(tmp_req)
        request = ros20190910_models.UpdateTemplateScratchShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.preference_parameters):
            request.preference_parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.preference_parameters, 'PreferenceParameters', 'json')
        if not UtilClient.is_unset(tmp_req.source_resource_group):
            request.source_resource_group_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resource_group, 'SourceResourceGroup', 'json')
        if not UtilClient.is_unset(tmp_req.source_resources):
            request.source_resources_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_resources, 'SourceResources', 'json')
        if not UtilClient.is_unset(tmp_req.source_tag):
            request.source_tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_tag, 'SourceTag', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execution_mode):
            query['ExecutionMode'] = request.execution_mode
        if not UtilClient.is_unset(request.logical_id_strategy):
            query['LogicalIdStrategy'] = request.logical_id_strategy
        if not UtilClient.is_unset(request.preference_parameters_shrink):
            query['PreferenceParameters'] = request.preference_parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_resource_group_shrink):
            query['SourceResourceGroup'] = request.source_resource_group_shrink
        if not UtilClient.is_unset(request.source_resources_shrink):
            query['SourceResources'] = request.source_resources_shrink
        if not UtilClient.is_unset(request.source_tag_shrink):
            query['SourceTag'] = request.source_tag_shrink
        if not UtilClient.is_unset(request.template_scratch_id):
            query['TemplateScratchId'] = request.template_scratch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTemplateScratch',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.UpdateTemplateScratchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_template_scratch(
        self,
        request: ros20190910_models.UpdateTemplateScratchRequest,
    ) -> ros20190910_models.UpdateTemplateScratchResponse:
        """
        In this topic, the `ts-7f7a704cf71c49a6***` scenario that is created in the China (Hangzhou) region is updated. In this scenario, the ID of the virtual private cloud (VPC) is updated to `ts-7f7a704cf71c49a6****`.
        
        @param request: UpdateTemplateScratchRequest
        @return: UpdateTemplateScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_template_scratch_with_options(request, runtime)

    async def update_template_scratch_async(
        self,
        request: ros20190910_models.UpdateTemplateScratchRequest,
    ) -> ros20190910_models.UpdateTemplateScratchResponse:
        """
        In this topic, the `ts-7f7a704cf71c49a6***` scenario that is created in the China (Hangzhou) region is updated. In this scenario, the ID of the virtual private cloud (VPC) is updated to `ts-7f7a704cf71c49a6****`.
        
        @param request: UpdateTemplateScratchRequest
        @return: UpdateTemplateScratchResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_template_scratch_with_options_async(request, runtime)

    def validate_template_with_options(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ValidateTemplateResponse:
        """
        The description of the template.
        
        @param request: ValidateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.validation_option):
            query['ValidationOption'] = request.validation_option
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ValidateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_template_with_options_async(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> ros20190910_models.ValidateTemplateResponse:
        """
        The description of the template.
        
        @param request: ValidateTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.template_url):
            query['TemplateURL'] = request.template_url
        if not UtilClient.is_unset(request.validation_option):
            query['ValidationOption'] = request.validation_option
        body = {}
        if not UtilClient.is_unset(request.template_body):
            body['TemplateBody'] = request.template_body
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateTemplate',
            version='2019-09-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            ros20190910_models.ValidateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_template(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
    ) -> ros20190910_models.ValidateTemplateResponse:
        """
        The description of the template.
        
        @param request: ValidateTemplateRequest
        @return: ValidateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_template_with_options(request, runtime)

    async def validate_template_async(
        self,
        request: ros20190910_models.ValidateTemplateRequest,
    ) -> ros20190910_models.ValidateTemplateResponse:
        """
        The description of the template.
        
        @param request: ValidateTemplateRequest
        @return: ValidateTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_template_with_options_async(request, runtime)
