# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_computenestsupplier20210521 import models as compute_nest_supplier_20210521_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_service_shared_accounts_with_options(
        self,
        request: compute_nest_supplier_20210521_models.AddServiceSharedAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse:
        """
        @summary Adds a shared account of a service.
        
        @param request: AddServiceSharedAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddServiceSharedAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.shared_accounts):
            query['SharedAccounts'] = request.shared_accounts
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddServiceSharedAccounts',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_service_shared_accounts_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.AddServiceSharedAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse:
        """
        @summary Adds a shared account of a service.
        
        @param request: AddServiceSharedAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: AddServiceSharedAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.shared_accounts):
            query['SharedAccounts'] = request.shared_accounts
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddServiceSharedAccounts',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_service_shared_accounts(
        self,
        request: compute_nest_supplier_20210521_models.AddServiceSharedAccountsRequest,
    ) -> compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse:
        """
        @summary Adds a shared account of a service.
        
        @param request: AddServiceSharedAccountsRequest
        @return: AddServiceSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_service_shared_accounts_with_options(request, runtime)

    async def add_service_shared_accounts_async(
        self,
        request: compute_nest_supplier_20210521_models.AddServiceSharedAccountsRequest,
    ) -> compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse:
        """
        @summary Adds a shared account of a service.
        
        @param request: AddServiceSharedAccountsRequest
        @return: AddServiceSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.add_service_shared_accounts_with_options_async(request, runtime)

    def approve_service_usage_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ApproveServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ApproveServiceUsageResponse:
        """
        @summary 商家通过服务使用请求
        
        @param request: ApproveServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveServiceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveServiceUsage',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ApproveServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_service_usage_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ApproveServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ApproveServiceUsageResponse:
        """
        @summary 商家通过服务使用请求
        
        @param request: ApproveServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ApproveServiceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApproveServiceUsage',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ApproveServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_service_usage(
        self,
        request: compute_nest_supplier_20210521_models.ApproveServiceUsageRequest,
    ) -> compute_nest_supplier_20210521_models.ApproveServiceUsageResponse:
        """
        @summary 商家通过服务使用请求
        
        @param request: ApproveServiceUsageRequest
        @return: ApproveServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.approve_service_usage_with_options(request, runtime)

    async def approve_service_usage_async(
        self,
        request: compute_nest_supplier_20210521_models.ApproveServiceUsageRequest,
    ) -> compute_nest_supplier_20210521_models.ApproveServiceUsageResponse:
        """
        @summary 商家通过服务使用请求
        
        @param request: ApproveServiceUsageRequest
        @return: ApproveServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.approve_service_usage_with_options_async(request, runtime)

    def continue_deploy_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse:
        """
        @summary Redeploys a service instance after the service instance failed to be deployed.
        
        @param request: ContinueDeployServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinueDeployServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinueDeployServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_deploy_service_instance_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse:
        """
        @summary Redeploys a service instance after the service instance failed to be deployed.
        
        @param request: ContinueDeployServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ContinueDeployServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinueDeployServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_deploy_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse:
        """
        @summary Redeploys a service instance after the service instance failed to be deployed.
        
        @param request: ContinueDeployServiceInstanceRequest
        @return: ContinueDeployServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.continue_deploy_service_instance_with_options(request, runtime)

    async def continue_deploy_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse:
        """
        @summary Redeploys a service instance after the service instance failed to be deployed.
        
        @param request: ContinueDeployServiceInstanceRequest
        @return: ContinueDeployServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.continue_deploy_service_instance_with_options_async(request, runtime)

    def create_artifact_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.CreateArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateArtifactResponse:
        """
        @summary Creates a deployment package.
        
        @param tmp_req: CreateArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArtifactResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.CreateArtifactShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_artifact_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.CreateArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateArtifactResponse:
        """
        @summary Creates a deployment package.
        
        @param tmp_req: CreateArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateArtifactResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.CreateArtifactShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_artifact(
        self,
        request: compute_nest_supplier_20210521_models.CreateArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.CreateArtifactResponse:
        """
        @summary Creates a deployment package.
        
        @param request: CreateArtifactRequest
        @return: CreateArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_artifact_with_options(request, runtime)

    async def create_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.CreateArtifactResponse:
        """
        @summary Creates a deployment package.
        
        @param request: CreateArtifactRequest
        @return: CreateArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_artifact_with_options_async(request, runtime)

    def create_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @param request: CreateServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not UtilClient.is_unset(request.build_parameters):
            query['BuildParameters'] = request.build_parameters
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not UtilClient.is_unset(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not UtilClient.is_unset(request.log_metadata):
            query['LogMetadata'] = request.log_metadata
        if not UtilClient.is_unset(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resellable):
            query['Resellable'] = request.resellable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.source_service_id):
            query['SourceServiceId'] = request.source_service_id
        if not UtilClient.is_unset(request.source_service_version):
            query['SourceServiceVersion'] = request.source_service_version
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not UtilClient.is_unset(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not UtilClient.is_unset(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @param request: CreateServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not UtilClient.is_unset(request.build_parameters):
            query['BuildParameters'] = request.build_parameters
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not UtilClient.is_unset(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not UtilClient.is_unset(request.log_metadata):
            query['LogMetadata'] = request.log_metadata
        if not UtilClient.is_unset(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resellable):
            query['Resellable'] = request.resellable
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.source_service_id):
            query['SourceServiceId'] = request.source_service_id
        if not UtilClient.is_unset(request.source_service_version):
            query['SourceServiceVersion'] = request.source_service_version
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not UtilClient.is_unset(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not UtilClient.is_unset(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @param request: CreateServiceRequest
        @return: CreateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    async def create_service_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @param request: CreateServiceRequest
        @return: CreateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_with_options_async(request, runtime)

    def create_service_instance_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.CreateServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceInstanceResponse:
        """
        @summary Creates and deploys a service instance.
        
        @param tmp_req: CreateServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.CreateServiceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_instance_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.CreateServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceInstanceResponse:
        """
        @summary Creates and deploys a service instance.
        
        @param tmp_req: CreateServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.CreateServiceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceInstanceResponse:
        """
        @summary Creates and deploys a service instance.
        
        @param request: CreateServiceInstanceRequest
        @return: CreateServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_instance_with_options(request, runtime)

    async def create_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceInstanceResponse:
        """
        @summary Creates and deploys a service instance.
        
        @param request: CreateServiceInstanceRequest
        @return: CreateServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_instance_with_options_async(request, runtime)

    def create_service_usage_with_options(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceUsageResponse:
        """
        @summary Create  Service resell application.
        
        @param request: CreateServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceUsage',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_usage_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceUsageResponse:
        """
        @summary Create  Service resell application.
        
        @param request: CreateServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceUsage',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.CreateServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_usage(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceUsageRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceUsageResponse:
        """
        @summary Create  Service resell application.
        
        @param request: CreateServiceUsageRequest
        @return: CreateServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_usage_with_options(request, runtime)

    async def create_service_usage_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceUsageRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceUsageResponse:
        """
        @summary Create  Service resell application.
        
        @param request: CreateServiceUsageRequest
        @return: CreateServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_usage_with_options_async(request, runtime)

    def delete_artifact_with_options(
        self,
        request: compute_nest_supplier_20210521_models.DeleteArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteArtifactResponse:
        """
        @summary Deletes an artifact.
        
        @param request: DeleteArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteArtifactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_artifact_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteArtifactResponse:
        """
        @summary Deletes an artifact.
        
        @param request: DeleteArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteArtifactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_artifact(
        self,
        request: compute_nest_supplier_20210521_models.DeleteArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteArtifactResponse:
        """
        @summary Deletes an artifact.
        
        @param request: DeleteArtifactRequest
        @return: DeleteArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_artifact_with_options(request, runtime)

    async def delete_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteArtifactResponse:
        """
        @summary Deletes an artifact.
        
        @param request: DeleteArtifactRequest
        @return: DeleteArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_artifact_with_options_async(request, runtime)

    def delete_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
        """
        @summary Deletes a service.
        
        @param request: DeleteServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
        """
        @summary Deletes a service.
        
        @param request: DeleteServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
        """
        @summary Deletes a service.
        
        @param request: DeleteServiceRequest
        @return: DeleteServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    async def delete_service_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
        """
        @summary Deletes a service.
        
        @param request: DeleteServiceRequest
        @return: DeleteServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_with_options_async(request, runtime)

    def delete_service_instances_with_options(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse:
        """
        @summary Deletes a service instance.
        
        @param request: DeleteServiceInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceInstances',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_instances_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse:
        """
        @summary Deletes a service instance.
        
        @param request: DeleteServiceInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceInstances',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_instances(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceInstancesRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse:
        """
        @summary Deletes a service instance.
        
        @param request: DeleteServiceInstancesRequest
        @return: DeleteServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_service_instances_with_options(request, runtime)

    async def delete_service_instances_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceInstancesRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse:
        """
        @summary Deletes a service instance.
        
        @param request: DeleteServiceInstancesRequest
        @return: DeleteServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_instances_with_options_async(request, runtime)

    def deploy_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.DeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeployServiceInstanceResponse:
        """
        @summary Deploys a service instance.
        
        @param request: DeployServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeployServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_service_instance_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.DeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeployServiceInstanceResponse:
        """
        @summary Deploys a service instance.
        
        @param request: DeployServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeployServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.DeployServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.DeployServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.DeployServiceInstanceResponse:
        """
        @summary Deploys a service instance.
        
        @param request: DeployServiceInstanceRequest
        @return: DeployServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deploy_service_instance_with_options(request, runtime)

    async def deploy_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.DeployServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.DeployServiceInstanceResponse:
        """
        @summary Deploys a service instance.
        
        @param request: DeployServiceInstanceRequest
        @return: DeployServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deploy_service_instance_with_options_async(request, runtime)

    def get_artifact_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetArtifactResponse:
        """
        @summary Queries the information about a deployment package.
        
        @param request: GetArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetArtifactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_name):
            query['ArtifactName'] = request.artifact_name
        if not UtilClient.is_unset(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetArtifactResponse:
        """
        @summary Queries the information about a deployment package.
        
        @param request: GetArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetArtifactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_name):
            query['ArtifactName'] = request.artifact_name
        if not UtilClient.is_unset(request.artifact_version):
            query['ArtifactVersion'] = request.artifact_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.GetArtifactResponse:
        """
        @summary Queries the information about a deployment package.
        
        @param request: GetArtifactRequest
        @return: GetArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_with_options(request, runtime)

    async def get_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.GetArtifactResponse:
        """
        @summary Queries the information about a deployment package.
        
        @param request: GetArtifactRequest
        @return: GetArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_artifact_with_options_async(request, runtime)

    def get_artifact_repository_credentials_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse:
        """
        @summary Queries the credentials that are required to upload a deployment package.
        
        @param request: GetArtifactRepositoryCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetArtifactRepositoryCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifactRepositoryCredentials',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_artifact_repository_credentials_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse:
        """
        @summary Queries the credentials that are required to upload a deployment package.
        
        @param request: GetArtifactRepositoryCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetArtifactRepositoryCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetArtifactRepositoryCredentials',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_artifact_repository_credentials(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsRequest,
    ) -> compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse:
        """
        @summary Queries the credentials that are required to upload a deployment package.
        
        @param request: GetArtifactRepositoryCredentialsRequest
        @return: GetArtifactRepositoryCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_repository_credentials_with_options(request, runtime)

    async def get_artifact_repository_credentials_async(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsRequest,
    ) -> compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse:
        """
        @summary Queries the credentials that are required to upload a deployment package.
        
        @param request: GetArtifactRepositoryCredentialsRequest
        @return: GetArtifactRepositoryCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_artifact_repository_credentials_with_options_async(request, runtime)

    def get_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
        """
        @summary Queries the information about a service.
        
        @param request: GetServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_ali_uid):
            query['FilterAliUid'] = request.filter_ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.shared_account_type):
            query['SharedAccountType'] = request.shared_account_type
        if not UtilClient.is_unset(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
        """
        @summary Queries the information about a service.
        
        @param request: GetServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter_ali_uid):
            query['FilterAliUid'] = request.filter_ali_uid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.shared_account_type):
            query['SharedAccountType'] = request.shared_account_type
        if not UtilClient.is_unset(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
        """
        @summary Queries the information about a service.
        
        @param request: GetServiceRequest
        @return: GetServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_with_options(request, runtime)

    async def get_service_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
        """
        @summary Queries the information about a service.
        
        @param request: GetServiceRequest
        @return: GetServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_with_options_async(request, runtime)

    def get_service_estimate_cost_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.GetServiceEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse:
        """
        @summary Queries the estimated price for creating a service instance.
        
        @param tmp_req: GetServiceEstimateCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceEstimateCostResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.GetServiceEstimateCostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commodity):
            request.commodity_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_shrink):
            query['Commodity'] = request.commodity_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceEstimateCost',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_estimate_cost_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.GetServiceEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse:
        """
        @summary Queries the estimated price for creating a service instance.
        
        @param tmp_req: GetServiceEstimateCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceEstimateCostResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.GetServiceEstimateCostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commodity):
            request.commodity_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_shrink):
            query['Commodity'] = request.commodity_shrink
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceEstimateCost',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_estimate_cost(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceEstimateCostRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse:
        """
        @summary Queries the estimated price for creating a service instance.
        
        @param request: GetServiceEstimateCostRequest
        @return: GetServiceEstimateCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_estimate_cost_with_options(request, runtime)

    async def get_service_estimate_cost_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceEstimateCostRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse:
        """
        @summary Queries the estimated price for creating a service instance.
        
        @param request: GetServiceEstimateCostRequest
        @return: GetServiceEstimateCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_estimate_cost_with_options_async(request, runtime)

    def get_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
        """
        @summary Queries the information about a service instance.
        
        @param request: GetServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_instance_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
        """
        @summary Queries the information about a service instance.
        
        @param request: GetServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
        """
        @summary Queries the information about a service instance.
        
        @param request: GetServiceInstanceRequest
        @return: GetServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_instance_with_options(request, runtime)

    async def get_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
        """
        @summary Queries the information about a service instance.
        
        @param request: GetServiceInstanceRequest
        @return: GetServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_instance_with_options_async(request, runtime)

    def get_service_template_parameter_constraints_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse:
        """
        @summary Queries the valid values of parameters in a Resource Orchestration Service (ROS) template.
        
        @param request: GetServiceTemplateParameterConstraintsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceTemplateParameterConstraintsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not UtilClient.is_unset(request.enable_private_vpc_connection):
            query['EnablePrivateVpcConnection'] = request.enable_private_vpc_connection
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceTemplateParameterConstraints',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_template_parameter_constraints_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse:
        """
        @summary Queries the valid values of parameters in a Resource Orchestration Service (ROS) template.
        
        @param request: GetServiceTemplateParameterConstraintsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceTemplateParameterConstraintsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.deploy_region_id):
            query['DeployRegionId'] = request.deploy_region_id
        if not UtilClient.is_unset(request.enable_private_vpc_connection):
            query['EnablePrivateVpcConnection'] = request.enable_private_vpc_connection
        if not UtilClient.is_unset(request.parameters):
            query['Parameters'] = request.parameters
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceTemplateParameterConstraints',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_template_parameter_constraints(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse:
        """
        @summary Queries the valid values of parameters in a Resource Orchestration Service (ROS) template.
        
        @param request: GetServiceTemplateParameterConstraintsRequest
        @return: GetServiceTemplateParameterConstraintsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_template_parameter_constraints_with_options(request, runtime)

    async def get_service_template_parameter_constraints_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse:
        """
        @summary Queries the valid values of parameters in a Resource Orchestration Service (ROS) template.
        
        @param request: GetServiceTemplateParameterConstraintsRequest
        @return: GetServiceTemplateParameterConstraintsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_template_parameter_constraints_with_options_async(request, runtime)

    def get_upload_credentials_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetUploadCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetUploadCredentialsResponse:
        """
        @summary Obtain the AccessKey pair of uploaded files.
        
        @param request: GetUploadCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUploadCredentials',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetUploadCredentialsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_upload_credentials_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetUploadCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetUploadCredentialsResponse:
        """
        @summary Obtain the AccessKey pair of uploaded files.
        
        @param request: GetUploadCredentialsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUploadCredentialsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.visibility):
            query['Visibility'] = request.visibility
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUploadCredentials',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.GetUploadCredentialsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_upload_credentials(
        self,
        request: compute_nest_supplier_20210521_models.GetUploadCredentialsRequest,
    ) -> compute_nest_supplier_20210521_models.GetUploadCredentialsResponse:
        """
        @summary Obtain the AccessKey pair of uploaded files.
        
        @param request: GetUploadCredentialsRequest
        @return: GetUploadCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_upload_credentials_with_options(request, runtime)

    async def get_upload_credentials_async(
        self,
        request: compute_nest_supplier_20210521_models.GetUploadCredentialsRequest,
    ) -> compute_nest_supplier_20210521_models.GetUploadCredentialsResponse:
        """
        @summary Obtain the AccessKey pair of uploaded files.
        
        @param request: GetUploadCredentialsRequest
        @return: GetUploadCredentialsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_credentials_with_options_async(request, runtime)

    def list_acr_image_repositories_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListAcrImageRepositoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse:
        """
        @summary Queries a list of images uploaded to Container Registry.
        
        @param request: ListAcrImageRepositoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAcrImageRepositoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAcrImageRepositories',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acr_image_repositories_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListAcrImageRepositoriesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse:
        """
        @summary Queries a list of images uploaded to Container Registry.
        
        @param request: ListAcrImageRepositoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAcrImageRepositoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.repo_name):
            query['RepoName'] = request.repo_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAcrImageRepositories',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acr_image_repositories(
        self,
        request: compute_nest_supplier_20210521_models.ListAcrImageRepositoriesRequest,
    ) -> compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse:
        """
        @summary Queries a list of images uploaded to Container Registry.
        
        @param request: ListAcrImageRepositoriesRequest
        @return: ListAcrImageRepositoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_acr_image_repositories_with_options(request, runtime)

    async def list_acr_image_repositories_async(
        self,
        request: compute_nest_supplier_20210521_models.ListAcrImageRepositoriesRequest,
    ) -> compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse:
        """
        @summary Queries a list of images uploaded to Container Registry.
        
        @param request: ListAcrImageRepositoriesRequest
        @return: ListAcrImageRepositoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_acr_image_repositories_with_options_async(request, runtime)

    def list_acr_image_tags_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListAcrImageTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListAcrImageTagsResponse:
        """
        @summary Queries the versions of images that are uploaded to the image repository.
        
        @param request: ListAcrImageTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAcrImageTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAcrImageTags',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListAcrImageTagsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_acr_image_tags_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListAcrImageTagsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListAcrImageTagsResponse:
        """
        @summary Queries the versions of images that are uploaded to the image repository.
        
        @param request: ListAcrImageTagsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListAcrImageTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.repo_id):
            query['RepoId'] = request.repo_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAcrImageTags',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListAcrImageTagsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_acr_image_tags(
        self,
        request: compute_nest_supplier_20210521_models.ListAcrImageTagsRequest,
    ) -> compute_nest_supplier_20210521_models.ListAcrImageTagsResponse:
        """
        @summary Queries the versions of images that are uploaded to the image repository.
        
        @param request: ListAcrImageTagsRequest
        @return: ListAcrImageTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_acr_image_tags_with_options(request, runtime)

    async def list_acr_image_tags_async(
        self,
        request: compute_nest_supplier_20210521_models.ListAcrImageTagsRequest,
    ) -> compute_nest_supplier_20210521_models.ListAcrImageTagsResponse:
        """
        @summary Queries the versions of images that are uploaded to the image repository.
        
        @param request: ListAcrImageTagsRequest
        @return: ListAcrImageTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_acr_image_tags_with_options_async(request, runtime)

    def list_artifact_versions_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactVersionsResponse:
        """
        @summary Queries the version information about a deployment package.
        
        @param request: ListArtifactVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArtifactVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifactVersions',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListArtifactVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifact_versions_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactVersionsResponse:
        """
        @summary Queries the version information about a deployment package.
        
        @param request: ListArtifactVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArtifactVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifactVersions',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListArtifactVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifact_versions(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactVersionsRequest,
    ) -> compute_nest_supplier_20210521_models.ListArtifactVersionsResponse:
        """
        @summary Queries the version information about a deployment package.
        
        @param request: ListArtifactVersionsRequest
        @return: ListArtifactVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_artifact_versions_with_options(request, runtime)

    async def list_artifact_versions_async(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactVersionsRequest,
    ) -> compute_nest_supplier_20210521_models.ListArtifactVersionsResponse:
        """
        @summary Queries the version information about a deployment package.
        
        @param request: ListArtifactVersionsRequest
        @return: ListArtifactVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_artifact_versions_with_options_async(request, runtime)

    def list_artifacts_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactsResponse:
        """
        @summary Queries a list of deployment packages.
        
        @param request: ListArtifactsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArtifactsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifacts',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListArtifactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_artifacts_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactsResponse:
        """
        @summary Queries a list of deployment packages.
        
        @param request: ListArtifactsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArtifactsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListArtifacts',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListArtifactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_artifacts(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactsRequest,
    ) -> compute_nest_supplier_20210521_models.ListArtifactsResponse:
        """
        @summary Queries a list of deployment packages.
        
        @param request: ListArtifactsRequest
        @return: ListArtifactsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_artifacts_with_options(request, runtime)

    async def list_artifacts_async(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactsRequest,
    ) -> compute_nest_supplier_20210521_models.ListArtifactsResponse:
        """
        @summary Queries a list of deployment packages.
        
        @param request: ListArtifactsRequest
        @return: ListArtifactsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_artifacts_with_options_async(request, runtime)

    def list_service_categories_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceCategoriesResponse:
        """
        @summary 查询服务分类
        
        @param request: ListServiceCategoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceCategoriesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListServiceCategories',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_categories_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceCategoriesResponse:
        """
        @summary 查询服务分类
        
        @param request: ListServiceCategoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceCategoriesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListServiceCategories',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_categories(self) -> compute_nest_supplier_20210521_models.ListServiceCategoriesResponse:
        """
        @summary 查询服务分类
        
        @return: ListServiceCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_categories_with_options(runtime)

    async def list_service_categories_async(self) -> compute_nest_supplier_20210521_models.ListServiceCategoriesResponse:
        """
        @summary 查询服务分类
        
        @return: ListServiceCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_categories_with_options_async(runtime)

    def list_service_instances_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
        """
        @summary Queries a list of service instances.
        
        @param request: ListServiceInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.show_deleted):
            query['ShowDeleted'] = request.show_deleted
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instances_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
        """
        @summary Queries a list of service instances.
        
        @param request: ListServiceInstancesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstancesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.show_deleted):
            query['ShowDeleted'] = request.show_deleted
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instances(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
        """
        @summary Queries a list of service instances.
        
        @param request: ListServiceInstancesRequest
        @return: ListServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instances_with_options(request, runtime)

    async def list_service_instances_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
        """
        @summary Queries a list of service instances.
        
        @param request: ListServiceInstancesRequest
        @return: ListServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instances_with_options_async(request, runtime)

    def list_service_shared_accounts_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceSharedAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse:
        """
        @param request: ListServiceSharedAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceSharedAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceSharedAccounts',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_shared_accounts_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceSharedAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse:
        """
        @param request: ListServiceSharedAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceSharedAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceSharedAccounts',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_shared_accounts(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceSharedAccountsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse:
        """
        @param request: ListServiceSharedAccountsRequest
        @return: ListServiceSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_shared_accounts_with_options(request, runtime)

    async def list_service_shared_accounts_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceSharedAccountsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse:
        """
        @param request: ListServiceSharedAccountsRequest
        @return: ListServiceSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_shared_accounts_with_options_async(request, runtime)

    def list_service_usages_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceUsagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceUsagesResponse:
        """
        @summary Queries the applications for using a service.
        
        @param request: ListServiceUsagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceUsagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.supplier_role):
            query['SupplierRole'] = request.supplier_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceUsages',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceUsagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_usages_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceUsagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceUsagesResponse:
        """
        @summary Queries the applications for using a service.
        
        @param request: ListServiceUsagesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceUsagesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.supplier_role):
            query['SupplierRole'] = request.supplier_role
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceUsages',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServiceUsagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_usages(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceUsagesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceUsagesResponse:
        """
        @summary Queries the applications for using a service.
        
        @param request: ListServiceUsagesRequest
        @return: ListServiceUsagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_usages_with_options(request, runtime)

    async def list_service_usages_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceUsagesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceUsagesResponse:
        """
        @summary Queries the applications for using a service.
        
        @param request: ListServiceUsagesRequest
        @return: ListServiceUsagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_usages_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_versions):
            query['AllVersions'] = request.all_versions
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_versions):
            query['AllVersions'] = request.all_versions
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)

    def modify_service_instance_resources_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse:
        """
        @summary Modifies the resource information about a service instance.
        
        @param request: ModifyServiceInstanceResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyServiceInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_instance_resources_action):
            query['ServiceInstanceResourcesAction'] = request.service_instance_resources_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyServiceInstanceResources',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def modify_service_instance_resources_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse:
        """
        @summary Modifies the resource information about a service instance.
        
        @param request: ModifyServiceInstanceResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ModifyServiceInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_instance_resources_action):
            query['ServiceInstanceResourcesAction'] = request.service_instance_resources_action
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyServiceInstanceResources',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def modify_service_instance_resources(
        self,
        request: compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse:
        """
        @summary Modifies the resource information about a service instance.
        
        @param request: ModifyServiceInstanceResourcesRequest
        @return: ModifyServiceInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_service_instance_resources_with_options(request, runtime)

    async def modify_service_instance_resources_async(
        self,
        request: compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse:
        """
        @summary Modifies the resource information about a service instance.
        
        @param request: ModifyServiceInstanceResourcesRequest
        @return: ModifyServiceInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.modify_service_instance_resources_with_options_async(request, runtime)

    def push_metering_data_with_options(
        self,
        request: compute_nest_supplier_20210521_models.PushMeteringDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.PushMeteringDataResponse:
        """
        @summary Pushes metering data of an Alibaba Cloud Marketplace commodity.
        
        @param request: PushMeteringDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushMeteringDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metering):
            query['Metering'] = request.metering
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMeteringData',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.PushMeteringDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def push_metering_data_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.PushMeteringDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.PushMeteringDataResponse:
        """
        @summary Pushes metering data of an Alibaba Cloud Marketplace commodity.
        
        @param request: PushMeteringDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PushMeteringDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.metering):
            query['Metering'] = request.metering
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMeteringData',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.PushMeteringDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def push_metering_data(
        self,
        request: compute_nest_supplier_20210521_models.PushMeteringDataRequest,
    ) -> compute_nest_supplier_20210521_models.PushMeteringDataResponse:
        """
        @summary Pushes metering data of an Alibaba Cloud Marketplace commodity.
        
        @param request: PushMeteringDataRequest
        @return: PushMeteringDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.push_metering_data_with_options(request, runtime)

    async def push_metering_data_async(
        self,
        request: compute_nest_supplier_20210521_models.PushMeteringDataRequest,
    ) -> compute_nest_supplier_20210521_models.PushMeteringDataResponse:
        """
        @summary Pushes metering data of an Alibaba Cloud Marketplace commodity.
        
        @param request: PushMeteringDataRequest
        @return: PushMeteringDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.push_metering_data_with_options_async(request, runtime)

    def register_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.RegisterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RegisterServiceResponse:
        """
        @summary Registers an artifact.
        
        @param request: RegisterServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RegisterServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.RegisterServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RegisterServiceResponse:
        """
        @summary Registers an artifact.
        
        @param request: RegisterServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RegisterServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RegisterServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_service(
        self,
        request: compute_nest_supplier_20210521_models.RegisterServiceRequest,
    ) -> compute_nest_supplier_20210521_models.RegisterServiceResponse:
        """
        @summary Registers an artifact.
        
        @param request: RegisterServiceRequest
        @return: RegisterServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_service_with_options(request, runtime)

    async def register_service_async(
        self,
        request: compute_nest_supplier_20210521_models.RegisterServiceRequest,
    ) -> compute_nest_supplier_20210521_models.RegisterServiceResponse:
        """
        @summary Registers an artifact.
        
        @param request: RegisterServiceRequest
        @return: RegisterServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.register_service_with_options_async(request, runtime)

    def reject_service_usage_with_options(
        self,
        request: compute_nest_supplier_20210521_models.RejectServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RejectServiceUsageResponse:
        """
        @summary 商家拒绝服务使用请求
        
        @param request: RejectServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectServiceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectServiceUsage',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RejectServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def reject_service_usage_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.RejectServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RejectServiceUsageResponse:
        """
        @summary 商家拒绝服务使用请求
        
        @param request: RejectServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RejectServiceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.comments):
            query['Comments'] = request.comments
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_ali_uid):
            query['UserAliUid'] = request.user_ali_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectServiceUsage',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RejectServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def reject_service_usage(
        self,
        request: compute_nest_supplier_20210521_models.RejectServiceUsageRequest,
    ) -> compute_nest_supplier_20210521_models.RejectServiceUsageResponse:
        """
        @summary 商家拒绝服务使用请求
        
        @param request: RejectServiceUsageRequest
        @return: RejectServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reject_service_usage_with_options(request, runtime)

    async def reject_service_usage_async(
        self,
        request: compute_nest_supplier_20210521_models.RejectServiceUsageRequest,
    ) -> compute_nest_supplier_20210521_models.RejectServiceUsageResponse:
        """
        @summary 商家拒绝服务使用请求
        
        @param request: RejectServiceUsageRequest
        @return: RejectServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.reject_service_usage_with_options_async(request, runtime)

    def release_artifact_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ReleaseArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ReleaseArtifactResponse:
        """
        @summary Publishes an artifact.
        
        @param request: ReleaseArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseArtifactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ReleaseArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def release_artifact_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ReleaseArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ReleaseArtifactResponse:
        """
        @summary Publishes an artifact.
        
        @param request: ReleaseArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ReleaseArtifactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.ReleaseArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def release_artifact(
        self,
        request: compute_nest_supplier_20210521_models.ReleaseArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.ReleaseArtifactResponse:
        """
        @summary Publishes an artifact.
        
        @param request: ReleaseArtifactRequest
        @return: ReleaseArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.release_artifact_with_options(request, runtime)

    async def release_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.ReleaseArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.ReleaseArtifactResponse:
        """
        @summary Publishes an artifact.
        
        @param request: ReleaseArtifactRequest
        @return: ReleaseArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.release_artifact_with_options_async(request, runtime)

    def remove_service_shared_accounts_with_options(
        self,
        request: compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse:
        """
        @summary Remove  service shared account.
        
        @param request: RemoveServiceSharedAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveServiceSharedAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_ali_uids):
            query['UserAliUids'] = request.user_ali_uids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveServiceSharedAccounts',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_service_shared_accounts_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse:
        """
        @summary Remove  service shared account.
        
        @param request: RemoveServiceSharedAccountsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RemoveServiceSharedAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.user_ali_uids):
            query['UserAliUids'] = request.user_ali_uids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveServiceSharedAccounts',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_service_shared_accounts(
        self,
        request: compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsRequest,
    ) -> compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse:
        """
        @summary Remove  service shared account.
        
        @param request: RemoveServiceSharedAccountsRequest
        @return: RemoveServiceSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_service_shared_accounts_with_options(request, runtime)

    async def remove_service_shared_accounts_async(
        self,
        request: compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsRequest,
    ) -> compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse:
        """
        @summary Remove  service shared account.
        
        @param request: RemoveServiceSharedAccountsRequest
        @return: RemoveServiceSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.remove_service_shared_accounts_with_options_async(request, runtime)

    def restart_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.RestartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RestartServiceInstanceResponse:
        """
        @summary When the service instance is Deployed, call the RestartServiceInstance interface to restart the service instance.
        
        @param request: RestartServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RestartServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_service_instance_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.RestartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RestartServiceInstanceResponse:
        """
        @summary When the service instance is Deployed, call the RestartServiceInstance interface to restart the service instance.
        
        @param request: RestartServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RestartServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.RestartServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.RestartServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.RestartServiceInstanceResponse:
        """
        @summary When the service instance is Deployed, call the RestartServiceInstance interface to restart the service instance.
        
        @param request: RestartServiceInstanceRequest
        @return: RestartServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_service_instance_with_options(request, runtime)

    async def restart_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.RestartServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.RestartServiceInstanceResponse:
        """
        @summary When the service instance is Deployed, call the RestartServiceInstance interface to restart the service instance.
        
        @param request: RestartServiceInstanceRequest
        @return: RestartServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_service_instance_with_options_async(request, runtime)

    def start_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.StartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.StartServiceInstanceResponse:
        """
        @summary When the service instance status is Stopped (Stopped) or StartFailed (Startup failed), the StartServiceInstance interface is invoked to start the service instance.
        
        @param request: StartServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.StartServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_service_instance_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.StartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.StartServiceInstanceResponse:
        """
        @summary When the service instance status is Stopped (Stopped) or StartFailed (Startup failed), the StartServiceInstance interface is invoked to start the service instance.
        
        @param request: StartServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StartServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.StartServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.StartServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.StartServiceInstanceResponse:
        """
        @summary When the service instance status is Stopped (Stopped) or StartFailed (Startup failed), the StartServiceInstance interface is invoked to start the service instance.
        
        @param request: StartServiceInstanceRequest
        @return: StartServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_service_instance_with_options(request, runtime)

    async def start_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.StartServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.StartServiceInstanceResponse:
        """
        @summary When the service instance status is Stopped (Stopped) or StartFailed (Startup failed), the StartServiceInstance interface is invoked to start the service instance.
        
        @param request: StartServiceInstanceRequest
        @return: StartServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_service_instance_with_options_async(request, runtime)

    def stop_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.StopServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.StopServiceInstanceResponse:
        """
        @summary When the service instance is Deployed and StopFailed, call the StopServiceInstance interface to stop the service instance.
        
        @param request: StopServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.StopServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_service_instance_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.StopServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.StopServiceInstanceResponse:
        """
        @summary When the service instance is Deployed and StopFailed, call the StopServiceInstance interface to stop the service instance.
        
        @param request: StopServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.StopServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.StopServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.StopServiceInstanceResponse:
        """
        @summary When the service instance is Deployed and StopFailed, call the StopServiceInstance interface to stop the service instance.
        
        @param request: StopServiceInstanceRequest
        @return: StopServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_service_instance_with_options(request, runtime)

    async def stop_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.StopServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.StopServiceInstanceResponse:
        """
        @summary When the service instance is Deployed and StopFailed, call the StopServiceInstance interface to stop the service instance.
        
        @param request: StopServiceInstanceRequest
        @return: StopServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_service_instance_with_options_async(request, runtime)

    def update_artifact_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateArtifactResponse:
        """
        @summary Updates a deployment package.
        
        @param tmp_req: UpdateArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateArtifactResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateArtifactShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateArtifactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_artifact_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateArtifactResponse:
        """
        @summary Updates a deployment package.
        
        @param tmp_req: UpdateArtifactRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateArtifactResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateArtifactShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateArtifact',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateArtifactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_artifact(
        self,
        request: compute_nest_supplier_20210521_models.UpdateArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateArtifactResponse:
        """
        @summary Updates a deployment package.
        
        @param request: UpdateArtifactRequest
        @return: UpdateArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_artifact_with_options(request, runtime)

    async def update_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateArtifactResponse:
        """
        @summary Updates a deployment package.
        
        @param request: UpdateArtifactRequest
        @return: UpdateArtifactResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_artifact_with_options_async(request, runtime)

    def update_service_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        """
        @summary Upgrades a service.
        
        @param tmp_req: UpdateServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commodity):
            request.commodity_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not UtilClient.is_unset(tmp_req.update_option):
            request.update_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_option, 'UpdateOption', 'json')
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_shrink):
            query['Commodity'] = request.commodity_shrink
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not UtilClient.is_unset(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not UtilClient.is_unset(request.log_metadata):
            query['LogMetadata'] = request.log_metadata
        if not UtilClient.is_unset(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resellable):
            query['Resellable'] = request.resellable
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not UtilClient.is_unset(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not UtilClient.is_unset(request.update_option_shrink):
            query['UpdateOption'] = request.update_option_shrink
        if not UtilClient.is_unset(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        """
        @summary Upgrades a service.
        
        @param tmp_req: UpdateServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commodity):
            request.commodity_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not UtilClient.is_unset(tmp_req.update_option):
            request.update_option_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_option, 'UpdateOption', 'json')
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity_shrink):
            query['Commodity'] = request.commodity_shrink
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.is_support_operated):
            query['IsSupportOperated'] = request.is_support_operated
        if not UtilClient.is_unset(request.license_metadata):
            query['LicenseMetadata'] = request.license_metadata
        if not UtilClient.is_unset(request.log_metadata):
            query['LogMetadata'] = request.log_metadata
        if not UtilClient.is_unset(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not UtilClient.is_unset(request.policy_names):
            query['PolicyNames'] = request.policy_names
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resellable):
            query['Resellable'] = request.resellable
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.share_type):
            query['ShareType'] = request.share_type
        if not UtilClient.is_unset(request.tenant_type):
            query['TenantType'] = request.tenant_type
        if not UtilClient.is_unset(request.trial_duration):
            query['TrialDuration'] = request.trial_duration
        if not UtilClient.is_unset(request.update_option_shrink):
            query['UpdateOption'] = request.update_option_shrink
        if not UtilClient.is_unset(request.upgrade_metadata):
            query['UpgradeMetadata'] = request.upgrade_metadata
        if not UtilClient.is_unset(request.version_name):
            query['VersionName'] = request.version_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        """
        @summary Upgrades a service.
        
        @param request: UpdateServiceRequest
        @return: UpdateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_with_options(request, runtime)

    async def update_service_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        """
        @summary Upgrades a service.
        
        @param request: UpdateServiceRequest
        @return: UpdateServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_with_options_async(request, runtime)

    def update_service_instance_attribute_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse:
        """
        @summary Updates the properties of a service instance.
        
        @param tmp_req: UpdateServiceInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceAttributeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.license_data):
            request.license_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.license_data, 'LicenseData', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.license_data_shrink):
            query['LicenseData'] = request.license_data_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceInstanceAttribute',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_instance_attribute_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse:
        """
        @summary Updates the properties of a service instance.
        
        @param tmp_req: UpdateServiceInstanceAttributeRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceAttributeResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.license_data):
            request.license_data_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.license_data, 'LicenseData', 'json')
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.license_data_shrink):
            query['LicenseData'] = request.license_data_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceInstanceAttribute',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_instance_attribute(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse:
        """
        @summary Updates the properties of a service instance.
        
        @param request: UpdateServiceInstanceAttributeRequest
        @return: UpdateServiceInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_instance_attribute_with_options(request, runtime)

    async def update_service_instance_attribute_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse:
        """
        @summary Updates the properties of a service instance.
        
        @param request: UpdateServiceInstanceAttributeRequest
        @return: UpdateServiceInstanceAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_instance_attribute_with_options_async(request, runtime)

    def update_service_instance_spec_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse:
        """
        @summary Updates the configurations of a service instance.
        
        @param tmp_req: UpdateServiceInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceSpecResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_user_prometheus):
            query['EnableUserPrometheus'] = request.enable_user_prometheus
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.predefined_parameters_name):
            query['PredefinedParametersName'] = request.predefined_parameters_name
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceInstanceSpec',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_instance_spec_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse:
        """
        @summary Updates the configurations of a service instance.
        
        @param tmp_req: UpdateServiceInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceSpecResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.enable_user_prometheus):
            query['EnableUserPrometheus'] = request.enable_user_prometheus
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.predefined_parameters_name):
            query['PredefinedParametersName'] = request.predefined_parameters_name
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceInstanceSpec',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_instance_spec(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse:
        """
        @summary Updates the configurations of a service instance.
        
        @param request: UpdateServiceInstanceSpecRequest
        @return: UpdateServiceInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_instance_spec_with_options(request, runtime)

    async def update_service_instance_spec_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse:
        """
        @summary Updates the configurations of a service instance.
        
        @param request: UpdateServiceInstanceSpecRequest
        @return: UpdateServiceInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_instance_spec_with_options_async(request, runtime)

    def upgrade_service_instance_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpgradeServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse:
        """
        @summary Upgrades a service instance.
        
        @param tmp_req: UpgradeServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeServiceInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpgradeServiceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_service_instance_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpgradeServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse:
        """
        @summary Upgrades a service instance.
        
        @param tmp_req: UpgradeServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeServiceInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpgradeServiceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.UpgradeServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse:
        """
        @summary Upgrades a service instance.
        
        @param request: UpgradeServiceInstanceRequest
        @return: UpgradeServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_service_instance_with_options(request, runtime)

    async def upgrade_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.UpgradeServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse:
        """
        @summary Upgrades a service instance.
        
        @param request: UpgradeServiceInstanceRequest
        @return: UpgradeServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_service_instance_with_options_async(request, runtime)
