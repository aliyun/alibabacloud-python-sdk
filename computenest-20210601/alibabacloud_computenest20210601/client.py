# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_computenest20210601 import models as main_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('computenest', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def cancel_service_usage_with_options(
        self,
        request: main_models.CancelServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.need_delete):
            query['NeedDelete'] = request.need_delete
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelServiceUsage',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_service_usage_with_options_async(
        self,
        request: main_models.CancelServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.need_delete):
            query['NeedDelete'] = request.need_delete
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelServiceUsage',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_service_usage(
        self,
        request: main_models.CancelServiceUsageRequest,
    ) -> main_models.CancelServiceUsageResponse:
        runtime = RuntimeOptions()
        return self.cancel_service_usage_with_options(request, runtime)

    async def cancel_service_usage_async(
        self,
        request: main_models.CancelServiceUsageRequest,
    ) -> main_models.CancelServiceUsageResponse:
        runtime = RuntimeOptions()
        return await self.cancel_service_usage_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
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
            action = 'ChangeResourceGroup',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChangeResourceGroupResponse:
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
            action = 'ChangeResourceGroup',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: main_models.ChangeResourceGroupRequest,
    ) -> main_models.ChangeResourceGroupResponse:
        runtime = RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_service_deployable_with_options(
        self,
        request: main_models.CheckServiceDeployableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceDeployableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.post_paid_amount):
            query['PostPaidAmount'] = request.post_paid_amount
        if not DaraCore.is_null(request.pre_paid_amount):
            query['PrePaidAmount'] = request.pre_paid_amount
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceDeployable',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceDeployableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_deployable_with_options_async(
        self,
        request: main_models.CheckServiceDeployableRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CheckServiceDeployableResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.post_paid_amount):
            query['PostPaidAmount'] = request.post_paid_amount
        if not DaraCore.is_null(request.pre_paid_amount):
            query['PrePaidAmount'] = request.pre_paid_amount
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CheckServiceDeployable',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckServiceDeployableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_deployable(
        self,
        request: main_models.CheckServiceDeployableRequest,
    ) -> main_models.CheckServiceDeployableResponse:
        runtime = RuntimeOptions()
        return self.check_service_deployable_with_options(request, runtime)

    async def check_service_deployable_async(
        self,
        request: main_models.CheckServiceDeployableRequest,
    ) -> main_models.CheckServiceDeployableResponse:
        runtime = RuntimeOptions()
        return await self.check_service_deployable_with_options_async(request, runtime)

    def continue_deploy_service_instance_with_options(
        self,
        request: main_models.ContinueDeployServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinueDeployServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinueDeployServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueDeployServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_deploy_service_instance_with_options_async(
        self,
        request: main_models.ContinueDeployServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ContinueDeployServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.option):
            query['Option'] = request.option
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ContinueDeployServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueDeployServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_deploy_service_instance(
        self,
        request: main_models.ContinueDeployServiceInstanceRequest,
    ) -> main_models.ContinueDeployServiceInstanceResponse:
        runtime = RuntimeOptions()
        return self.continue_deploy_service_instance_with_options(request, runtime)

    async def continue_deploy_service_instance_async(
        self,
        request: main_models.ContinueDeployServiceInstanceRequest,
    ) -> main_models.ContinueDeployServiceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.continue_deploy_service_instance_with_options_async(request, runtime)

    def create_backup_with_options(
        self,
        request: main_models.CreateBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackup',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_backup_with_options_async(
        self,
        request: main_models.CreateBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateBackup',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_backup(
        self,
        request: main_models.CreateBackupRequest,
    ) -> main_models.CreateBackupResponse:
        runtime = RuntimeOptions()
        return self.create_backup_with_options(request, runtime)

    async def create_backup_async(
        self,
        request: main_models.CreateBackupRequest,
    ) -> main_models.CreateBackupResponse:
        runtime = RuntimeOptions()
        return await self.create_backup_with_options_async(request, runtime)

    def create_restore_task_with_options(
        self,
        request: main_models.CreateRestoreTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRestoreTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRestoreTask',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRestoreTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_restore_task_with_options_async(
        self,
        request: main_models.CreateRestoreTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateRestoreTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateRestoreTask',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRestoreTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_restore_task(
        self,
        request: main_models.CreateRestoreTaskRequest,
    ) -> main_models.CreateRestoreTaskResponse:
        runtime = RuntimeOptions()
        return self.create_restore_task_with_options(request, runtime)

    async def create_restore_task_async(
        self,
        request: main_models.CreateRestoreTaskRequest,
    ) -> main_models.CreateRestoreTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_restore_task_with_options_async(request, runtime)

    def create_service_instance_with_options(
        self,
        tmp_req: main_models.CreateServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateServiceInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_instance_ops):
            query['EnableInstanceOps'] = request.enable_instance_ops
        if not DaraCore.is_null(request.enable_user_prometheus):
            query['EnableUserPrometheus'] = request.enable_user_prometheus
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_auto_pay):
            query['ResourceAutoPay'] = request.resource_auto_pay
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.specification_code):
            query['SpecificationCode'] = request.specification_code
        if not DaraCore.is_null(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_instance_with_options_async(
        self,
        tmp_req: main_models.CreateServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceInstanceResponse:
        tmp_req.validate()
        request = main_models.CreateServiceInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_instance_ops):
            query['EnableInstanceOps'] = request.enable_instance_ops
        if not DaraCore.is_null(request.enable_user_prometheus):
            query['EnableUserPrometheus'] = request.enable_user_prometheus
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_auto_pay):
            query['ResourceAutoPay'] = request.resource_auto_pay
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.specification_code):
            query['SpecificationCode'] = request.specification_code
        if not DaraCore.is_null(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_instance(
        self,
        request: main_models.CreateServiceInstanceRequest,
    ) -> main_models.CreateServiceInstanceResponse:
        runtime = RuntimeOptions()
        return self.create_service_instance_with_options(request, runtime)

    async def create_service_instance_async(
        self,
        request: main_models.CreateServiceInstanceRequest,
    ) -> main_models.CreateServiceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.create_service_instance_with_options_async(request, runtime)

    def create_service_usage_with_options(
        self,
        tmp_req: main_models.CreateServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceUsageResponse:
        tmp_req.validate()
        request = main_models.CreateServiceUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_information):
            request.user_information_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_information, 'UserInformation', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_information_shrink):
            query['UserInformation'] = request.user_information_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceUsage',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_usage_with_options_async(
        self,
        tmp_req: main_models.CreateServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceUsageResponse:
        tmp_req.validate()
        request = main_models.CreateServiceUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_information):
            request.user_information_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_information, 'UserInformation', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_information_shrink):
            query['UserInformation'] = request.user_information_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceUsage',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_usage(
        self,
        request: main_models.CreateServiceUsageRequest,
    ) -> main_models.CreateServiceUsageResponse:
        runtime = RuntimeOptions()
        return self.create_service_usage_with_options(request, runtime)

    async def create_service_usage_async(
        self,
        request: main_models.CreateServiceUsageRequest,
    ) -> main_models.CreateServiceUsageResponse:
        runtime = RuntimeOptions()
        return await self.create_service_usage_with_options_async(request, runtime)

    def delete_backup_with_options(
        self,
        request: main_models.DeleteBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackup',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_backup_with_options_async(
        self,
        request: main_models.DeleteBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteBackup',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_backup(
        self,
        request: main_models.DeleteBackupRequest,
    ) -> main_models.DeleteBackupResponse:
        runtime = RuntimeOptions()
        return self.delete_backup_with_options(request, runtime)

    async def delete_backup_async(
        self,
        request: main_models.DeleteBackupRequest,
    ) -> main_models.DeleteBackupResponse:
        runtime = RuntimeOptions()
        return await self.delete_backup_with_options_async(request, runtime)

    def delete_service_instances_with_options(
        self,
        request: main_models.DeleteServiceInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceInstances',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_instances_with_options_async(
        self,
        request: main_models.DeleteServiceInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceInstances',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_instances(
        self,
        request: main_models.DeleteServiceInstancesRequest,
    ) -> main_models.DeleteServiceInstancesResponse:
        runtime = RuntimeOptions()
        return self.delete_service_instances_with_options(request, runtime)

    async def delete_service_instances_async(
        self,
        request: main_models.DeleteServiceInstancesRequest,
    ) -> main_models.DeleteServiceInstancesResponse:
        runtime = RuntimeOptions()
        return await self.delete_service_instances_with_options_async(request, runtime)

    def deploy_service_instance_with_options(
        self,
        request: main_models.DeployServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_service_instance_with_options_async(
        self,
        request: main_models.DeployServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeployServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeployServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeployServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_service_instance(
        self,
        request: main_models.DeployServiceInstanceRequest,
    ) -> main_models.DeployServiceInstanceResponse:
        runtime = RuntimeOptions()
        return self.deploy_service_instance_with_options(request, runtime)

    async def deploy_service_instance_async(
        self,
        request: main_models.DeployServiceInstanceRequest,
    ) -> main_models.DeployServiceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.deploy_service_instance_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2021-06-01',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2021-06-01',
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

    def generate_service_policy_with_options(
        self,
        request: main_models.GenerateServicePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateServicePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_types):
            query['OperationTypes'] = request.operation_types
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateServicePolicy',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateServicePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_service_policy_with_options_async(
        self,
        request: main_models.GenerateServicePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateServicePolicyResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.operation_types):
            query['OperationTypes'] = request.operation_types
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateServicePolicy',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateServicePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_service_policy(
        self,
        request: main_models.GenerateServicePolicyRequest,
    ) -> main_models.GenerateServicePolicyResponse:
        runtime = RuntimeOptions()
        return self.generate_service_policy_with_options(request, runtime)

    async def generate_service_policy_async(
        self,
        request: main_models.GenerateServicePolicyRequest,
    ) -> main_models.GenerateServicePolicyResponse:
        runtime = RuntimeOptions()
        return await self.generate_service_policy_with_options_async(request, runtime)

    def get_backup_with_options(
        self,
        request: main_models.GetBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBackup',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBackupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_backup_with_options_async(
        self,
        request: main_models.GetBackupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetBackupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.backup_id):
            query['BackupId'] = request.backup_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetBackup',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBackupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_backup(
        self,
        request: main_models.GetBackupRequest,
    ) -> main_models.GetBackupResponse:
        runtime = RuntimeOptions()
        return self.get_backup_with_options(request, runtime)

    async def get_backup_async(
        self,
        request: main_models.GetBackupRequest,
    ) -> main_models.GetBackupResponse:
        runtime = RuntimeOptions()
        return await self.get_backup_with_options_async(request, runtime)

    def get_network_available_zones_with_options(
        self,
        request: main_models.GetNetworkAvailableZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkAvailableZonesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_poc):
            body['IsPoc'] = request.is_poc
        if not DaraCore.is_null(request.network_region_id):
            body['NetworkRegionId'] = request.network_region_id
        if not DaraCore.is_null(request.private_vpc_connection_mode):
            body['PrivateVpcConnectionMode'] = request.private_vpc_connection_mode
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_endpoint_service_type):
            body['ServiceInstanceEndpointServiceType'] = request.service_instance_endpoint_service_type
        if not DaraCore.is_null(request.service_region_id):
            body['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.service_version):
            body['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkAvailableZones',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkAvailableZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_available_zones_with_options_async(
        self,
        request: main_models.GetNetworkAvailableZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetNetworkAvailableZonesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_poc):
            body['IsPoc'] = request.is_poc
        if not DaraCore.is_null(request.network_region_id):
            body['NetworkRegionId'] = request.network_region_id
        if not DaraCore.is_null(request.private_vpc_connection_mode):
            body['PrivateVpcConnectionMode'] = request.private_vpc_connection_mode
        if not DaraCore.is_null(request.service_id):
            body['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_endpoint_service_type):
            body['ServiceInstanceEndpointServiceType'] = request.service_instance_endpoint_service_type
        if not DaraCore.is_null(request.service_region_id):
            body['ServiceRegionId'] = request.service_region_id
        if not DaraCore.is_null(request.service_version):
            body['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.zone_id):
            body['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetNetworkAvailableZones',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetNetworkAvailableZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_available_zones(
        self,
        request: main_models.GetNetworkAvailableZonesRequest,
    ) -> main_models.GetNetworkAvailableZonesResponse:
        runtime = RuntimeOptions()
        return self.get_network_available_zones_with_options(request, runtime)

    async def get_network_available_zones_async(
        self,
        request: main_models.GetNetworkAvailableZonesRequest,
    ) -> main_models.GetNetworkAvailableZonesResponse:
        runtime = RuntimeOptions()
        return await self.get_network_available_zones_with_options_async(request, runtime)

    def get_service_with_options(
        self,
        request: main_models.GetServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.show_details):
            query['ShowDetails'] = request.show_details
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        request: main_models.GetServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_name):
            query['ServiceName'] = request.service_name
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.show_details):
            query['ShowDetails'] = request.show_details
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        request: main_models.GetServiceRequest,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        return self.get_service_with_options(request, runtime)

    async def get_service_async(
        self,
        request: main_models.GetServiceRequest,
    ) -> main_models.GetServiceResponse:
        runtime = RuntimeOptions()
        return await self.get_service_with_options_async(request, runtime)

    def get_service_estimate_cost_with_options(
        self,
        tmp_req: main_models.GetServiceEstimateCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceEstimateCostResponse:
        tmp_req.validate()
        request = main_models.GetServiceEstimateCostShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.commodity):
            request.commodity_shrink = Utils.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity_shrink):
            query['Commodity'] = request.commodity_shrink
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEstimateCost',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceEstimateCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_estimate_cost_with_options_async(
        self,
        tmp_req: main_models.GetServiceEstimateCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceEstimateCostResponse:
        tmp_req.validate()
        request = main_models.GetServiceEstimateCostShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.commodity):
            request.commodity_shrink = Utils.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity_shrink):
            query['Commodity'] = request.commodity_shrink
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEstimateCost',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceEstimateCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_estimate_cost(
        self,
        request: main_models.GetServiceEstimateCostRequest,
    ) -> main_models.GetServiceEstimateCostResponse:
        runtime = RuntimeOptions()
        return self.get_service_estimate_cost_with_options(request, runtime)

    async def get_service_estimate_cost_async(
        self,
        request: main_models.GetServiceEstimateCostRequest,
    ) -> main_models.GetServiceEstimateCostResponse:
        runtime = RuntimeOptions()
        return await self.get_service_estimate_cost_with_options_async(request, runtime)

    def get_service_instance_with_options(
        self,
        request: main_models.GetServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.market_instance_id):
            query['MarketInstanceId'] = request.market_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_instance_with_options_async(
        self,
        request: main_models.GetServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.market_instance_id):
            query['MarketInstanceId'] = request.market_instance_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_instance(
        self,
        request: main_models.GetServiceInstanceRequest,
    ) -> main_models.GetServiceInstanceResponse:
        runtime = RuntimeOptions()
        return self.get_service_instance_with_options(request, runtime)

    async def get_service_instance_async(
        self,
        request: main_models.GetServiceInstanceRequest,
    ) -> main_models.GetServiceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.get_service_instance_with_options_async(request, runtime)

    def get_service_instance_subscription_estimate_cost_with_options(
        self,
        request: main_models.GetServiceInstanceSubscriptionEstimateCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceInstanceSubscriptionEstimateCostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_period):
            query['ResourcePeriod'] = request.resource_period
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceInstanceSubscriptionEstimateCost',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceInstanceSubscriptionEstimateCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_instance_subscription_estimate_cost_with_options_async(
        self,
        request: main_models.GetServiceInstanceSubscriptionEstimateCostRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceInstanceSubscriptionEstimateCostResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.order_type):
            query['OrderType'] = request.order_type
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_period):
            query['ResourcePeriod'] = request.resource_period
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceInstanceSubscriptionEstimateCost',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceInstanceSubscriptionEstimateCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_instance_subscription_estimate_cost(
        self,
        request: main_models.GetServiceInstanceSubscriptionEstimateCostRequest,
    ) -> main_models.GetServiceInstanceSubscriptionEstimateCostResponse:
        runtime = RuntimeOptions()
        return self.get_service_instance_subscription_estimate_cost_with_options(request, runtime)

    async def get_service_instance_subscription_estimate_cost_async(
        self,
        request: main_models.GetServiceInstanceSubscriptionEstimateCostRequest,
    ) -> main_models.GetServiceInstanceSubscriptionEstimateCostResponse:
        runtime = RuntimeOptions()
        return await self.get_service_instance_subscription_estimate_cost_with_options_async(request, runtime)

    def get_service_provisions_with_options(
        self,
        tmp_req: main_models.GetServiceProvisionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceProvisionsResponse:
        tmp_req.validate()
        request = main_models.GetServiceProvisionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceProvisions',
            version = '2021-06-01',
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
        tmp_req: main_models.GetServiceProvisionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceProvisionsResponse:
        tmp_req.validate()
        request = main_models.GetServiceProvisionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceProvisions',
            version = '2021-06-01',
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

    def get_service_template_parameter_constraints_with_options(
        self,
        request: main_models.GetServiceTemplateParameterConstraintsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceTemplateParameterConstraintsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not DaraCore.is_null(request.enable_private_vpc_connection):
            query['EnablePrivateVpcConnection'] = request.enable_private_vpc_connection
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceTemplateParameterConstraints',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceTemplateParameterConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_template_parameter_constraints_with_options_async(
        self,
        request: main_models.GetServiceTemplateParameterConstraintsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceTemplateParameterConstraintsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not DaraCore.is_null(request.enable_private_vpc_connection):
            query['EnablePrivateVpcConnection'] = request.enable_private_vpc_connection
        if not DaraCore.is_null(request.parameters):
            query['Parameters'] = request.parameters
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceTemplateParameterConstraints',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceTemplateParameterConstraintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_template_parameter_constraints(
        self,
        request: main_models.GetServiceTemplateParameterConstraintsRequest,
    ) -> main_models.GetServiceTemplateParameterConstraintsResponse:
        runtime = RuntimeOptions()
        return self.get_service_template_parameter_constraints_with_options(request, runtime)

    async def get_service_template_parameter_constraints_async(
        self,
        request: main_models.GetServiceTemplateParameterConstraintsRequest,
    ) -> main_models.GetServiceTemplateParameterConstraintsResponse:
        runtime = RuntimeOptions()
        return await self.get_service_template_parameter_constraints_with_options_async(request, runtime)

    def get_user_information_with_options(
        self,
        request: main_models.GetUserInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserInformation',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_information_with_options_async(
        self,
        request: main_models.GetUserInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserInformation',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_information(
        self,
        request: main_models.GetUserInformationRequest,
    ) -> main_models.GetUserInformationResponse:
        runtime = RuntimeOptions()
        return self.get_user_information_with_options(request, runtime)

    async def get_user_information_async(
        self,
        request: main_models.GetUserInformationRequest,
    ) -> main_models.GetUserInformationResponse:
        runtime = RuntimeOptions()
        return await self.get_user_information_with_options_async(request, runtime)

    def list_backups_with_options(
        self,
        request: main_models.ListBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBackups',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBackupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_backups_with_options_async(
        self,
        request: main_models.ListBackupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListBackupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBackups',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBackupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_backups(
        self,
        request: main_models.ListBackupsRequest,
    ) -> main_models.ListBackupsResponse:
        runtime = RuntimeOptions()
        return self.list_backups_with_options(request, runtime)

    async def list_backups_async(
        self,
        request: main_models.ListBackupsRequest,
    ) -> main_models.ListBackupsResponse:
        runtime = RuntimeOptions()
        return await self.list_backups_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: main_models.ListPoliciesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPoliciesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPolicies',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: main_models.ListPoliciesRequest,
    ) -> main_models.ListPoliciesResponse:
        runtime = RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_restore_tasks_with_options(
        self,
        request: main_models.ListRestoreTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRestoreTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRestoreTasks',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRestoreTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_restore_tasks_with_options_async(
        self,
        request: main_models.ListRestoreTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListRestoreTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRestoreTasks',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRestoreTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_restore_tasks(
        self,
        request: main_models.ListRestoreTasksRequest,
    ) -> main_models.ListRestoreTasksResponse:
        runtime = RuntimeOptions()
        return self.list_restore_tasks_with_options(request, runtime)

    async def list_restore_tasks_async(
        self,
        request: main_models.ListRestoreTasksRequest,
    ) -> main_models.ListRestoreTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_restore_tasks_with_options_async(request, runtime)

    def list_service_categories_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceCategoriesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListServiceCategories',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_categories_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceCategoriesResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListServiceCategories',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_categories(self) -> main_models.ListServiceCategoriesResponse:
        runtime = RuntimeOptions()
        return self.list_service_categories_with_options(runtime)

    async def list_service_categories_async(self) -> main_models.ListServiceCategoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_service_categories_with_options_async(runtime)

    def list_service_instance_bill_with_options(
        self,
        request: main_models.ListServiceInstanceBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceBill',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_bill_with_options_async(
        self,
        request: main_models.ListServiceInstanceBillRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceBillResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not DaraCore.is_null(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not DaraCore.is_null(request.granularity):
            query['Granularity'] = request.granularity
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceBill',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_bill(
        self,
        request: main_models.ListServiceInstanceBillRequest,
    ) -> main_models.ListServiceInstanceBillResponse:
        runtime = RuntimeOptions()
        return self.list_service_instance_bill_with_options(request, runtime)

    async def list_service_instance_bill_async(
        self,
        request: main_models.ListServiceInstanceBillRequest,
    ) -> main_models.ListServiceInstanceBillResponse:
        runtime = RuntimeOptions()
        return await self.list_service_instance_bill_with_options_async(request, runtime)

    def list_service_instance_logs_with_options(
        self,
        request: main_models.ListServiceInstanceLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.log_source):
            query['LogSource'] = request.log_source
        if not DaraCore.is_null(request.logstore):
            query['Logstore'] = request.logstore
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceLogs',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_logs_with_options_async(
        self,
        request: main_models.ListServiceInstanceLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.log_source):
            query['LogSource'] = request.log_source
        if not DaraCore.is_null(request.logstore):
            query['Logstore'] = request.logstore
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceLogs',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_logs(
        self,
        request: main_models.ListServiceInstanceLogsRequest,
    ) -> main_models.ListServiceInstanceLogsResponse:
        runtime = RuntimeOptions()
        return self.list_service_instance_logs_with_options(request, runtime)

    async def list_service_instance_logs_async(
        self,
        request: main_models.ListServiceInstanceLogsRequest,
    ) -> main_models.ListServiceInstanceLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_service_instance_logs_with_options_async(request, runtime)

    def list_service_instance_resources_with_options(
        self,
        request: main_models.ListServiceInstanceResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_instance_resource_type):
            query['ServiceInstanceResourceType'] = request.service_instance_resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceResources',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_resources_with_options_async(
        self,
        request: main_models.ListServiceInstanceResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_instance_resource_type):
            query['ServiceInstanceResourceType'] = request.service_instance_resource_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceResources',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_resources(
        self,
        request: main_models.ListServiceInstanceResourcesRequest,
    ) -> main_models.ListServiceInstanceResourcesResponse:
        runtime = RuntimeOptions()
        return self.list_service_instance_resources_with_options(request, runtime)

    async def list_service_instance_resources_async(
        self,
        request: main_models.ListServiceInstanceResourcesRequest,
    ) -> main_models.ListServiceInstanceResourcesResponse:
        runtime = RuntimeOptions()
        return await self.list_service_instance_resources_with_options_async(request, runtime)

    def list_service_instance_upgrade_history_with_options(
        self,
        request: main_models.ListServiceInstanceUpgradeHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceUpgradeHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceUpgradeHistory',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceUpgradeHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_upgrade_history_with_options_async(
        self,
        request: main_models.ListServiceInstanceUpgradeHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceUpgradeHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceUpgradeHistory',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceUpgradeHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_upgrade_history(
        self,
        request: main_models.ListServiceInstanceUpgradeHistoryRequest,
    ) -> main_models.ListServiceInstanceUpgradeHistoryResponse:
        runtime = RuntimeOptions()
        return self.list_service_instance_upgrade_history_with_options(request, runtime)

    async def list_service_instance_upgrade_history_async(
        self,
        request: main_models.ListServiceInstanceUpgradeHistoryRequest,
    ) -> main_models.ListServiceInstanceUpgradeHistoryResponse:
        runtime = RuntimeOptions()
        return await self.list_service_instance_upgrade_history_with_options_async(request, runtime)

    def list_service_instances_with_options(
        self,
        request: main_models.ListServiceInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstances',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instances_with_options_async(
        self,
        request: main_models.ListServiceInstancesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstancesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstances',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instances(
        self,
        request: main_models.ListServiceInstancesRequest,
    ) -> main_models.ListServiceInstancesResponse:
        runtime = RuntimeOptions()
        return self.list_service_instances_with_options(request, runtime)

    async def list_service_instances_async(
        self,
        request: main_models.ListServiceInstancesRequest,
    ) -> main_models.ListServiceInstancesResponse:
        runtime = RuntimeOptions()
        return await self.list_service_instances_with_options_async(request, runtime)

    def list_service_usages_with_options(
        self,
        request: main_models.ListServiceUsagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceUsagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceUsages',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceUsagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_usages_with_options_async(
        self,
        request: main_models.ListServiceUsagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceUsagesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceUsages',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceUsagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_usages(
        self,
        request: main_models.ListServiceUsagesRequest,
    ) -> main_models.ListServiceUsagesResponse:
        runtime = RuntimeOptions()
        return self.list_service_usages_with_options(request, runtime)

    async def list_service_usages_async(
        self,
        request: main_models.ListServiceUsagesRequest,
    ) -> main_models.ListServiceUsagesResponse:
        runtime = RuntimeOptions()
        return await self.list_service_usages_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: main_models.ListServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.fuzzy_keyword):
            query['FuzzyKeyword'] = request.fuzzy_keyword
        if not DaraCore.is_null(request.in_used):
            query['InUsed'] = request.in_used
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_access_type):
            query['ServiceAccessType'] = request.service_access_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: main_models.ListServicesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServicesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.fuzzy_keyword):
            query['FuzzyKeyword'] = request.fuzzy_keyword
        if not DaraCore.is_null(request.in_used):
            query['InUsed'] = request.in_used
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_access_type):
            query['ServiceAccessType'] = request.service_access_type
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServices',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: main_models.ListServicesRequest,
    ) -> main_models.ListServicesResponse:
        runtime = RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)

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
            version = '2021-06-01',
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
            version = '2021-06-01',
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
            version = '2021-06-01',
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
            version = '2021-06-01',
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
            version = '2021-06-01',
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
            version = '2021-06-01',
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

    def renew_service_instance_resources_with_options(
        self,
        request: main_models.RenewServiceInstanceResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewServiceInstanceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_period):
            query['ResourcePeriod'] = request.resource_period
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewServiceInstanceResources',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewServiceInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_service_instance_resources_with_options_async(
        self,
        request: main_models.RenewServiceInstanceResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RenewServiceInstanceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.period):
            query['Period'] = request.period
        if not DaraCore.is_null(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_period):
            query['ResourcePeriod'] = request.resource_period
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RenewServiceInstanceResources',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RenewServiceInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_service_instance_resources(
        self,
        request: main_models.RenewServiceInstanceResourcesRequest,
    ) -> main_models.RenewServiceInstanceResourcesResponse:
        runtime = RuntimeOptions()
        return self.renew_service_instance_resources_with_options(request, runtime)

    async def renew_service_instance_resources_async(
        self,
        request: main_models.RenewServiceInstanceResourcesRequest,
    ) -> main_models.RenewServiceInstanceResourcesResponse:
        runtime = RuntimeOptions()
        return await self.renew_service_instance_resources_with_options_async(request, runtime)

    def restart_service_instance_with_options(
        self,
        request: main_models.RestartServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_service_instance_with_options_async(
        self,
        request: main_models.RestartServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RestartServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RestartServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RestartServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_service_instance(
        self,
        request: main_models.RestartServiceInstanceRequest,
    ) -> main_models.RestartServiceInstanceResponse:
        runtime = RuntimeOptions()
        return self.restart_service_instance_with_options(request, runtime)

    async def restart_service_instance_async(
        self,
        request: main_models.RestartServiceInstanceRequest,
    ) -> main_models.RestartServiceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.restart_service_instance_with_options_async(request, runtime)

    def rollback_service_instance_with_options(
        self,
        request: main_models.RollbackServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_service_instance_with_options_async(
        self,
        request: main_models.RollbackServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RollbackServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RollbackServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_service_instance(
        self,
        request: main_models.RollbackServiceInstanceRequest,
    ) -> main_models.RollbackServiceInstanceResponse:
        runtime = RuntimeOptions()
        return self.rollback_service_instance_with_options(request, runtime)

    async def rollback_service_instance_async(
        self,
        request: main_models.RollbackServiceInstanceRequest,
    ) -> main_models.RollbackServiceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.rollback_service_instance_with_options_async(request, runtime)

    def start_service_instance_with_options(
        self,
        request: main_models.StartServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_service_instance_with_options_async(
        self,
        request: main_models.StartServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StartServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StartServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StartServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_service_instance(
        self,
        request: main_models.StartServiceInstanceRequest,
    ) -> main_models.StartServiceInstanceResponse:
        runtime = RuntimeOptions()
        return self.start_service_instance_with_options(request, runtime)

    async def start_service_instance_async(
        self,
        request: main_models.StartServiceInstanceRequest,
    ) -> main_models.StartServiceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.start_service_instance_with_options_async(request, runtime)

    def stop_service_instance_with_options(
        self,
        request: main_models.StopServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_service_instance_with_options_async(
        self,
        request: main_models.StopServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.StopServiceInstanceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'StopServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.StopServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_service_instance(
        self,
        request: main_models.StopServiceInstanceRequest,
    ) -> main_models.StopServiceInstanceResponse:
        runtime = RuntimeOptions()
        return self.stop_service_instance_with_options(request, runtime)

    async def stop_service_instance_async(
        self,
        request: main_models.StopServiceInstanceRequest,
    ) -> main_models.StopServiceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.stop_service_instance_with_options_async(request, runtime)

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
            version = '2021-06-01',
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
            version = '2021-06-01',
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

    def un_tag_resources_with_options(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
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
            action = 'UnTagResources',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: main_models.UnTagResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UnTagResourcesResponse:
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
            action = 'UnTagResources',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: main_models.UnTagResourcesRequest,
    ) -> main_models.UnTagResourcesResponse:
        runtime = RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def update_service_instance_attributes_with_options(
        self,
        request: main_models.UpdateServiceInstanceAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceInstanceAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_operation):
            query['EnableOperation'] = request.enable_operation
        if not DaraCore.is_null(request.granted_permission):
            query['GrantedPermission'] = request.granted_permission
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceInstanceAttributes',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceInstanceAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_instance_attributes_with_options_async(
        self,
        request: main_models.UpdateServiceInstanceAttributesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceInstanceAttributesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enable_operation):
            query['EnableOperation'] = request.enable_operation
        if not DaraCore.is_null(request.granted_permission):
            query['GrantedPermission'] = request.granted_permission
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceInstanceAttributes',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceInstanceAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_instance_attributes(
        self,
        request: main_models.UpdateServiceInstanceAttributesRequest,
    ) -> main_models.UpdateServiceInstanceAttributesResponse:
        runtime = RuntimeOptions()
        return self.update_service_instance_attributes_with_options(request, runtime)

    async def update_service_instance_attributes_async(
        self,
        request: main_models.UpdateServiceInstanceAttributesRequest,
    ) -> main_models.UpdateServiceInstanceAttributesResponse:
        runtime = RuntimeOptions()
        return await self.update_service_instance_attributes_with_options_async(request, runtime)

    def update_service_instance_spec_with_options(
        self,
        tmp_req: main_models.UpdateServiceInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceInstanceSpecResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceInstanceSpecShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_user_prometheus):
            query['EnableUserPrometheus'] = request.enable_user_prometheus
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.predefined_parameters_name):
            query['PredefinedParametersName'] = request.predefined_parameters_name
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceInstanceSpec',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_instance_spec_with_options_async(
        self,
        tmp_req: main_models.UpdateServiceInstanceSpecRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceInstanceSpecResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceInstanceSpecShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity):
            query['Commodity'] = request.commodity
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.enable_user_prometheus):
            query['EnableUserPrometheus'] = request.enable_user_prometheus
        if not DaraCore.is_null(request.operation_name):
            query['OperationName'] = request.operation_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.predefined_parameters_name):
            query['PredefinedParametersName'] = request.predefined_parameters_name
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceInstanceSpec',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_instance_spec(
        self,
        request: main_models.UpdateServiceInstanceSpecRequest,
    ) -> main_models.UpdateServiceInstanceSpecResponse:
        runtime = RuntimeOptions()
        return self.update_service_instance_spec_with_options(request, runtime)

    async def update_service_instance_spec_async(
        self,
        request: main_models.UpdateServiceInstanceSpecRequest,
    ) -> main_models.UpdateServiceInstanceSpecResponse:
        runtime = RuntimeOptions()
        return await self.update_service_instance_spec_with_options_async(request, runtime)

    def update_service_usage_with_options(
        self,
        tmp_req: main_models.UpdateServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceUsageResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_information):
            request.user_information_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_information, 'UserInformation', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_information_shrink):
            query['UserInformation'] = request.user_information_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceUsage',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_usage_with_options_async(
        self,
        tmp_req: main_models.UpdateServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceUsageResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceUsageShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.user_information):
            request.user_information_shrink = Utils.array_to_string_with_specified_style(tmp_req.user_information, 'UserInformation', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.user_information_shrink):
            query['UserInformation'] = request.user_information_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceUsage',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_usage(
        self,
        request: main_models.UpdateServiceUsageRequest,
    ) -> main_models.UpdateServiceUsageResponse:
        runtime = RuntimeOptions()
        return self.update_service_usage_with_options(request, runtime)

    async def update_service_usage_async(
        self,
        request: main_models.UpdateServiceUsageRequest,
    ) -> main_models.UpdateServiceUsageResponse:
        runtime = RuntimeOptions()
        return await self.update_service_usage_with_options_async(request, runtime)

    def update_user_information_with_options(
        self,
        request: main_models.UpdateUserInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_settings):
            query['DeliverySettings'] = request.delivery_settings
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserInformation',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_information_with_options_async(
        self,
        request: main_models.UpdateUserInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateUserInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_settings):
            query['DeliverySettings'] = request.delivery_settings
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateUserInformation',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateUserInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_information(
        self,
        request: main_models.UpdateUserInformationRequest,
    ) -> main_models.UpdateUserInformationResponse:
        runtime = RuntimeOptions()
        return self.update_user_information_with_options(request, runtime)

    async def update_user_information_async(
        self,
        request: main_models.UpdateUserInformationRequest,
    ) -> main_models.UpdateUserInformationResponse:
        runtime = RuntimeOptions()
        return await self.update_user_information_with_options_async(request, runtime)

    def upgrade_service_instance_with_options(
        self,
        tmp_req: main_models.UpgradeServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeServiceInstanceResponse:
        tmp_req.validate()
        request = main_models.UpgradeServiceInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_service_instance_with_options_async(
        self,
        tmp_req: main_models.UpgradeServiceInstanceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpgradeServiceInstanceResponse:
        tmp_req.validate()
        request = main_models.UpgradeServiceInstanceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpgradeServiceInstance',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpgradeServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_service_instance(
        self,
        request: main_models.UpgradeServiceInstanceRequest,
    ) -> main_models.UpgradeServiceInstanceResponse:
        runtime = RuntimeOptions()
        return self.upgrade_service_instance_with_options(request, runtime)

    async def upgrade_service_instance_async(
        self,
        request: main_models.UpgradeServiceInstanceRequest,
    ) -> main_models.UpgradeServiceInstanceResponse:
        runtime = RuntimeOptions()
        return await self.upgrade_service_instance_with_options_async(request, runtime)

    def validate_service_instance_name_with_options(
        self,
        request: main_models.ValidateServiceInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateServiceInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.is_trial):
            query['IsTrial'] = request.is_trial
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_name):
            query['ServiceInstanceName'] = request.service_instance_name
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateServiceInstanceName',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateServiceInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_service_instance_name_with_options_async(
        self,
        request: main_models.ValidateServiceInstanceNameRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateServiceInstanceNameResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.is_trial):
            query['IsTrial'] = request.is_trial
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_name):
            query['ServiceInstanceName'] = request.service_instance_name
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateServiceInstanceName',
            version = '2021-06-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateServiceInstanceNameResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_service_instance_name(
        self,
        request: main_models.ValidateServiceInstanceNameRequest,
    ) -> main_models.ValidateServiceInstanceNameResponse:
        runtime = RuntimeOptions()
        return self.validate_service_instance_name_with_options(request, runtime)

    async def validate_service_instance_name_async(
        self,
        request: main_models.ValidateServiceInstanceNameRequest,
    ) -> main_models.ValidateServiceInstanceNameResponse:
        runtime = RuntimeOptions()
        return await self.validate_service_instance_name_with_options_async(request, runtime)
