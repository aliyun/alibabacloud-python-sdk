# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eflo_cnp20230828 import models as eflo_cnp_20230828_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('eflo-cnp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
        request: eflo_cnp_20230828_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ChangeResourceGroupResponse:
        """
        @summary Change resource group
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def change_resource_group_with_options_async(
        self,
        request: eflo_cnp_20230828_models.ChangeResourceGroupRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ChangeResourceGroupResponse:
        """
        @summary Change resource group
        
        @param request: ChangeResourceGroupRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ChangeResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ChangeResourceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def change_resource_group(
        self,
        request: eflo_cnp_20230828_models.ChangeResourceGroupRequest,
    ) -> eflo_cnp_20230828_models.ChangeResourceGroupResponse:
        """
        @summary Change resource group
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    async def change_resource_group_async(
        self,
        request: eflo_cnp_20230828_models.ChangeResourceGroupRequest,
    ) -> eflo_cnp_20230828_models.ChangeResourceGroupResponse:
        """
        @summary Change resource group
        
        @param request: ChangeResourceGroupRequest
        @return: ChangeResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.change_resource_group_with_options_async(request, runtime)

    def create_experiment_plan_with_options(
        self,
        tmp_req: eflo_cnp_20230828_models.CreateExperimentPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.CreateExperimentPlanResponse:
        """
        @summary Create Experiment Plan
        
        @param tmp_req: CreateExperimentPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.CreateExperimentPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.external_params):
            request.external_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_params, 'ExternalParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.external_params_shrink):
            query['ExternalParams'] = request.external_params_shrink
        if not UtilClient.is_unset(request.plan_template_name):
            query['PlanTemplateName'] = request.plan_template_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateExperimentPlan',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.CreateExperimentPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_plan_with_options_async(
        self,
        tmp_req: eflo_cnp_20230828_models.CreateExperimentPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.CreateExperimentPlanResponse:
        """
        @summary Create Experiment Plan
        
        @param tmp_req: CreateExperimentPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentPlanResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.CreateExperimentPlanShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.external_params):
            request.external_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.external_params, 'ExternalParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.external_params_shrink):
            query['ExternalParams'] = request.external_params_shrink
        if not UtilClient.is_unset(request.plan_template_name):
            query['PlanTemplateName'] = request.plan_template_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateExperimentPlan',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.CreateExperimentPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment_plan(
        self,
        request: eflo_cnp_20230828_models.CreateExperimentPlanRequest,
    ) -> eflo_cnp_20230828_models.CreateExperimentPlanResponse:
        """
        @summary Create Experiment Plan
        
        @param request: CreateExperimentPlanRequest
        @return: CreateExperimentPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_experiment_plan_with_options(request, runtime)

    async def create_experiment_plan_async(
        self,
        request: eflo_cnp_20230828_models.CreateExperimentPlanRequest,
    ) -> eflo_cnp_20230828_models.CreateExperimentPlanResponse:
        """
        @summary Create Experiment Plan
        
        @param request: CreateExperimentPlanRequest
        @return: CreateExperimentPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_experiment_plan_with_options_async(request, runtime)

    def create_experiment_plan_template_with_options(
        self,
        tmp_req: eflo_cnp_20230828_models.CreateExperimentPlanTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.CreateExperimentPlanTemplateResponse:
        """
        @summary Create/Update Test Plan Template
        
        @param tmp_req: CreateExperimentPlanTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentPlanTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.CreateExperimentPlanTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_pipeline):
            request.template_pipeline_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_pipeline, 'TemplatePipeline', 'json')
        query = {}
        if not UtilClient.is_unset(request.privacy_level):
            query['PrivacyLevel'] = request.privacy_level
        if not UtilClient.is_unset(request.template_description):
            query['TemplateDescription'] = request.template_description
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        body = {}
        if not UtilClient.is_unset(request.template_pipeline_shrink):
            body['TemplatePipeline'] = request.template_pipeline_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperimentPlanTemplate',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.CreateExperimentPlanTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_experiment_plan_template_with_options_async(
        self,
        tmp_req: eflo_cnp_20230828_models.CreateExperimentPlanTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.CreateExperimentPlanTemplateResponse:
        """
        @summary Create/Update Test Plan Template
        
        @param tmp_req: CreateExperimentPlanTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateExperimentPlanTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.CreateExperimentPlanTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_pipeline):
            request.template_pipeline_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_pipeline, 'TemplatePipeline', 'json')
        query = {}
        if not UtilClient.is_unset(request.privacy_level):
            query['PrivacyLevel'] = request.privacy_level
        if not UtilClient.is_unset(request.template_description):
            query['TemplateDescription'] = request.template_description
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_name):
            query['TemplateName'] = request.template_name
        body = {}
        if not UtilClient.is_unset(request.template_pipeline_shrink):
            body['TemplatePipeline'] = request.template_pipeline_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateExperimentPlanTemplate',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.CreateExperimentPlanTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_experiment_plan_template(
        self,
        request: eflo_cnp_20230828_models.CreateExperimentPlanTemplateRequest,
    ) -> eflo_cnp_20230828_models.CreateExperimentPlanTemplateResponse:
        """
        @summary Create/Update Test Plan Template
        
        @param request: CreateExperimentPlanTemplateRequest
        @return: CreateExperimentPlanTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_experiment_plan_template_with_options(request, runtime)

    async def create_experiment_plan_template_async(
        self,
        request: eflo_cnp_20230828_models.CreateExperimentPlanTemplateRequest,
    ) -> eflo_cnp_20230828_models.CreateExperimentPlanTemplateResponse:
        """
        @summary Create/Update Test Plan Template
        
        @param request: CreateExperimentPlanTemplateRequest
        @return: CreateExperimentPlanTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_experiment_plan_template_with_options_async(request, runtime)

    def create_resource_with_options(
        self,
        tmp_req: eflo_cnp_20230828_models.CreateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.CreateResourceResponse:
        """
        @summary Create Evaluation Resource
        
        @param tmp_req: CreateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.CreateResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.machine_types):
            request.machine_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.machine_types, 'MachineTypes', 'json')
        if not UtilClient.is_unset(tmp_req.user_access_param):
            request.user_access_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_access_param, 'UserAccessParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_desc):
            query['ClusterDesc'] = request.cluster_desc
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        body = {}
        if not UtilClient.is_unset(request.machine_types_shrink):
            body['MachineTypes'] = request.machine_types_shrink
        if not UtilClient.is_unset(request.user_access_param_shrink):
            body['UserAccessParam'] = request.user_access_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        tmp_req: eflo_cnp_20230828_models.CreateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.CreateResourceResponse:
        """
        @summary Create Evaluation Resource
        
        @param tmp_req: CreateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: CreateResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.CreateResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.machine_types):
            request.machine_types_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.machine_types, 'MachineTypes', 'json')
        if not UtilClient.is_unset(tmp_req.user_access_param):
            request.user_access_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_access_param, 'UserAccessParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_desc):
            query['ClusterDesc'] = request.cluster_desc
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        body = {}
        if not UtilClient.is_unset(request.machine_types_shrink):
            body['MachineTypes'] = request.machine_types_shrink
        if not UtilClient.is_unset(request.user_access_param_shrink):
            body['UserAccessParam'] = request.user_access_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateResource',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: eflo_cnp_20230828_models.CreateResourceRequest,
    ) -> eflo_cnp_20230828_models.CreateResourceResponse:
        """
        @summary Create Evaluation Resource
        
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_with_options(request, runtime)

    async def create_resource_async(
        self,
        request: eflo_cnp_20230828_models.CreateResourceRequest,
    ) -> eflo_cnp_20230828_models.CreateResourceResponse:
        """
        @summary Create Evaluation Resource
        
        @param request: CreateResourceRequest
        @return: CreateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.create_resource_with_options_async(request, runtime)

    def delete_experiment_with_options(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.DeleteExperimentResponse:
        """
        @summary Delete Experiment
        
        @param request: DeleteExperimentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.DeleteExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_with_options_async(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.DeleteExperimentResponse:
        """
        @summary Delete Experiment
        
        @param request: DeleteExperimentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperiment',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.DeleteExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentRequest,
    ) -> eflo_cnp_20230828_models.DeleteExperimentResponse:
        """
        @summary Delete Experiment
        
        @param request: DeleteExperimentRequest
        @return: DeleteExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_experiment_with_options(request, runtime)

    async def delete_experiment_async(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentRequest,
    ) -> eflo_cnp_20230828_models.DeleteExperimentResponse:
        """
        @summary Delete Experiment
        
        @param request: DeleteExperimentRequest
        @return: DeleteExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_experiment_with_options_async(request, runtime)

    def delete_experiment_plan_with_options(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.DeleteExperimentPlanResponse:
        """
        @summary 获取实验计划详情
        
        @param request: DeleteExperimentPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperimentPlan',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.DeleteExperimentPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_plan_with_options_async(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.DeleteExperimentPlanResponse:
        """
        @summary 获取实验计划详情
        
        @param request: DeleteExperimentPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperimentPlan',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.DeleteExperimentPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment_plan(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentPlanRequest,
    ) -> eflo_cnp_20230828_models.DeleteExperimentPlanResponse:
        """
        @summary 获取实验计划详情
        
        @param request: DeleteExperimentPlanRequest
        @return: DeleteExperimentPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_experiment_plan_with_options(request, runtime)

    async def delete_experiment_plan_async(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentPlanRequest,
    ) -> eflo_cnp_20230828_models.DeleteExperimentPlanResponse:
        """
        @summary 获取实验计划详情
        
        @param request: DeleteExperimentPlanRequest
        @return: DeleteExperimentPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_experiment_plan_with_options_async(request, runtime)

    def delete_experiment_plan_template_with_options(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentPlanTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.DeleteExperimentPlanTemplateResponse:
        """
        @summary Delete Test Plan Template
        
        @param request: DeleteExperimentPlanTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentPlanTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperimentPlanTemplate',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.DeleteExperimentPlanTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_experiment_plan_template_with_options_async(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentPlanTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.DeleteExperimentPlanTemplateResponse:
        """
        @summary Delete Test Plan Template
        
        @param request: DeleteExperimentPlanTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: DeleteExperimentPlanTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteExperimentPlanTemplate',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.DeleteExperimentPlanTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_experiment_plan_template(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentPlanTemplateRequest,
    ) -> eflo_cnp_20230828_models.DeleteExperimentPlanTemplateResponse:
        """
        @summary Delete Test Plan Template
        
        @param request: DeleteExperimentPlanTemplateRequest
        @return: DeleteExperimentPlanTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_experiment_plan_template_with_options(request, runtime)

    async def delete_experiment_plan_template_async(
        self,
        request: eflo_cnp_20230828_models.DeleteExperimentPlanTemplateRequest,
    ) -> eflo_cnp_20230828_models.DeleteExperimentPlanTemplateResponse:
        """
        @summary Delete Test Plan Template
        
        @param request: DeleteExperimentPlanTemplateRequest
        @return: DeleteExperimentPlanTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.delete_experiment_plan_template_with_options_async(request, runtime)

    def get_experiment_with_options(
        self,
        request: eflo_cnp_20230828_models.GetExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetExperimentResponse:
        """
        @summary Get Experiment Details
        
        @param request: GetExperimentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperiment',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_with_options_async(
        self,
        request: eflo_cnp_20230828_models.GetExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetExperimentResponse:
        """
        @summary Get Experiment Details
        
        @param request: GetExperimentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperiment',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment(
        self,
        request: eflo_cnp_20230828_models.GetExperimentRequest,
    ) -> eflo_cnp_20230828_models.GetExperimentResponse:
        """
        @summary Get Experiment Details
        
        @param request: GetExperimentRequest
        @return: GetExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_experiment_with_options(request, runtime)

    async def get_experiment_async(
        self,
        request: eflo_cnp_20230828_models.GetExperimentRequest,
    ) -> eflo_cnp_20230828_models.GetExperimentResponse:
        """
        @summary Get Experiment Details
        
        @param request: GetExperimentRequest
        @return: GetExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_experiment_with_options_async(request, runtime)

    def get_experiment_plan_with_options(
        self,
        request: eflo_cnp_20230828_models.GetExperimentPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetExperimentPlanResponse:
        """
        @summary Get Experiment Plan Details
        
        @param request: GetExperimentPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperimentPlan',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetExperimentPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_plan_with_options_async(
        self,
        request: eflo_cnp_20230828_models.GetExperimentPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetExperimentPlanResponse:
        """
        @summary Get Experiment Plan Details
        
        @param request: GetExperimentPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperimentPlan',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetExperimentPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment_plan(
        self,
        request: eflo_cnp_20230828_models.GetExperimentPlanRequest,
    ) -> eflo_cnp_20230828_models.GetExperimentPlanResponse:
        """
        @summary Get Experiment Plan Details
        
        @param request: GetExperimentPlanRequest
        @return: GetExperimentPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_experiment_plan_with_options(request, runtime)

    async def get_experiment_plan_async(
        self,
        request: eflo_cnp_20230828_models.GetExperimentPlanRequest,
    ) -> eflo_cnp_20230828_models.GetExperimentPlanResponse:
        """
        @summary Get Experiment Plan Details
        
        @param request: GetExperimentPlanRequest
        @return: GetExperimentPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_experiment_plan_with_options_async(request, runtime)

    def get_experiment_plan_template_with_options(
        self,
        request: eflo_cnp_20230828_models.GetExperimentPlanTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetExperimentPlanTemplateResponse:
        """
        @summary Query Test Plan Template Details
        
        @param request: GetExperimentPlanTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentPlanTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperimentPlanTemplate',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetExperimentPlanTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_plan_template_with_options_async(
        self,
        request: eflo_cnp_20230828_models.GetExperimentPlanTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetExperimentPlanTemplateResponse:
        """
        @summary Query Test Plan Template Details
        
        @param request: GetExperimentPlanTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentPlanTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperimentPlanTemplate',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetExperimentPlanTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment_plan_template(
        self,
        request: eflo_cnp_20230828_models.GetExperimentPlanTemplateRequest,
    ) -> eflo_cnp_20230828_models.GetExperimentPlanTemplateResponse:
        """
        @summary Query Test Plan Template Details
        
        @param request: GetExperimentPlanTemplateRequest
        @return: GetExperimentPlanTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_experiment_plan_template_with_options(request, runtime)

    async def get_experiment_plan_template_async(
        self,
        request: eflo_cnp_20230828_models.GetExperimentPlanTemplateRequest,
    ) -> eflo_cnp_20230828_models.GetExperimentPlanTemplateResponse:
        """
        @summary Query Test Plan Template Details
        
        @param request: GetExperimentPlanTemplateRequest
        @return: GetExperimentPlanTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_experiment_plan_template_with_options_async(request, runtime)

    def get_experiment_result_data_with_options(
        self,
        request: eflo_cnp_20230828_models.GetExperimentResultDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetExperimentResultDataResponse:
        """
        @summary Fetch Experiment Result Data
        
        @param request: GetExperimentResultDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResultDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.hostname):
            query['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.workload_type):
            query['WorkloadType'] = request.workload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperimentResultData',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetExperimentResultDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_experiment_result_data_with_options_async(
        self,
        request: eflo_cnp_20230828_models.GetExperimentResultDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetExperimentResultDataResponse:
        """
        @summary Fetch Experiment Result Data
        
        @param request: GetExperimentResultDataRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetExperimentResultDataResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.hostname):
            query['Hostname'] = request.hostname
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.workload_type):
            query['WorkloadType'] = request.workload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExperimentResultData',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetExperimentResultDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_experiment_result_data(
        self,
        request: eflo_cnp_20230828_models.GetExperimentResultDataRequest,
    ) -> eflo_cnp_20230828_models.GetExperimentResultDataResponse:
        """
        @summary Fetch Experiment Result Data
        
        @param request: GetExperimentResultDataRequest
        @return: GetExperimentResultDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_experiment_result_data_with_options(request, runtime)

    async def get_experiment_result_data_async(
        self,
        request: eflo_cnp_20230828_models.GetExperimentResultDataRequest,
    ) -> eflo_cnp_20230828_models.GetExperimentResultDataResponse:
        """
        @summary Fetch Experiment Result Data
        
        @param request: GetExperimentResultDataRequest
        @return: GetExperimentResultDataResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_experiment_result_data_with_options_async(request, runtime)

    def get_resource_with_options(
        self,
        request: eflo_cnp_20230828_models.GetResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetResourceResponse:
        """
        @summary Get Resource Information
        
        @param request: GetResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        request: eflo_cnp_20230828_models.GetResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetResourceResponse:
        """
        @summary Get Resource Information
        
        @param request: GetResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResource',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource(
        self,
        request: eflo_cnp_20230828_models.GetResourceRequest,
    ) -> eflo_cnp_20230828_models.GetResourceResponse:
        """
        @summary Get Resource Information
        
        @param request: GetResourceRequest
        @return: GetResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_with_options(request, runtime)

    async def get_resource_async(
        self,
        request: eflo_cnp_20230828_models.GetResourceRequest,
    ) -> eflo_cnp_20230828_models.GetResourceResponse:
        """
        @summary Get Resource Information
        
        @param request: GetResourceRequest
        @return: GetResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_with_options_async(request, runtime)

    def get_resource_predict_result_with_options(
        self,
        request: eflo_cnp_20230828_models.GetResourcePredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetResourcePredictResultResponse:
        """
        @summary Query the resource prediction results of the test plan template
        
        @param request: GetResourcePredictResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcePredictResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourcePredictResult',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetResourcePredictResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_predict_result_with_options_async(
        self,
        request: eflo_cnp_20230828_models.GetResourcePredictResultRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetResourcePredictResultResponse:
        """
        @summary Query the resource prediction results of the test plan template
        
        @param request: GetResourcePredictResultRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetResourcePredictResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourcePredictResult',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetResourcePredictResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_predict_result(
        self,
        request: eflo_cnp_20230828_models.GetResourcePredictResultRequest,
    ) -> eflo_cnp_20230828_models.GetResourcePredictResultResponse:
        """
        @summary Query the resource prediction results of the test plan template
        
        @param request: GetResourcePredictResultRequest
        @return: GetResourcePredictResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_predict_result_with_options(request, runtime)

    async def get_resource_predict_result_async(
        self,
        request: eflo_cnp_20230828_models.GetResourcePredictResultRequest,
    ) -> eflo_cnp_20230828_models.GetResourcePredictResultResponse:
        """
        @summary Query the resource prediction results of the test plan template
        
        @param request: GetResourcePredictResultRequest
        @return: GetResourcePredictResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_resource_predict_result_with_options_async(request, runtime)

    def get_workload_with_options(
        self,
        request: eflo_cnp_20230828_models.GetWorkloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetWorkloadResponse:
        """
        @summary Retrieve workload information by ID
        
        @param request: GetWorkloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workload_id):
            query['WorkloadId'] = request.workload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkload',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetWorkloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_workload_with_options_async(
        self,
        request: eflo_cnp_20230828_models.GetWorkloadRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.GetWorkloadResponse:
        """
        @summary Retrieve workload information by ID
        
        @param request: GetWorkloadRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetWorkloadResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.workload_id):
            query['WorkloadId'] = request.workload_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWorkload',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.GetWorkloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_workload(
        self,
        request: eflo_cnp_20230828_models.GetWorkloadRequest,
    ) -> eflo_cnp_20230828_models.GetWorkloadResponse:
        """
        @summary Retrieve workload information by ID
        
        @param request: GetWorkloadRequest
        @return: GetWorkloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_workload_with_options(request, runtime)

    async def get_workload_async(
        self,
        request: eflo_cnp_20230828_models.GetWorkloadRequest,
    ) -> eflo_cnp_20230828_models.GetWorkloadResponse:
        """
        @summary Retrieve workload information by ID
        
        @param request: GetWorkloadRequest
        @return: GetWorkloadResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.get_workload_with_options_async(request, runtime)

    def list_experiment_plan_templates_with_options(
        self,
        request: eflo_cnp_20230828_models.ListExperimentPlanTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListExperimentPlanTemplatesResponse:
        """
        @summary Query Test Plan Template List
        
        @param request: ListExperimentPlanTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentPlanTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.privacy_level):
            query['PrivacyLevel'] = request.privacy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperimentPlanTemplates',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListExperimentPlanTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiment_plan_templates_with_options_async(
        self,
        request: eflo_cnp_20230828_models.ListExperimentPlanTemplatesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListExperimentPlanTemplatesResponse:
        """
        @summary Query Test Plan Template List
        
        @param request: ListExperimentPlanTemplatesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentPlanTemplatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.privacy_level):
            query['PrivacyLevel'] = request.privacy_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperimentPlanTemplates',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListExperimentPlanTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiment_plan_templates(
        self,
        request: eflo_cnp_20230828_models.ListExperimentPlanTemplatesRequest,
    ) -> eflo_cnp_20230828_models.ListExperimentPlanTemplatesResponse:
        """
        @summary Query Test Plan Template List
        
        @param request: ListExperimentPlanTemplatesRequest
        @return: ListExperimentPlanTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_experiment_plan_templates_with_options(request, runtime)

    async def list_experiment_plan_templates_async(
        self,
        request: eflo_cnp_20230828_models.ListExperimentPlanTemplatesRequest,
    ) -> eflo_cnp_20230828_models.ListExperimentPlanTemplatesResponse:
        """
        @summary Query Test Plan Template List
        
        @param request: ListExperimentPlanTemplatesRequest
        @return: ListExperimentPlanTemplatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_experiment_plan_templates_with_options_async(request, runtime)

    def list_experiment_plans_with_options(
        self,
        tmp_req: eflo_cnp_20230828_models.ListExperimentPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListExperimentPlansResponse:
        """
        @summary Query Experiment Plan List
        
        @param tmp_req: ListExperimentPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentPlansResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.ListExperimentPlansShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.plan_task_status):
            request.plan_task_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.plan_task_status, 'PlanTaskStatus', 'json')
        if not UtilClient.is_unset(tmp_req.resource_name):
            request.resource_name_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_name, 'ResourceName', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.creat_time_order):
            query['CreatTimeOrder'] = request.creat_time_order
        if not UtilClient.is_unset(request.end_time_order):
            query['EndTimeOrder'] = request.end_time_order
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time_order):
            query['StartTimeOrder'] = request.start_time_order
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not UtilClient.is_unset(request.plan_task_status_shrink):
            body['PlanTaskStatus'] = request.plan_task_status_shrink
        if not UtilClient.is_unset(request.resource_name_shrink):
            body['ResourceName'] = request.resource_name_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListExperimentPlans',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListExperimentPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiment_plans_with_options_async(
        self,
        tmp_req: eflo_cnp_20230828_models.ListExperimentPlansRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListExperimentPlansResponse:
        """
        @summary Query Experiment Plan List
        
        @param tmp_req: ListExperimentPlansRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentPlansResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.ListExperimentPlansShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.plan_task_status):
            request.plan_task_status_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.plan_task_status, 'PlanTaskStatus', 'json')
        if not UtilClient.is_unset(tmp_req.resource_name):
            request.resource_name_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.resource_name, 'ResourceName', 'json')
        if not UtilClient.is_unset(tmp_req.tag):
            request.tag_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not UtilClient.is_unset(request.creat_time_order):
            query['CreatTimeOrder'] = request.creat_time_order
        if not UtilClient.is_unset(request.end_time_order):
            query['EndTimeOrder'] = request.end_time_order
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time_order):
            query['StartTimeOrder'] = request.start_time_order
        if not UtilClient.is_unset(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not UtilClient.is_unset(request.plan_task_status_shrink):
            body['PlanTaskStatus'] = request.plan_task_status_shrink
        if not UtilClient.is_unset(request.resource_name_shrink):
            body['ResourceName'] = request.resource_name_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListExperimentPlans',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListExperimentPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiment_plans(
        self,
        request: eflo_cnp_20230828_models.ListExperimentPlansRequest,
    ) -> eflo_cnp_20230828_models.ListExperimentPlansResponse:
        """
        @summary Query Experiment Plan List
        
        @param request: ListExperimentPlansRequest
        @return: ListExperimentPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_experiment_plans_with_options(request, runtime)

    async def list_experiment_plans_async(
        self,
        request: eflo_cnp_20230828_models.ListExperimentPlansRequest,
    ) -> eflo_cnp_20230828_models.ListExperimentPlansResponse:
        """
        @summary Query Experiment Plan List
        
        @param request: ListExperimentPlansRequest
        @return: ListExperimentPlansResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_experiment_plans_with_options_async(request, runtime)

    def list_experiments_with_options(
        self,
        request: eflo_cnp_20230828_models.ListExperimentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListExperimentsResponse:
        """
        @summary Query the experiment list based on the plan ID
        
        @param request: ListExperimentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListExperimentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_experiments_with_options_async(
        self,
        request: eflo_cnp_20230828_models.ListExperimentsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListExperimentsResponse:
        """
        @summary Query the experiment list based on the plan ID
        
        @param request: ListExperimentsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListExperimentsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListExperiments',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListExperimentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_experiments(
        self,
        request: eflo_cnp_20230828_models.ListExperimentsRequest,
    ) -> eflo_cnp_20230828_models.ListExperimentsResponse:
        """
        @summary Query the experiment list based on the plan ID
        
        @param request: ListExperimentsRequest
        @return: ListExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_experiments_with_options(request, runtime)

    async def list_experiments_async(
        self,
        request: eflo_cnp_20230828_models.ListExperimentsRequest,
    ) -> eflo_cnp_20230828_models.ListExperimentsResponse:
        """
        @summary Query the experiment list based on the plan ID
        
        @param request: ListExperimentsRequest
        @return: ListExperimentsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_experiments_with_options_async(request, runtime)

    def list_tag_resources_with_options(
        self,
        request: eflo_cnp_20230828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListTagResourcesResponse:
        """
        @summary Query Resource Tags
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_resources_with_options_async(
        self,
        request: eflo_cnp_20230828_models.ListTagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListTagResourcesResponse:
        """
        @summary Query Resource Tags
        
        @param request: ListTagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListTagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_resources(
        self,
        request: eflo_cnp_20230828_models.ListTagResourcesRequest,
    ) -> eflo_cnp_20230828_models.ListTagResourcesResponse:
        """
        @summary Query Resource Tags
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    async def list_tag_resources_async(
        self,
        request: eflo_cnp_20230828_models.ListTagResourcesRequest,
    ) -> eflo_cnp_20230828_models.ListTagResourcesResponse:
        """
        @summary Query Resource Tags
        
        @param request: ListTagResourcesRequest
        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_tag_resources_with_options_async(request, runtime)

    def list_workloads_with_options(
        self,
        request: eflo_cnp_20230828_models.ListWorkloadsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListWorkloadsResponse:
        """
        @summary Get Workload List
        
        @param request: ListWorkloadsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkloadsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkloads',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListWorkloadsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_workloads_with_options_async(
        self,
        request: eflo_cnp_20230828_models.ListWorkloadsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ListWorkloadsResponse:
        """
        @summary Get Workload List
        
        @param request: ListWorkloadsRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListWorkloadsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListWorkloads',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ListWorkloadsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_workloads(
        self,
        request: eflo_cnp_20230828_models.ListWorkloadsRequest,
    ) -> eflo_cnp_20230828_models.ListWorkloadsResponse:
        """
        @summary Get Workload List
        
        @param request: ListWorkloadsRequest
        @return: ListWorkloadsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_workloads_with_options(request, runtime)

    async def list_workloads_async(
        self,
        request: eflo_cnp_20230828_models.ListWorkloadsRequest,
    ) -> eflo_cnp_20230828_models.ListWorkloadsResponse:
        """
        @summary Get Workload List
        
        @param request: ListWorkloadsRequest
        @return: ListWorkloadsResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.list_workloads_with_options_async(request, runtime)

    def stop_experiment_with_options(
        self,
        request: eflo_cnp_20230828_models.StopExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.StopExperimentResponse:
        """
        @summary Stop Experiment
        
        @param request: StopExperimentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopExperiment',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.StopExperimentResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_experiment_with_options_async(
        self,
        request: eflo_cnp_20230828_models.StopExperimentRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.StopExperimentResponse:
        """
        @summary Stop Experiment
        
        @param request: StopExperimentRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: StopExperimentResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.experiment_id):
            query['ExperimentId'] = request.experiment_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopExperiment',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.StopExperimentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_experiment(
        self,
        request: eflo_cnp_20230828_models.StopExperimentRequest,
    ) -> eflo_cnp_20230828_models.StopExperimentResponse:
        """
        @summary Stop Experiment
        
        @param request: StopExperimentRequest
        @return: StopExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_experiment_with_options(request, runtime)

    async def stop_experiment_async(
        self,
        request: eflo_cnp_20230828_models.StopExperimentRequest,
    ) -> eflo_cnp_20230828_models.StopExperimentResponse:
        """
        @summary Stop Experiment
        
        @param request: StopExperimentRequest
        @return: StopExperimentResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.stop_experiment_with_options_async(request, runtime)

    def tag_resources_with_options(
        self,
        request: eflo_cnp_20230828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.TagResourcesResponse:
        """
        @summary Tag Resources with User Labels
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def tag_resources_with_options_async(
        self,
        request: eflo_cnp_20230828_models.TagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.TagResourcesResponse:
        """
        @summary Tag Resources with User Labels
        
        @param request: TagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.TagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def tag_resources(
        self,
        request: eflo_cnp_20230828_models.TagResourcesRequest,
    ) -> eflo_cnp_20230828_models.TagResourcesResponse:
        """
        @summary Tag Resources with User Labels
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    async def tag_resources_async(
        self,
        request: eflo_cnp_20230828_models.TagResourcesRequest,
    ) -> eflo_cnp_20230828_models.TagResourcesResponse:
        """
        @summary Tag Resources with User Labels
        
        @param request: TagResourcesRequest
        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.tag_resources_with_options_async(request, runtime)

    def untag_resources_with_options(
        self,
        request: eflo_cnp_20230828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.UntagResourcesResponse:
        """
        @summary Remove User Tags from Resources
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
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
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def untag_resources_with_options_async(
        self,
        request: eflo_cnp_20230828_models.UntagResourcesRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.UntagResourcesResponse:
        """
        @summary Remove User Tags from Resources
        
        @param request: UntagResourcesRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
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
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.UntagResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def untag_resources(
        self,
        request: eflo_cnp_20230828_models.UntagResourcesRequest,
    ) -> eflo_cnp_20230828_models.UntagResourcesResponse:
        """
        @summary Remove User Tags from Resources
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    async def untag_resources_async(
        self,
        request: eflo_cnp_20230828_models.UntagResourcesRequest,
    ) -> eflo_cnp_20230828_models.UntagResourcesResponse:
        """
        @summary Remove User Tags from Resources
        
        @param request: UntagResourcesRequest
        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.untag_resources_with_options_async(request, runtime)

    def update_experiment_plan_with_options(
        self,
        request: eflo_cnp_20230828_models.UpdateExperimentPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.UpdateExperimentPlanResponse:
        """
        @summary Update Experiment Plan
        
        @param request: UpdateExperimentPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_template_name):
            query['PlanTemplateName'] = request.plan_template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateExperimentPlan',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.UpdateExperimentPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_plan_with_options_async(
        self,
        request: eflo_cnp_20230828_models.UpdateExperimentPlanRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.UpdateExperimentPlanResponse:
        """
        @summary Update Experiment Plan
        
        @param request: UpdateExperimentPlanRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentPlanResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.plan_template_name):
            query['PlanTemplateName'] = request.plan_template_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateExperimentPlan',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.UpdateExperimentPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment_plan(
        self,
        request: eflo_cnp_20230828_models.UpdateExperimentPlanRequest,
    ) -> eflo_cnp_20230828_models.UpdateExperimentPlanResponse:
        """
        @summary Update Experiment Plan
        
        @param request: UpdateExperimentPlanRequest
        @return: UpdateExperimentPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_experiment_plan_with_options(request, runtime)

    async def update_experiment_plan_async(
        self,
        request: eflo_cnp_20230828_models.UpdateExperimentPlanRequest,
    ) -> eflo_cnp_20230828_models.UpdateExperimentPlanResponse:
        """
        @summary Update Experiment Plan
        
        @param request: UpdateExperimentPlanRequest
        @return: UpdateExperimentPlanResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_experiment_plan_with_options_async(request, runtime)

    def update_experiment_plan_template_with_options(
        self,
        tmp_req: eflo_cnp_20230828_models.UpdateExperimentPlanTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.UpdateExperimentPlanTemplateResponse:
        """
        @summary Update Test Plan Template
        
        @param tmp_req: UpdateExperimentPlanTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentPlanTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.UpdateExperimentPlanTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_pipeline):
            request.template_pipeline_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_pipeline, 'TemplatePipeline', 'json')
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not UtilClient.is_unset(request.template_pipeline_shrink):
            body['TemplatePipeline'] = request.template_pipeline_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperimentPlanTemplate',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.UpdateExperimentPlanTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_experiment_plan_template_with_options_async(
        self,
        tmp_req: eflo_cnp_20230828_models.UpdateExperimentPlanTemplateRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.UpdateExperimentPlanTemplateResponse:
        """
        @summary Update Test Plan Template
        
        @param tmp_req: UpdateExperimentPlanTemplateRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: UpdateExperimentPlanTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.UpdateExperimentPlanTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.template_pipeline):
            request.template_pipeline_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_pipeline, 'TemplatePipeline', 'json')
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        body = {}
        if not UtilClient.is_unset(request.template_pipeline_shrink):
            body['TemplatePipeline'] = request.template_pipeline_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateExperimentPlanTemplate',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.UpdateExperimentPlanTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_experiment_plan_template(
        self,
        request: eflo_cnp_20230828_models.UpdateExperimentPlanTemplateRequest,
    ) -> eflo_cnp_20230828_models.UpdateExperimentPlanTemplateResponse:
        """
        @summary Update Test Plan Template
        
        @param request: UpdateExperimentPlanTemplateRequest
        @return: UpdateExperimentPlanTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_experiment_plan_template_with_options(request, runtime)

    async def update_experiment_plan_template_async(
        self,
        request: eflo_cnp_20230828_models.UpdateExperimentPlanTemplateRequest,
    ) -> eflo_cnp_20230828_models.UpdateExperimentPlanTemplateResponse:
        """
        @summary Update Test Plan Template
        
        @param request: UpdateExperimentPlanTemplateRequest
        @return: UpdateExperimentPlanTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.update_experiment_plan_template_with_options_async(request, runtime)

    def validate_resource_with_options(
        self,
        tmp_req: eflo_cnp_20230828_models.ValidateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ValidateResourceResponse:
        """
        @summary Resource Connectivity Test
        
        @param tmp_req: ValidateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.ValidateResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_access_param):
            request.user_access_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_access_param, 'UserAccessParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        body = {}
        if not UtilClient.is_unset(request.user_access_param_shrink):
            body['UserAccessParam'] = request.user_access_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateResource',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ValidateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_resource_with_options_async(
        self,
        tmp_req: eflo_cnp_20230828_models.ValidateResourceRequest,
        runtime: util_models.RuntimeOptions,
    ) -> eflo_cnp_20230828_models.ValidateResourceResponse:
        """
        @summary Resource Connectivity Test
        
        @param tmp_req: ValidateResourceRequest
        @param runtime: runtime options for this request RuntimeOptions
        @return: ValidateResourceResponse
        """
        UtilClient.validate_model(tmp_req)
        request = eflo_cnp_20230828_models.ValidateResourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.user_access_param):
            request.user_access_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_access_param, 'UserAccessParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        body = {}
        if not UtilClient.is_unset(request.user_access_param_shrink):
            body['UserAccessParam'] = request.user_access_param_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ValidateResource',
            version='2023-08-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eflo_cnp_20230828_models.ValidateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_resource(
        self,
        request: eflo_cnp_20230828_models.ValidateResourceRequest,
    ) -> eflo_cnp_20230828_models.ValidateResourceResponse:
        """
        @summary Resource Connectivity Test
        
        @param request: ValidateResourceRequest
        @return: ValidateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.validate_resource_with_options(request, runtime)

    async def validate_resource_async(
        self,
        request: eflo_cnp_20230828_models.ValidateResourceRequest,
    ) -> eflo_cnp_20230828_models.ValidateResourceResponse:
        """
        @summary Resource Connectivity Test
        
        @param request: ValidateResourceRequest
        @return: ValidateResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return await self.validate_resource_with_options_async(request, runtime)
