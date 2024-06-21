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

    def change_resource_group_with_options(
        self,
        request: compute_nest_20210601_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ChangeResourceGroupResponse:
        """
        @summary 资源组转组
        
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
        @summary 资源组转组
        
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
        @summary 资源组转组
        
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
        @summary 资源组转组
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def continue_deploy_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.ContinueDeployServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ContinueDeployServiceInstanceResponse:
        """
        @summary 继续部署服务实例
        
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
        @summary 继续部署服务实例
        
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
        @summary 继续部署服务实例
        
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
        @summary 继续部署服务实例
        
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
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
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
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
        @param request: CreateServiceInstanceRequest
        @return: CreateServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_service_instance_with_options_async(request, runtime)

    def delete_service_instances_with_options(
        self,
        request: compute_nest_20210601_models.DeleteServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.DeleteServiceInstancesResponse:
        """
        @summary 删除服务实例
        
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
        @summary 删除服务实例
        
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
        @summary 删除服务实例
        
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
        @summary 删除服务实例
        
        @param request: DeleteServiceInstancesRequest
        @return: DeleteServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_service_instances_with_options_async(request, runtime)

    def get_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.GetServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceInstanceResponse:
        """
        @summary 查询服务实例详情
        
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
        @summary 查询服务实例详情
        
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
        @summary 查询服务实例详情
        
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
        @summary 查询服务实例详情
        
        @param request: GetServiceInstanceRequest
        @return: GetServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_instance_with_options_async(request, runtime)

    def get_service_template_parameter_constraints_with_options(
        self,
        request: compute_nest_20210601_models.GetServiceTemplateParameterConstraintsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.GetServiceTemplateParameterConstraintsResponse:
        """
        @summary 获取ROS参数限制
        
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
        @summary 获取ROS参数限制
        
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
        @summary 获取ROS参数限制
        
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
        @summary 获取ROS参数限制
        
        @param request: GetServiceTemplateParameterConstraintsRequest
        @return: GetServiceTemplateParameterConstraintsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_service_template_parameter_constraints_with_options_async(request, runtime)

    def list_service_instance_logs_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceInstanceLogsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstanceLogsResponse:
        """
        @summary 查询服务实例部署升级以及应用日志
        
        @param request: ListServiceInstanceLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        @summary 查询服务实例部署升级以及应用日志
        
        @param request: ListServiceInstanceLogsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceLogsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
        @summary 查询服务实例部署升级以及应用日志
        
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
        @summary 查询服务实例部署升级以及应用日志
        
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
        @summary 展示实例资源
        
        @param request: ListServiceInstanceResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time_end):
            query['ExpireTimeEnd'] = request.expire_time_end
        if not UtilClient.is_unset(request.expire_time_start):
            query['ExpireTimeStart'] = request.expire_time_start
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
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
        @summary 展示实例资源
        
        @param request: ListServiceInstanceResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListServiceInstanceResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.expire_time_end):
            query['ExpireTimeEnd'] = request.expire_time_end
        if not UtilClient.is_unset(request.expire_time_start):
            query['ExpireTimeStart'] = request.expire_time_start
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_arn):
            query['ResourceARN'] = request.resource_arn
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
        @summary 展示实例资源
        
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
        @summary 展示实例资源
        
        @param request: ListServiceInstanceResourcesRequest
        @return: ListServiceInstanceResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instance_resources_with_options_async(request, runtime)

    def list_service_instances_with_options(
        self,
        request: compute_nest_20210601_models.ListServiceInstancesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.ListServiceInstancesResponse:
        """
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
        @param request: ListServiceInstancesRequest
        @return: ListServiceInstancesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_service_instances_with_options_async(request, runtime)

    def restart_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.RestartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.RestartServiceInstanceResponse:
        """
        @summary 重启服务实例
        
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
        @summary 重启服务实例
        
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
        @summary 重启服务实例
        
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
        @summary 重启服务实例
        
        @param request: RestartServiceInstanceRequest
        @return: RestartServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.restart_service_instance_with_options_async(request, runtime)

    def start_service_instance_with_options(
        self,
        request: compute_nest_20210601_models.StartServiceInstanceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.StartServiceInstanceResponse:
        """
        @summary 启动服务实例
        
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
        @summary 启动服务实例
        
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
        @summary 启动服务实例
        
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
        @summary 启动服务实例
        
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
        @summary 停止服务实例
        
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
        @summary 停止服务实例
        
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
        @summary 停止服务实例
        
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
        @summary 停止服务实例
        
        @param request: StopServiceInstanceRequest
        @return: StopServiceInstanceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_service_instance_with_options_async(request, runtime)

    def update_service_instance_spec_with_options(
        self,
        tmp_req: compute_nest_20210601_models.UpdateServiceInstanceSpecRequest,
        runtime: util_models.RuntimeOptions,
    ) -> compute_nest_20210601_models.UpdateServiceInstanceSpecResponse:
        """
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
        @param request: UpdateServiceInstanceSpecRequest
        @return: UpdateServiceInstanceSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_service_instance_spec_with_options_async(request, runtime)
