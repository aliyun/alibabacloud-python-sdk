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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.AddServiceSharedAccountsResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ApproveServiceUsageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ApproveServiceUsageResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ApproveServiceUsageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ApproveServiceUsageResponse(),
                await self.execute_async(params, req, runtime)
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

    def cancel_service_registration_with_options(
        self,
        request: compute_nest_supplier_20210521_models.CancelServiceRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse:
        """
        @summary Cancel service registration.
        
        @description Only service registration in the Submitted status can be canceled.
        
        @param request: CancelServiceRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelServiceRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelServiceRegistration',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse(),
                self.execute(params, req, runtime)
            )

    async def cancel_service_registration_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.CancelServiceRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse:
        """
        @summary Cancel service registration.
        
        @description Only service registration in the Submitted status can be canceled.
        
        @param request: CancelServiceRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelServiceRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelServiceRegistration',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def cancel_service_registration(
        self,
        request: compute_nest_supplier_20210521_models.CancelServiceRegistrationRequest,
    ) -> compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse:
        """
        @summary Cancel service registration.
        
        @description Only service registration in the Submitted status can be canceled.
        
        @param request: CancelServiceRegistrationRequest
        @return: CancelServiceRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_service_registration_with_options(request, runtime)

    async def cancel_service_registration_async(
        self,
        request: compute_nest_supplier_20210521_models.CancelServiceRegistrationRequest,
    ) -> compute_nest_supplier_20210521_models.CancelServiceRegistrationResponse:
        """
        @summary Cancel service registration.
        
        @description Only service registration in the Submitted status can be canceled.
        
        @param request: CancelServiceRegistrationRequest
        @return: CancelServiceRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_service_registration_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse(),
                await self.execute_async(params, req, runtime)
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
        if not UtilClient.is_unset(tmp_req.artifact_build_property):
            request.artifact_build_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_build_property, 'ArtifactBuildProperty', 'json')
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_build_property_shrink):
            query['ArtifactBuildProperty'] = request.artifact_build_property_shrink
        if not UtilClient.is_unset(request.artifact_build_type):
            query['ArtifactBuildType'] = request.artifact_build_type
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateArtifactResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateArtifactResponse(),
                self.execute(params, req, runtime)
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
        if not UtilClient.is_unset(tmp_req.artifact_build_property):
            request.artifact_build_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_build_property, 'ArtifactBuildProperty', 'json')
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_build_property_shrink):
            query['ArtifactBuildProperty'] = request.artifact_build_property_shrink
        if not UtilClient.is_unset(request.artifact_build_type):
            query['ArtifactBuildType'] = request.artifact_build_type
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.artifact_type):
            query['ArtifactType'] = request.artifact_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateArtifactResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateArtifactResponse(),
                await self.execute_async(params, req, runtime)
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
        tmp_req: compute_nest_supplier_20210521_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @param tmp_req: CreateServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.CreateServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.compliance_metadata):
            request.compliance_metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.compliance_metadata, 'ComplianceMetadata', 'json')
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not UtilClient.is_unset(request.build_parameters):
            query['BuildParameters'] = request.build_parameters
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_metadata_shrink):
            query['ComplianceMetadata'] = request.compliance_metadata_shrink
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def create_service_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        """
        @summary Creates a service.
        
        @param tmp_req: CreateServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.CreateServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.compliance_metadata):
            request.compliance_metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.compliance_metadata, 'ComplianceMetadata', 'json')
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
        if not UtilClient.is_unset(request.build_parameters):
            query['BuildParameters'] = request.build_parameters
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.compliance_metadata_shrink):
            query['ComplianceMetadata'] = request.compliance_metadata_shrink
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceInstanceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceInstanceResponse(),
                await self.execute_async(params, req, runtime)
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

    def create_service_test_case_with_options(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceTestCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceTestCaseResponse:
        """
        @summary Create service test case.
        
        @param request: CreateServiceTestCaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceTestCaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.test_case_name):
            query['TestCaseName'] = request.test_case_name
        if not UtilClient.is_unset(request.test_config):
            query['TestConfig'] = request.test_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceTestCase',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceTestCaseResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceTestCaseResponse(),
                self.execute(params, req, runtime)
            )

    async def create_service_test_case_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceTestCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceTestCaseResponse:
        """
        @summary Create service test case.
        
        @param request: CreateServiceTestCaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceTestCaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.test_case_name):
            query['TestCaseName'] = request.test_case_name
        if not UtilClient.is_unset(request.test_config):
            query['TestConfig'] = request.test_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceTestCase',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceTestCaseResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceTestCaseResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_service_test_case(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceTestCaseRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceTestCaseResponse:
        """
        @summary Create service test case.
        
        @param request: CreateServiceTestCaseRequest
        @return: CreateServiceTestCaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_test_case_with_options(request, runtime)

    async def create_service_test_case_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceTestCaseRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceTestCaseResponse:
        """
        @summary Create service test case.
        
        @param request: CreateServiceTestCaseRequest
        @return: CreateServiceTestCaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_test_case_with_options_async(request, runtime)

    def create_service_test_task_with_options(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceTestTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceTestTaskResponse:
        """
        @summary 创建服务测试任务
        
        @param request: CreateServiceTestTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceTestTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_region_id):
            query['TaskRegionId'] = request.task_region_id
        if not UtilClient.is_unset(request.test_case_ids):
            query['TestCaseIds'] = request.test_case_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceTestTask',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceTestTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceTestTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def create_service_test_task_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceTestTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceTestTaskResponse:
        """
        @summary 创建服务测试任务
        
        @param request: CreateServiceTestTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceTestTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_region_id):
            query['TaskRegionId'] = request.task_region_id
        if not UtilClient.is_unset(request.test_case_ids):
            query['TestCaseIds'] = request.test_case_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceTestTask',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceTestTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceTestTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_service_test_task(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceTestTaskRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceTestTaskResponse:
        """
        @summary 创建服务测试任务
        
        @param request: CreateServiceTestTaskRequest
        @return: CreateServiceTestTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_test_task_with_options(request, runtime)

    async def create_service_test_task_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceTestTaskRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceTestTaskResponse:
        """
        @summary 创建服务测试任务
        
        @param request: CreateServiceTestTaskRequest
        @return: CreateServiceTestTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_test_task_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceUsageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceUsageResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceUsageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateServiceUsageResponse(),
                await self.execute_async(params, req, runtime)
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

    def create_supplier_registration_with_options(
        self,
        request: compute_nest_supplier_20210521_models.CreateSupplierRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateSupplierRegistrationResponse:
        """
        @summary 注册成为服务商
        
        @param request: CreateSupplierRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSupplierRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.contact_person):
            query['ContactPerson'] = request.contact_person
        if not UtilClient.is_unset(request.contact_person_title):
            query['ContactPersonTitle'] = request.contact_person_title
        if not UtilClient.is_unset(request.enable_reseller_mode):
            query['EnableResellerMode'] = request.enable_reseller_mode
        if not UtilClient.is_unset(request.product_annual_revenue):
            query['ProductAnnualRevenue'] = request.product_annual_revenue
        if not UtilClient.is_unset(request.product_business):
            query['ProductBusiness'] = request.product_business
        if not UtilClient.is_unset(request.product_delivery_types):
            query['ProductDeliveryTypes'] = request.product_delivery_types
        if not UtilClient.is_unset(request.product_publish_time):
            query['ProductPublishTime'] = request.product_publish_time
        if not UtilClient.is_unset(request.product_sell_types):
            query['ProductSellTypes'] = request.product_sell_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resell_business_desc):
            query['ResellBusinessDesc'] = request.resell_business_desc
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.supplier_desc):
            query['SupplierDesc'] = request.supplier_desc
        if not UtilClient.is_unset(request.supplier_logo):
            query['SupplierLogo'] = request.supplier_logo
        if not UtilClient.is_unset(request.supplier_name):
            query['SupplierName'] = request.supplier_name
        if not UtilClient.is_unset(request.supplier_name_en):
            query['SupplierNameEn'] = request.supplier_name_en
        if not UtilClient.is_unset(request.supplier_url):
            query['SupplierUrl'] = request.supplier_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSupplierRegistration',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateSupplierRegistrationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateSupplierRegistrationResponse(),
                self.execute(params, req, runtime)
            )

    async def create_supplier_registration_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateSupplierRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateSupplierRegistrationResponse:
        """
        @summary 注册成为服务商
        
        @param request: CreateSupplierRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateSupplierRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_email):
            query['ContactEmail'] = request.contact_email
        if not UtilClient.is_unset(request.contact_number):
            query['ContactNumber'] = request.contact_number
        if not UtilClient.is_unset(request.contact_person):
            query['ContactPerson'] = request.contact_person
        if not UtilClient.is_unset(request.contact_person_title):
            query['ContactPersonTitle'] = request.contact_person_title
        if not UtilClient.is_unset(request.enable_reseller_mode):
            query['EnableResellerMode'] = request.enable_reseller_mode
        if not UtilClient.is_unset(request.product_annual_revenue):
            query['ProductAnnualRevenue'] = request.product_annual_revenue
        if not UtilClient.is_unset(request.product_business):
            query['ProductBusiness'] = request.product_business
        if not UtilClient.is_unset(request.product_delivery_types):
            query['ProductDeliveryTypes'] = request.product_delivery_types
        if not UtilClient.is_unset(request.product_publish_time):
            query['ProductPublishTime'] = request.product_publish_time
        if not UtilClient.is_unset(request.product_sell_types):
            query['ProductSellTypes'] = request.product_sell_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resell_business_desc):
            query['ResellBusinessDesc'] = request.resell_business_desc
        if not UtilClient.is_unset(request.suggestion):
            query['Suggestion'] = request.suggestion
        if not UtilClient.is_unset(request.supplier_desc):
            query['SupplierDesc'] = request.supplier_desc
        if not UtilClient.is_unset(request.supplier_logo):
            query['SupplierLogo'] = request.supplier_logo
        if not UtilClient.is_unset(request.supplier_name):
            query['SupplierName'] = request.supplier_name
        if not UtilClient.is_unset(request.supplier_name_en):
            query['SupplierNameEn'] = request.supplier_name_en
        if not UtilClient.is_unset(request.supplier_url):
            query['SupplierUrl'] = request.supplier_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSupplierRegistration',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateSupplierRegistrationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.CreateSupplierRegistrationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def create_supplier_registration(
        self,
        request: compute_nest_supplier_20210521_models.CreateSupplierRegistrationRequest,
    ) -> compute_nest_supplier_20210521_models.CreateSupplierRegistrationResponse:
        """
        @summary 注册成为服务商
        
        @param request: CreateSupplierRegistrationRequest
        @return: CreateSupplierRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_supplier_registration_with_options(request, runtime)

    async def create_supplier_registration_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateSupplierRegistrationRequest,
    ) -> compute_nest_supplier_20210521_models.CreateSupplierRegistrationResponse:
        """
        @summary 注册成为服务商
        
        @param request: CreateSupplierRegistrationRequest
        @return: CreateSupplierRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_supplier_registration_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteArtifactResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteArtifactResponse(),
                self.execute(params, req, runtime)
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteArtifactResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteArtifactResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse(),
                await self.execute_async(params, req, runtime)
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

    def delete_service_test_case_with_options(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceTestCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceTestCaseResponse:
        """
        @summary 删除服务测试配置
        
        @param request: DeleteServiceTestCaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceTestCaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.test_case_id):
            query['TestCaseId'] = request.test_case_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceTestCase',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceTestCaseResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceTestCaseResponse(),
                self.execute(params, req, runtime)
            )

    async def delete_service_test_case_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceTestCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceTestCaseResponse:
        """
        @summary 删除服务测试配置
        
        @param request: DeleteServiceTestCaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteServiceTestCaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.test_case_id):
            query['TestCaseId'] = request.test_case_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceTestCase',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceTestCaseResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeleteServiceTestCaseResponse(),
                await self.execute_async(params, req, runtime)
            )

    def delete_service_test_case(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceTestCaseRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceTestCaseResponse:
        """
        @summary 删除服务测试配置
        
        @param request: DeleteServiceTestCaseRequest
        @return: DeleteServiceTestCaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_service_test_case_with_options(request, runtime)

    async def delete_service_test_case_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceTestCaseRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceTestCaseResponse:
        """
        @summary 删除服务测试配置
        
        @param request: DeleteServiceTestCaseRequest
        @return: DeleteServiceTestCaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_test_case_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeployServiceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeployServiceInstanceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeployServiceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.DeployServiceInstanceResponse(),
                await self.execute_async(params, req, runtime)
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

    def generate_default_service_test_config_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigResponse:
        """
        @summary 生成默认服务测试配置
        
        @param request: GenerateDefaultServiceTestConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateDefaultServiceTestConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDefaultServiceTestConfig',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigResponse(),
                self.execute(params, req, runtime)
            )

    async def generate_default_service_test_config_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigResponse:
        """
        @summary 生成默认服务测试配置
        
        @param request: GenerateDefaultServiceTestConfigRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateDefaultServiceTestConfigResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDefaultServiceTestConfig',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigResponse(),
                await self.execute_async(params, req, runtime)
            )

    def generate_default_service_test_config(
        self,
        request: compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigRequest,
    ) -> compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigResponse:
        """
        @summary 生成默认服务测试配置
        
        @param request: GenerateDefaultServiceTestConfigRequest
        @return: GenerateDefaultServiceTestConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_default_service_test_config_with_options(request, runtime)

    async def generate_default_service_test_config_async(
        self,
        request: compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigRequest,
    ) -> compute_nest_supplier_20210521_models.GenerateDefaultServiceTestConfigResponse:
        """
        @summary 生成默认服务测试配置
        
        @param request: GenerateDefaultServiceTestConfigRequest
        @return: GenerateDefaultServiceTestConfigResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_default_service_test_config_with_options_async(request, runtime)

    def generate_service_policy_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GenerateServicePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GenerateServicePolicyResponse:
        """
        @summary 生成并校验服务创建stack所需要
        
        @param request: GenerateServicePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateServicePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_types):
            query['OperationTypes'] = request.operation_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateServicePolicy',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GenerateServicePolicyResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GenerateServicePolicyResponse(),
                self.execute(params, req, runtime)
            )

    async def generate_service_policy_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GenerateServicePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GenerateServicePolicyResponse:
        """
        @summary 生成并校验服务创建stack所需要
        
        @param request: GenerateServicePolicyRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GenerateServicePolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.operation_types):
            query['OperationTypes'] = request.operation_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateServicePolicy',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GenerateServicePolicyResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GenerateServicePolicyResponse(),
                await self.execute_async(params, req, runtime)
            )

    def generate_service_policy(
        self,
        request: compute_nest_supplier_20210521_models.GenerateServicePolicyRequest,
    ) -> compute_nest_supplier_20210521_models.GenerateServicePolicyResponse:
        """
        @summary 生成并校验服务创建stack所需要
        
        @param request: GenerateServicePolicyRequest
        @return: GenerateServicePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_service_policy_with_options(request, runtime)

    async def generate_service_policy_async(
        self,
        request: compute_nest_supplier_20210521_models.GenerateServicePolicyRequest,
    ) -> compute_nest_supplier_20210521_models.GenerateServicePolicyResponse:
        """
        @summary 生成并校验服务创建stack所需要
        
        @param request: GenerateServicePolicyRequest
        @return: GenerateServicePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_service_policy_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetArtifactResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetArtifactResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetArtifactResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetArtifactResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse(),
                await self.execute_async(params, req, runtime)
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
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceResponse(),
                self.execute(params, req, runtime)
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
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceInstanceResponse(),
                await self.execute_async(params, req, runtime)
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

    def get_service_provisions_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.GetServiceProvisionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceProvisionsResponse:
        """
        @summary 计算巢查询服务是否开通
        
        @param tmp_req: GetServiceProvisionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceProvisionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.GetServiceProvisionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceProvisions',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceProvisionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceProvisionsResponse(),
                self.execute(params, req, runtime)
            )

    async def get_service_provisions_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.GetServiceProvisionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceProvisionsResponse:
        """
        @summary 计算巢查询服务是否开通
        
        @param tmp_req: GetServiceProvisionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceProvisionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.GetServiceProvisionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceProvisions',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceProvisionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceProvisionsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_service_provisions(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceProvisionsRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceProvisionsResponse:
        """
        @summary 计算巢查询服务是否开通
        
        @param request: GetServiceProvisionsRequest
        @return: GetServiceProvisionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_provisions_with_options(request, runtime)

    async def get_service_provisions_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceProvisionsRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceProvisionsResponse:
        """
        @summary 计算巢查询服务是否开通
        
        @param request: GetServiceProvisionsRequest
        @return: GetServiceProvisionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_provisions_with_options_async(request, runtime)

    def get_service_registration_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceRegistrationResponse:
        """
        @summary Get service registration detail.
        
        @param request: GetServiceRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceRegistration',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceRegistrationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceRegistrationResponse(),
                self.execute(params, req, runtime)
            )

    async def get_service_registration_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRegistrationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceRegistrationResponse:
        """
        @summary Get service registration detail.
        
        @param request: GetServiceRegistrationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceRegistrationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.registration_id):
            query['RegistrationId'] = request.registration_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceRegistration',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceRegistrationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceRegistrationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_service_registration(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRegistrationRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceRegistrationResponse:
        """
        @summary Get service registration detail.
        
        @param request: GetServiceRegistrationRequest
        @return: GetServiceRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_registration_with_options(request, runtime)

    async def get_service_registration_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRegistrationRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceRegistrationResponse:
        """
        @summary Get service registration detail.
        
        @param request: GetServiceRegistrationRequest
        @return: GetServiceRegistrationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_registration_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceTemplateParameterConstraintsResponse(),
                await self.execute_async(params, req, runtime)
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

    def get_service_test_task_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceTestTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceTestTaskResponse:
        """
        @summary 获取服务测试任务中Cases执行情况
        
        @param request: GetServiceTestTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceTestTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceTestTask',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceTestTaskResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceTestTaskResponse(),
                self.execute(params, req, runtime)
            )

    async def get_service_test_task_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceTestTaskRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceTestTaskResponse:
        """
        @summary 获取服务测试任务中Cases执行情况
        
        @param request: GetServiceTestTaskRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceTestTaskResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceTestTask',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceTestTaskResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetServiceTestTaskResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_service_test_task(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceTestTaskRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceTestTaskResponse:
        """
        @summary 获取服务测试任务中Cases执行情况
        
        @param request: GetServiceTestTaskRequest
        @return: GetServiceTestTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_test_task_with_options(request, runtime)

    async def get_service_test_task_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceTestTaskRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceTestTaskResponse:
        """
        @summary 获取服务测试任务中Cases执行情况
        
        @param request: GetServiceTestTaskRequest
        @return: GetServiceTestTaskResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_test_task_with_options_async(request, runtime)

    def get_supplier_information_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetSupplierInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetSupplierInformationResponse:
        """
        @summary 获取服务商信息
        
        @param request: GetSupplierInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSupplierInformationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSupplierInformation',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetSupplierInformationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetSupplierInformationResponse(),
                self.execute(params, req, runtime)
            )

    async def get_supplier_information_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.GetSupplierInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetSupplierInformationResponse:
        """
        @summary 获取服务商信息
        
        @param request: GetSupplierInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetSupplierInformationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSupplierInformation',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetSupplierInformationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetSupplierInformationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def get_supplier_information(
        self,
        request: compute_nest_supplier_20210521_models.GetSupplierInformationRequest,
    ) -> compute_nest_supplier_20210521_models.GetSupplierInformationResponse:
        """
        @summary 获取服务商信息
        
        @param request: GetSupplierInformationRequest
        @return: GetSupplierInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_supplier_information_with_options(request, runtime)

    async def get_supplier_information_async(
        self,
        request: compute_nest_supplier_20210521_models.GetSupplierInformationRequest,
    ) -> compute_nest_supplier_20210521_models.GetSupplierInformationResponse:
        """
        @summary 获取服务商信息
        
        @param request: GetSupplierInformationRequest
        @return: GetSupplierInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_supplier_information_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetUploadCredentialsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetUploadCredentialsResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetUploadCredentialsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.GetUploadCredentialsResponse(),
                await self.execute_async(params, req, runtime)
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

    def launch_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.LaunchServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.LaunchServiceResponse:
        """
        @summary 上线服务
        
        @param request: LaunchServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LaunchServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.categories):
            query['Categories'] = request.categories
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.recommend):
            query['Recommend'] = request.recommend
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
            action='LaunchService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.LaunchServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.LaunchServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def launch_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.LaunchServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.LaunchServiceResponse:
        """
        @summary 上线服务
        
        @param request: LaunchServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: LaunchServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.categories):
            query['Categories'] = request.categories
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.recommend):
            query['Recommend'] = request.recommend
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
            action='LaunchService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.LaunchServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.LaunchServiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def launch_service(
        self,
        request: compute_nest_supplier_20210521_models.LaunchServiceRequest,
    ) -> compute_nest_supplier_20210521_models.LaunchServiceResponse:
        """
        @summary 上线服务
        
        @param request: LaunchServiceRequest
        @return: LaunchServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.launch_service_with_options(request, runtime)

    async def launch_service_async(
        self,
        request: compute_nest_supplier_20210521_models.LaunchServiceRequest,
    ) -> compute_nest_supplier_20210521_models.LaunchServiceResponse:
        """
        @summary 上线服务
        
        @param request: LaunchServiceRequest
        @return: LaunchServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.launch_service_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListAcrImageRepositoriesResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListAcrImageTagsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListAcrImageTagsResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListAcrImageTagsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListAcrImageTagsResponse(),
                await self.execute_async(params, req, runtime)
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

    def list_artifact_risks_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactRisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactRisksResponse:
        """
        @summary Get the list of artifact security risks
        
        @param request: ListArtifactRisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArtifactRisksResponse
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
            action='ListArtifactRisks',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactRisksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactRisksResponse(),
                self.execute(params, req, runtime)
            )

    async def list_artifact_risks_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactRisksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactRisksResponse:
        """
        @summary Get the list of artifact security risks
        
        @param request: ListArtifactRisksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArtifactRisksResponse
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
            action='ListArtifactRisks',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactRisksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactRisksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_artifact_risks(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactRisksRequest,
    ) -> compute_nest_supplier_20210521_models.ListArtifactRisksResponse:
        """
        @summary Get the list of artifact security risks
        
        @param request: ListArtifactRisksRequest
        @return: ListArtifactRisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_artifact_risks_with_options(request, runtime)

    async def list_artifact_risks_async(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactRisksRequest,
    ) -> compute_nest_supplier_20210521_models.ListArtifactRisksResponse:
        """
        @summary Get the list of artifact security risks
        
        @param request: ListArtifactRisksRequest
        @return: ListArtifactRisksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_artifact_risks_with_options_async(request, runtime)

    def list_artifact_versions_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.ListArtifactVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactVersionsResponse:
        """
        @summary Queries the version information about a deployment package.
        
        @param tmp_req: ListArtifactVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArtifactVersionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.ListArtifactVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.filters_shrink):
            query['Filters'] = request.filters_shrink
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactVersionsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactVersionsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_artifact_versions_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.ListArtifactVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactVersionsResponse:
        """
        @summary Queries the version information about a deployment package.
        
        @param tmp_req: ListArtifactVersionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListArtifactVersionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.ListArtifactVersionsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.filters):
            request.filters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.filters_shrink):
            query['Filters'] = request.filters_shrink
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactVersionsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactVersionsResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactsResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListArtifactsResponse(),
                await self.execute_async(params, req, runtime)
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

    def list_resellers_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListResellersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListResellersResponse:
        """
        @summary Paginated query of distributor information list
        
        @param request: ListResellersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResellersResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResellers',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListResellersResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListResellersResponse(),
                self.execute(params, req, runtime)
            )

    async def list_resellers_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListResellersRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListResellersResponse:
        """
        @summary Paginated query of distributor information list
        
        @param request: ListResellersRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListResellersResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResellers',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListResellersResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListResellersResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_resellers(
        self,
        request: compute_nest_supplier_20210521_models.ListResellersRequest,
    ) -> compute_nest_supplier_20210521_models.ListResellersResponse:
        """
        @summary Paginated query of distributor information list
        
        @param request: ListResellersRequest
        @return: ListResellersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resellers_with_options(request, runtime)

    async def list_resellers_async(
        self,
        request: compute_nest_supplier_20210521_models.ListResellersRequest,
    ) -> compute_nest_supplier_20210521_models.ListResellersResponse:
        """
        @summary Paginated query of distributor information list
        
        @param request: ListResellersRequest
        @return: ListResellersResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_resellers_with_options_async(request, runtime)

    def list_service_instance_deploy_details_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsResponse:
        """
        @summary 查询服务实例部署详情
        
        @param request: ListServiceInstanceDeployDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceDeployDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle_time_zone):
            query['CycleTimeZone'] = request.cycle_time_zone
        if not UtilClient.is_unset(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceDeployDetails',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_instance_deploy_details_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsResponse:
        """
        @summary 查询服务实例部署详情
        
        @param request: ListServiceInstanceDeployDetailsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceDeployDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cycle_time_zone):
            query['CycleTimeZone'] = request.cycle_time_zone
        if not UtilClient.is_unset(request.cycle_type):
            query['CycleType'] = request.cycle_type
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceDeployDetails',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_instance_deploy_details(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsResponse:
        """
        @summary 查询服务实例部署详情
        
        @param request: ListServiceInstanceDeployDetailsRequest
        @return: ListServiceInstanceDeployDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instance_deploy_details_with_options(request, runtime)

    async def list_service_instance_deploy_details_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceDeployDetailsResponse:
        """
        @summary 查询服务实例部署详情
        
        @param request: ListServiceInstanceDeployDetailsRequest
        @return: ListServiceInstanceDeployDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_deploy_details_with_options_async(request, runtime)

    def list_service_instance_logs_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceLogsResponse:
        """
        @summary “Query logs at various levels, including service instance application, instance, and resource.”
        
        @param request: ListServiceInstanceLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.log_source):
            query['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.logstore):
            query['Logstore'] = request.logstore
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceLogs',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceLogsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceLogsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_instance_logs_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceLogsResponse:
        """
        @summary “Query logs at various levels, including service instance application, instance, and resource.”
        
        @param request: ListServiceInstanceLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.log_source):
            query['LogSource'] = request.log_source
        if not UtilClient.is_unset(request.logstore):
            query['Logstore'] = request.logstore
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceLogs',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceLogsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceLogsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_instance_logs(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceLogsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceLogsResponse:
        """
        @summary “Query logs at various levels, including service instance application, instance, and resource.”
        
        @param request: ListServiceInstanceLogsRequest
        @return: ListServiceInstanceLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instance_logs_with_options(request, runtime)

    async def list_service_instance_logs_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceLogsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceLogsResponse:
        """
        @summary “Query logs at various levels, including service instance application, instance, and resource.”
        
        @param request: ListServiceInstanceLogsRequest
        @return: ListServiceInstanceLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_logs_with_options_async(request, runtime)

    def list_service_instance_resources_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceResourcesResponse:
        """
        @summary 查询服务实例资源
        
        @param request: ListServiceInstanceResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_instance_resource_type):
            query['ServiceInstanceResourceType'] = request.service_instance_resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceResources',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_instance_resources_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceResourcesResponse:
        """
        @summary 查询服务实例资源
        
        @param request: ListServiceInstanceResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_instance_resource_type):
            query['ServiceInstanceResourceType'] = request.service_instance_resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceResources',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_instance_resources(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceResourcesResponse:
        """
        @summary 查询服务实例资源
        
        @param request: ListServiceInstanceResourcesRequest
        @return: ListServiceInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instance_resources_with_options(request, runtime)

    async def list_service_instance_resources_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceResourcesResponse:
        """
        @summary 查询服务实例资源
        
        @param request: ListServiceInstanceResourcesRequest
        @return: ListServiceInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_resources_with_options_async(request, runtime)

    def list_service_instance_upgrade_history_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryResponse:
        """
        @summary View the upgrade history of a service instance
        
        @param request: ListServiceInstanceUpgradeHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceUpgradeHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceUpgradeHistory',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_instance_upgrade_history_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryResponse:
        """
        @summary View the upgrade history of a service instance
        
        @param request: ListServiceInstanceUpgradeHistoryRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceUpgradeHistoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceUpgradeHistory',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_instance_upgrade_history(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryResponse:
        """
        @summary View the upgrade history of a service instance
        
        @param request: ListServiceInstanceUpgradeHistoryRequest
        @return: ListServiceInstanceUpgradeHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instance_upgrade_history_with_options(request, runtime)

    async def list_service_instance_upgrade_history_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstanceUpgradeHistoryResponse:
        """
        @summary View the upgrade history of a service instance
        
        @param request: ListServiceInstanceUpgradeHistoryRequest
        @return: ListServiceInstanceUpgradeHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_upgrade_history_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceInstancesResponse(),
                await self.execute_async(params, req, runtime)
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

    def list_service_registrations_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse:
        """
        @summary Query service registrations.
        
        @param request: ListServiceRegistrationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceRegistrationsResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceRegistrations',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_registrations_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse:
        """
        @summary Query service registrations.
        
        @param request: ListServiceRegistrationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceRegistrationsResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceRegistrations',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_registrations(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceRegistrationsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse:
        """
        @summary Query service registrations.
        
        @param request: ListServiceRegistrationsRequest
        @return: ListServiceRegistrationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_registrations_with_options(request, runtime)

    async def list_service_registrations_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceRegistrationsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceRegistrationsResponse:
        """
        @summary Query service registrations.
        
        @param request: ListServiceRegistrationsRequest
        @return: ListServiceRegistrationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_registrations_with_options_async(request, runtime)

    def list_service_shared_accounts_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceSharedAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse:
        """
        @summary 调用ListServiceSharedAccounts查看服务共享账号列表。
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_shared_accounts_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceSharedAccountsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse:
        """
        @summary 调用ListServiceSharedAccounts查看服务共享账号列表。
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_shared_accounts(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceSharedAccountsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceSharedAccountsResponse:
        """
        @summary 调用ListServiceSharedAccounts查看服务共享账号列表。
        
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
        @summary 调用ListServiceSharedAccounts查看服务共享账号列表。
        
        @param request: ListServiceSharedAccountsRequest
        @return: ListServiceSharedAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_shared_accounts_with_options_async(request, runtime)

    def list_service_test_cases_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestCasesResponse:
        """
        @summary 服务测试用例列表
        
        @param request: ListServiceTestCasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceTestCasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='ListServiceTestCases',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestCasesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestCasesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_test_cases_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestCasesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestCasesResponse:
        """
        @summary 服务测试用例列表
        
        @param request: ListServiceTestCasesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceTestCasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            action='ListServiceTestCases',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestCasesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestCasesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_test_cases(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestCasesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestCasesResponse:
        """
        @summary 服务测试用例列表
        
        @param request: ListServiceTestCasesRequest
        @return: ListServiceTestCasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_test_cases_with_options(request, runtime)

    async def list_service_test_cases_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestCasesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestCasesResponse:
        """
        @summary 服务测试用例列表
        
        @param request: ListServiceTestCasesRequest
        @return: ListServiceTestCasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_test_cases_with_options_async(request, runtime)

    def list_service_test_task_logs_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestTaskLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestTaskLogsResponse:
        """
        @summary 获取服务测试实时日志
        
        @param request: ListServiceTestTaskLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceTestTaskLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceTestTaskLogs',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestTaskLogsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestTaskLogsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_test_task_logs_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestTaskLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestTaskLogsResponse:
        """
        @summary 获取服务测试实时日志
        
        @param request: ListServiceTestTaskLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceTestTaskLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.sort_order):
            query['SortOrder'] = request.sort_order
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceTestTaskLogs',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestTaskLogsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestTaskLogsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_test_task_logs(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestTaskLogsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestTaskLogsResponse:
        """
        @summary 获取服务测试实时日志
        
        @param request: ListServiceTestTaskLogsRequest
        @return: ListServiceTestTaskLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_test_task_logs_with_options(request, runtime)

    async def list_service_test_task_logs_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestTaskLogsRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestTaskLogsResponse:
        """
        @summary 获取服务测试实时日志
        
        @param request: ListServiceTestTaskLogsRequest
        @return: ListServiceTestTaskLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_test_task_logs_with_options_async(request, runtime)

    def list_service_test_tasks_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestTasksResponse:
        """
        @summary 获取任务执行列表
        
        @param request: ListServiceTestTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceTestTasksResponse
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
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceTestTasks',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestTasksResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestTasksResponse(),
                self.execute(params, req, runtime)
            )

    async def list_service_test_tasks_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestTasksRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestTasksResponse:
        """
        @summary 获取任务执行列表
        
        @param request: ListServiceTestTasksRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceTestTasksResponse
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
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceTestTasks',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestTasksResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceTestTasksResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_service_test_tasks(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestTasksRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestTasksResponse:
        """
        @summary 获取任务执行列表
        
        @param request: ListServiceTestTasksRequest
        @return: ListServiceTestTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_test_tasks_with_options(request, runtime)

    async def list_service_test_tasks_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceTestTasksRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceTestTasksResponse:
        """
        @summary 获取任务执行列表
        
        @param request: ListServiceTestTasksRequest
        @return: ListServiceTestTasksResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_test_tasks_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceUsagesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceUsagesResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceUsagesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServiceUsagesResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServicesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServicesResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServicesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListServicesResponse(),
                await self.execute_async(params, req, runtime)
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

    def list_supplier_registrations_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListSupplierRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListSupplierRegistrationsResponse:
        """
        @summary 查询服务商入职审核列表
        
        @param request: ListSupplierRegistrationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSupplierRegistrationsResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSupplierRegistrations',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListSupplierRegistrationsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListSupplierRegistrationsResponse(),
                self.execute(params, req, runtime)
            )

    async def list_supplier_registrations_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListSupplierRegistrationsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListSupplierRegistrationsResponse:
        """
        @summary 查询服务商入职审核列表
        
        @param request: ListSupplierRegistrationsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListSupplierRegistrationsResponse
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSupplierRegistrations',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListSupplierRegistrationsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListSupplierRegistrationsResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_supplier_registrations(
        self,
        request: compute_nest_supplier_20210521_models.ListSupplierRegistrationsRequest,
    ) -> compute_nest_supplier_20210521_models.ListSupplierRegistrationsResponse:
        """
        @summary 查询服务商入职审核列表
        
        @param request: ListSupplierRegistrationsRequest
        @return: ListSupplierRegistrationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_supplier_registrations_with_options(request, runtime)

    async def list_supplier_registrations_async(
        self,
        request: compute_nest_supplier_20210521_models.ListSupplierRegistrationsRequest,
    ) -> compute_nest_supplier_20210521_models.ListSupplierRegistrationsResponse:
        """
        @summary 查询服务商入职审核列表
        
        @param request: ListSupplierRegistrationsRequest
        @return: ListSupplierRegistrationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_supplier_registrations_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListTagKeysResponse:
        """
        @summary 查询标签键列表
        
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
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagKeysResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagKeysResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_keys_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListTagKeysResponse:
        """
        @summary 查询标签键列表
        
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
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagKeysResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagKeysResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_keys(
        self,
        request: compute_nest_supplier_20210521_models.ListTagKeysRequest,
    ) -> compute_nest_supplier_20210521_models.ListTagKeysResponse:
        """
        @summary 查询标签键列表
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: compute_nest_supplier_20210521_models.ListTagKeysRequest,
    ) -> compute_nest_supplier_20210521_models.ListTagKeysResponse:
        """
        @summary 查询标签键列表
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListTagResourcesResponse:
        """
        @summary 查询资源标签
        
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
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_resources_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListTagResourcesResponse:
        """
        @summary 查询资源标签
        
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
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_resources(
        self,
        request: compute_nest_supplier_20210521_models.ListTagResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.ListTagResourcesResponse:
        """
        @summary 查询资源标签
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: compute_nest_supplier_20210521_models.ListTagResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.ListTagResourcesResponse:
        """
        @summary 查询资源标签
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListTagValuesResponse:
        """
        @summary 查询标签值列表
        
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
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagValuesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagValuesResponse(),
                self.execute(params, req, runtime)
            )

    async def list_tag_values_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListTagValuesResponse:
        """
        @summary 查询标签值列表
        
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
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagValuesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ListTagValuesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def list_tag_values(
        self,
        request: compute_nest_supplier_20210521_models.ListTagValuesRequest,
    ) -> compute_nest_supplier_20210521_models.ListTagValuesResponse:
        """
        @summary 查询标签值列表
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: compute_nest_supplier_20210521_models.ListTagValuesRequest,
    ) -> compute_nest_supplier_20210521_models.ListTagValuesResponse:
        """
        @summary 查询标签值列表
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse(),
                await self.execute_async(params, req, runtime)
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

    def pre_launch_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.PreLaunchServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.PreLaunchServiceResponse:
        """
        @summary 预发布服务
        
        @param request: PreLaunchServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreLaunchServiceResponse
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
            action='PreLaunchService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.PreLaunchServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.PreLaunchServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def pre_launch_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.PreLaunchServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.PreLaunchServiceResponse:
        """
        @summary 预发布服务
        
        @param request: PreLaunchServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: PreLaunchServiceResponse
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
            action='PreLaunchService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.PreLaunchServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.PreLaunchServiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def pre_launch_service(
        self,
        request: compute_nest_supplier_20210521_models.PreLaunchServiceRequest,
    ) -> compute_nest_supplier_20210521_models.PreLaunchServiceResponse:
        """
        @summary 预发布服务
        
        @param request: PreLaunchServiceRequest
        @return: PreLaunchServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.pre_launch_service_with_options(request, runtime)

    async def pre_launch_service_async(
        self,
        request: compute_nest_supplier_20210521_models.PreLaunchServiceRequest,
    ) -> compute_nest_supplier_20210521_models.PreLaunchServiceResponse:
        """
        @summary 预发布服务
        
        @param request: PreLaunchServiceRequest
        @return: PreLaunchServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.pre_launch_service_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.PushMeteringDataResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.PushMeteringDataResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.PushMeteringDataResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.PushMeteringDataResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RegisterServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RegisterServiceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RegisterServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RegisterServiceResponse(),
                await self.execute_async(params, req, runtime)
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
        @summary Reject service usage.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RejectServiceUsageResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RejectServiceUsageResponse(),
                self.execute(params, req, runtime)
            )

    async def reject_service_usage_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.RejectServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RejectServiceUsageResponse:
        """
        @summary Reject service usage.
        
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RejectServiceUsageResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RejectServiceUsageResponse(),
                await self.execute_async(params, req, runtime)
            )

    def reject_service_usage(
        self,
        request: compute_nest_supplier_20210521_models.RejectServiceUsageRequest,
    ) -> compute_nest_supplier_20210521_models.RejectServiceUsageResponse:
        """
        @summary Reject service usage.
        
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
        @summary Reject service usage.
        
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ReleaseArtifactResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ReleaseArtifactResponse(),
                self.execute(params, req, runtime)
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
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ReleaseArtifactResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.ReleaseArtifactResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RemoveServiceSharedAccountsResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RestartServiceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RestartServiceInstanceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RestartServiceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RestartServiceInstanceResponse(),
                await self.execute_async(params, req, runtime)
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

    def rollback_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.RollbackServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RollbackServiceInstanceResponse:
        """
        @summary Rollback Service Instance
        
        @param request: RollbackServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackServiceInstanceResponse
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
            action='RollbackServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RollbackServiceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RollbackServiceInstanceResponse(),
                self.execute(params, req, runtime)
            )

    async def rollback_service_instance_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.RollbackServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.RollbackServiceInstanceResponse:
        """
        @summary Rollback Service Instance
        
        @param request: RollbackServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RollbackServiceInstanceResponse
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
            action='RollbackServiceInstance',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RollbackServiceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.RollbackServiceInstanceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def rollback_service_instance(
        self,
        request: compute_nest_supplier_20210521_models.RollbackServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.RollbackServiceInstanceResponse:
        """
        @summary Rollback Service Instance
        
        @param request: RollbackServiceInstanceRequest
        @return: RollbackServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rollback_service_instance_with_options(request, runtime)

    async def rollback_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.RollbackServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.RollbackServiceInstanceResponse:
        """
        @summary Rollback Service Instance
        
        @param request: RollbackServiceInstanceRequest
        @return: RollbackServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rollback_service_instance_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.StartServiceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.StartServiceInstanceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.StartServiceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.StartServiceInstanceResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.StopServiceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.StopServiceInstanceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.StopServiceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.StopServiceInstanceResponse(),
                await self.execute_async(params, req, runtime)
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

    def tag_resources_with_options(
        self,
        request: compute_nest_supplier_20210521_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.TagResourcesResponse:
        """
        @summary 给资源打标签
        
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
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.TagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.TagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def tag_resources_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.TagResourcesResponse:
        """
        @summary 给资源打标签
        
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
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.TagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.TagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def tag_resources(
        self,
        request: compute_nest_supplier_20210521_models.TagResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.TagResourcesResponse:
        """
        @summary 给资源打标签
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: compute_nest_supplier_20210521_models.TagResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.TagResourcesResponse:
        """
        @summary 给资源打标签
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: compute_nest_supplier_20210521_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UnTagResourcesResponse:
        """
        @summary 资源解绑标签
        
        @param request: UnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
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
            action='UnTagResources',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UnTagResourcesResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UnTagResourcesResponse(),
                self.execute(params, req, runtime)
            )

    async def un_tag_resources_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UnTagResourcesResponse:
        """
        @summary 资源解绑标签
        
        @param request: UnTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UnTagResourcesResponse
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
            action='UnTagResources',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UnTagResourcesResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UnTagResourcesResponse(),
                await self.execute_async(params, req, runtime)
            )

    def un_tag_resources(
        self,
        request: compute_nest_supplier_20210521_models.UnTagResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.UnTagResourcesResponse:
        """
        @summary 资源解绑标签
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: compute_nest_supplier_20210521_models.UnTagResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.UnTagResourcesResponse:
        """
        @summary 资源解绑标签
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

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
        if not UtilClient.is_unset(tmp_req.artifact_build_property):
            request.artifact_build_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_build_property, 'ArtifactBuildProperty', 'json')
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_build_property_shrink):
            query['ArtifactBuildProperty'] = request.artifact_build_property_shrink
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateArtifactResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateArtifactResponse(),
                self.execute(params, req, runtime)
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
        if not UtilClient.is_unset(tmp_req.artifact_build_property):
            request.artifact_build_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_build_property, 'ArtifactBuildProperty', 'json')
        if not UtilClient.is_unset(tmp_req.artifact_property):
            request.artifact_property_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.artifact_property, 'ArtifactProperty', 'json')
        query = {}
        if not UtilClient.is_unset(request.artifact_build_property_shrink):
            query['ArtifactBuildProperty'] = request.artifact_build_property_shrink
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.artifact_property_shrink):
            query['ArtifactProperty'] = request.artifact_property_shrink
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.permission_type):
            query['PermissionType'] = request.permission_type
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateArtifactResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateArtifactResponse(),
                await self.execute_async(params, req, runtime)
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
        @summary Update a service.
        
        @param tmp_req: UpdateServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commodity):
            request.commodity_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not UtilClient.is_unset(tmp_req.compliance_metadata):
            request.compliance_metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.compliance_metadata, 'ComplianceMetadata', 'json')
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
        if not UtilClient.is_unset(request.compliance_metadata_shrink):
            query['ComplianceMetadata'] = request.compliance_metadata_shrink
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def update_service_with_options_async(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        """
        @summary Update a service.
        
        @param tmp_req: UpdateServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.UpdateServiceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.commodity):
            request.commodity_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.commodity, 'Commodity', 'json')
        if not UtilClient.is_unset(tmp_req.compliance_metadata):
            request.compliance_metadata_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.compliance_metadata, 'ComplianceMetadata', 'json')
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
        if not UtilClient.is_unset(request.compliance_metadata_shrink):
            query['ComplianceMetadata'] = request.compliance_metadata_shrink
        if not UtilClient.is_unset(request.deploy_metadata):
            query['DeployMetadata'] = request.deploy_metadata
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_service(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        """
        @summary Update a service.
        
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
        @summary Update a service.
        
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
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse(),
                self.execute(params, req, runtime)
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
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceInstanceAttributeResponse(),
                await self.execute_async(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceInstanceSpecResponse(),
                await self.execute_async(params, req, runtime)
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

    def update_service_test_case_with_options(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceTestCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceTestCaseResponse:
        """
        @summary 修改服务测试用例
        
        @param request: UpdateServiceTestCaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceTestCaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.test_case_id):
            query['TestCaseId'] = request.test_case_id
        if not UtilClient.is_unset(request.test_case_name):
            query['TestCaseName'] = request.test_case_name
        if not UtilClient.is_unset(request.test_config):
            query['TestConfig'] = request.test_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceTestCase',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceTestCaseResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceTestCaseResponse(),
                self.execute(params, req, runtime)
            )

    async def update_service_test_case_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceTestCaseRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceTestCaseResponse:
        """
        @summary 修改服务测试用例
        
        @param request: UpdateServiceTestCaseRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceTestCaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.test_case_id):
            query['TestCaseId'] = request.test_case_id
        if not UtilClient.is_unset(request.test_case_name):
            query['TestCaseName'] = request.test_case_name
        if not UtilClient.is_unset(request.test_config):
            query['TestConfig'] = request.test_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceTestCase',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceTestCaseResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateServiceTestCaseResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_service_test_case(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceTestCaseRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceTestCaseResponse:
        """
        @summary 修改服务测试用例
        
        @param request: UpdateServiceTestCaseRequest
        @return: UpdateServiceTestCaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_test_case_with_options(request, runtime)

    async def update_service_test_case_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceTestCaseRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceTestCaseResponse:
        """
        @summary 修改服务测试用例
        
        @param request: UpdateServiceTestCaseRequest
        @return: UpdateServiceTestCaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_test_case_with_options_async(request, runtime)

    def update_shared_account_permission_with_options(
        self,
        request: compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionResponse:
        """
        @summary Update Service Sharing Permissions
        
        @param request: UpdateSharedAccountPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSharedAccountPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
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
            action='UpdateSharedAccountPermission',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionResponse(),
                self.execute(params, req, runtime)
            )

    async def update_shared_account_permission_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionResponse:
        """
        @summary Update Service Sharing Permissions
        
        @param request: UpdateSharedAccountPermissionRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSharedAccountPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.permission):
            query['Permission'] = request.permission
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
            action='UpdateSharedAccountPermission',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_shared_account_permission(
        self,
        request: compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionResponse:
        """
        @summary Update Service Sharing Permissions
        
        @param request: UpdateSharedAccountPermissionRequest
        @return: UpdateSharedAccountPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_shared_account_permission_with_options(request, runtime)

    async def update_shared_account_permission_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateSharedAccountPermissionResponse:
        """
        @summary Update Service Sharing Permissions
        
        @param request: UpdateSharedAccountPermissionRequest
        @return: UpdateSharedAccountPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_shared_account_permission_with_options_async(request, runtime)

    def update_supplier_information_with_options(
        self,
        request: compute_nest_supplier_20210521_models.UpdateSupplierInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateSupplierInformationResponse:
        """
        @summary 更新供应商全局信息
        
        @param request: UpdateSupplierInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSupplierInformationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_settings):
            query['DeliverySettings'] = request.delivery_settings
        if not UtilClient.is_unset(request.operation_ip):
            query['OperationIp'] = request.operation_ip
        if not UtilClient.is_unset(request.operation_mfa_present):
            query['OperationMfaPresent'] = request.operation_mfa_present
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.supplier_desc):
            query['SupplierDesc'] = request.supplier_desc
        if not UtilClient.is_unset(request.supplier_logo):
            query['SupplierLogo'] = request.supplier_logo
        if not UtilClient.is_unset(request.supplier_url):
            query['SupplierUrl'] = request.supplier_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSupplierInformation',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateSupplierInformationResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateSupplierInformationResponse(),
                self.execute(params, req, runtime)
            )

    async def update_supplier_information_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateSupplierInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateSupplierInformationResponse:
        """
        @summary 更新供应商全局信息
        
        @param request: UpdateSupplierInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateSupplierInformationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_settings):
            query['DeliverySettings'] = request.delivery_settings
        if not UtilClient.is_unset(request.operation_ip):
            query['OperationIp'] = request.operation_ip
        if not UtilClient.is_unset(request.operation_mfa_present):
            query['OperationMfaPresent'] = request.operation_mfa_present
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.supplier_desc):
            query['SupplierDesc'] = request.supplier_desc
        if not UtilClient.is_unset(request.supplier_logo):
            query['SupplierLogo'] = request.supplier_logo
        if not UtilClient.is_unset(request.supplier_url):
            query['SupplierUrl'] = request.supplier_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSupplierInformation',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateSupplierInformationResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpdateSupplierInformationResponse(),
                await self.execute_async(params, req, runtime)
            )

    def update_supplier_information(
        self,
        request: compute_nest_supplier_20210521_models.UpdateSupplierInformationRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateSupplierInformationResponse:
        """
        @summary 更新供应商全局信息
        
        @param request: UpdateSupplierInformationRequest
        @return: UpdateSupplierInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_supplier_information_with_options(request, runtime)

    async def update_supplier_information_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateSupplierInformationRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateSupplierInformationResponse:
        """
        @summary 更新供应商全局信息
        
        @param request: UpdateSupplierInformationRequest
        @return: UpdateSupplierInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_supplier_information_with_options_async(request, runtime)

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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse(),
                self.execute(params, req, runtime)
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
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.UpgradeServiceInstanceResponse(),
                await self.execute_async(params, req, runtime)
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

    def withdraw_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.WithdrawServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.WithdrawServiceResponse:
        """
        @summary Withdraw service version.
        
        @param request: WithdrawServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: WithdrawServiceResponse
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
            action='WithdrawService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.WithdrawServiceResponse(),
                self.call_api(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.WithdrawServiceResponse(),
                self.execute(params, req, runtime)
            )

    async def withdraw_service_with_options_async(
        self,
        request: compute_nest_supplier_20210521_models.WithdrawServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.WithdrawServiceResponse:
        """
        @summary Withdraw service version.
        
        @param request: WithdrawServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: WithdrawServiceResponse
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
            action='WithdrawService',
            version='2021-05-21',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        if UtilClient.is_unset(self._signature_version) or not UtilClient.equal_string(self._signature_version, 'v4'):
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.WithdrawServiceResponse(),
                await self.call_api_async(params, req, runtime)
            )
        else:
            return TeaCore.from_map(
                compute_nest_supplier_20210521_models.WithdrawServiceResponse(),
                await self.execute_async(params, req, runtime)
            )

    def withdraw_service(
        self,
        request: compute_nest_supplier_20210521_models.WithdrawServiceRequest,
    ) -> compute_nest_supplier_20210521_models.WithdrawServiceResponse:
        """
        @summary Withdraw service version.
        
        @param request: WithdrawServiceRequest
        @return: WithdrawServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.withdraw_service_with_options(request, runtime)

    async def withdraw_service_async(
        self,
        request: compute_nest_supplier_20210521_models.WithdrawServiceRequest,
    ) -> compute_nest_supplier_20210521_models.WithdrawServiceResponse:
        """
        @summary Withdraw service version.
        
        @param request: WithdrawServiceRequest
        @return: WithdrawServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.withdraw_service_with_options_async(request, runtime)
