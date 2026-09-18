# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_paimodelgallery20250630 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.runtime import RuntimeOptions
from darabonba.url import Url as DaraURL

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
        self._endpoint = self.get_endpoint('paimodelgallery', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def create_job_plan_with_options(
        self,
        request: main_models.CreateJobPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_plan_name):
            body['JobPlanName'] = request.job_plan_name
        if not DaraCore.is_null(request.job_plan_steps):
            body['JobPlanSteps'] = request.job_plan_steps
        if not DaraCore.is_null(request.job_plan_type):
            body['JobPlanType'] = request.job_plan_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobPlan',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_job_plan_with_options_async(
        self,
        request: main_models.CreateJobPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateJobPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_plan_name):
            body['JobPlanName'] = request.job_plan_name
        if not DaraCore.is_null(request.job_plan_steps):
            body['JobPlanSteps'] = request.job_plan_steps
        if not DaraCore.is_null(request.job_plan_type):
            body['JobPlanType'] = request.job_plan_type
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        if not DaraCore.is_null(request.template_id):
            body['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateJobPlan',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateJobPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_job_plan(
        self,
        request: main_models.CreateJobPlanRequest,
    ) -> main_models.CreateJobPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_job_plan_with_options(request, headers, runtime)

    async def create_job_plan_async(
        self,
        request: main_models.CreateJobPlanRequest,
    ) -> main_models.CreateJobPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_job_plan_with_options_async(request, headers, runtime)

    def delete_job_plan_with_options(
        self,
        job_plan_id: str,
        request: main_models.DeleteJobPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobPlanResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobPlan',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans/{DaraURL.percent_encode(job_plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_job_plan_with_options_async(
        self,
        job_plan_id: str,
        request: main_models.DeleteJobPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteJobPlanResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteJobPlan',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans/{DaraURL.percent_encode(job_plan_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteJobPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_job_plan(
        self,
        job_plan_id: str,
        request: main_models.DeleteJobPlanRequest,
    ) -> main_models.DeleteJobPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_job_plan_with_options(job_plan_id, request, headers, runtime)

    async def delete_job_plan_async(
        self,
        job_plan_id: str,
        request: main_models.DeleteJobPlanRequest,
    ) -> main_models.DeleteJobPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_job_plan_with_options_async(job_plan_id, request, headers, runtime)

    def get_distillation_template_with_options(
        self,
        template_id: str,
        request: main_models.GetDistillationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDistillationTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDistillationTemplate',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/distillationtemplates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDistillationTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_distillation_template_with_options_async(
        self,
        template_id: str,
        request: main_models.GetDistillationTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDistillationTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDistillationTemplate',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/distillationtemplates/{DaraURL.percent_encode(template_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDistillationTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_distillation_template(
        self,
        template_id: str,
        request: main_models.GetDistillationTemplateRequest,
    ) -> main_models.GetDistillationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_distillation_template_with_options(template_id, request, headers, runtime)

    async def get_distillation_template_async(
        self,
        template_id: str,
        request: main_models.GetDistillationTemplateRequest,
    ) -> main_models.GetDistillationTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_distillation_template_with_options_async(template_id, request, headers, runtime)

    def get_job_plan_with_options(
        self,
        job_plan_id: str,
        request: main_models.GetJobPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobPlanResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetJobPlan',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans/{DaraURL.percent_encode(job_plan_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_job_plan_with_options_async(
        self,
        job_plan_id: str,
        request: main_models.GetJobPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetJobPlanResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetJobPlan',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans/{DaraURL.percent_encode(job_plan_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetJobPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_job_plan(
        self,
        job_plan_id: str,
        request: main_models.GetJobPlanRequest,
    ) -> main_models.GetJobPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_job_plan_with_options(job_plan_id, request, headers, runtime)

    async def get_job_plan_async(
        self,
        job_plan_id: str,
        request: main_models.GetJobPlanRequest,
    ) -> main_models.GetJobPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_job_plan_with_options_async(job_plan_id, request, headers, runtime)

    def list_distillation_templates_with_options(
        self,
        request: main_models.ListDistillationTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDistillationTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDistillationTemplates',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/distillationtemplates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDistillationTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_distillation_templates_with_options_async(
        self,
        request: main_models.ListDistillationTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDistillationTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.category):
            query['Category'] = request.category
        if not DaraCore.is_null(request.keyword):
            query['Keyword'] = request.keyword
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDistillationTemplates',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/distillationtemplates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDistillationTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_distillation_templates(
        self,
        request: main_models.ListDistillationTemplatesRequest,
    ) -> main_models.ListDistillationTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_distillation_templates_with_options(request, headers, runtime)

    async def list_distillation_templates_async(
        self,
        request: main_models.ListDistillationTemplatesRequest,
    ) -> main_models.ListDistillationTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_distillation_templates_with_options_async(request, headers, runtime)

    def list_job_plans_with_options(
        self,
        tmp_req: main_models.ListJobPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobPlansResponse:
        tmp_req.validate()
        request = main_models.ListJobPlansShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.has_template):
            query['HasTemplate'] = request.has_template
        if not DaraCore.is_null(request.job_plan_name):
            query['JobPlanName'] = request.job_plan_name
        if not DaraCore.is_null(request.job_plan_type):
            query['JobPlanType'] = request.job_plan_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobPlans',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_job_plans_with_options_async(
        self,
        tmp_req: main_models.ListJobPlansRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListJobPlansResponse:
        tmp_req.validate()
        request = main_models.ListJobPlansShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.has_template):
            query['HasTemplate'] = request.has_template
        if not DaraCore.is_null(request.job_plan_name):
            query['JobPlanName'] = request.job_plan_name
        if not DaraCore.is_null(request.job_plan_type):
            query['JobPlanType'] = request.job_plan_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.template_id):
            query['TemplateId'] = request.template_id
        if not DaraCore.is_null(request.workspace_id):
            query['WorkspaceId'] = request.workspace_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListJobPlans',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListJobPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_job_plans(
        self,
        request: main_models.ListJobPlansRequest,
    ) -> main_models.ListJobPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_job_plans_with_options(request, headers, runtime)

    async def list_job_plans_async(
        self,
        request: main_models.ListJobPlansRequest,
    ) -> main_models.ListJobPlansResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_job_plans_with_options_async(request, headers, runtime)

    def list_model_gallery_models_with_options(
        self,
        tmp_req: main_models.ListModelGalleryModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelGalleryModelsResponse:
        tmp_req.validate()
        request = main_models.ListModelGalleryModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.conditions):
            request.conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.collections):
            query['Collections'] = request.collections
        if not DaraCore.is_null(request.compressible):
            query['Compressible'] = request.compressible
        if not DaraCore.is_null(request.conditions_shrink):
            query['Conditions'] = request.conditions_shrink
        if not DaraCore.is_null(request.deep_think):
            query['DeepThink'] = request.deep_think
        if not DaraCore.is_null(request.demonstrable):
            query['Demonstrable'] = request.demonstrable
        if not DaraCore.is_null(request.deployable):
            query['Deployable'] = request.deployable
        if not DaraCore.is_null(request.distillable):
            query['Distillable'] = request.distillable
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.evaluable):
            query['Evaluable'] = request.evaluable
        if not DaraCore.is_null(request.function_call):
            query['FunctionCall'] = request.function_call
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_series):
            query['ModelSeries'] = request.model_series
        if not DaraCore.is_null(request.model_type):
            query['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.supported_compression_resource):
            query['SupportedCompressionResource'] = request.supported_compression_resource
        if not DaraCore.is_null(request.supported_distillation_resource):
            query['SupportedDistillationResource'] = request.supported_distillation_resource
        if not DaraCore.is_null(request.supported_evaluation_resource):
            query['SupportedEvaluationResource'] = request.supported_evaluation_resource
        if not DaraCore.is_null(request.supported_inference_resource):
            query['SupportedInferenceResource'] = request.supported_inference_resource
        if not DaraCore.is_null(request.supported_training_resource):
            query['SupportedTrainingResource'] = request.supported_training_resource
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.task):
            query['Task'] = request.task
        if not DaraCore.is_null(request.trainable):
            query['Trainable'] = request.trainable
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelGalleryModels',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelgallery/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelGalleryModelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_model_gallery_models_with_options_async(
        self,
        tmp_req: main_models.ListModelGalleryModelsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListModelGalleryModelsResponse:
        tmp_req.validate()
        request = main_models.ListModelGalleryModelsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.conditions):
            request.conditions_shrink = Utils.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.collections):
            query['Collections'] = request.collections
        if not DaraCore.is_null(request.compressible):
            query['Compressible'] = request.compressible
        if not DaraCore.is_null(request.conditions_shrink):
            query['Conditions'] = request.conditions_shrink
        if not DaraCore.is_null(request.deep_think):
            query['DeepThink'] = request.deep_think
        if not DaraCore.is_null(request.demonstrable):
            query['Demonstrable'] = request.demonstrable
        if not DaraCore.is_null(request.deployable):
            query['Deployable'] = request.deployable
        if not DaraCore.is_null(request.distillable):
            query['Distillable'] = request.distillable
        if not DaraCore.is_null(request.domain):
            query['Domain'] = request.domain
        if not DaraCore.is_null(request.evaluable):
            query['Evaluable'] = request.evaluable
        if not DaraCore.is_null(request.function_call):
            query['FunctionCall'] = request.function_call
        if not DaraCore.is_null(request.model_name):
            query['ModelName'] = request.model_name
        if not DaraCore.is_null(request.model_series):
            query['ModelSeries'] = request.model_series
        if not DaraCore.is_null(request.model_type):
            query['ModelType'] = request.model_type
        if not DaraCore.is_null(request.order):
            query['Order'] = request.order
        if not DaraCore.is_null(request.origin):
            query['Origin'] = request.origin
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.supported_compression_resource):
            query['SupportedCompressionResource'] = request.supported_compression_resource
        if not DaraCore.is_null(request.supported_distillation_resource):
            query['SupportedDistillationResource'] = request.supported_distillation_resource
        if not DaraCore.is_null(request.supported_evaluation_resource):
            query['SupportedEvaluationResource'] = request.supported_evaluation_resource
        if not DaraCore.is_null(request.supported_inference_resource):
            query['SupportedInferenceResource'] = request.supported_inference_resource
        if not DaraCore.is_null(request.supported_training_resource):
            query['SupportedTrainingResource'] = request.supported_training_resource
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        if not DaraCore.is_null(request.task):
            query['Task'] = request.task
        if not DaraCore.is_null(request.trainable):
            query['Trainable'] = request.trainable
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListModelGalleryModels',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/modelgallery/models',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListModelGalleryModelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_model_gallery_models(
        self,
        request: main_models.ListModelGalleryModelsRequest,
    ) -> main_models.ListModelGalleryModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_model_gallery_models_with_options(request, headers, runtime)

    async def list_model_gallery_models_async(
        self,
        request: main_models.ListModelGalleryModelsRequest,
    ) -> main_models.ListModelGalleryModelsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_model_gallery_models_with_options_async(request, headers, runtime)

    def update_job_plan_with_options(
        self,
        job_plan_id: str,
        request: main_models.UpdateJobPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_plan_current_step):
            body['JobPlanCurrentStep'] = request.job_plan_current_step
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJobPlan',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans/{DaraURL.percent_encode(job_plan_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_job_plan_with_options_async(
        self,
        job_plan_id: str,
        request: main_models.UpdateJobPlanRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateJobPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.job_plan_current_step):
            body['JobPlanCurrentStep'] = request.job_plan_current_step
        if not DaraCore.is_null(request.tag):
            body['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateJobPlan',
            version = '2025-06-30',
            protocol = 'HTTPS',
            pathname = f'/api/v1/jobplans/{DaraURL.percent_encode(job_plan_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateJobPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_job_plan(
        self,
        job_plan_id: str,
        request: main_models.UpdateJobPlanRequest,
    ) -> main_models.UpdateJobPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_job_plan_with_options(job_plan_id, request, headers, runtime)

    async def update_job_plan_async(
        self,
        job_plan_id: str,
        request: main_models.UpdateJobPlanRequest,
    ) -> main_models.UpdateJobPlanResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_job_plan_with_options_async(job_plan_id, request, headers, runtime)
