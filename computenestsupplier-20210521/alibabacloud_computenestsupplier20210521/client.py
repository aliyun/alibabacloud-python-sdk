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

    def continue_deploy_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.continue_deploy_service_instance_with_options(request, runtime)

    async def continue_deploy_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.ContinueDeployServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.continue_deploy_service_instance_with_options_async(request, runtime)

    def create_artifact_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.CreateArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateArtifactResponse:
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
        if not UtilClient.is_unset(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
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
        if not UtilClient.is_unset(request.support_region_ids):
            query['SupportRegionIds'] = request.support_region_ids
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
        runtime = util_models.RuntimeOptions()
        return self.create_artifact_with_options(request, runtime)

    async def create_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.CreateArtifactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_artifact_with_options_async(request, runtime)

    def create_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
        if not UtilClient.is_unset(request.approval_type):
            query['ApprovalType'] = request.approval_type
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
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    async def create_service_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_with_options_async(request, runtime)

    def create_service_instance_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.CreateServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.CreateServiceInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.create_service_instance_with_options(request, runtime)

    async def create_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.CreateServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.CreateServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.create_service_instance_with_options_async(request, runtime)

    def delete_artifact_with_options(
        self,
        request: compute_nest_supplier_20210521_models.DeleteArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteArtifactResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_artifact_with_options(request, runtime)

    async def delete_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteArtifactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_artifact_with_options_async(request, runtime)

    def delete_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    async def delete_service_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_with_options_async(request, runtime)

    def delete_service_instances_with_options(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.delete_service_instances_with_options(request, runtime)

    async def delete_service_instances_async(
        self,
        request: compute_nest_supplier_20210521_models.DeleteServiceInstancesRequest,
    ) -> compute_nest_supplier_20210521_models.DeleteServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_instances_with_options_async(request, runtime)

    def get_artifact_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetArtifactResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_with_options(request, runtime)

    async def get_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.GetArtifactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_artifact_with_options_async(request, runtime)

    def get_artifact_repository_credentials_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_artifact_repository_credentials_with_options(request, runtime)

    async def get_artifact_repository_credentials_async(
        self,
        request: compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsRequest,
    ) -> compute_nest_supplier_20210521_models.GetArtifactRepositoryCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_artifact_repository_credentials_with_options_async(request, runtime)

    def get_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_service_with_options(request, runtime)

    async def get_service_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_with_options_async(request, runtime)

    def get_service_estimate_cost_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.GetServiceEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse:
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.GetServiceEstimateCostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        UtilClient.validate_model(tmp_req)
        request = compute_nest_supplier_20210521_models.GetServiceEstimateCostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
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
        runtime = util_models.RuntimeOptions()
        return self.get_service_estimate_cost_with_options(request, runtime)

    async def get_service_estimate_cost_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceEstimateCostRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceEstimateCostResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_estimate_cost_with_options_async(request, runtime)

    def get_service_instance_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.get_service_instance_with_options(request, runtime)

    async def get_service_instance_async(
        self,
        request: compute_nest_supplier_20210521_models.GetServiceInstanceRequest,
    ) -> compute_nest_supplier_20210521_models.GetServiceInstanceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_service_instance_with_options_async(request, runtime)

    def get_upload_credentials_with_options(
        self,
        request: compute_nest_supplier_20210521_models.GetUploadCredentialsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.GetUploadCredentialsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
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
        runtime = util_models.RuntimeOptions()
        return self.get_upload_credentials_with_options(request, runtime)

    async def get_upload_credentials_async(
        self,
        request: compute_nest_supplier_20210521_models.GetUploadCredentialsRequest,
    ) -> compute_nest_supplier_20210521_models.GetUploadCredentialsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_upload_credentials_with_options_async(request, runtime)

    def list_artifact_versions_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactVersionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactVersionsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.artifact_id):
            query['ArtifactId'] = request.artifact_id
        if not UtilClient.is_unset(request.max_result):
            query['MaxResult'] = request.max_result
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
        runtime = util_models.RuntimeOptions()
        return self.list_artifact_versions_with_options(request, runtime)

    async def list_artifact_versions_async(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactVersionsRequest,
    ) -> compute_nest_supplier_20210521_models.ListArtifactVersionsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_artifact_versions_with_options_async(request, runtime)

    def list_artifacts_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListArtifactsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        runtime = util_models.RuntimeOptions()
        return self.list_artifacts_with_options(request, runtime)

    async def list_artifacts_async(
        self,
        request: compute_nest_supplier_20210521_models.ListArtifactsRequest,
    ) -> compute_nest_supplier_20210521_models.ListArtifactsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_artifacts_with_options_async(request, runtime)

    def list_service_instances_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_service_instances_with_options(request, runtime)

    async def list_service_instances_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceInstancesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceInstancesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instances_with_options_async(request, runtime)

    def list_service_usages_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceUsagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServiceUsagesResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
        runtime = util_models.RuntimeOptions()
        return self.list_service_usages_with_options(request, runtime)

    async def list_service_usages_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServiceUsagesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServiceUsagesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_service_usages_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: compute_nest_supplier_20210521_models.ListServicesRequest,
    ) -> compute_nest_supplier_20210521_models.ListServicesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)

    def modify_service_instance_resources_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.modify_service_instance_resources_with_options(request, runtime)

    async def modify_service_instance_resources_async(
        self,
        request: compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesRequest,
    ) -> compute_nest_supplier_20210521_models.ModifyServiceInstanceResourcesResponse:
        runtime = util_models.RuntimeOptions()
        return await self.modify_service_instance_resources_with_options_async(request, runtime)

    def release_artifact_with_options(
        self,
        request: compute_nest_supplier_20210521_models.ReleaseArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.ReleaseArtifactResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.release_artifact_with_options(request, runtime)

    async def release_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.ReleaseArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.ReleaseArtifactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.release_artifact_with_options_async(request, runtime)

    def update_artifact_with_options(
        self,
        tmp_req: compute_nest_supplier_20210521_models.UpdateArtifactRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateArtifactResponse:
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
        runtime = util_models.RuntimeOptions()
        return self.update_artifact_with_options(request, runtime)

    async def update_artifact_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateArtifactRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateArtifactResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_artifact_with_options_async(request, runtime)

    def update_service_with_options(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
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
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
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
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_metadata):
            query['AlarmMetadata'] = request.alarm_metadata
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
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_info):
            query['ServiceInfo'] = request.service_info
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
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
        runtime = util_models.RuntimeOptions()
        return self.update_service_with_options(request, runtime)

    async def update_service_async(
        self,
        request: compute_nest_supplier_20210521_models.UpdateServiceRequest,
    ) -> compute_nest_supplier_20210521_models.UpdateServiceResponse:
        runtime = util_models.RuntimeOptions()
        return await self.update_service_with_options_async(request, runtime)
