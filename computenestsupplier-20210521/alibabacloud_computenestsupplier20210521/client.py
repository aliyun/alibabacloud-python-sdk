# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_computenestsupplier20210521 import models as main_models
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
        self._endpoint = self.get_endpoint('computenestsupplier', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_service_shared_accounts_with_options(
        self,
        request: main_models.AddServiceSharedAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddServiceSharedAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.shared_accounts):
            query['SharedAccounts'] = request.shared_accounts
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddServiceSharedAccounts',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddServiceSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_service_shared_accounts_with_options_async(
        self,
        request: main_models.AddServiceSharedAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddServiceSharedAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.shared_accounts):
            query['SharedAccounts'] = request.shared_accounts
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddServiceSharedAccounts',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddServiceSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_service_shared_accounts(
        self,
        request: main_models.AddServiceSharedAccountsRequest,
    ) -> main_models.AddServiceSharedAccountsResponse:
        runtime = RuntimeOptions()
        return self.add_service_shared_accounts_with_options(request, runtime)

    async def add_service_shared_accounts_async(
        self,
        request: main_models.AddServiceSharedAccountsRequest,
    ) -> main_models.AddServiceSharedAccountsResponse:
        runtime = RuntimeOptions()
        return await self.add_service_shared_accounts_with_options_async(request, runtime)

    def approve_service_usage_with_options(
        self,
        request: main_models.ApproveServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApproveServiceUsage',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_service_usage_with_options_async(
        self,
        request: main_models.ApproveServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ApproveServiceUsage',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_service_usage(
        self,
        request: main_models.ApproveServiceUsageRequest,
    ) -> main_models.ApproveServiceUsageResponse:
        runtime = RuntimeOptions()
        return self.approve_service_usage_with_options(request, runtime)

    async def approve_service_usage_async(
        self,
        request: main_models.ApproveServiceUsageRequest,
    ) -> main_models.ApproveServiceUsageResponse:
        runtime = RuntimeOptions()
        return await self.approve_service_usage_with_options_async(request, runtime)

    def cancel_service_registration_with_options(
        self,
        request: main_models.CancelServiceRegistrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelServiceRegistrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelServiceRegistration',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelServiceRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_service_registration_with_options_async(
        self,
        request: main_models.CancelServiceRegistrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelServiceRegistrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CancelServiceRegistration',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelServiceRegistrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_service_registration(
        self,
        request: main_models.CancelServiceRegistrationRequest,
    ) -> main_models.CancelServiceRegistrationResponse:
        runtime = RuntimeOptions()
        return self.cancel_service_registration_with_options(request, runtime)

    async def cancel_service_registration_async(
        self,
        request: main_models.CancelServiceRegistrationRequest,
    ) -> main_models.CancelServiceRegistrationResponse:
        runtime = RuntimeOptions()
        return await self.cancel_service_registration_with_options_async(request, runtime)

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
            version = '2021-05-21',
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
            version = '2021-05-21',
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

    def create_artifact_with_options(
        self,
        tmp_req: main_models.CreateArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactResponse:
        tmp_req.validate()
        request = main_models.CreateArtifactShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.artifact_build_property):
            request.artifact_build_property_shrink = Utils.array_to_string_with_specified_style(tmp_req.artifact_build_property, 'ArtifactBuildProperty', 'json')
        if not DaraCore.is_null(tmp_req.artifact_property):
            request.artifact_property_shrink = Utils.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not DaraCore.is_null(request.artifact_build_property_shrink):
            query['ArtifactBuildProperty'] = request.artifact_build_property_shrink
        if not DaraCore.is_null(request.artifact_build_type):
            query['ArtifactBuildType'] = request.artifact_build_type
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_artifact_with_options_async(
        self,
        tmp_req: main_models.CreateArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateArtifactResponse:
        tmp_req.validate()
        request = main_models.CreateArtifactShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.artifact_build_property):
            request.artifact_build_property_shrink = Utils.array_to_string_with_specified_style(tmp_req.artifact_build_property, 'ArtifactBuildProperty', 'json')
        if not DaraCore.is_null(tmp_req.artifact_property):
            request.artifact_property_shrink = Utils.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not DaraCore.is_null(request.artifact_build_property_shrink):
            query['ArtifactBuildProperty'] = request.artifact_build_property_shrink
        if not DaraCore.is_null(request.artifact_build_type):
            query['ArtifactBuildType'] = request.artifact_build_type
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_artifact(
        self,
        request: main_models.CreateArtifactRequest,
    ) -> main_models.CreateArtifactResponse:
        runtime = RuntimeOptions()
        return self.create_artifact_with_options(request, runtime)

    async def create_artifact_async(
        self,
        request: main_models.CreateArtifactRequest,
    ) -> main_models.CreateArtifactResponse:
        runtime = RuntimeOptions()
        return await self.create_artifact_with_options_async(request, runtime)

    def create_ops_notice_with_options(
        self,
        tmp_req: main_models.CreateOpsNoticeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOpsNoticeResponse:
        tmp_req.validate()
        request = main_models.CreateOpsNoticeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['Attributes'] = request.attributes_shrink
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.solutions):
            query['Solutions'] = request.solutions
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOpsNotice',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOpsNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_ops_notice_with_options_async(
        self,
        tmp_req: main_models.CreateOpsNoticeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateOpsNoticeResponse:
        tmp_req.validate()
        request = main_models.CreateOpsNoticeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.attributes):
            request.attributes_shrink = Utils.array_to_string_with_specified_style(tmp_req.attributes, 'Attributes', 'json')
        query = {}
        if not DaraCore.is_null(request.attributes_shrink):
            query['Attributes'] = request.attributes_shrink
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.content):
            query['Content'] = request.content
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.severity):
            query['Severity'] = request.severity
        if not DaraCore.is_null(request.solutions):
            query['Solutions'] = request.solutions
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateOpsNotice',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateOpsNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_ops_notice(
        self,
        request: main_models.CreateOpsNoticeRequest,
    ) -> main_models.CreateOpsNoticeResponse:
        runtime = RuntimeOptions()
        return self.create_ops_notice_with_options(request, runtime)

    async def create_ops_notice_async(
        self,
        request: main_models.CreateOpsNoticeRequest,
    ) -> main_models.CreateOpsNoticeResponse:
        runtime = RuntimeOptions()
        return await self.create_ops_notice_with_options_async(request, runtime)

    def create_service_with_options(
        self,
        tmp_req: main_models.CreateServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        tmp_req.validate()
        request = main_models.CreateServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compliance_metadata):
            request.compliance_metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.compliance_metadata, 'ComplianceMetadata', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not DaraCore.is_null(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not DaraCore.is_null(request.build_parameters):
            query['BuildParameters'] = request.build_parameters
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_metadata_shrink):
            query['ComplianceMetadata'] = request.compliance_metadata_shrink
        if not DaraCore.is_null(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not DaraCore.is_null(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not DaraCore.is_null(request.log_metadata):
            query['LogMetadata'] = request.log_metadata
        if not DaraCore.is_null(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resellable):
            query['Resellable'] = request.resellable
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.source_service_id):
            query['SourceServiceId'] = request.source_service_id
        if not DaraCore.is_null(request.source_service_version):
            query['SourceServiceVersion'] = request.source_service_version
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not DaraCore.is_null(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not DaraCore.is_null(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        tmp_req: main_models.CreateServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceResponse:
        tmp_req.validate()
        request = main_models.CreateServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.compliance_metadata):
            request.compliance_metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.compliance_metadata, 'ComplianceMetadata', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not DaraCore.is_null(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not DaraCore.is_null(request.build_parameters):
            query['BuildParameters'] = request.build_parameters
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.compliance_metadata_shrink):
            query['ComplianceMetadata'] = request.compliance_metadata_shrink
        if not DaraCore.is_null(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not DaraCore.is_null(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not DaraCore.is_null(request.log_metadata):
            query['LogMetadata'] = request.log_metadata
        if not DaraCore.is_null(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resellable):
            query['Resellable'] = request.resellable
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.source_service_id):
            query['SourceServiceId'] = request.source_service_id
        if not DaraCore.is_null(request.source_service_version):
            query['SourceServiceVersion'] = request.source_service_version
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not DaraCore.is_null(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not DaraCore.is_null(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    async def create_service_async(
        self,
        request: main_models.CreateServiceRequest,
    ) -> main_models.CreateServiceResponse:
        runtime = RuntimeOptions()
        return await self.create_service_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceInstance',
            version = '2021-05-21',
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
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceInstance',
            version = '2021-05-21',
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

    def create_service_test_case_with_options(
        self,
        request: main_models.CreateServiceTestCaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceTestCaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.test_case_name):
            query['TestCaseName'] = request.test_case_name
        if not DaraCore.is_null(request.test_config):
            query['TestConfig'] = request.test_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceTestCase',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceTestCaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_test_case_with_options_async(
        self,
        request: main_models.CreateServiceTestCaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceTestCaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        if not DaraCore.is_null(request.test_case_name):
            query['TestCaseName'] = request.test_case_name
        if not DaraCore.is_null(request.test_config):
            query['TestConfig'] = request.test_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceTestCase',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceTestCaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_test_case(
        self,
        request: main_models.CreateServiceTestCaseRequest,
    ) -> main_models.CreateServiceTestCaseResponse:
        runtime = RuntimeOptions()
        return self.create_service_test_case_with_options(request, runtime)

    async def create_service_test_case_async(
        self,
        request: main_models.CreateServiceTestCaseRequest,
    ) -> main_models.CreateServiceTestCaseResponse:
        runtime = RuntimeOptions()
        return await self.create_service_test_case_with_options_async(request, runtime)

    def create_service_test_task_with_options(
        self,
        request: main_models.CreateServiceTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceTestTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_region_id):
            query['TaskRegionId'] = request.task_region_id
        if not DaraCore.is_null(request.test_case_ids):
            query['TestCaseIds'] = request.test_case_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceTestTask',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceTestTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_test_task_with_options_async(
        self,
        request: main_models.CreateServiceTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceTestTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_name):
            query['TaskName'] = request.task_name
        if not DaraCore.is_null(request.task_region_id):
            query['TaskRegionId'] = request.task_region_id
        if not DaraCore.is_null(request.test_case_ids):
            query['TestCaseIds'] = request.test_case_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceTestTask',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateServiceTestTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_test_task(
        self,
        request: main_models.CreateServiceTestTaskRequest,
    ) -> main_models.CreateServiceTestTaskResponse:
        runtime = RuntimeOptions()
        return self.create_service_test_task_with_options(request, runtime)

    async def create_service_test_task_async(
        self,
        request: main_models.CreateServiceTestTaskRequest,
    ) -> main_models.CreateServiceTestTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_service_test_task_with_options_async(request, runtime)

    def create_service_usage_with_options(
        self,
        request: main_models.CreateServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceUsage',
            version = '2021-05-21',
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
        request: main_models.CreateServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateServiceUsage',
            version = '2021-05-21',
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

    def create_supplier_registration_with_options(
        self,
        request: main_models.CreateSupplierRegistrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSupplierRegistrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not DaraCore.is_null(request.contact_person):
            query['ContactPerson'] = request.contact_person
        if not DaraCore.is_null(request.contact_person_title):
            query['ContactPersonTitle'] = request.contact_person_title
        if not DaraCore.is_null(request.enable_reseller_mode):
            query['EnableResellerMode'] = request.enable_reseller_mode
        if not DaraCore.is_null(request.product_annual_revenue):
            query['ProductAnnualRevenue'] = request.product_annual_revenue
        if not DaraCore.is_null(request.product_business):
            query['ProductBusiness'] = request.product_business
        if not DaraCore.is_null(request.product_delivery_types):
            query['ProductDeliveryTypes'] = request.product_delivery_types
        if not DaraCore.is_null(request.product_publish_time):
            query['ProductPublishTime'] = request.product_publish_time
        if not DaraCore.is_null(request.product_sell_types):
            query['ProductSellTypes'] = request.product_sell_types
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resell_business_desc):
            query['ResellBusinessDesc'] = request.resell_business_desc
        if not DaraCore.is_null(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not DaraCore.is_null(request.supplier_desc):
            query['SupplierDesc'] = request.supplier_desc
        if not DaraCore.is_null(request.supplier_logo):
            query['SupplierLogo'] = request.supplier_logo
        if not DaraCore.is_null(request.supplier_name):
            query['SupplierName'] = request.supplier_name
        if not DaraCore.is_null(request.supplier_name_en):
            query['SupplierNameEn'] = request.supplier_name_en
        if not DaraCore.is_null(request.supplier_url):
            query['SupplierUrl'] = request.supplier_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSupplierRegistration',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSupplierRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_supplier_registration_with_options_async(
        self,
        request: main_models.CreateSupplierRegistrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSupplierRegistrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not DaraCore.is_null(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not DaraCore.is_null(request.contact_person):
            query['ContactPerson'] = request.contact_person
        if not DaraCore.is_null(request.contact_person_title):
            query['ContactPersonTitle'] = request.contact_person_title
        if not DaraCore.is_null(request.enable_reseller_mode):
            query['EnableResellerMode'] = request.enable_reseller_mode
        if not DaraCore.is_null(request.product_annual_revenue):
            query['ProductAnnualRevenue'] = request.product_annual_revenue
        if not DaraCore.is_null(request.product_business):
            query['ProductBusiness'] = request.product_business
        if not DaraCore.is_null(request.product_delivery_types):
            query['ProductDeliveryTypes'] = request.product_delivery_types
        if not DaraCore.is_null(request.product_publish_time):
            query['ProductPublishTime'] = request.product_publish_time
        if not DaraCore.is_null(request.product_sell_types):
            query['ProductSellTypes'] = request.product_sell_types
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resell_business_desc):
            query['ResellBusinessDesc'] = request.resell_business_desc
        if not DaraCore.is_null(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not DaraCore.is_null(request.supplier_desc):
            query['SupplierDesc'] = request.supplier_desc
        if not DaraCore.is_null(request.supplier_logo):
            query['SupplierLogo'] = request.supplier_logo
        if not DaraCore.is_null(request.supplier_name):
            query['SupplierName'] = request.supplier_name
        if not DaraCore.is_null(request.supplier_name_en):
            query['SupplierNameEn'] = request.supplier_name_en
        if not DaraCore.is_null(request.supplier_url):
            query['SupplierUrl'] = request.supplier_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSupplierRegistration',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSupplierRegistrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_supplier_registration(
        self,
        request: main_models.CreateSupplierRegistrationRequest,
    ) -> main_models.CreateSupplierRegistrationResponse:
        runtime = RuntimeOptions()
        return self.create_supplier_registration_with_options(request, runtime)

    async def create_supplier_registration_async(
        self,
        request: main_models.CreateSupplierRegistrationRequest,
    ) -> main_models.CreateSupplierRegistrationResponse:
        runtime = RuntimeOptions()
        return await self.create_supplier_registration_with_options_async(request, runtime)

    def delete_acr_image_repositories_with_options(
        self,
        request: main_models.DeleteAcrImageRepositoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAcrImageRepositoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcrImageRepositories',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAcrImageRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acr_image_repositories_with_options_async(
        self,
        request: main_models.DeleteAcrImageRepositoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAcrImageRepositoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcrImageRepositories',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAcrImageRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acr_image_repositories(
        self,
        request: main_models.DeleteAcrImageRepositoriesRequest,
    ) -> main_models.DeleteAcrImageRepositoriesResponse:
        runtime = RuntimeOptions()
        return self.delete_acr_image_repositories_with_options(request, runtime)

    async def delete_acr_image_repositories_async(
        self,
        request: main_models.DeleteAcrImageRepositoriesRequest,
    ) -> main_models.DeleteAcrImageRepositoriesResponse:
        runtime = RuntimeOptions()
        return await self.delete_acr_image_repositories_with_options_async(request, runtime)

    def delete_acr_image_tags_with_options(
        self,
        request: main_models.DeleteAcrImageTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAcrImageTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcrImageTags',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAcrImageTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_acr_image_tags_with_options_async(
        self,
        request: main_models.DeleteAcrImageTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAcrImageTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAcrImageTags',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAcrImageTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_acr_image_tags(
        self,
        request: main_models.DeleteAcrImageTagsRequest,
    ) -> main_models.DeleteAcrImageTagsResponse:
        runtime = RuntimeOptions()
        return self.delete_acr_image_tags_with_options(request, runtime)

    async def delete_acr_image_tags_async(
        self,
        request: main_models.DeleteAcrImageTagsRequest,
    ) -> main_models.DeleteAcrImageTagsResponse:
        runtime = RuntimeOptions()
        return await self.delete_acr_image_tags_with_options_async(request, runtime)

    def delete_artifact_with_options(
        self,
        request: main_models.DeleteArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteArtifactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_artifact_with_options_async(
        self,
        request: main_models.DeleteArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteArtifactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_artifact(
        self,
        request: main_models.DeleteArtifactRequest,
    ) -> main_models.DeleteArtifactResponse:
        runtime = RuntimeOptions()
        return self.delete_artifact_with_options(request, runtime)

    async def delete_artifact_async(
        self,
        request: main_models.DeleteArtifactRequest,
    ) -> main_models.DeleteArtifactResponse:
        runtime = RuntimeOptions()
        return await self.delete_artifact_with_options_async(request, runtime)

    def delete_service_with_options(
        self,
        request: main_models.DeleteServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        request: main_models.DeleteServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        request: main_models.DeleteServiceRequest,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    async def delete_service_async(
        self,
        request: main_models.DeleteServiceRequest,
    ) -> main_models.DeleteServiceResponse:
        runtime = RuntimeOptions()
        return await self.delete_service_with_options_async(request, runtime)

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
            version = '2021-05-21',
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
            version = '2021-05-21',
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

    def delete_service_test_case_with_options(
        self,
        request: main_models.DeleteServiceTestCaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceTestCaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.test_case_id):
            query['TestCaseId'] = request.test_case_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceTestCase',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceTestCaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_test_case_with_options_async(
        self,
        request: main_models.DeleteServiceTestCaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteServiceTestCaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.test_case_id):
            query['TestCaseId'] = request.test_case_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteServiceTestCase',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteServiceTestCaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_test_case(
        self,
        request: main_models.DeleteServiceTestCaseRequest,
    ) -> main_models.DeleteServiceTestCaseResponse:
        runtime = RuntimeOptions()
        return self.delete_service_test_case_with_options(request, runtime)

    async def delete_service_test_case_async(
        self,
        request: main_models.DeleteServiceTestCaseRequest,
    ) -> main_models.DeleteServiceTestCaseResponse:
        runtime = RuntimeOptions()
        return await self.delete_service_test_case_with_options_async(request, runtime)

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
            version = '2021-05-21',
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
            version = '2021-05-21',
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

    def generate_default_service_test_config_with_options(
        self,
        request: main_models.GenerateDefaultServiceTestConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDefaultServiceTestConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDefaultServiceTestConfig',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDefaultServiceTestConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_default_service_test_config_with_options_async(
        self,
        request: main_models.GenerateDefaultServiceTestConfigRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateDefaultServiceTestConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateDefaultServiceTestConfig',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateDefaultServiceTestConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_default_service_test_config(
        self,
        request: main_models.GenerateDefaultServiceTestConfigRequest,
    ) -> main_models.GenerateDefaultServiceTestConfigResponse:
        runtime = RuntimeOptions()
        return self.generate_default_service_test_config_with_options(request, runtime)

    async def generate_default_service_test_config_async(
        self,
        request: main_models.GenerateDefaultServiceTestConfigRequest,
    ) -> main_models.GenerateDefaultServiceTestConfigResponse:
        runtime = RuntimeOptions()
        return await self.generate_default_service_test_config_with_options_async(request, runtime)

    def generate_service_policy_with_options(
        self,
        tmp_req: main_models.GenerateServicePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateServicePolicyResponse:
        tmp_req.validate()
        request = main_models.GenerateServicePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_types):
            query['OperationTypes'] = request.operation_types
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
            action = 'GenerateServicePolicy',
            version = '2021-05-21',
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
        tmp_req: main_models.GenerateServicePolicyRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateServicePolicyResponse:
        tmp_req.validate()
        request = main_models.GenerateServicePolicyShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.operation_types):
            query['OperationTypes'] = request.operation_types
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
            action = 'GenerateServicePolicy',
            version = '2021-05-21',
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

    def get_artifact_with_options(
        self,
        request: main_models.GetArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_name):
            query['ArtifactName'] = request.artifact_name
        if not DaraCore.is_null(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_with_options_async(
        self,
        request: main_models.GetArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_name):
            query['ArtifactName'] = request.artifact_name
        if not DaraCore.is_null(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact(
        self,
        request: main_models.GetArtifactRequest,
    ) -> main_models.GetArtifactResponse:
        runtime = RuntimeOptions()
        return self.get_artifact_with_options(request, runtime)

    async def get_artifact_async(
        self,
        request: main_models.GetArtifactRequest,
    ) -> main_models.GetArtifactResponse:
        runtime = RuntimeOptions()
        return await self.get_artifact_with_options_async(request, runtime)

    def get_artifact_repository_credentials_with_options(
        self,
        request: main_models.GetArtifactRepositoryCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactRepositoryCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactRepositoryCredentials',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactRepositoryCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_repository_credentials_with_options_async(
        self,
        request: main_models.GetArtifactRepositoryCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetArtifactRepositoryCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetArtifactRepositoryCredentials',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetArtifactRepositoryCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_repository_credentials(
        self,
        request: main_models.GetArtifactRepositoryCredentialsRequest,
    ) -> main_models.GetArtifactRepositoryCredentialsResponse:
        runtime = RuntimeOptions()
        return self.get_artifact_repository_credentials_with_options(request, runtime)

    async def get_artifact_repository_credentials_async(
        self,
        request: main_models.GetArtifactRepositoryCredentialsRequest,
    ) -> main_models.GetArtifactRepositoryCredentialsResponse:
        runtime = RuntimeOptions()
        return await self.get_artifact_repository_credentials_with_options_async(request, runtime)

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
            version = '2021-05-21',
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
            version = '2021-05-21',
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

    def get_ops_notice_with_options(
        self,
        request: main_models.GetOpsNoticeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOpsNoticeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.notice_id):
            query['NoticeId'] = request.notice_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOpsNotice',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOpsNoticeResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_ops_notice_with_options_async(
        self,
        request: main_models.GetOpsNoticeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetOpsNoticeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.notice_id):
            query['NoticeId'] = request.notice_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetOpsNotice',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetOpsNoticeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_ops_notice(
        self,
        request: main_models.GetOpsNoticeRequest,
    ) -> main_models.GetOpsNoticeResponse:
        runtime = RuntimeOptions()
        return self.get_ops_notice_with_options(request, runtime)

    async def get_ops_notice_async(
        self,
        request: main_models.GetOpsNoticeRequest,
    ) -> main_models.GetOpsNoticeResponse:
        runtime = RuntimeOptions()
        return await self.get_ops_notice_with_options_async(request, runtime)

    def get_service_with_options(
        self,
        request: main_models.GetServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_ali_uid):
            query['FilterAliUid'] = request.filter_ali_uid
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
        if not DaraCore.is_null(request.shared_account_type):
            query['SharedAccountType'] = request.shared_account_type
        if not DaraCore.is_null(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2021-05-21',
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
        if not DaraCore.is_null(request.filter_ali_uid):
            query['FilterAliUid'] = request.filter_ali_uid
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
        if not DaraCore.is_null(request.shared_account_type):
            query['SharedAccountType'] = request.shared_account_type
        if not DaraCore.is_null(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetService',
            version = '2021-05-21',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEstimateCost',
            version = '2021-05-21',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceEstimateCost',
            version = '2021-05-21',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceInstance',
            version = '2021-05-21',
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
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceInstance',
            version = '2021-05-21',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceProvisions',
            version = '2021-05-21',
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
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceProvisions',
            version = '2021-05-21',
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

    def get_service_registration_with_options(
        self,
        request: main_models.GetServiceRegistrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceRegistrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceRegistration',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceRegistrationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_registration_with_options_async(
        self,
        request: main_models.GetServiceRegistrationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceRegistrationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceRegistration',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceRegistrationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_registration(
        self,
        request: main_models.GetServiceRegistrationRequest,
    ) -> main_models.GetServiceRegistrationResponse:
        runtime = RuntimeOptions()
        return self.get_service_registration_with_options(request, runtime)

    async def get_service_registration_async(
        self,
        request: main_models.GetServiceRegistrationRequest,
    ) -> main_models.GetServiceRegistrationResponse:
        runtime = RuntimeOptions()
        return await self.get_service_registration_with_options_async(request, runtime)

    def get_service_template_criterion_issues_with_options(
        self,
        request: main_models.GetServiceTemplateCriterionIssuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceTemplateCriterionIssuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceTemplateCriterionIssues',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceTemplateCriterionIssuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_template_criterion_issues_with_options_async(
        self,
        request: main_models.GetServiceTemplateCriterionIssuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceTemplateCriterionIssuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceTemplateCriterionIssues',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceTemplateCriterionIssuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_template_criterion_issues(
        self,
        request: main_models.GetServiceTemplateCriterionIssuesRequest,
    ) -> main_models.GetServiceTemplateCriterionIssuesResponse:
        runtime = RuntimeOptions()
        return self.get_service_template_criterion_issues_with_options(request, runtime)

    async def get_service_template_criterion_issues_async(
        self,
        request: main_models.GetServiceTemplateCriterionIssuesRequest,
    ) -> main_models.GetServiceTemplateCriterionIssuesResponse:
        runtime = RuntimeOptions()
        return await self.get_service_template_criterion_issues_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceTemplateParameterConstraints',
            version = '2021-05-21',
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
        if not DaraCore.is_null(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceTemplateParameterConstraints',
            version = '2021-05-21',
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

    def get_service_test_task_with_options(
        self,
        request: main_models.GetServiceTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceTestTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceTestTask',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceTestTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_test_task_with_options_async(
        self,
        request: main_models.GetServiceTestTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetServiceTestTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetServiceTestTask',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetServiceTestTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_test_task(
        self,
        request: main_models.GetServiceTestTaskRequest,
    ) -> main_models.GetServiceTestTaskResponse:
        runtime = RuntimeOptions()
        return self.get_service_test_task_with_options(request, runtime)

    async def get_service_test_task_async(
        self,
        request: main_models.GetServiceTestTaskRequest,
    ) -> main_models.GetServiceTestTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_service_test_task_with_options_async(request, runtime)

    def get_supplier_information_with_options(
        self,
        request: main_models.GetSupplierInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupplierInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupplierInformation',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupplierInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_supplier_information_with_options_async(
        self,
        request: main_models.GetSupplierInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSupplierInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSupplierInformation',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSupplierInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_supplier_information(
        self,
        request: main_models.GetSupplierInformationRequest,
    ) -> main_models.GetSupplierInformationResponse:
        runtime = RuntimeOptions()
        return self.get_supplier_information_with_options(request, runtime)

    async def get_supplier_information_async(
        self,
        request: main_models.GetSupplierInformationRequest,
    ) -> main_models.GetSupplierInformationResponse:
        runtime = RuntimeOptions()
        return await self.get_supplier_information_with_options_async(request, runtime)

    def get_upload_credentials_with_options(
        self,
        request: main_models.GetUploadCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadCredentials',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_credentials_with_options_async(
        self,
        request: main_models.GetUploadCredentialsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUploadCredentialsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUploadCredentials',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUploadCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_credentials(
        self,
        request: main_models.GetUploadCredentialsRequest,
    ) -> main_models.GetUploadCredentialsResponse:
        runtime = RuntimeOptions()
        return self.get_upload_credentials_with_options(request, runtime)

    async def get_upload_credentials_async(
        self,
        request: main_models.GetUploadCredentialsRequest,
    ) -> main_models.GetUploadCredentialsResponse:
        runtime = RuntimeOptions()
        return await self.get_upload_credentials_with_options_async(request, runtime)

    def launch_service_with_options(
        self,
        request: main_models.LaunchServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.categories):
            query['Categories'] = request.categories
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.recommend):
            query['Recommend'] = request.recommend
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LaunchService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_service_with_options_async(
        self,
        request: main_models.LaunchServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.categories):
            query['Categories'] = request.categories
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.recommend):
            query['Recommend'] = request.recommend
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'LaunchService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_service(
        self,
        request: main_models.LaunchServiceRequest,
    ) -> main_models.LaunchServiceResponse:
        runtime = RuntimeOptions()
        return self.launch_service_with_options(request, runtime)

    async def launch_service_async(
        self,
        request: main_models.LaunchServiceRequest,
    ) -> main_models.LaunchServiceResponse:
        runtime = RuntimeOptions()
        return await self.launch_service_with_options_async(request, runtime)

    def list_acr_image_repositories_with_options(
        self,
        request: main_models.ListAcrImageRepositoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAcrImageRepositoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAcrImageRepositories',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAcrImageRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acr_image_repositories_with_options_async(
        self,
        request: main_models.ListAcrImageRepositoriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAcrImageRepositoriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.repo_name):
            query['RepoName'] = request.repo_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAcrImageRepositories',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAcrImageRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acr_image_repositories(
        self,
        request: main_models.ListAcrImageRepositoriesRequest,
    ) -> main_models.ListAcrImageRepositoriesResponse:
        runtime = RuntimeOptions()
        return self.list_acr_image_repositories_with_options(request, runtime)

    async def list_acr_image_repositories_async(
        self,
        request: main_models.ListAcrImageRepositoriesRequest,
    ) -> main_models.ListAcrImageRepositoriesResponse:
        runtime = RuntimeOptions()
        return await self.list_acr_image_repositories_with_options_async(request, runtime)

    def list_acr_image_tags_with_options(
        self,
        request: main_models.ListAcrImageTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAcrImageTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAcrImageTags',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAcrImageTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acr_image_tags_with_options_async(
        self,
        request: main_models.ListAcrImageTagsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAcrImageTagsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAcrImageTags',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAcrImageTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acr_image_tags(
        self,
        request: main_models.ListAcrImageTagsRequest,
    ) -> main_models.ListAcrImageTagsResponse:
        runtime = RuntimeOptions()
        return self.list_acr_image_tags_with_options(request, runtime)

    async def list_acr_image_tags_async(
        self,
        request: main_models.ListAcrImageTagsRequest,
    ) -> main_models.ListAcrImageTagsResponse:
        runtime = RuntimeOptions()
        return await self.list_acr_image_tags_with_options_async(request, runtime)

    def list_artifact_build_logs_with_options(
        self,
        request: main_models.ListArtifactBuildLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactBuildLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactBuildLogs',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactBuildLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifact_build_logs_with_options_async(
        self,
        request: main_models.ListArtifactBuildLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactBuildLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactBuildLogs',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactBuildLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifact_build_logs(
        self,
        request: main_models.ListArtifactBuildLogsRequest,
    ) -> main_models.ListArtifactBuildLogsResponse:
        runtime = RuntimeOptions()
        return self.list_artifact_build_logs_with_options(request, runtime)

    async def list_artifact_build_logs_async(
        self,
        request: main_models.ListArtifactBuildLogsRequest,
    ) -> main_models.ListArtifactBuildLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_artifact_build_logs_with_options_async(request, runtime)

    def list_artifact_risks_with_options(
        self,
        request: main_models.ListArtifactRisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactRisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactRisks',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactRisksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifact_risks_with_options_async(
        self,
        request: main_models.ListArtifactRisksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactRisksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactRisks',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactRisksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifact_risks(
        self,
        request: main_models.ListArtifactRisksRequest,
    ) -> main_models.ListArtifactRisksResponse:
        runtime = RuntimeOptions()
        return self.list_artifact_risks_with_options(request, runtime)

    async def list_artifact_risks_async(
        self,
        request: main_models.ListArtifactRisksRequest,
    ) -> main_models.ListArtifactRisksResponse:
        runtime = RuntimeOptions()
        return await self.list_artifact_risks_with_options_async(request, runtime)

    def list_artifact_versions_with_options(
        self,
        tmp_req: main_models.ListArtifactVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactVersionsResponse:
        tmp_req.validate()
        request = main_models.ListArtifactVersionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filters):
            request.filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.filters_shrink):
            query['Filters'] = request.filters_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactVersions',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifact_versions_with_options_async(
        self,
        tmp_req: main_models.ListArtifactVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactVersionsResponse:
        tmp_req.validate()
        request = main_models.ListArtifactVersionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filters):
            request.filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.filters_shrink):
            query['Filters'] = request.filters_shrink
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifactVersions',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifact_versions(
        self,
        request: main_models.ListArtifactVersionsRequest,
    ) -> main_models.ListArtifactVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_artifact_versions_with_options(request, runtime)

    async def list_artifact_versions_async(
        self,
        request: main_models.ListArtifactVersionsRequest,
    ) -> main_models.ListArtifactVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_artifact_versions_with_options_async(request, runtime)

    def list_artifacts_with_options(
        self,
        request: main_models.ListArtifactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifacts',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifacts_with_options_async(
        self,
        request: main_models.ListArtifactsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListArtifactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListArtifacts',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListArtifactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifacts(
        self,
        request: main_models.ListArtifactsRequest,
    ) -> main_models.ListArtifactsResponse:
        runtime = RuntimeOptions()
        return self.list_artifacts_with_options(request, runtime)

    async def list_artifacts_async(
        self,
        request: main_models.ListArtifactsRequest,
    ) -> main_models.ListArtifactsResponse:
        runtime = RuntimeOptions()
        return await self.list_artifacts_with_options_async(request, runtime)

    def list_ops_notices_with_options(
        self,
        request: main_models.ListOpsNoticesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOpsNoticesResponse:
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
            action = 'ListOpsNotices',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOpsNoticesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_ops_notices_with_options_async(
        self,
        request: main_models.ListOpsNoticesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListOpsNoticesResponse:
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
            action = 'ListOpsNotices',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListOpsNoticesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_ops_notices(
        self,
        request: main_models.ListOpsNoticesRequest,
    ) -> main_models.ListOpsNoticesResponse:
        runtime = RuntimeOptions()
        return self.list_ops_notices_with_options(request, runtime)

    async def list_ops_notices_async(
        self,
        request: main_models.ListOpsNoticesRequest,
    ) -> main_models.ListOpsNoticesResponse:
        runtime = RuntimeOptions()
        return await self.list_ops_notices_with_options_async(request, runtime)

    def list_resellers_with_options(
        self,
        request: main_models.ListResellersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResellersResponse:
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
            action = 'ListResellers',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResellersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resellers_with_options_async(
        self,
        request: main_models.ListResellersRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResellersResponse:
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
            action = 'ListResellers',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResellersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resellers(
        self,
        request: main_models.ListResellersRequest,
    ) -> main_models.ListResellersResponse:
        runtime = RuntimeOptions()
        return self.list_resellers_with_options(request, runtime)

    async def list_resellers_async(
        self,
        request: main_models.ListResellersRequest,
    ) -> main_models.ListResellersResponse:
        runtime = RuntimeOptions()
        return await self.list_resellers_with_options_async(request, runtime)

    def list_service_build_logs_with_options(
        self,
        request: main_models.ListServiceBuildLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceBuildLogsResponse:
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
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceBuildLogs',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceBuildLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_build_logs_with_options_async(
        self,
        request: main_models.ListServiceBuildLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceBuildLogsResponse:
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
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceBuildLogs',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceBuildLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_build_logs(
        self,
        request: main_models.ListServiceBuildLogsRequest,
    ) -> main_models.ListServiceBuildLogsResponse:
        runtime = RuntimeOptions()
        return self.list_service_build_logs_with_options(request, runtime)

    async def list_service_build_logs_async(
        self,
        request: main_models.ListServiceBuildLogsRequest,
    ) -> main_models.ListServiceBuildLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_service_build_logs_with_options_async(request, runtime)

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
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceBill',
            version = '2021-05-21',
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
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceBill',
            version = '2021-05-21',
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

    def list_service_instance_deploy_details_with_options(
        self,
        request: main_models.ListServiceInstanceDeployDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceDeployDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cycle_time_zone):
            query['CycleTimeZone'] = request.cycle_time_zone
        if not DaraCore.is_null(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceDeployDetails',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceDeployDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_deploy_details_with_options_async(
        self,
        request: main_models.ListServiceInstanceDeployDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceInstanceDeployDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.cycle_time_zone):
            query['CycleTimeZone'] = request.cycle_time_zone
        if not DaraCore.is_null(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not DaraCore.is_null(request.dimension):
            query['Dimension'] = request.dimension
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstanceDeployDetails',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceInstanceDeployDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_deploy_details(
        self,
        request: main_models.ListServiceInstanceDeployDetailsRequest,
    ) -> main_models.ListServiceInstanceDeployDetailsResponse:
        runtime = RuntimeOptions()
        return self.list_service_instance_deploy_details_with_options(request, runtime)

    async def list_service_instance_deploy_details_async(
        self,
        request: main_models.ListServiceInstanceDeployDetailsRequest,
    ) -> main_models.ListServiceInstanceDeployDetailsResponse:
        runtime = RuntimeOptions()
        return await self.list_service_instance_deploy_details_with_options_async(request, runtime)

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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
        if not DaraCore.is_null(request.show_deleted):
            query['ShowDeleted'] = request.show_deleted
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstances',
            version = '2021-05-21',
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
        if not DaraCore.is_null(request.show_deleted):
            query['ShowDeleted'] = request.show_deleted
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceInstances',
            version = '2021-05-21',
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

    def list_service_registrations_with_options(
        self,
        request: main_models.ListServiceRegistrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceRegistrationsResponse:
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
            action = 'ListServiceRegistrations',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceRegistrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_registrations_with_options_async(
        self,
        request: main_models.ListServiceRegistrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceRegistrationsResponse:
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
            action = 'ListServiceRegistrations',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceRegistrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_registrations(
        self,
        request: main_models.ListServiceRegistrationsRequest,
    ) -> main_models.ListServiceRegistrationsResponse:
        runtime = RuntimeOptions()
        return self.list_service_registrations_with_options(request, runtime)

    async def list_service_registrations_async(
        self,
        request: main_models.ListServiceRegistrationsRequest,
    ) -> main_models.ListServiceRegistrationsResponse:
        runtime = RuntimeOptions()
        return await self.list_service_registrations_with_options_async(request, runtime)

    def list_service_shared_accounts_with_options(
        self,
        request: main_models.ListServiceSharedAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceSharedAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.permission):
            query['Permission'] = request.permission
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceSharedAccounts',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_shared_accounts_with_options_async(
        self,
        request: main_models.ListServiceSharedAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceSharedAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.permission):
            query['Permission'] = request.permission
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceSharedAccounts',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_shared_accounts(
        self,
        request: main_models.ListServiceSharedAccountsRequest,
    ) -> main_models.ListServiceSharedAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_service_shared_accounts_with_options(request, runtime)

    async def list_service_shared_accounts_async(
        self,
        request: main_models.ListServiceSharedAccountsRequest,
    ) -> main_models.ListServiceSharedAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_service_shared_accounts_with_options_async(request, runtime)

    def list_service_test_cases_with_options(
        self,
        request: main_models.ListServiceTestCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceTestCasesResponse:
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
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceTestCases',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceTestCasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_test_cases_with_options_async(
        self,
        request: main_models.ListServiceTestCasesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceTestCasesResponse:
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
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceTestCases',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceTestCasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_test_cases(
        self,
        request: main_models.ListServiceTestCasesRequest,
    ) -> main_models.ListServiceTestCasesResponse:
        runtime = RuntimeOptions()
        return self.list_service_test_cases_with_options(request, runtime)

    async def list_service_test_cases_async(
        self,
        request: main_models.ListServiceTestCasesRequest,
    ) -> main_models.ListServiceTestCasesResponse:
        runtime = RuntimeOptions()
        return await self.list_service_test_cases_with_options_async(request, runtime)

    def list_service_test_task_logs_with_options(
        self,
        request: main_models.ListServiceTestTaskLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceTestTaskLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceTestTaskLogs',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceTestTaskLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_test_task_logs_with_options_async(
        self,
        request: main_models.ListServiceTestTaskLogsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceTestTaskLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceTestTaskLogs',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceTestTaskLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_test_task_logs(
        self,
        request: main_models.ListServiceTestTaskLogsRequest,
    ) -> main_models.ListServiceTestTaskLogsResponse:
        runtime = RuntimeOptions()
        return self.list_service_test_task_logs_with_options(request, runtime)

    async def list_service_test_task_logs_async(
        self,
        request: main_models.ListServiceTestTaskLogsRequest,
    ) -> main_models.ListServiceTestTaskLogsResponse:
        runtime = RuntimeOptions()
        return await self.list_service_test_task_logs_with_options_async(request, runtime)

    def list_service_test_tasks_with_options(
        self,
        request: main_models.ListServiceTestTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceTestTasksResponse:
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
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceTestTasks',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceTestTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_test_tasks_with_options_async(
        self,
        request: main_models.ListServiceTestTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceTestTasksResponse:
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
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceTestTasks',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceTestTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_test_tasks(
        self,
        request: main_models.ListServiceTestTasksRequest,
    ) -> main_models.ListServiceTestTasksResponse:
        runtime = RuntimeOptions()
        return self.list_service_test_tasks_with_options(request, runtime)

    async def list_service_test_tasks_async(
        self,
        request: main_models.ListServiceTestTasksRequest,
    ) -> main_models.ListServiceTestTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_service_test_tasks_with_options_async(request, runtime)

    def list_service_usages_with_options(
        self,
        request: main_models.ListServiceUsagesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceUsagesResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceUsages',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceUsages',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
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
        if not DaraCore.is_null(request.all_versions):
            query['AllVersions'] = request.all_versions
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
            action = 'ListServices',
            version = '2021-05-21',
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
        if not DaraCore.is_null(request.all_versions):
            query['AllVersions'] = request.all_versions
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
            action = 'ListServices',
            version = '2021-05-21',
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

    def list_supplier_registrations_with_options(
        self,
        request: main_models.ListSupplierRegistrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupplierRegistrationsResponse:
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
            action = 'ListSupplierRegistrations',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupplierRegistrationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_supplier_registrations_with_options_async(
        self,
        request: main_models.ListSupplierRegistrationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSupplierRegistrationsResponse:
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
            action = 'ListSupplierRegistrations',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSupplierRegistrationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_supplier_registrations(
        self,
        request: main_models.ListSupplierRegistrationsRequest,
    ) -> main_models.ListSupplierRegistrationsResponse:
        runtime = RuntimeOptions()
        return self.list_supplier_registrations_with_options(request, runtime)

    async def list_supplier_registrations_async(
        self,
        request: main_models.ListSupplierRegistrationsRequest,
    ) -> main_models.ListSupplierRegistrationsResponse:
        runtime = RuntimeOptions()
        return await self.list_supplier_registrations_with_options_async(request, runtime)

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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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

    def modify_service_instance_resources_with_options(
        self,
        request: main_models.ModifyServiceInstanceResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyServiceInstanceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_instance_resources_action):
            query['ServiceInstanceResourcesAction'] = request.service_instance_resources_action
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyServiceInstanceResources',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyServiceInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_service_instance_resources_with_options_async(
        self,
        request: main_models.ModifyServiceInstanceResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ModifyServiceInstanceResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not DaraCore.is_null(request.service_instance_resources_action):
            query['ServiceInstanceResourcesAction'] = request.service_instance_resources_action
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ModifyServiceInstanceResources',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ModifyServiceInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_service_instance_resources(
        self,
        request: main_models.ModifyServiceInstanceResourcesRequest,
    ) -> main_models.ModifyServiceInstanceResourcesResponse:
        runtime = RuntimeOptions()
        return self.modify_service_instance_resources_with_options(request, runtime)

    async def modify_service_instance_resources_async(
        self,
        request: main_models.ModifyServiceInstanceResourcesRequest,
    ) -> main_models.ModifyServiceInstanceResourcesResponse:
        runtime = RuntimeOptions()
        return await self.modify_service_instance_resources_with_options_async(request, runtime)

    def pre_launch_service_with_options(
        self,
        request: main_models.PreLaunchServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreLaunchServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreLaunchService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreLaunchServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def pre_launch_service_with_options_async(
        self,
        request: main_models.PreLaunchServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PreLaunchServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PreLaunchService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreLaunchServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def pre_launch_service(
        self,
        request: main_models.PreLaunchServiceRequest,
    ) -> main_models.PreLaunchServiceResponse:
        runtime = RuntimeOptions()
        return self.pre_launch_service_with_options(request, runtime)

    async def pre_launch_service_async(
        self,
        request: main_models.PreLaunchServiceRequest,
    ) -> main_models.PreLaunchServiceResponse:
        runtime = RuntimeOptions()
        return await self.pre_launch_service_with_options_async(request, runtime)

    def push_metering_data_with_options(
        self,
        request: main_models.PushMeteringDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMeteringDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metering):
            query['Metering'] = request.metering
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushMeteringData',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMeteringDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_metering_data_with_options_async(
        self,
        request: main_models.PushMeteringDataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.PushMeteringDataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.metering):
            query['Metering'] = request.metering
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'PushMeteringData',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PushMeteringDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_metering_data(
        self,
        request: main_models.PushMeteringDataRequest,
    ) -> main_models.PushMeteringDataResponse:
        runtime = RuntimeOptions()
        return self.push_metering_data_with_options(request, runtime)

    async def push_metering_data_async(
        self,
        request: main_models.PushMeteringDataRequest,
    ) -> main_models.PushMeteringDataResponse:
        runtime = RuntimeOptions()
        return await self.push_metering_data_with_options_async(request, runtime)

    def register_service_with_options(
        self,
        request: main_models.RegisterServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_service_with_options_async(
        self,
        request: main_models.RegisterServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RegisterServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RegisterService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_service(
        self,
        request: main_models.RegisterServiceRequest,
    ) -> main_models.RegisterServiceResponse:
        runtime = RuntimeOptions()
        return self.register_service_with_options(request, runtime)

    async def register_service_async(
        self,
        request: main_models.RegisterServiceRequest,
    ) -> main_models.RegisterServiceResponse:
        runtime = RuntimeOptions()
        return await self.register_service_with_options_async(request, runtime)

    def reject_service_usage_with_options(
        self,
        request: main_models.RejectServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectServiceUsage',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_service_usage_with_options_async(
        self,
        request: main_models.RejectServiceUsageRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RejectServiceUsageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.comments):
            query['Comments'] = request.comments
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RejectServiceUsage',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RejectServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_service_usage(
        self,
        request: main_models.RejectServiceUsageRequest,
    ) -> main_models.RejectServiceUsageResponse:
        runtime = RuntimeOptions()
        return self.reject_service_usage_with_options(request, runtime)

    async def reject_service_usage_async(
        self,
        request: main_models.RejectServiceUsageRequest,
    ) -> main_models.RejectServiceUsageResponse:
        runtime = RuntimeOptions()
        return await self.reject_service_usage_with_options_async(request, runtime)

    def release_artifact_with_options(
        self,
        request: main_models.ReleaseArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseArtifactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_artifact_with_options_async(
        self,
        request: main_models.ReleaseArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ReleaseArtifactResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ReleaseArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ReleaseArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_artifact(
        self,
        request: main_models.ReleaseArtifactRequest,
    ) -> main_models.ReleaseArtifactResponse:
        runtime = RuntimeOptions()
        return self.release_artifact_with_options(request, runtime)

    async def release_artifact_async(
        self,
        request: main_models.ReleaseArtifactRequest,
    ) -> main_models.ReleaseArtifactResponse:
        runtime = RuntimeOptions()
        return await self.release_artifact_with_options_async(request, runtime)

    def remove_service_shared_accounts_with_options(
        self,
        request: main_models.RemoveServiceSharedAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveServiceSharedAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_ali_uids):
            query['UserAliUids'] = request.user_ali_uids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveServiceSharedAccounts',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveServiceSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_service_shared_accounts_with_options_async(
        self,
        request: main_models.RemoveServiceSharedAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RemoveServiceSharedAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_ali_uids):
            query['UserAliUids'] = request.user_ali_uids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveServiceSharedAccounts',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveServiceSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_service_shared_accounts(
        self,
        request: main_models.RemoveServiceSharedAccountsRequest,
    ) -> main_models.RemoveServiceSharedAccountsResponse:
        runtime = RuntimeOptions()
        return self.remove_service_shared_accounts_with_options(request, runtime)

    async def remove_service_shared_accounts_async(
        self,
        request: main_models.RemoveServiceSharedAccountsRequest,
    ) -> main_models.RemoveServiceSharedAccountsResponse:
        runtime = RuntimeOptions()
        return await self.remove_service_shared_accounts_with_options_async(request, runtime)

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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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
            version = '2021-05-21',
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

    def update_artifact_with_options(
        self,
        tmp_req: main_models.UpdateArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateArtifactResponse:
        tmp_req.validate()
        request = main_models.UpdateArtifactShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.artifact_build_property):
            request.artifact_build_property_shrink = Utils.array_to_string_with_specified_style(tmp_req.artifact_build_property, 'ArtifactBuildProperty', 'json')
        if not DaraCore.is_null(tmp_req.artifact_property):
            request.artifact_property_shrink = Utils.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not DaraCore.is_null(request.artifact_build_property_shrink):
            query['ArtifactBuildProperty'] = request.artifact_build_property_shrink
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not DaraCore.is_null(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_artifact_with_options_async(
        self,
        tmp_req: main_models.UpdateArtifactRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateArtifactResponse:
        tmp_req.validate()
        request = main_models.UpdateArtifactShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.artifact_build_property):
            request.artifact_build_property_shrink = Utils.array_to_string_with_specified_style(tmp_req.artifact_build_property, 'ArtifactBuildProperty', 'json')
        if not DaraCore.is_null(tmp_req.artifact_property):
            request.artifact_property_shrink = Utils.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not DaraCore.is_null(request.artifact_build_property_shrink):
            query['ArtifactBuildProperty'] = request.artifact_build_property_shrink
        if not DaraCore.is_null(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not DaraCore.is_null(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.permission_type):
            query['PermissionType'] = request.permission_type
        if not DaraCore.is_null(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateArtifact',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_artifact(
        self,
        request: main_models.UpdateArtifactRequest,
    ) -> main_models.UpdateArtifactResponse:
        runtime = RuntimeOptions()
        return self.update_artifact_with_options(request, runtime)

    async def update_artifact_async(
        self,
        request: main_models.UpdateArtifactRequest,
    ) -> main_models.UpdateArtifactResponse:
        runtime = RuntimeOptions()
        return await self.update_artifact_with_options_async(request, runtime)

    def update_service_with_options(
        self,
        tmp_req: main_models.UpdateServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.commodity):
            request.commodity_shrink = Utils.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not DaraCore.is_null(tmp_req.compliance_metadata):
            request.compliance_metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.compliance_metadata, 'ComplianceMetadata', 'json')
        if not DaraCore.is_null(tmp_req.update_option):
            request.update_option_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_option, 'UpdateOption', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not DaraCore.is_null(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not DaraCore.is_null(request.build_parameters):
            query['BuildParameters'] = request.build_parameters
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity_shrink):
            query['Commodity'] = request.commodity_shrink
        if not DaraCore.is_null(request.compliance_metadata_shrink):
            query['ComplianceMetadata'] = request.compliance_metadata_shrink
        if not DaraCore.is_null(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not DaraCore.is_null(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not DaraCore.is_null(request.log_metadata):
            query['LogMetadata'] = request.log_metadata
        if not DaraCore.is_null(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resellable):
            query['Resellable'] = request.resellable
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not DaraCore.is_null(request.service_locale_configs):
            query['ServiceLocaleConfigs'] = request.service_locale_configs
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not DaraCore.is_null(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not DaraCore.is_null(request.update_option_shrink):
            query['UpdateOption'] = request.update_option_shrink
        if not DaraCore.is_null(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        tmp_req: main_models.UpdateServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.commodity):
            request.commodity_shrink = Utils.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not DaraCore.is_null(tmp_req.compliance_metadata):
            request.compliance_metadata_shrink = Utils.array_to_string_with_specified_style(tmp_req.compliance_metadata, 'ComplianceMetadata', 'json')
        if not DaraCore.is_null(tmp_req.update_option):
            request.update_option_shrink = Utils.array_to_string_with_specified_style(tmp_req.update_option, 'UpdateOption', 'json')
        query = {}
        if not DaraCore.is_null(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not DaraCore.is_null(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not DaraCore.is_null(request.build_parameters):
            query['BuildParameters'] = request.build_parameters
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.commodity_shrink):
            query['Commodity'] = request.commodity_shrink
        if not DaraCore.is_null(request.compliance_metadata_shrink):
            query['ComplianceMetadata'] = request.compliance_metadata_shrink
        if not DaraCore.is_null(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not DaraCore.is_null(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not DaraCore.is_null(request.dry_run):
            query['DryRun'] = request.dry_run
        if not DaraCore.is_null(request.duration):
            query['Duration'] = request.duration
        if not DaraCore.is_null(request.is_default):
            query['IsDefault'] = request.is_default
        if not DaraCore.is_null(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not DaraCore.is_null(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not DaraCore.is_null(request.log_metadata):
            query['LogMetadata'] = request.log_metadata
        if not DaraCore.is_null(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not DaraCore.is_null(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resellable):
            query['Resellable'] = request.resellable
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not DaraCore.is_null(request.service_locale_configs):
            query['ServiceLocaleConfigs'] = request.service_locale_configs
        if not DaraCore.is_null(request.service_type):
            query['ServiceType'] = request.service_type
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not DaraCore.is_null(request.share_type):
            query['ShareType'] = request.share_type
        if not DaraCore.is_null(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not DaraCore.is_null(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not DaraCore.is_null(request.update_option_shrink):
            query['UpdateOption'] = request.update_option_shrink
        if not DaraCore.is_null(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not DaraCore.is_null(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        return self.update_service_with_options(request, runtime)

    async def update_service_async(
        self,
        request: main_models.UpdateServiceRequest,
    ) -> main_models.UpdateServiceResponse:
        runtime = RuntimeOptions()
        return await self.update_service_with_options_async(request, runtime)

    def update_service_instance_attribute_with_options(
        self,
        tmp_req: main_models.UpdateServiceInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceInstanceAttributeResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceInstanceAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.license_data):
            request.license_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.license_data, 'LicenseData', 'json')
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.license_data_shrink):
            query['LicenseData'] = request.license_data_shrink
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceInstanceAttribute',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_instance_attribute_with_options_async(
        self,
        tmp_req: main_models.UpdateServiceInstanceAttributeRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceInstanceAttributeResponse:
        tmp_req.validate()
        request = main_models.UpdateServiceInstanceAttributeShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.license_data):
            request.license_data_shrink = Utils.array_to_string_with_specified_style(tmp_req.license_data, 'LicenseData', 'json')
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['EndTime'] = request.end_time
        if not DaraCore.is_null(request.license_data_shrink):
            query['LicenseData'] = request.license_data_shrink
        if not DaraCore.is_null(request.reason):
            query['Reason'] = request.reason
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceInstanceAttribute',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_instance_attribute(
        self,
        request: main_models.UpdateServiceInstanceAttributeRequest,
    ) -> main_models.UpdateServiceInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return self.update_service_instance_attribute_with_options(request, runtime)

    async def update_service_instance_attribute_async(
        self,
        request: main_models.UpdateServiceInstanceAttributeRequest,
    ) -> main_models.UpdateServiceInstanceAttributeResponse:
        runtime = RuntimeOptions()
        return await self.update_service_instance_attribute_with_options_async(request, runtime)

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
            version = '2021-05-21',
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
            version = '2021-05-21',
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

    def update_service_test_case_with_options(
        self,
        request: main_models.UpdateServiceTestCaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceTestCaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.test_case_id):
            query['TestCaseId'] = request.test_case_id
        if not DaraCore.is_null(request.test_case_name):
            query['TestCaseName'] = request.test_case_name
        if not DaraCore.is_null(request.test_config):
            query['TestConfig'] = request.test_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceTestCase',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceTestCaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_test_case_with_options_async(
        self,
        request: main_models.UpdateServiceTestCaseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateServiceTestCaseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.test_case_id):
            query['TestCaseId'] = request.test_case_id
        if not DaraCore.is_null(request.test_case_name):
            query['TestCaseName'] = request.test_case_name
        if not DaraCore.is_null(request.test_config):
            query['TestConfig'] = request.test_config
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateServiceTestCase',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateServiceTestCaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_test_case(
        self,
        request: main_models.UpdateServiceTestCaseRequest,
    ) -> main_models.UpdateServiceTestCaseResponse:
        runtime = RuntimeOptions()
        return self.update_service_test_case_with_options(request, runtime)

    async def update_service_test_case_async(
        self,
        request: main_models.UpdateServiceTestCaseRequest,
    ) -> main_models.UpdateServiceTestCaseResponse:
        runtime = RuntimeOptions()
        return await self.update_service_test_case_with_options_async(request, runtime)

    def update_shared_account_permission_with_options(
        self,
        request: main_models.UpdateSharedAccountPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSharedAccountPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.permission):
            query['Permission'] = request.permission
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSharedAccountPermission',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSharedAccountPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_shared_account_permission_with_options_async(
        self,
        request: main_models.UpdateSharedAccountPermissionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSharedAccountPermissionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.permission):
            query['Permission'] = request.permission
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSharedAccountPermission',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSharedAccountPermissionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_shared_account_permission(
        self,
        request: main_models.UpdateSharedAccountPermissionRequest,
    ) -> main_models.UpdateSharedAccountPermissionResponse:
        runtime = RuntimeOptions()
        return self.update_shared_account_permission_with_options(request, runtime)

    async def update_shared_account_permission_async(
        self,
        request: main_models.UpdateSharedAccountPermissionRequest,
    ) -> main_models.UpdateSharedAccountPermissionResponse:
        runtime = RuntimeOptions()
        return await self.update_shared_account_permission_with_options_async(request, runtime)

    def update_supplier_information_with_options(
        self,
        request: main_models.UpdateSupplierInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSupplierInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_settings):
            query['DeliverySettings'] = request.delivery_settings
        if not DaraCore.is_null(request.operation_ip):
            query['OperationIp'] = request.operation_ip
        if not DaraCore.is_null(request.operation_mfa_present):
            query['OperationMfaPresent'] = request.operation_mfa_present
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.supplier_desc):
            query['SupplierDesc'] = request.supplier_desc
        if not DaraCore.is_null(request.supplier_logo):
            query['SupplierLogo'] = request.supplier_logo
        if not DaraCore.is_null(request.supplier_url):
            query['SupplierUrl'] = request.supplier_url
        if not DaraCore.is_null(request.support_contacts):
            query['SupportContacts'] = request.support_contacts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSupplierInformation',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSupplierInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_supplier_information_with_options_async(
        self,
        request: main_models.UpdateSupplierInformationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSupplierInformationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_settings):
            query['DeliverySettings'] = request.delivery_settings
        if not DaraCore.is_null(request.operation_ip):
            query['OperationIp'] = request.operation_ip
        if not DaraCore.is_null(request.operation_mfa_present):
            query['OperationMfaPresent'] = request.operation_mfa_present
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.supplier_desc):
            query['SupplierDesc'] = request.supplier_desc
        if not DaraCore.is_null(request.supplier_logo):
            query['SupplierLogo'] = request.supplier_logo
        if not DaraCore.is_null(request.supplier_url):
            query['SupplierUrl'] = request.supplier_url
        if not DaraCore.is_null(request.support_contacts):
            query['SupportContacts'] = request.support_contacts
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSupplierInformation',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSupplierInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_supplier_information(
        self,
        request: main_models.UpdateSupplierInformationRequest,
    ) -> main_models.UpdateSupplierInformationResponse:
        runtime = RuntimeOptions()
        return self.update_supplier_information_with_options(request, runtime)

    async def update_supplier_information_async(
        self,
        request: main_models.UpdateSupplierInformationRequest,
    ) -> main_models.UpdateSupplierInformationResponse:
        runtime = RuntimeOptions()
        return await self.update_supplier_information_with_options_async(request, runtime)

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
            version = '2021-05-21',
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
            version = '2021-05-21',
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

    def withdraw_service_with_options(
        self,
        request: main_models.WithdrawServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def withdraw_service_with_options_async(
        self,
        request: main_models.WithdrawServiceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.WithdrawServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.service_id):
            query['ServiceId'] = request.service_id
        if not DaraCore.is_null(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'WithdrawService',
            version = '2021-05-21',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.WithdrawServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def withdraw_service(
        self,
        request: main_models.WithdrawServiceRequest,
    ) -> main_models.WithdrawServiceResponse:
        runtime = RuntimeOptions()
        return self.withdraw_service_with_options(request, runtime)

    async def withdraw_service_async(
        self,
        request: main_models.WithdrawServiceRequest,
    ) -> main_models.WithdrawServiceResponse:
        runtime = RuntimeOptions()
        return await self.withdraw_service_with_options_async(request, runtime)
