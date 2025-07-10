# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_computenest20210601 import models as compute_nest_20210601_models
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
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def cancel_service_usage_with_options(
        self,
        request: compute_nest_20210601_models.CancelServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CancelServiceUsageResponse:
        """
        @summary Cancels the application for using a service.
        
        @param request: CancelServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelServiceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.need_delete):
            query['NeedDelete'] = request.need_delete
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelServiceUsage',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CancelServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_service_usage_with_options_async(
        self,
        request: compute_nest_20210601_models.CancelServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CancelServiceUsageResponse:
        """
        @summary Cancels the application for using a service.
        
        @param request: CancelServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CancelServiceUsageResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.need_delete):
            query['NeedDelete'] = request.need_delete
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelServiceUsage',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CancelServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_service_usage(
        self,
        request: compute_nest_20210601_models.CancelServiceUsageRequest,
    ) -> compute_nest_20210601_models.CancelServiceUsageResponse:
        """
        @summary Cancels the application for using a service.
        
        @param request: CancelServiceUsageRequest
        @return: CancelServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.cancel_service_usage_with_options(request, runtime)

    async def cancel_service_usage_async(
        self,
        request: compute_nest_20210601_models.CancelServiceUsageRequest,
    ) -> compute_nest_20210601_models.CancelServiceUsageResponse:
        """
        @summary Cancels the application for using a service.
        
        @param request: CancelServiceUsageRequest
        @return: CancelServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.cancel_service_usage_with_options_async(request, runtime)

    def change_resource_group_with_options(
        self,
        request: compute_nest_20210601_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a cloud resource belongs.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
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
            action='ChangeResourceGroup',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: compute_nest_20210601_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a cloud resource belongs.
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
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
            action='ChangeResourceGroup',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: compute_nest_20210601_models.ChangeResourceGroupRequest,
    ) -> compute_nest_20210601_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a cloud resource belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: compute_nest_20210601_models.ChangeResourceGroupRequest,
    ) -> compute_nest_20210601_models.ChangeResourceGroupResponse:
        """
        @summary Changes the resource group to which a cloud resource belongs.
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def check_service_deployable_with_options(
        self,
        request: compute_nest_20210601_models.CheckServiceDeployableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CheckServiceDeployableResponse:
        """
        @summary 服务实例部署前的预检查
        
        @param request: CheckServiceDeployableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceDeployableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.post_paid_amount):
            query['PostPaidAmount'] = request.post_paid_amount
        if not UtilClient.is_unset(request.pre_paid_amount):
            query['PrePaidAmount'] = request.pre_paid_amount
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceDeployable',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CheckServiceDeployableResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_service_deployable_with_options_async(
        self,
        request: compute_nest_20210601_models.CheckServiceDeployableRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CheckServiceDeployableResponse:
        """
        @summary 服务实例部署前的预检查
        
        @param request: CheckServiceDeployableRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CheckServiceDeployableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.post_paid_amount):
            query['PostPaidAmount'] = request.post_paid_amount
        if not UtilClient.is_unset(request.pre_paid_amount):
            query['PrePaidAmount'] = request.pre_paid_amount
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceDeployable',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CheckServiceDeployableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_service_deployable(
        self,
        request: compute_nest_20210601_models.CheckServiceDeployableRequest,
    ) -> compute_nest_20210601_models.CheckServiceDeployableResponse:
        """
        @summary 服务实例部署前的预检查
        
        @param request: CheckServiceDeployableRequest
        @return: CheckServiceDeployableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_service_deployable_with_options(request, runtime)

    async def check_service_deployable_async(
        self,
        request: compute_nest_20210601_models.CheckServiceDeployableRequest,
    ) -> compute_nest_20210601_models.CheckServiceDeployableResponse:
        """
        @summary 服务实例部署前的预检查
        
        @param request: CheckServiceDeployableRequest
        @return: CheckServiceDeployableResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.check_service_deployable_with_options_async(request, runtime)

    def continue_deploy_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.ContinueDeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ContinueDeployServiceInstanceResponse:
        """
        @summary Continues to deploy a service instance after the service instance failed to be deployed.
        
        @description This operation is available only for service instances that belong to private services deployed by using Resource Orchestration Service (ROS).
        
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
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ContinueDeployServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_deploy_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.ContinueDeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ContinueDeployServiceInstanceResponse:
        """
        @summary Continues to deploy a service instance after the service instance failed to be deployed.
        
        @description This operation is available only for service instances that belong to private services deployed by using Resource Orchestration Service (ROS).
        
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
        if not UtilClient.is_unset(request.option):
            query['Option'] = request.option
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ContinueDeployServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_deploy_service_instance(
        self,
        request: compute_nest_20210601_models.ContinueDeployServiceInstanceRequest,
    ) -> compute_nest_20210601_models.ContinueDeployServiceInstanceResponse:
        """
        @summary Continues to deploy a service instance after the service instance failed to be deployed.
        
        @description This operation is available only for service instances that belong to private services deployed by using Resource Orchestration Service (ROS).
        
        @param request: ContinueDeployServiceInstanceRequest
        @return: ContinueDeployServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.continue_deploy_service_instance_with_options(request, runtime)

    async def continue_deploy_service_instance_async(
        self,
        request: compute_nest_20210601_models.ContinueDeployServiceInstanceRequest,
    ) -> compute_nest_20210601_models.ContinueDeployServiceInstanceResponse:
        """
        @summary Continues to deploy a service instance after the service instance failed to be deployed.
        
        @description This operation is available only for service instances that belong to private services deployed by using Resource Orchestration Service (ROS).
        
        @param request: ContinueDeployServiceInstanceRequest
        @return: ContinueDeployServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.continue_deploy_service_instance_with_options_async(request, runtime)

    def create_service_instance_with_options(
        self,
        tmp_req: compute_nest_20210601_models.CreateServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CreateServiceInstanceResponse:
        """
        @summary Creates and deploys a service instance.
        
        @param tmp_req: CreateServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.CreateServiceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.enable_instance_ops):
            query['EnableInstanceOps'] = request.enable_instance_ops
        if not UtilClient.is_unset(request.enable_user_prometheus):
            query['EnableUserPrometheus'] = request.enable_user_prometheus
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_auto_pay):
            query['ResourceAutoPay'] = request.resource_auto_pay
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.specification_code):
            query['SpecificationCode'] = request.specification_code
        if not UtilClient.is_unset(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceInstance',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CreateServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_instance_with_options_async(
        self,
        tmp_req: compute_nest_20210601_models.CreateServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CreateServiceInstanceResponse:
        """
        @summary Creates and deploys a service instance.
        
        @param tmp_req: CreateServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.CreateServiceInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.contact_group):
            query['ContactGroup'] = request.contact_group
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
        if not UtilClient.is_unset(request.enable_instance_ops):
            query['EnableInstanceOps'] = request.enable_instance_ops
        if not UtilClient.is_unset(request.enable_user_prometheus):
            query['EnableUserPrometheus'] = request.enable_user_prometheus
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.operation_metadata):
            query['OperationMetadata'] = request.operation_metadata
        if not UtilClient.is_unset(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_auto_pay):
            query['ResourceAutoPay'] = request.resource_auto_pay
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.specification_code):
            query['SpecificationCode'] = request.specification_code
        if not UtilClient.is_unset(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceInstance',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CreateServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_instance(
        self,
        request: compute_nest_20210601_models.CreateServiceInstanceRequest,
    ) -> compute_nest_20210601_models.CreateServiceInstanceResponse:
        """
        @summary Creates and deploys a service instance.
        
        @param request: CreateServiceInstanceRequest
        @return: CreateServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_instance_with_options(request, runtime)

    async def create_service_instance_async(
        self,
        request: compute_nest_20210601_models.CreateServiceInstanceRequest,
    ) -> compute_nest_20210601_models.CreateServiceInstanceResponse:
        """
        @summary Creates and deploys a service instance.
        
        @param request: CreateServiceInstanceRequest
        @return: CreateServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_instance_with_options_async(request, runtime)

    def create_service_usage_with_options(
        self,
        tmp_req: compute_nest_20210601_models.CreateServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CreateServiceUsageResponse:
        """
        @summary Creates an application for using a service.
        
        @param tmp_req: CreateServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceUsageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.CreateServiceUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_information):
            request.user_information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_information, 'UserInformation', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_information_shrink):
            query['UserInformation'] = request.user_information_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceUsage',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CreateServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_service_usage_with_options_async(
        self,
        tmp_req: compute_nest_20210601_models.CreateServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.CreateServiceUsageResponse:
        """
        @summary Creates an application for using a service.
        
        @param tmp_req: CreateServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateServiceUsageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.CreateServiceUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_information):
            request.user_information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_information, 'UserInformation', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_information_shrink):
            query['UserInformation'] = request.user_information_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceUsage',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.CreateServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_service_usage(
        self,
        request: compute_nest_20210601_models.CreateServiceUsageRequest,
    ) -> compute_nest_20210601_models.CreateServiceUsageResponse:
        """
        @summary Creates an application for using a service.
        
        @param request: CreateServiceUsageRequest
        @return: CreateServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_service_usage_with_options(request, runtime)

    async def create_service_usage_async(
        self,
        request: compute_nest_20210601_models.CreateServiceUsageRequest,
    ) -> compute_nest_20210601_models.CreateServiceUsageResponse:
        """
        @summary Creates an application for using a service.
        
        @param request: CreateServiceUsageRequest
        @return: CreateServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_usage_with_options_async(request, runtime)

    def delete_service_instances_with_options(
        self,
        request: compute_nest_20210601_models.DeleteServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DeleteServiceInstancesResponse:
        """
        @summary Delete service instances.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeleteServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_service_instances_with_options_async(
        self,
        request: compute_nest_20210601_models.DeleteServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DeleteServiceInstancesResponse:
        """
        @summary Delete service instances.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeleteServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_service_instances(
        self,
        request: compute_nest_20210601_models.DeleteServiceInstancesRequest,
    ) -> compute_nest_20210601_models.DeleteServiceInstancesResponse:
        """
        @summary Delete service instances.
        
        @param request: DeleteServiceInstancesRequest
        @return: DeleteServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_service_instances_with_options(request, runtime)

    async def delete_service_instances_async(
        self,
        request: compute_nest_20210601_models.DeleteServiceInstancesRequest,
    ) -> compute_nest_20210601_models.DeleteServiceInstancesResponse:
        """
        @summary Delete service instances.
        
        @param request: DeleteServiceInstancesRequest
        @return: DeleteServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_instances_with_options_async(request, runtime)

    def deploy_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.DeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DeployServiceInstanceResponse:
        """
        @summary Deploy service instance in Created status.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeployServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def deploy_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.DeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DeployServiceInstanceResponse:
        """
        @summary Deploy service instance in Created status.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DeployServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def deploy_service_instance(
        self,
        request: compute_nest_20210601_models.DeployServiceInstanceRequest,
    ) -> compute_nest_20210601_models.DeployServiceInstanceResponse:
        """
        @summary Deploy service instance in Created status.
        
        @param request: DeployServiceInstanceRequest
        @return: DeployServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deploy_service_instance_with_options(request, runtime)

    async def deploy_service_instance_async(
        self,
        request: compute_nest_20210601_models.DeployServiceInstanceRequest,
    ) -> compute_nest_20210601_models.DeployServiceInstanceResponse:
        """
        @summary Deploy service instance in Created status.
        
        @param request: DeployServiceInstanceRequest
        @return: DeployServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.deploy_service_instance_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: compute_nest_20210601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DescribeRegionsResponse:
        """
        @summary List available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: compute_nest_20210601_models.DescribeRegionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DescribeRegionsResponse:
        """
        @summary List available regions.
        
        @param request: DescribeRegionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DescribeRegionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: compute_nest_20210601_models.DescribeRegionsRequest,
    ) -> compute_nest_20210601_models.DescribeRegionsResponse:
        """
        @summary List available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: compute_nest_20210601_models.DescribeRegionsRequest,
    ) -> compute_nest_20210601_models.DescribeRegionsResponse:
        """
        @summary List available regions.
        
        @param request: DescribeRegionsRequest
        @return: DescribeRegionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def generate_service_policy_with_options(
        self,
        request: compute_nest_20210601_models.GenerateServicePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GenerateServicePolicyResponse:
        """
        @summary 生成并校验服务创建stack所需要的权限
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GenerateServicePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_service_policy_with_options_async(
        self,
        request: compute_nest_20210601_models.GenerateServicePolicyRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GenerateServicePolicyResponse:
        """
        @summary 生成并校验服务创建stack所需要的权限
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GenerateServicePolicyResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_service_policy(
        self,
        request: compute_nest_20210601_models.GenerateServicePolicyRequest,
    ) -> compute_nest_20210601_models.GenerateServicePolicyResponse:
        """
        @summary 生成并校验服务创建stack所需要的权限
        
        @param request: GenerateServicePolicyRequest
        @return: GenerateServicePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.generate_service_policy_with_options(request, runtime)

    async def generate_service_policy_async(
        self,
        request: compute_nest_20210601_models.GenerateServicePolicyRequest,
    ) -> compute_nest_20210601_models.GenerateServicePolicyResponse:
        """
        @summary 生成并校验服务创建stack所需要的权限
        
        @param request: GenerateServicePolicyRequest
        @return: GenerateServicePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.generate_service_policy_with_options_async(request, runtime)

    def get_service_with_options(
        self,
        request: compute_nest_20210601_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceResponse:
        """
        @summary Queries the information about a service.
        
        @param request: GetServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.show_details):
            query['ShowDetails'] = request.show_details
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_with_options_async(
        self,
        request: compute_nest_20210601_models.GetServiceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceResponse:
        """
        @summary Queries the information about a service.
        
        @param request: GetServiceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.show_details):
            query['ShowDetails'] = request.show_details
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetService',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service(
        self,
        request: compute_nest_20210601_models.GetServiceRequest,
    ) -> compute_nest_20210601_models.GetServiceResponse:
        """
        @summary Queries the information about a service.
        
        @param request: GetServiceRequest
        @return: GetServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_with_options(request, runtime)

    async def get_service_async(
        self,
        request: compute_nest_20210601_models.GetServiceRequest,
    ) -> compute_nest_20210601_models.GetServiceResponse:
        """
        @summary Queries the information about a service.
        
        @param request: GetServiceRequest
        @return: GetServiceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_with_options_async(request, runtime)

    def get_service_estimate_cost_with_options(
        self,
        tmp_req: compute_nest_20210601_models.GetServiceEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceEstimateCostResponse:
        """
        @summary Queries the estimated price for creating a service instance.
        
        @param tmp_req: GetServiceEstimateCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceEstimateCostResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.GetServiceEstimateCostShrinkRequest()
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
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
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
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceEstimateCost',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceEstimateCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_estimate_cost_with_options_async(
        self,
        tmp_req: compute_nest_20210601_models.GetServiceEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceEstimateCostResponse:
        """
        @summary Queries the estimated price for creating a service instance.
        
        @param tmp_req: GetServiceEstimateCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceEstimateCostResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.GetServiceEstimateCostShrinkRequest()
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
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
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
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceEstimateCost',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceEstimateCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_estimate_cost(
        self,
        request: compute_nest_20210601_models.GetServiceEstimateCostRequest,
    ) -> compute_nest_20210601_models.GetServiceEstimateCostResponse:
        """
        @summary Queries the estimated price for creating a service instance.
        
        @param request: GetServiceEstimateCostRequest
        @return: GetServiceEstimateCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_estimate_cost_with_options(request, runtime)

    async def get_service_estimate_cost_async(
        self,
        request: compute_nest_20210601_models.GetServiceEstimateCostRequest,
    ) -> compute_nest_20210601_models.GetServiceEstimateCostResponse:
        """
        @summary Queries the estimated price for creating a service instance.
        
        @param request: GetServiceEstimateCostRequest
        @return: GetServiceEstimateCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_estimate_cost_with_options_async(request, runtime)

    def get_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceInstanceResponse:
        """
        @summary Queries the information about a service instance based on the region ID and the ID of the service instance or the Alibaba Cloud Marketplace instance. Information including the service status, template name, and involved resources are returned.
        
        @param request: GetServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.market_instance_id):
            query['MarketInstanceId'] = request.market_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceInstance',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceInstanceResponse:
        """
        @summary Queries the information about a service instance based on the region ID and the ID of the service instance or the Alibaba Cloud Marketplace instance. Information including the service status, template name, and involved resources are returned.
        
        @param request: GetServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceInstanceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.market_instance_id):
            query['MarketInstanceId'] = request.market_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceInstance',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_instance(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceRequest,
    ) -> compute_nest_20210601_models.GetServiceInstanceResponse:
        """
        @summary Queries the information about a service instance based on the region ID and the ID of the service instance or the Alibaba Cloud Marketplace instance. Information including the service status, template name, and involved resources are returned.
        
        @param request: GetServiceInstanceRequest
        @return: GetServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_instance_with_options(request, runtime)

    async def get_service_instance_async(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceRequest,
    ) -> compute_nest_20210601_models.GetServiceInstanceResponse:
        """
        @summary Queries the information about a service instance based on the region ID and the ID of the service instance or the Alibaba Cloud Marketplace instance. Information including the service status, template name, and involved resources are returned.
        
        @param request: GetServiceInstanceRequest
        @return: GetServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_instance_with_options_async(request, runtime)

    def get_service_instance_subscription_estimate_cost_with_options(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostResponse:
        """
        @summary Query renewal prices for prepaid resources of private deployment service instance. You can query renewal prices for all prepaid resources included in a service instance, or query renewal prices for specified resources. Only one of the two methods can be used.
        
        @param request: GetServiceInstanceSubscriptionEstimateCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceInstanceSubscriptionEstimateCostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_period):
            query['ResourcePeriod'] = request.resource_period
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceInstanceSubscriptionEstimateCost',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_instance_subscription_estimate_cost_with_options_async(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostResponse:
        """
        @summary Query renewal prices for prepaid resources of private deployment service instance. You can query renewal prices for all prepaid resources included in a service instance, or query renewal prices for specified resources. Only one of the two methods can be used.
        
        @param request: GetServiceInstanceSubscriptionEstimateCostRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceInstanceSubscriptionEstimateCostResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_period):
            query['ResourcePeriod'] = request.resource_period
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceInstanceSubscriptionEstimateCost',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_instance_subscription_estimate_cost(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostRequest,
    ) -> compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostResponse:
        """
        @summary Query renewal prices for prepaid resources of private deployment service instance. You can query renewal prices for all prepaid resources included in a service instance, or query renewal prices for specified resources. Only one of the two methods can be used.
        
        @param request: GetServiceInstanceSubscriptionEstimateCostRequest
        @return: GetServiceInstanceSubscriptionEstimateCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_instance_subscription_estimate_cost_with_options(request, runtime)

    async def get_service_instance_subscription_estimate_cost_async(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostRequest,
    ) -> compute_nest_20210601_models.GetServiceInstanceSubscriptionEstimateCostResponse:
        """
        @summary Query renewal prices for prepaid resources of private deployment service instance. You can query renewal prices for all prepaid resources included in a service instance, or query renewal prices for specified resources. Only one of the two methods can be used.
        
        @param request: GetServiceInstanceSubscriptionEstimateCostRequest
        @return: GetServiceInstanceSubscriptionEstimateCostResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_instance_subscription_estimate_cost_with_options_async(request, runtime)

    def get_service_provisions_with_options(
        self,
        tmp_req: compute_nest_20210601_models.GetServiceProvisionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceProvisionsResponse:
        """
        @summary 计算巢查询服务是否开通
        
        @param tmp_req: GetServiceProvisionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceProvisionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.GetServiceProvisionsShrinkRequest()
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
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceProvisions',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceProvisionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_provisions_with_options_async(
        self,
        tmp_req: compute_nest_20210601_models.GetServiceProvisionsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceProvisionsResponse:
        """
        @summary 计算巢查询服务是否开通
        
        @param tmp_req: GetServiceProvisionsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetServiceProvisionsResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.GetServiceProvisionsShrinkRequest()
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
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceProvisions',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceProvisionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_provisions(
        self,
        request: compute_nest_20210601_models.GetServiceProvisionsRequest,
    ) -> compute_nest_20210601_models.GetServiceProvisionsResponse:
        """
        @summary 计算巢查询服务是否开通
        
        @param request: GetServiceProvisionsRequest
        @return: GetServiceProvisionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_provisions_with_options(request, runtime)

    async def get_service_provisions_async(
        self,
        request: compute_nest_20210601_models.GetServiceProvisionsRequest,
    ) -> compute_nest_20210601_models.GetServiceProvisionsResponse:
        """
        @summary 计算巢查询服务是否开通
        
        @param request: GetServiceProvisionsRequest
        @return: GetServiceProvisionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_provisions_with_options_async(request, runtime)

    def get_service_template_parameter_constraints_with_options(
        self,
        request: compute_nest_20210601_models.GetServiceTemplateParameterConstraintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceTemplateParameterConstraintsResponse:
        """
        @summary Queries the constraints on the parameters in an Resource Orchestration Service (ROS) template.
        
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
        if not UtilClient.is_unset(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceTemplateParameterConstraints',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceTemplateParameterConstraintsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_service_template_parameter_constraints_with_options_async(
        self,
        request: compute_nest_20210601_models.GetServiceTemplateParameterConstraintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceTemplateParameterConstraintsResponse:
        """
        @summary Queries the constraints on the parameters in an Resource Orchestration Service (ROS) template.
        
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
        if not UtilClient.is_unset(request.specification_name):
            query['SpecificationName'] = request.specification_name
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.trial_type):
            query['TrialType'] = request.trial_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceTemplateParameterConstraints',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetServiceTemplateParameterConstraintsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_service_template_parameter_constraints(
        self,
        request: compute_nest_20210601_models.GetServiceTemplateParameterConstraintsRequest,
    ) -> compute_nest_20210601_models.GetServiceTemplateParameterConstraintsResponse:
        """
        @summary Queries the constraints on the parameters in an Resource Orchestration Service (ROS) template.
        
        @param request: GetServiceTemplateParameterConstraintsRequest
        @return: GetServiceTemplateParameterConstraintsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_service_template_parameter_constraints_with_options(request, runtime)

    async def get_service_template_parameter_constraints_async(
        self,
        request: compute_nest_20210601_models.GetServiceTemplateParameterConstraintsRequest,
    ) -> compute_nest_20210601_models.GetServiceTemplateParameterConstraintsResponse:
        """
        @summary Queries the constraints on the parameters in an Resource Orchestration Service (ROS) template.
        
        @param request: GetServiceTemplateParameterConstraintsRequest
        @return: GetServiceTemplateParameterConstraintsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_template_parameter_constraints_with_options_async(request, runtime)

    def get_user_information_with_options(
        self,
        request: compute_nest_20210601_models.GetUserInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetUserInformationResponse:
        """
        @summary Queries the information about a customer.
        
        @param request: GetUserInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserInformationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInformation',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetUserInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_information_with_options_async(
        self,
        request: compute_nest_20210601_models.GetUserInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetUserInformationResponse:
        """
        @summary Queries the information about a customer.
        
        @param request: GetUserInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetUserInformationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserInformation',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.GetUserInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_information(
        self,
        request: compute_nest_20210601_models.GetUserInformationRequest,
    ) -> compute_nest_20210601_models.GetUserInformationResponse:
        """
        @summary Queries the information about a customer.
        
        @param request: GetUserInformationRequest
        @return: GetUserInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_user_information_with_options(request, runtime)

    async def get_user_information_async(
        self,
        request: compute_nest_20210601_models.GetUserInformationRequest,
    ) -> compute_nest_20210601_models.GetUserInformationResponse:
        """
        @summary Queries the information about a customer.
        
        @param request: GetUserInformationRequest
        @return: GetUserInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_user_information_with_options_async(request, runtime)

    def list_policies_with_options(
        self,
        request: compute_nest_20210601_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListPoliciesResponse:
        """
        @summary Query Permission Policy List
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='ListPolicies',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_policies_with_options_async(
        self,
        request: compute_nest_20210601_models.ListPoliciesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListPoliciesResponse:
        """
        @summary Query Permission Policy List
        
        @param request: ListPoliciesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListPoliciesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='ListPolicies',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListPoliciesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_policies(
        self,
        request: compute_nest_20210601_models.ListPoliciesRequest,
    ) -> compute_nest_20210601_models.ListPoliciesResponse:
        """
        @summary Query Permission Policy List
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    async def list_policies_async(
        self,
        request: compute_nest_20210601_models.ListPoliciesRequest,
    ) -> compute_nest_20210601_models.ListPoliciesResponse:
        """
        @summary Query Permission Policy List
        
        @param request: ListPoliciesRequest
        @return: ListPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_policies_with_options_async(request, runtime)

    def list_service_categories_with_options(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceCategoriesResponse:
        """
        @summary 查询服务类别
        
        @param request: ListServiceCategoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceCategoriesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListServiceCategories',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_categories_with_options_async(
        self,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceCategoriesResponse:
        """
        @summary 查询服务类别
        
        @param request: ListServiceCategoriesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceCategoriesResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListServiceCategories',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceCategoriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_categories(self) -> compute_nest_20210601_models.ListServiceCategoriesResponse:
        """
        @summary 查询服务类别
        
        @return: ListServiceCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_categories_with_options(runtime)

    async def list_service_categories_async(self) -> compute_nest_20210601_models.ListServiceCategoriesResponse:
        """
        @summary 查询服务类别
        
        @return: ListServiceCategoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_categories_with_options_async(runtime)

    def list_service_instance_bill_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceBillResponse:
        """
        @summary 展示服务实例账单
        
        @param request: ListServiceInstanceBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceBill',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceBillResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_bill_with_options_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceBillRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceBillResponse:
        """
        @summary 展示服务实例账单
        
        @param request: ListServiceInstanceBillRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceBillResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.billing_cycle):
            query['BillingCycle'] = request.billing_cycle
        if not UtilClient.is_unset(request.billing_date):
            query['BillingDate'] = request.billing_date
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstanceBill',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceBillResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_bill(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceBillRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceBillResponse:
        """
        @summary 展示服务实例账单
        
        @param request: ListServiceInstanceBillRequest
        @return: ListServiceInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instance_bill_with_options(request, runtime)

    async def list_service_instance_bill_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceBillRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceBillResponse:
        """
        @summary 展示服务实例账单
        
        @param request: ListServiceInstanceBillRequest
        @return: ListServiceInstanceBillResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_bill_with_options_async(request, runtime)

    def list_service_instance_logs_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceLogsResponse:
        """
        @summary Queries the deployment and upgrade logs of a service instance.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_logs_with_options_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceLogsResponse:
        """
        @summary Queries the deployment and upgrade logs of a service instance.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_logs(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceLogsRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceLogsResponse:
        """
        @summary Queries the deployment and upgrade logs of a service instance.
        
        @param request: ListServiceInstanceLogsRequest
        @return: ListServiceInstanceLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instance_logs_with_options(request, runtime)

    async def list_service_instance_logs_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceLogsRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceLogsResponse:
        """
        @summary Queries the deployment and upgrade logs of a service instance.
        
        @param request: ListServiceInstanceLogsRequest
        @return: ListServiceInstanceLogsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_logs_with_options_async(request, runtime)

    def list_service_instance_resources_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceResourcesResponse:
        """
        @summary Queries the resources contained in a service instance.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_resources_with_options_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceResourcesResponse:
        """
        @summary Queries the resources contained in a service instance.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_resources(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceResourcesRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceResourcesResponse:
        """
        @summary Queries the resources contained in a service instance.
        
        @param request: ListServiceInstanceResourcesRequest
        @return: ListServiceInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instance_resources_with_options(request, runtime)

    async def list_service_instance_resources_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceResourcesRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceResourcesResponse:
        """
        @summary Queries the resources contained in a service instance.
        
        @param request: ListServiceInstanceResourcesRequest
        @return: ListServiceInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_resources_with_options_async(request, runtime)

    def list_service_instance_upgrade_history_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryResponse:
        """
        @summary Queries the upgrade history of a service instance.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instance_upgrade_history_with_options_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryResponse:
        """
        @summary Queries the upgrade history of a service instance.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instance_upgrade_history(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryResponse:
        """
        @summary Queries the upgrade history of a service instance.
        
        @param request: ListServiceInstanceUpgradeHistoryRequest
        @return: ListServiceInstanceUpgradeHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instance_upgrade_history_with_options(request, runtime)

    async def list_service_instance_upgrade_history_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryRequest,
    ) -> compute_nest_20210601_models.ListServiceInstanceUpgradeHistoryResponse:
        """
        @summary Queries the upgrade history of a service instance.
        
        @param request: ListServiceInstanceUpgradeHistoryRequest
        @return: ListServiceInstanceUpgradeHistoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_upgrade_history_with_options_async(request, runtime)

    def list_service_instances_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstancesResponse:
        """
        @summary {}
        
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_instances_with_options_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstancesResponse:
        """
        @summary {}
        
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceInstances',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_instances(
        self,
        request: compute_nest_20210601_models.ListServiceInstancesRequest,
    ) -> compute_nest_20210601_models.ListServiceInstancesResponse:
        """
        @summary {}
        
        @param request: ListServiceInstancesRequest
        @return: ListServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_instances_with_options(request, runtime)

    async def list_service_instances_async(
        self,
        request: compute_nest_20210601_models.ListServiceInstancesRequest,
    ) -> compute_nest_20210601_models.ListServiceInstancesResponse:
        """
        @summary {}
        
        @param request: ListServiceInstancesRequest
        @return: ListServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instances_with_options_async(request, runtime)

    def list_service_usages_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceUsagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceUsagesResponse:
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceUsages',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceUsagesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_usages_with_options_async(
        self,
        request: compute_nest_20210601_models.ListServiceUsagesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceUsagesResponse:
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServiceUsages',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServiceUsagesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_usages(
        self,
        request: compute_nest_20210601_models.ListServiceUsagesRequest,
    ) -> compute_nest_20210601_models.ListServiceUsagesResponse:
        """
        @summary Queries the applications for using a service.
        
        @param request: ListServiceUsagesRequest
        @return: ListServiceUsagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_service_usages_with_options(request, runtime)

    async def list_service_usages_async(
        self,
        request: compute_nest_20210601_models.ListServiceUsagesRequest,
    ) -> compute_nest_20210601_models.ListServiceUsagesResponse:
        """
        @summary Queries the applications for using a service.
        
        @param request: ListServiceUsagesRequest
        @return: ListServiceUsagesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_usages_with_options_async(request, runtime)

    def list_services_with_options(
        self,
        request: compute_nest_20210601_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.fuzzy_keyword):
            query['FuzzyKeyword'] = request.fuzzy_keyword
        if not UtilClient.is_unset(request.in_used):
            query['InUsed'] = request.in_used
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_access_type):
            query['ServiceAccessType'] = request.service_access_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_services_with_options_async(
        self,
        request: compute_nest_20210601_models.ListServicesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServicesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.fuzzy_keyword):
            query['FuzzyKeyword'] = request.fuzzy_keyword
        if not UtilClient.is_unset(request.in_used):
            query['InUsed'] = request.in_used
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by_type):
            query['OrderByType'] = request.order_by_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_access_type):
            query['ServiceAccessType'] = request.service_access_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_services(
        self,
        request: compute_nest_20210601_models.ListServicesRequest,
    ) -> compute_nest_20210601_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    async def list_services_async(
        self,
        request: compute_nest_20210601_models.ListServicesRequest,
    ) -> compute_nest_20210601_models.ListServicesResponse:
        """
        @summary Queries a list of services.
        
        @param request: ListServicesRequest
        @return: ListServicesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_services_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: compute_nest_20210601_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListTagKeysResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: compute_nest_20210601_models.ListTagKeysRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListTagKeysResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: compute_nest_20210601_models.ListTagKeysRequest,
    ) -> compute_nest_20210601_models.ListTagKeysResponse:
        """
        @summary 查询标签键列表
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: compute_nest_20210601_models.ListTagKeysRequest,
    ) -> compute_nest_20210601_models.ListTagKeysResponse:
        """
        @summary 查询标签键列表
        
        @param request: ListTagKeysRequest
        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: compute_nest_20210601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListTagResourcesResponse:
        """
        @summary 查询标签资源列表
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: compute_nest_20210601_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListTagResourcesResponse:
        """
        @summary 查询标签资源列表
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: compute_nest_20210601_models.ListTagResourcesRequest,
    ) -> compute_nest_20210601_models.ListTagResourcesResponse:
        """
        @summary 查询标签资源列表
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: compute_nest_20210601_models.ListTagResourcesRequest,
    ) -> compute_nest_20210601_models.ListTagResourcesResponse:
        """
        @summary 查询标签资源列表
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: compute_nest_20210601_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListTagValuesResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: compute_nest_20210601_models.ListTagValuesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListTagValuesResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: compute_nest_20210601_models.ListTagValuesRequest,
    ) -> compute_nest_20210601_models.ListTagValuesResponse:
        """
        @summary 查询标签值列表
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: compute_nest_20210601_models.ListTagValuesRequest,
    ) -> compute_nest_20210601_models.ListTagValuesResponse:
        """
        @summary 查询标签值列表
        
        @param request: ListTagValuesRequest
        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def renew_service_instance_resources_with_options(
        self,
        request: compute_nest_20210601_models.RenewServiceInstanceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.RenewServiceInstanceResourcesResponse:
        """
        @summary Renew the prepaid resources included in the private deployment service instance. You can renew all prepaid resources under the specified service instance ID, or you can renew the specified resources. Only one of the two renewal methods can be used.
        
        @param request: RenewServiceInstanceResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewServiceInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_period):
            query['ResourcePeriod'] = request.resource_period
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewServiceInstanceResources',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.RenewServiceInstanceResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def renew_service_instance_resources_with_options_async(
        self,
        request: compute_nest_20210601_models.RenewServiceInstanceResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.RenewServiceInstanceResourcesResponse:
        """
        @summary Renew the prepaid resources included in the private deployment service instance. You can renew all prepaid resources under the specified service instance ID, or you can renew the specified resources. Only one of the two renewal methods can be used.
        
        @param request: RenewServiceInstanceResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: RenewServiceInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_period):
            query['ResourcePeriod'] = request.resource_period
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RenewServiceInstanceResources',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.RenewServiceInstanceResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def renew_service_instance_resources(
        self,
        request: compute_nest_20210601_models.RenewServiceInstanceResourcesRequest,
    ) -> compute_nest_20210601_models.RenewServiceInstanceResourcesResponse:
        """
        @summary Renew the prepaid resources included in the private deployment service instance. You can renew all prepaid resources under the specified service instance ID, or you can renew the specified resources. Only one of the two renewal methods can be used.
        
        @param request: RenewServiceInstanceResourcesRequest
        @return: RenewServiceInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.renew_service_instance_resources_with_options(request, runtime)

    async def renew_service_instance_resources_async(
        self,
        request: compute_nest_20210601_models.RenewServiceInstanceResourcesRequest,
    ) -> compute_nest_20210601_models.RenewServiceInstanceResourcesResponse:
        """
        @summary Renew the prepaid resources included in the private deployment service instance. You can renew all prepaid resources under the specified service instance ID, or you can renew the specified resources. Only one of the two renewal methods can be used.
        
        @param request: RenewServiceInstanceResourcesRequest
        @return: RenewServiceInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.renew_service_instance_resources_with_options_async(request, runtime)

    def restart_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.RestartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.RestartServiceInstanceResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.RestartServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def restart_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.RestartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.RestartServiceInstanceResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.RestartServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def restart_service_instance(
        self,
        request: compute_nest_20210601_models.RestartServiceInstanceRequest,
    ) -> compute_nest_20210601_models.RestartServiceInstanceResponse:
        """
        @summary When the service instance is Deployed, call the RestartServiceInstance interface to restart the service instance.
        
        @param request: RestartServiceInstanceRequest
        @return: RestartServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.restart_service_instance_with_options(request, runtime)

    async def restart_service_instance_async(
        self,
        request: compute_nest_20210601_models.RestartServiceInstanceRequest,
    ) -> compute_nest_20210601_models.RestartServiceInstanceResponse:
        """
        @summary When the service instance is Deployed, call the RestartServiceInstance interface to restart the service instance.
        
        @param request: RestartServiceInstanceRequest
        @return: RestartServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_service_instance_with_options_async(request, runtime)

    def rollback_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.RollbackServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.RollbackServiceInstanceResponse:
        """
        @summary Rolls back an upgraded service instance to the previous version.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.RollbackServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.RollbackServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.RollbackServiceInstanceResponse:
        """
        @summary Rolls back an upgraded service instance to the previous version.
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.RollbackServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_service_instance(
        self,
        request: compute_nest_20210601_models.RollbackServiceInstanceRequest,
    ) -> compute_nest_20210601_models.RollbackServiceInstanceResponse:
        """
        @summary Rolls back an upgraded service instance to the previous version.
        
        @param request: RollbackServiceInstanceRequest
        @return: RollbackServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.rollback_service_instance_with_options(request, runtime)

    async def rollback_service_instance_async(
        self,
        request: compute_nest_20210601_models.RollbackServiceInstanceRequest,
    ) -> compute_nest_20210601_models.RollbackServiceInstanceResponse:
        """
        @summary Rolls back an upgraded service instance to the previous version.
        
        @param request: RollbackServiceInstanceRequest
        @return: RollbackServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.rollback_service_instance_with_options_async(request, runtime)

    def start_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.StartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.StartServiceInstanceResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.StartServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def start_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.StartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.StartServiceInstanceResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.StartServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def start_service_instance(
        self,
        request: compute_nest_20210601_models.StartServiceInstanceRequest,
    ) -> compute_nest_20210601_models.StartServiceInstanceResponse:
        """
        @summary When the service instance status is Stopped (Stopped) or StartFailed (Startup failed), the StartServiceInstance interface is invoked to start the service instance.
        
        @param request: StartServiceInstanceRequest
        @return: StartServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_service_instance_with_options(request, runtime)

    async def start_service_instance_async(
        self,
        request: compute_nest_20210601_models.StartServiceInstanceRequest,
    ) -> compute_nest_20210601_models.StartServiceInstanceResponse:
        """
        @summary When the service instance status is Stopped (Stopped) or StartFailed (Startup failed), the StartServiceInstance interface is invoked to start the service instance.
        
        @param request: StartServiceInstanceRequest
        @return: StartServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.start_service_instance_with_options_async(request, runtime)

    def stop_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.StopServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.StopServiceInstanceResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.StopServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_service_instance_with_options_async(
        self,
        request: compute_nest_20210601_models.StopServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.StopServiceInstanceResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.StopServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_service_instance(
        self,
        request: compute_nest_20210601_models.StopServiceInstanceRequest,
    ) -> compute_nest_20210601_models.StopServiceInstanceResponse:
        """
        @summary When the service instance is Deployed and StopFailed, call the StopServiceInstance interface to stop the service instance.
        
        @param request: StopServiceInstanceRequest
        @return: StopServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_service_instance_with_options(request, runtime)

    async def stop_service_instance_async(
        self,
        request: compute_nest_20210601_models.StopServiceInstanceRequest,
    ) -> compute_nest_20210601_models.StopServiceInstanceResponse:
        """
        @summary When the service instance is Deployed and StopFailed, call the StopServiceInstance interface to stop the service instance.
        
        @param request: StopServiceInstanceRequest
        @return: StopServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_service_instance_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: compute_nest_20210601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.TagResourcesResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: compute_nest_20210601_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.TagResourcesResponse:
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: compute_nest_20210601_models.TagResourcesRequest,
    ) -> compute_nest_20210601_models.TagResourcesResponse:
        """
        @summary 给资源打标签
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: compute_nest_20210601_models.TagResourcesRequest,
    ) -> compute_nest_20210601_models.TagResourcesResponse:
        """
        @summary 给资源打标签
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def un_tag_resources_with_options(
        self,
        request: compute_nest_20210601_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UnTagResourcesResponse:
        """
        @summary 给资源解除标签
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UnTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def un_tag_resources_with_options_async(
        self,
        request: compute_nest_20210601_models.UnTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UnTagResourcesResponse:
        """
        @summary 给资源解除标签
        
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UnTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def un_tag_resources(
        self,
        request: compute_nest_20210601_models.UnTagResourcesRequest,
    ) -> compute_nest_20210601_models.UnTagResourcesResponse:
        """
        @summary 给资源解除标签
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.un_tag_resources_with_options(request, runtime)

    async def un_tag_resources_async(
        self,
        request: compute_nest_20210601_models.UnTagResourcesRequest,
    ) -> compute_nest_20210601_models.UnTagResourcesResponse:
        """
        @summary 给资源解除标签
        
        @param request: UnTagResourcesRequest
        @return: UnTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.un_tag_resources_with_options_async(request, runtime)

    def update_service_instance_attributes_with_options(
        self,
        request: compute_nest_20210601_models.UpdateServiceInstanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpdateServiceInstanceAttributesResponse:
        """
        @summary Updates the attributes of a service instance.
        
        @param request: UpdateServiceInstanceAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_operation):
            query['EnableOperation'] = request.enable_operation
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceInstanceAttributes',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpdateServiceInstanceAttributesResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_instance_attributes_with_options_async(
        self,
        request: compute_nest_20210601_models.UpdateServiceInstanceAttributesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpdateServiceInstanceAttributesResponse:
        """
        @summary Updates the attributes of a service instance.
        
        @param request: UpdateServiceInstanceAttributesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceAttributesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_operation):
            query['EnableOperation'] = request.enable_operation
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.service_instance_id):
            query['ServiceInstanceId'] = request.service_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceInstanceAttributes',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpdateServiceInstanceAttributesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_instance_attributes(
        self,
        request: compute_nest_20210601_models.UpdateServiceInstanceAttributesRequest,
    ) -> compute_nest_20210601_models.UpdateServiceInstanceAttributesResponse:
        """
        @summary Updates the attributes of a service instance.
        
        @param request: UpdateServiceInstanceAttributesRequest
        @return: UpdateServiceInstanceAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_instance_attributes_with_options(request, runtime)

    async def update_service_instance_attributes_async(
        self,
        request: compute_nest_20210601_models.UpdateServiceInstanceAttributesRequest,
    ) -> compute_nest_20210601_models.UpdateServiceInstanceAttributesResponse:
        """
        @summary Updates the attributes of a service instance.
        
        @param request: UpdateServiceInstanceAttributesRequest
        @return: UpdateServiceInstanceAttributesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_instance_attributes_with_options_async(request, runtime)

    def update_service_instance_spec_with_options(
        self,
        tmp_req: compute_nest_20210601_models.UpdateServiceInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpdateServiceInstanceSpecResponse:
        """
        @summary Changes the configurations of a service instance.
        
        @description ### [](#)Prerequisites
        Configuration change is enabled and the related parameters are configured for the service by the service provider.
        
        @param tmp_req: UpdateServiceInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceSpecResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.UpdateServiceInstanceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpdateServiceInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_instance_spec_with_options_async(
        self,
        tmp_req: compute_nest_20210601_models.UpdateServiceInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpdateServiceInstanceSpecResponse:
        """
        @summary Changes the configurations of a service instance.
        
        @description ### [](#)Prerequisites
        Configuration change is enabled and the related parameters are configured for the service by the service provider.
        
        @param tmp_req: UpdateServiceInstanceSpecRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceInstanceSpecResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.UpdateServiceInstanceSpecShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.parameters):
            request.parameters_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.commodity):
            query['Commodity'] = request.commodity
        if not UtilClient.is_unset(request.dry_run):
            query['DryRun'] = request.dry_run
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpdateServiceInstanceSpecResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_instance_spec(
        self,
        request: compute_nest_20210601_models.UpdateServiceInstanceSpecRequest,
    ) -> compute_nest_20210601_models.UpdateServiceInstanceSpecResponse:
        """
        @summary Changes the configurations of a service instance.
        
        @description ### [](#)Prerequisites
        Configuration change is enabled and the related parameters are configured for the service by the service provider.
        
        @param request: UpdateServiceInstanceSpecRequest
        @return: UpdateServiceInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_instance_spec_with_options(request, runtime)

    async def update_service_instance_spec_async(
        self,
        request: compute_nest_20210601_models.UpdateServiceInstanceSpecRequest,
    ) -> compute_nest_20210601_models.UpdateServiceInstanceSpecResponse:
        """
        @summary Changes the configurations of a service instance.
        
        @description ### [](#)Prerequisites
        Configuration change is enabled and the related parameters are configured for the service by the service provider.
        
        @param request: UpdateServiceInstanceSpecRequest
        @return: UpdateServiceInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_instance_spec_with_options_async(request, runtime)

    def update_service_usage_with_options(
        self,
        tmp_req: compute_nest_20210601_models.UpdateServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpdateServiceUsageResponse:
        """
        @summary Updates the application for using a service.
        
        @param tmp_req: UpdateServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceUsageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.UpdateServiceUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_information):
            request.user_information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_information, 'UserInformation', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_information_shrink):
            query['UserInformation'] = request.user_information_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceUsage',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpdateServiceUsageResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_service_usage_with_options_async(
        self,
        tmp_req: compute_nest_20210601_models.UpdateServiceUsageRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpdateServiceUsageResponse:
        """
        @summary Updates the application for using a service.
        
        @param tmp_req: UpdateServiceUsageRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateServiceUsageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.UpdateServiceUsageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_information):
            request.user_information_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_information, 'UserInformation', 'json')
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        if not UtilClient.is_unset(request.user_information_shrink):
            query['UserInformation'] = request.user_information_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateServiceUsage',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpdateServiceUsageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_service_usage(
        self,
        request: compute_nest_20210601_models.UpdateServiceUsageRequest,
    ) -> compute_nest_20210601_models.UpdateServiceUsageResponse:
        """
        @summary Updates the application for using a service.
        
        @param request: UpdateServiceUsageRequest
        @return: UpdateServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_service_usage_with_options(request, runtime)

    async def update_service_usage_async(
        self,
        request: compute_nest_20210601_models.UpdateServiceUsageRequest,
    ) -> compute_nest_20210601_models.UpdateServiceUsageResponse:
        """
        @summary Updates the application for using a service.
        
        @param request: UpdateServiceUsageRequest
        @return: UpdateServiceUsageResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_usage_with_options_async(request, runtime)

    def update_user_information_with_options(
        self,
        request: compute_nest_20210601_models.UpdateUserInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpdateUserInformationResponse:
        """
        @summary Updates the information about a customer.
        
        @param request: UpdateUserInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserInformationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_settings):
            query['DeliverySettings'] = request.delivery_settings
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserInformation',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpdateUserInformationResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_user_information_with_options_async(
        self,
        request: compute_nest_20210601_models.UpdateUserInformationRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpdateUserInformationResponse:
        """
        @summary Updates the information about a customer.
        
        @param request: UpdateUserInformationRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateUserInformationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delivery_settings):
            query['DeliverySettings'] = request.delivery_settings
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateUserInformation',
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpdateUserInformationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_user_information(
        self,
        request: compute_nest_20210601_models.UpdateUserInformationRequest,
    ) -> compute_nest_20210601_models.UpdateUserInformationResponse:
        """
        @summary Updates the information about a customer.
        
        @param request: UpdateUserInformationRequest
        @return: UpdateUserInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_user_information_with_options(request, runtime)

    async def update_user_information_async(
        self,
        request: compute_nest_20210601_models.UpdateUserInformationRequest,
    ) -> compute_nest_20210601_models.UpdateUserInformationResponse:
        """
        @summary Updates the information about a customer.
        
        @param request: UpdateUserInformationRequest
        @return: UpdateUserInformationResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_user_information_with_options_async(request, runtime)

    def upgrade_service_instance_with_options(
        self,
        tmp_req: compute_nest_20210601_models.UpgradeServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpgradeServiceInstanceResponse:
        """
        @summary Upgrades the version of a service instance.
        
        @param tmp_req: UpgradeServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeServiceInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.UpgradeServiceInstanceShrinkRequest()
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpgradeServiceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    async def upgrade_service_instance_with_options_async(
        self,
        tmp_req: compute_nest_20210601_models.UpgradeServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpgradeServiceInstanceResponse:
        """
        @summary Upgrades the version of a service instance.
        
        @param tmp_req: UpgradeServiceInstanceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpgradeServiceInstanceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = compute_nest_20210601_models.UpgradeServiceInstanceShrinkRequest()
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
            version='2021-06-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            compute_nest_20210601_models.UpgradeServiceInstanceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upgrade_service_instance(
        self,
        request: compute_nest_20210601_models.UpgradeServiceInstanceRequest,
    ) -> compute_nest_20210601_models.UpgradeServiceInstanceResponse:
        """
        @summary Upgrades the version of a service instance.
        
        @param request: UpgradeServiceInstanceRequest
        @return: UpgradeServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upgrade_service_instance_with_options(request, runtime)

    async def upgrade_service_instance_async(
        self,
        request: compute_nest_20210601_models.UpgradeServiceInstanceRequest,
    ) -> compute_nest_20210601_models.UpgradeServiceInstanceResponse:
        """
        @summary Upgrades the version of a service instance.
        
        @param request: UpgradeServiceInstanceRequest
        @return: UpgradeServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.upgrade_service_instance_with_options_async(request, runtime)
