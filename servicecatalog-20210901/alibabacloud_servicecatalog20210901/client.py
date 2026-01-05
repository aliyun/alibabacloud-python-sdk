# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_servicecatalog20210901 import models as main_models
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
        self._endpoint = self.get_endpoint('servicecatalog', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def approve_provisioned_product_plan_with_options(
        self,
        request: main_models.ApproveProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approval_action):
            body['ApprovalAction'] = request.approval_action
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApproveProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def approve_provisioned_product_plan_with_options_async(
        self,
        request: main_models.ApproveProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ApproveProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approval_action):
            body['ApprovalAction'] = request.approval_action
        if not DaraCore.is_null(request.comment):
            body['Comment'] = request.comment
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ApproveProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ApproveProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def approve_provisioned_product_plan(
        self,
        request: main_models.ApproveProvisionedProductPlanRequest,
    ) -> main_models.ApproveProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return self.approve_provisioned_product_plan_with_options(request, runtime)

    async def approve_provisioned_product_plan_async(
        self,
        request: main_models.ApproveProvisionedProductPlanRequest,
    ) -> main_models.ApproveProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return await self.approve_provisioned_product_plan_with_options_async(request, runtime)

    def associate_principal_with_portfolio_with_options(
        self,
        request: main_models.AssociatePrincipalWithPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociatePrincipalWithPortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociatePrincipalWithPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociatePrincipalWithPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_principal_with_portfolio_with_options_async(
        self,
        request: main_models.AssociatePrincipalWithPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociatePrincipalWithPortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociatePrincipalWithPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociatePrincipalWithPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_principal_with_portfolio(
        self,
        request: main_models.AssociatePrincipalWithPortfolioRequest,
    ) -> main_models.AssociatePrincipalWithPortfolioResponse:
        runtime = RuntimeOptions()
        return self.associate_principal_with_portfolio_with_options(request, runtime)

    async def associate_principal_with_portfolio_async(
        self,
        request: main_models.AssociatePrincipalWithPortfolioRequest,
    ) -> main_models.AssociatePrincipalWithPortfolioResponse:
        runtime = RuntimeOptions()
        return await self.associate_principal_with_portfolio_with_options_async(request, runtime)

    def associate_product_with_portfolio_with_options(
        self,
        request: main_models.AssociateProductWithPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateProductWithPortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateProductWithPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateProductWithPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_product_with_portfolio_with_options_async(
        self,
        request: main_models.AssociateProductWithPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateProductWithPortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateProductWithPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateProductWithPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_product_with_portfolio(
        self,
        request: main_models.AssociateProductWithPortfolioRequest,
    ) -> main_models.AssociateProductWithPortfolioResponse:
        runtime = RuntimeOptions()
        return self.associate_product_with_portfolio_with_options(request, runtime)

    async def associate_product_with_portfolio_async(
        self,
        request: main_models.AssociateProductWithPortfolioRequest,
    ) -> main_models.AssociateProductWithPortfolioResponse:
        runtime = RuntimeOptions()
        return await self.associate_product_with_portfolio_with_options_async(request, runtime)

    def associate_tag_option_with_resource_with_options(
        self,
        request: main_models.AssociateTagOptionWithResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateTagOptionWithResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateTagOptionWithResource',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateTagOptionWithResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_tag_option_with_resource_with_options_async(
        self,
        request: main_models.AssociateTagOptionWithResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateTagOptionWithResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AssociateTagOptionWithResource',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateTagOptionWithResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_tag_option_with_resource(
        self,
        request: main_models.AssociateTagOptionWithResourceRequest,
    ) -> main_models.AssociateTagOptionWithResourceResponse:
        runtime = RuntimeOptions()
        return self.associate_tag_option_with_resource_with_options(request, runtime)

    async def associate_tag_option_with_resource_async(
        self,
        request: main_models.AssociateTagOptionWithResourceRequest,
    ) -> main_models.AssociateTagOptionWithResourceResponse:
        runtime = RuntimeOptions()
        return await self.associate_tag_option_with_resource_with_options_async(request, runtime)

    def cancel_provisioned_product_plan_with_options(
        self,
        request: main_models.CancelProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def cancel_provisioned_product_plan_with_options_async(
        self,
        request: main_models.CancelProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CancelProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CancelProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CancelProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def cancel_provisioned_product_plan(
        self,
        request: main_models.CancelProvisionedProductPlanRequest,
    ) -> main_models.CancelProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return self.cancel_provisioned_product_plan_with_options(request, runtime)

    async def cancel_provisioned_product_plan_async(
        self,
        request: main_models.CancelProvisionedProductPlanRequest,
    ) -> main_models.CancelProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return await self.cancel_provisioned_product_plan_with_options_async(request, runtime)

    def copy_product_with_options(
        self,
        request: main_models.CopyProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_product_arn):
            body['SourceProductArn'] = request.source_product_arn
        if not DaraCore.is_null(request.target_product_name):
            body['TargetProductName'] = request.target_product_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def copy_product_with_options_async(
        self,
        request: main_models.CopyProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CopyProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.source_product_arn):
            body['SourceProductArn'] = request.source_product_arn
        if not DaraCore.is_null(request.target_product_name):
            body['TargetProductName'] = request.target_product_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CopyProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CopyProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def copy_product(
        self,
        request: main_models.CopyProductRequest,
    ) -> main_models.CopyProductResponse:
        runtime = RuntimeOptions()
        return self.copy_product_with_options(request, runtime)

    async def copy_product_async(
        self,
        request: main_models.CopyProductRequest,
    ) -> main_models.CopyProductResponse:
        runtime = RuntimeOptions()
        return await self.copy_product_with_options_async(request, runtime)

    def create_constraint_with_options(
        self,
        request: main_models.CreateConstraintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConstraintResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.constraint_type):
            body['ConstraintType'] = request.constraint_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConstraint',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_constraint_with_options_async(
        self,
        request: main_models.CreateConstraintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateConstraintResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.constraint_type):
            body['ConstraintType'] = request.constraint_type
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateConstraint',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateConstraintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_constraint(
        self,
        request: main_models.CreateConstraintRequest,
    ) -> main_models.CreateConstraintResponse:
        runtime = RuntimeOptions()
        return self.create_constraint_with_options(request, runtime)

    async def create_constraint_async(
        self,
        request: main_models.CreateConstraintRequest,
    ) -> main_models.CreateConstraintResponse:
        runtime = RuntimeOptions()
        return await self.create_constraint_with_options_async(request, runtime)

    def create_portfolio_with_options(
        self,
        request: main_models.CreatePortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_portfolio_with_options_async(
        self,
        request: main_models.CreatePortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreatePortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_portfolio(
        self,
        request: main_models.CreatePortfolioRequest,
    ) -> main_models.CreatePortfolioResponse:
        runtime = RuntimeOptions()
        return self.create_portfolio_with_options(request, runtime)

    async def create_portfolio_async(
        self,
        request: main_models.CreatePortfolioRequest,
    ) -> main_models.CreatePortfolioResponse:
        runtime = RuntimeOptions()
        return await self.create_portfolio_with_options_async(request, runtime)

    def create_product_with_options(
        self,
        tmp_req: main_models.CreateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductResponse:
        tmp_req.validate()
        request = main_models.CreateProductShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.product_version_parameters):
            request.product_version_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.product_version_parameters, 'ProductVersionParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.product_version_parameters_shrink):
            body['ProductVersionParameters'] = request.product_version_parameters_shrink
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        tmp_req: main_models.CreateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductResponse:
        tmp_req.validate()
        request = main_models.CreateProductShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.product_version_parameters):
            request.product_version_parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.product_version_parameters, 'ProductVersionParameters', 'json')
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.product_type):
            body['ProductType'] = request.product_type
        if not DaraCore.is_null(request.product_version_parameters_shrink):
            body['ProductVersionParameters'] = request.product_version_parameters_shrink
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product(
        self,
        request: main_models.CreateProductRequest,
    ) -> main_models.CreateProductResponse:
        runtime = RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    async def create_product_async(
        self,
        request: main_models.CreateProductRequest,
    ) -> main_models.CreateProductResponse:
        runtime = RuntimeOptions()
        return await self.create_product_with_options_async(request, runtime)

    def create_product_version_with_options(
        self,
        request: main_models.CreateProductVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.active):
            body['Active'] = request.active
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.guidance):
            body['Guidance'] = request.guidance
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.template_url):
            body['TemplateUrl'] = request.template_url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProductVersion',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_version_with_options_async(
        self,
        request: main_models.CreateProductVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.active):
            body['Active'] = request.active
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.guidance):
            body['Guidance'] = request.guidance
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.template_url):
            body['TemplateUrl'] = request.template_url
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProductVersion',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_product_version(
        self,
        request: main_models.CreateProductVersionRequest,
    ) -> main_models.CreateProductVersionResponse:
        runtime = RuntimeOptions()
        return self.create_product_version_with_options(request, runtime)

    async def create_product_version_async(
        self,
        request: main_models.CreateProductVersionRequest,
    ) -> main_models.CreateProductVersionResponse:
        runtime = RuntimeOptions()
        return await self.create_product_version_with_options_async(request, runtime)

    def create_provisioned_product_plan_with_options(
        self,
        request: main_models.CreateProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.plan_name):
            body['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.plan_type):
            body['PlanType'] = request.plan_type
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not DaraCore.is_null(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_provisioned_product_plan_with_options_async(
        self,
        request: main_models.CreateProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.operation_type):
            body['OperationType'] = request.operation_type
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.plan_name):
            body['PlanName'] = request.plan_name
        if not DaraCore.is_null(request.plan_type):
            body['PlanType'] = request.plan_type
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not DaraCore.is_null(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_provisioned_product_plan(
        self,
        request: main_models.CreateProvisionedProductPlanRequest,
    ) -> main_models.CreateProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return self.create_provisioned_product_plan_with_options(request, runtime)

    async def create_provisioned_product_plan_async(
        self,
        request: main_models.CreateProvisionedProductPlanRequest,
    ) -> main_models.CreateProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return await self.create_provisioned_product_plan_with_options_async(request, runtime)

    def create_tag_option_with_options(
        self,
        request: main_models.CreateTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagOptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.key):
            body['Key'] = request.key
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_tag_option_with_options_async(
        self,
        request: main_models.CreateTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTagOptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.key):
            body['Key'] = request.key
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_tag_option(
        self,
        request: main_models.CreateTagOptionRequest,
    ) -> main_models.CreateTagOptionResponse:
        runtime = RuntimeOptions()
        return self.create_tag_option_with_options(request, runtime)

    async def create_tag_option_async(
        self,
        request: main_models.CreateTagOptionRequest,
    ) -> main_models.CreateTagOptionResponse:
        runtime = RuntimeOptions()
        return await self.create_tag_option_with_options_async(request, runtime)

    def create_template_with_options(
        self,
        request: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.terraform_variables):
            body['TerraformVariables'] = request.terraform_variables
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_template_with_options_async(
        self,
        request: main_models.CreateTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateTemplateResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.template_body):
            body['TemplateBody'] = request.template_body
        if not DaraCore.is_null(request.template_type):
            body['TemplateType'] = request.template_type
        if not DaraCore.is_null(request.terraform_variables):
            body['TerraformVariables'] = request.terraform_variables
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTemplate',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_template(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    async def create_template_async(
        self,
        request: main_models.CreateTemplateRequest,
    ) -> main_models.CreateTemplateResponse:
        runtime = RuntimeOptions()
        return await self.create_template_with_options_async(request, runtime)

    def delete_constraint_with_options(
        self,
        request: main_models.DeleteConstraintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConstraintResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConstraint',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_constraint_with_options_async(
        self,
        request: main_models.DeleteConstraintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteConstraintResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteConstraint',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteConstraintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_constraint(
        self,
        request: main_models.DeleteConstraintRequest,
    ) -> main_models.DeleteConstraintResponse:
        runtime = RuntimeOptions()
        return self.delete_constraint_with_options(request, runtime)

    async def delete_constraint_async(
        self,
        request: main_models.DeleteConstraintRequest,
    ) -> main_models.DeleteConstraintResponse:
        runtime = RuntimeOptions()
        return await self.delete_constraint_with_options_async(request, runtime)

    def delete_portfolio_with_options(
        self,
        request: main_models.DeletePortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_portfolio_with_options_async(
        self,
        request: main_models.DeletePortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeletePortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeletePortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_portfolio(
        self,
        request: main_models.DeletePortfolioRequest,
    ) -> main_models.DeletePortfolioResponse:
        runtime = RuntimeOptions()
        return self.delete_portfolio_with_options(request, runtime)

    async def delete_portfolio_async(
        self,
        request: main_models.DeletePortfolioRequest,
    ) -> main_models.DeletePortfolioResponse:
        runtime = RuntimeOptions()
        return await self.delete_portfolio_with_options_async(request, runtime)

    def delete_product_with_options(
        self,
        request: main_models.DeleteProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_with_options_async(
        self,
        request: main_models.DeleteProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product(
        self,
        request: main_models.DeleteProductRequest,
    ) -> main_models.DeleteProductResponse:
        runtime = RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    async def delete_product_async(
        self,
        request: main_models.DeleteProductRequest,
    ) -> main_models.DeleteProductResponse:
        runtime = RuntimeOptions()
        return await self.delete_product_with_options_async(request, runtime)

    def delete_product_version_with_options(
        self,
        request: main_models.DeleteProductVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProductVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProductVersion',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_version_with_options_async(
        self,
        request: main_models.DeleteProductVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProductVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProductVersion',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product_version(
        self,
        request: main_models.DeleteProductVersionRequest,
    ) -> main_models.DeleteProductVersionResponse:
        runtime = RuntimeOptions()
        return self.delete_product_version_with_options(request, runtime)

    async def delete_product_version_async(
        self,
        request: main_models.DeleteProductVersionRequest,
    ) -> main_models.DeleteProductVersionResponse:
        runtime = RuntimeOptions()
        return await self.delete_product_version_with_options_async(request, runtime)

    def delete_provisioned_product_plan_with_options(
        self,
        request: main_models.DeleteProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_provisioned_product_plan_with_options_async(
        self,
        request: main_models.DeleteProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_provisioned_product_plan(
        self,
        request: main_models.DeleteProvisionedProductPlanRequest,
    ) -> main_models.DeleteProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return self.delete_provisioned_product_plan_with_options(request, runtime)

    async def delete_provisioned_product_plan_async(
        self,
        request: main_models.DeleteProvisionedProductPlanRequest,
    ) -> main_models.DeleteProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return await self.delete_provisioned_product_plan_with_options_async(request, runtime)

    def delete_tag_option_with_options(
        self,
        request: main_models.DeleteTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagOptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_tag_option_with_options_async(
        self,
        request: main_models.DeleteTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteTagOptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DeleteTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_tag_option(
        self,
        request: main_models.DeleteTagOptionRequest,
    ) -> main_models.DeleteTagOptionResponse:
        runtime = RuntimeOptions()
        return self.delete_tag_option_with_options(request, runtime)

    async def delete_tag_option_async(
        self,
        request: main_models.DeleteTagOptionRequest,
    ) -> main_models.DeleteTagOptionResponse:
        runtime = RuntimeOptions()
        return await self.delete_tag_option_with_options_async(request, runtime)

    def dis_associate_tag_option_from_resource_with_options(
        self,
        request: main_models.DisAssociateTagOptionFromResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisAssociateTagOptionFromResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisAssociateTagOptionFromResource',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisAssociateTagOptionFromResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def dis_associate_tag_option_from_resource_with_options_async(
        self,
        request: main_models.DisAssociateTagOptionFromResourceRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisAssociateTagOptionFromResourceResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.resource_id):
            body['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisAssociateTagOptionFromResource',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisAssociateTagOptionFromResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def dis_associate_tag_option_from_resource(
        self,
        request: main_models.DisAssociateTagOptionFromResourceRequest,
    ) -> main_models.DisAssociateTagOptionFromResourceResponse:
        runtime = RuntimeOptions()
        return self.dis_associate_tag_option_from_resource_with_options(request, runtime)

    async def dis_associate_tag_option_from_resource_async(
        self,
        request: main_models.DisAssociateTagOptionFromResourceRequest,
    ) -> main_models.DisAssociateTagOptionFromResourceResponse:
        runtime = RuntimeOptions()
        return await self.dis_associate_tag_option_from_resource_with_options_async(request, runtime)

    def disassociate_principal_from_portfolio_with_options(
        self,
        request: main_models.DisassociatePrincipalFromPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociatePrincipalFromPortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisassociatePrincipalFromPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociatePrincipalFromPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_principal_from_portfolio_with_options_async(
        self,
        request: main_models.DisassociatePrincipalFromPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociatePrincipalFromPortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.principal_id):
            body['PrincipalId'] = request.principal_id
        if not DaraCore.is_null(request.principal_type):
            body['PrincipalType'] = request.principal_type
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisassociatePrincipalFromPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociatePrincipalFromPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_principal_from_portfolio(
        self,
        request: main_models.DisassociatePrincipalFromPortfolioRequest,
    ) -> main_models.DisassociatePrincipalFromPortfolioResponse:
        runtime = RuntimeOptions()
        return self.disassociate_principal_from_portfolio_with_options(request, runtime)

    async def disassociate_principal_from_portfolio_async(
        self,
        request: main_models.DisassociatePrincipalFromPortfolioRequest,
    ) -> main_models.DisassociatePrincipalFromPortfolioResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_principal_from_portfolio_with_options_async(request, runtime)

    def disassociate_product_from_portfolio_with_options(
        self,
        request: main_models.DisassociateProductFromPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateProductFromPortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateProductFromPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateProductFromPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_product_from_portfolio_with_options_async(
        self,
        request: main_models.DisassociateProductFromPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateProductFromPortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'DisassociateProductFromPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateProductFromPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_product_from_portfolio(
        self,
        request: main_models.DisassociateProductFromPortfolioRequest,
    ) -> main_models.DisassociateProductFromPortfolioResponse:
        runtime = RuntimeOptions()
        return self.disassociate_product_from_portfolio_with_options(request, runtime)

    async def disassociate_product_from_portfolio_async(
        self,
        request: main_models.DisassociateProductFromPortfolioRequest,
    ) -> main_models.DisassociateProductFromPortfolioResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_product_from_portfolio_with_options_async(request, runtime)

    def execute_provisioned_product_plan_with_options(
        self,
        request: main_models.ExecuteProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_provisioned_product_plan_with_options_async(
        self,
        request: main_models.ExecuteProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_provisioned_product_plan(
        self,
        request: main_models.ExecuteProvisionedProductPlanRequest,
    ) -> main_models.ExecuteProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return self.execute_provisioned_product_plan_with_options(request, runtime)

    async def execute_provisioned_product_plan_async(
        self,
        request: main_models.ExecuteProvisionedProductPlanRequest,
    ) -> main_models.ExecuteProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return await self.execute_provisioned_product_plan_with_options_async(request, runtime)

    def get_constraint_with_options(
        self,
        request: main_models.GetConstraintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConstraintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.constraint_id):
            query['ConstraintId'] = request.constraint_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConstraint',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_constraint_with_options_async(
        self,
        request: main_models.GetConstraintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetConstraintResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.constraint_id):
            query['ConstraintId'] = request.constraint_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetConstraint',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetConstraintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_constraint(
        self,
        request: main_models.GetConstraintRequest,
    ) -> main_models.GetConstraintResponse:
        runtime = RuntimeOptions()
        return self.get_constraint_with_options(request, runtime)

    async def get_constraint_async(
        self,
        request: main_models.GetConstraintRequest,
    ) -> main_models.GetConstraintResponse:
        runtime = RuntimeOptions()
        return await self.get_constraint_with_options_async(request, runtime)

    def get_portfolio_with_options(
        self,
        request: main_models.GetPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPortfolioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_portfolio_with_options_async(
        self,
        request: main_models.GetPortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetPortfolioResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetPortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_portfolio(
        self,
        request: main_models.GetPortfolioRequest,
    ) -> main_models.GetPortfolioResponse:
        runtime = RuntimeOptions()
        return self.get_portfolio_with_options(request, runtime)

    async def get_portfolio_async(
        self,
        request: main_models.GetPortfolioRequest,
    ) -> main_models.GetPortfolioResponse:
        runtime = RuntimeOptions()
        return await self.get_portfolio_with_options_async(request, runtime)

    def get_product_as_admin_with_options(
        self,
        request: main_models.GetProductAsAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductAsAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductAsAdmin',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductAsAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_as_admin_with_options_async(
        self,
        request: main_models.GetProductAsAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductAsAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductAsAdmin',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductAsAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_as_admin(
        self,
        request: main_models.GetProductAsAdminRequest,
    ) -> main_models.GetProductAsAdminResponse:
        runtime = RuntimeOptions()
        return self.get_product_as_admin_with_options(request, runtime)

    async def get_product_as_admin_async(
        self,
        request: main_models.GetProductAsAdminRequest,
    ) -> main_models.GetProductAsAdminResponse:
        runtime = RuntimeOptions()
        return await self.get_product_as_admin_with_options_async(request, runtime)

    def get_product_as_end_user_with_options(
        self,
        request: main_models.GetProductAsEndUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductAsEndUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductAsEndUser',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductAsEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_as_end_user_with_options_async(
        self,
        request: main_models.GetProductAsEndUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductAsEndUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductAsEndUser',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductAsEndUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_as_end_user(
        self,
        request: main_models.GetProductAsEndUserRequest,
    ) -> main_models.GetProductAsEndUserResponse:
        runtime = RuntimeOptions()
        return self.get_product_as_end_user_with_options(request, runtime)

    async def get_product_as_end_user_async(
        self,
        request: main_models.GetProductAsEndUserRequest,
    ) -> main_models.GetProductAsEndUserResponse:
        runtime = RuntimeOptions()
        return await self.get_product_as_end_user_with_options_async(request, runtime)

    def get_product_version_with_options(
        self,
        request: main_models.GetProductVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductVersion',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_version_with_options_async(
        self,
        request: main_models.GetProductVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProductVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProductVersion',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product_version(
        self,
        request: main_models.GetProductVersionRequest,
    ) -> main_models.GetProductVersionResponse:
        runtime = RuntimeOptions()
        return self.get_product_version_with_options(request, runtime)

    async def get_product_version_async(
        self,
        request: main_models.GetProductVersionRequest,
    ) -> main_models.GetProductVersionResponse:
        runtime = RuntimeOptions()
        return await self.get_product_version_with_options_async(request, runtime)

    def get_provisioned_product_with_options(
        self,
        request: main_models.GetProvisionedProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProvisionedProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProvisionedProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProvisionedProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_provisioned_product_with_options_async(
        self,
        request: main_models.GetProvisionedProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProvisionedProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetProvisionedProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProvisionedProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_provisioned_product(
        self,
        request: main_models.GetProvisionedProductRequest,
    ) -> main_models.GetProvisionedProductResponse:
        runtime = RuntimeOptions()
        return self.get_provisioned_product_with_options(request, runtime)

    async def get_provisioned_product_async(
        self,
        request: main_models.GetProvisionedProductRequest,
    ) -> main_models.GetProvisionedProductResponse:
        runtime = RuntimeOptions()
        return await self.get_provisioned_product_with_options_async(request, runtime)

    def get_provisioned_product_plan_with_options(
        self,
        request: main_models.GetProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_provisioned_product_plan_with_options_async(
        self,
        request: main_models.GetProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_provisioned_product_plan(
        self,
        request: main_models.GetProvisionedProductPlanRequest,
    ) -> main_models.GetProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return self.get_provisioned_product_plan_with_options(request, runtime)

    async def get_provisioned_product_plan_async(
        self,
        request: main_models.GetProvisionedProductPlanRequest,
    ) -> main_models.GetProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return await self.get_provisioned_product_plan_with_options_async(request, runtime)

    def get_tag_option_with_options(
        self,
        request: main_models.GetTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTagOptionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_tag_option_with_options_async(
        self,
        request: main_models.GetTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTagOptionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_tag_option(
        self,
        request: main_models.GetTagOptionRequest,
    ) -> main_models.GetTagOptionResponse:
        runtime = RuntimeOptions()
        return self.get_tag_option_with_options(request, runtime)

    async def get_tag_option_async(
        self,
        request: main_models.GetTagOptionRequest,
    ) -> main_models.GetTagOptionResponse:
        runtime = RuntimeOptions()
        return await self.get_tag_option_with_options_async(request, runtime)

    def get_task_with_options(
        self,
        request: main_models.GetTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_task_with_options_async(
        self,
        request: main_models.GetTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTaskResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetTask',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_task(
        self,
        request: main_models.GetTaskRequest,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        return self.get_task_with_options(request, runtime)

    async def get_task_async(
        self,
        request: main_models.GetTaskRequest,
    ) -> main_models.GetTaskResponse:
        runtime = RuntimeOptions()
        return await self.get_task_with_options_async(request, runtime)

    def get_template_with_options(
        self,
        request: main_models.GetTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_template_with_options_async(
        self,
        request: main_models.GetTemplateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetTemplateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            query['ProductVersionId'] = request.product_version_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTemplate',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_template(
        self,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        return self.get_template_with_options(request, runtime)

    async def get_template_async(
        self,
        request: main_models.GetTemplateRequest,
    ) -> main_models.GetTemplateResponse:
        runtime = RuntimeOptions()
        return await self.get_template_with_options_async(request, runtime)

    def launch_product_with_options(
        self,
        request: main_models.LaunchProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not DaraCore.is_null(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LaunchProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def launch_product_with_options_async(
        self,
        request: main_models.LaunchProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.LaunchProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.provisioned_product_name):
            body['ProvisionedProductName'] = request.provisioned_product_name
        if not DaraCore.is_null(request.stack_region_id):
            body['StackRegionId'] = request.stack_region_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'LaunchProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.LaunchProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def launch_product(
        self,
        request: main_models.LaunchProductRequest,
    ) -> main_models.LaunchProductResponse:
        runtime = RuntimeOptions()
        return self.launch_product_with_options(request, runtime)

    async def launch_product_async(
        self,
        request: main_models.LaunchProductRequest,
    ) -> main_models.LaunchProductResponse:
        runtime = RuntimeOptions()
        return await self.launch_product_with_options_async(request, runtime)

    def list_launch_options_with_options(
        self,
        request: main_models.ListLaunchOptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLaunchOptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLaunchOptions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLaunchOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_launch_options_with_options_async(
        self,
        request: main_models.ListLaunchOptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListLaunchOptionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLaunchOptions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLaunchOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_launch_options(
        self,
        request: main_models.ListLaunchOptionsRequest,
    ) -> main_models.ListLaunchOptionsResponse:
        runtime = RuntimeOptions()
        return self.list_launch_options_with_options(request, runtime)

    async def list_launch_options_async(
        self,
        request: main_models.ListLaunchOptionsRequest,
    ) -> main_models.ListLaunchOptionsResponse:
        runtime = RuntimeOptions()
        return await self.list_launch_options_with_options_async(request, runtime)

    def list_portfolios_with_options(
        self,
        request: main_models.ListPortfoliosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPortfoliosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPortfolios',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPortfoliosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_portfolios_with_options_async(
        self,
        request: main_models.ListPortfoliosRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPortfoliosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPortfolios',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPortfoliosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_portfolios(
        self,
        request: main_models.ListPortfoliosRequest,
    ) -> main_models.ListPortfoliosResponse:
        runtime = RuntimeOptions()
        return self.list_portfolios_with_options(request, runtime)

    async def list_portfolios_async(
        self,
        request: main_models.ListPortfoliosRequest,
    ) -> main_models.ListPortfoliosResponse:
        runtime = RuntimeOptions()
        return await self.list_portfolios_with_options_async(request, runtime)

    def list_principals_with_options(
        self,
        request: main_models.ListPrincipalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrincipalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrincipals',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrincipalsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_principals_with_options_async(
        self,
        request: main_models.ListPrincipalsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListPrincipalsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrincipals',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrincipalsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_principals(
        self,
        request: main_models.ListPrincipalsRequest,
    ) -> main_models.ListPrincipalsResponse:
        runtime = RuntimeOptions()
        return self.list_principals_with_options(request, runtime)

    async def list_principals_async(
        self,
        request: main_models.ListPrincipalsRequest,
    ) -> main_models.ListPrincipalsResponse:
        runtime = RuntimeOptions()
        return await self.list_principals_with_options_async(request, runtime)

    def list_product_versions_with_options(
        self,
        request: main_models.ListProductVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductVersions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_versions_with_options_async(
        self,
        request: main_models.ListProductVersionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductVersionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.product_id):
            query['ProductId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductVersions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductVersionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_versions(
        self,
        request: main_models.ListProductVersionsRequest,
    ) -> main_models.ListProductVersionsResponse:
        runtime = RuntimeOptions()
        return self.list_product_versions_with_options(request, runtime)

    async def list_product_versions_async(
        self,
        request: main_models.ListProductVersionsRequest,
    ) -> main_models.ListProductVersionsResponse:
        runtime = RuntimeOptions()
        return await self.list_product_versions_with_options_async(request, runtime)

    def list_products_as_admin_with_options(
        self,
        request: main_models.ListProductsAsAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsAsAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductsAsAdmin',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsAsAdminResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_as_admin_with_options_async(
        self,
        request: main_models.ListProductsAsAdminRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsAsAdminResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.portfolio_id):
            query['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductsAsAdmin',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsAsAdminResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products_as_admin(
        self,
        request: main_models.ListProductsAsAdminRequest,
    ) -> main_models.ListProductsAsAdminResponse:
        runtime = RuntimeOptions()
        return self.list_products_as_admin_with_options(request, runtime)

    async def list_products_as_admin_async(
        self,
        request: main_models.ListProductsAsAdminRequest,
    ) -> main_models.ListProductsAsAdminResponse:
        runtime = RuntimeOptions()
        return await self.list_products_as_admin_with_options_async(request, runtime)

    def list_products_as_end_user_with_options(
        self,
        request: main_models.ListProductsAsEndUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsAsEndUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductsAsEndUser',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsAsEndUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_as_end_user_with_options_async(
        self,
        request: main_models.ListProductsAsEndUserRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsAsEndUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductsAsEndUser',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsAsEndUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products_as_end_user(
        self,
        request: main_models.ListProductsAsEndUserRequest,
    ) -> main_models.ListProductsAsEndUserResponse:
        runtime = RuntimeOptions()
        return self.list_products_as_end_user_with_options(request, runtime)

    async def list_products_as_end_user_async(
        self,
        request: main_models.ListProductsAsEndUserRequest,
    ) -> main_models.ListProductsAsEndUserResponse:
        runtime = RuntimeOptions()
        return await self.list_products_as_end_user_with_options_async(request, runtime)

    def list_provisioned_product_plan_approvers_with_options(
        self,
        request: main_models.ListProvisionedProductPlanApproversRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProvisionedProductPlanApproversResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvisionedProductPlanApprovers',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvisionedProductPlanApproversResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provisioned_product_plan_approvers_with_options_async(
        self,
        request: main_models.ListProvisionedProductPlanApproversRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProvisionedProductPlanApproversResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvisionedProductPlanApprovers',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvisionedProductPlanApproversResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provisioned_product_plan_approvers(
        self,
        request: main_models.ListProvisionedProductPlanApproversRequest,
    ) -> main_models.ListProvisionedProductPlanApproversResponse:
        runtime = RuntimeOptions()
        return self.list_provisioned_product_plan_approvers_with_options(request, runtime)

    async def list_provisioned_product_plan_approvers_async(
        self,
        request: main_models.ListProvisionedProductPlanApproversRequest,
    ) -> main_models.ListProvisionedProductPlanApproversResponse:
        runtime = RuntimeOptions()
        return await self.list_provisioned_product_plan_approvers_with_options_async(request, runtime)

    def list_provisioned_product_plans_with_options(
        self,
        request: main_models.ListProvisionedProductPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProvisionedProductPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not DaraCore.is_null(request.approval_filter):
            query['ApprovalFilter'] = request.approval_filter
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvisionedProductPlans',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvisionedProductPlansResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provisioned_product_plans_with_options_async(
        self,
        request: main_models.ListProvisionedProductPlansRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProvisionedProductPlansResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not DaraCore.is_null(request.approval_filter):
            query['ApprovalFilter'] = request.approval_filter
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvisionedProductPlans',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvisionedProductPlansResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provisioned_product_plans(
        self,
        request: main_models.ListProvisionedProductPlansRequest,
    ) -> main_models.ListProvisionedProductPlansResponse:
        runtime = RuntimeOptions()
        return self.list_provisioned_product_plans_with_options(request, runtime)

    async def list_provisioned_product_plans_async(
        self,
        request: main_models.ListProvisionedProductPlansRequest,
    ) -> main_models.ListProvisionedProductPlansResponse:
        runtime = RuntimeOptions()
        return await self.list_provisioned_product_plans_with_options_async(request, runtime)

    def list_provisioned_products_with_options(
        self,
        request: main_models.ListProvisionedProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProvisionedProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvisionedProducts',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvisionedProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provisioned_products_with_options_async(
        self,
        request: main_models.ListProvisionedProductsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListProvisionedProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.access_level_filter):
            query['AccessLevelFilter'] = request.access_level_filter
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvisionedProducts',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvisionedProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provisioned_products(
        self,
        request: main_models.ListProvisionedProductsRequest,
    ) -> main_models.ListProvisionedProductsResponse:
        runtime = RuntimeOptions()
        return self.list_provisioned_products_with_options(request, runtime)

    async def list_provisioned_products_async(
        self,
        request: main_models.ListProvisionedProductsRequest,
    ) -> main_models.ListProvisionedProductsResponse:
        runtime = RuntimeOptions()
        return await self.list_provisioned_products_with_options_async(request, runtime)

    def list_regions_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_regions_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListRegionsResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListRegions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_regions(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return self.list_regions_with_options(runtime)

    async def list_regions_async(self) -> main_models.ListRegionsResponse:
        runtime = RuntimeOptions()
        return await self.list_regions_with_options_async(runtime)

    def list_resources_for_tag_option_with_options(
        self,
        request: main_models.ListResourcesForTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesForTagOptionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcesForTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesForTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_for_tag_option_with_options_async(
        self,
        request: main_models.ListResourcesForTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesForTagOptionResponse:
        request.validate()
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourcesForTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesForTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources_for_tag_option(
        self,
        request: main_models.ListResourcesForTagOptionRequest,
    ) -> main_models.ListResourcesForTagOptionResponse:
        runtime = RuntimeOptions()
        return self.list_resources_for_tag_option_with_options(request, runtime)

    async def list_resources_for_tag_option_async(
        self,
        request: main_models.ListResourcesForTagOptionRequest,
    ) -> main_models.ListResourcesForTagOptionResponse:
        runtime = RuntimeOptions()
        return await self.list_resources_for_tag_option_with_options_async(request, runtime)

    def list_tag_options_with_options(
        self,
        tmp_req: main_models.ListTagOptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagOptionsResponse:
        tmp_req.validate()
        request = main_models.ListTagOptionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filters):
            request.filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagOptions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_options_with_options_async(
        self,
        tmp_req: main_models.ListTagOptionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagOptionsResponse:
        tmp_req.validate()
        request = main_models.ListTagOptionsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.filters):
            request.filters_shrink = Utils.array_to_string_with_specified_style(tmp_req.filters, 'Filters', 'json')
        query = Utils.query(request.to_map())
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagOptions',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'GET',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagOptionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_options(
        self,
        request: main_models.ListTagOptionsRequest,
    ) -> main_models.ListTagOptionsResponse:
        runtime = RuntimeOptions()
        return self.list_tag_options_with_options(request, runtime)

    async def list_tag_options_async(
        self,
        request: main_models.ListTagOptionsRequest,
    ) -> main_models.ListTagOptionsResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_options_with_options_async(request, runtime)

    def list_tasks_with_options(
        self,
        request: main_models.ListTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tasks_with_options_async(
        self,
        request: main_models.ListTasksRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.provisioned_product_id):
            query['ProvisionedProductId'] = request.provisioned_product_id
        if not DaraCore.is_null(request.sort_by):
            query['SortBy'] = request.sort_by
        if not DaraCore.is_null(request.sort_order):
            query['SortOrder'] = request.sort_order
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTasks',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tasks(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        return self.list_tasks_with_options(request, runtime)

    async def list_tasks_async(
        self,
        request: main_models.ListTasksRequest,
    ) -> main_models.ListTasksResponse:
        runtime = RuntimeOptions()
        return await self.list_tasks_with_options_async(request, runtime)

    def terminate_provisioned_product_with_options(
        self,
        request: main_models.TerminateProvisionedProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TerminateProvisionedProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TerminateProvisionedProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateProvisionedProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def terminate_provisioned_product_with_options_async(
        self,
        request: main_models.TerminateProvisionedProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.TerminateProvisionedProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'TerminateProvisionedProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TerminateProvisionedProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def terminate_provisioned_product(
        self,
        request: main_models.TerminateProvisionedProductRequest,
    ) -> main_models.TerminateProvisionedProductResponse:
        runtime = RuntimeOptions()
        return self.terminate_provisioned_product_with_options(request, runtime)

    async def terminate_provisioned_product_async(
        self,
        request: main_models.TerminateProvisionedProductRequest,
    ) -> main_models.TerminateProvisionedProductResponse:
        runtime = RuntimeOptions()
        return await self.terminate_provisioned_product_with_options_async(request, runtime)

    def update_constraint_with_options(
        self,
        request: main_models.UpdateConstraintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConstraintResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConstraint',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConstraintResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_constraint_with_options_async(
        self,
        request: main_models.UpdateConstraintRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateConstraintResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.config):
            body['Config'] = request.config
        if not DaraCore.is_null(request.constraint_id):
            body['ConstraintId'] = request.constraint_id
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateConstraint',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateConstraintResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_constraint(
        self,
        request: main_models.UpdateConstraintRequest,
    ) -> main_models.UpdateConstraintResponse:
        runtime = RuntimeOptions()
        return self.update_constraint_with_options(request, runtime)

    async def update_constraint_async(
        self,
        request: main_models.UpdateConstraintRequest,
    ) -> main_models.UpdateConstraintResponse:
        runtime = RuntimeOptions()
        return await self.update_constraint_with_options_async(request, runtime)

    def update_portfolio_with_options(
        self,
        request: main_models.UpdatePortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePortfolioResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_portfolio_with_options_async(
        self,
        request: main_models.UpdatePortfolioRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePortfolioResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.portfolio_name):
            body['PortfolioName'] = request.portfolio_name
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePortfolio',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePortfolioResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_portfolio(
        self,
        request: main_models.UpdatePortfolioRequest,
    ) -> main_models.UpdatePortfolioResponse:
        runtime = RuntimeOptions()
        return self.update_portfolio_with_options(request, runtime)

    async def update_portfolio_async(
        self,
        request: main_models.UpdatePortfolioRequest,
    ) -> main_models.UpdatePortfolioResponse:
        runtime = RuntimeOptions()
        return await self.update_portfolio_with_options_async(request, runtime)

    def update_product_with_options(
        self,
        request: main_models.UpdateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_with_options_async(
        self,
        request: main_models.UpdateProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_name):
            body['ProductName'] = request.product_name
        if not DaraCore.is_null(request.provider_name):
            body['ProviderName'] = request.provider_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product(
        self,
        request: main_models.UpdateProductRequest,
    ) -> main_models.UpdateProductResponse:
        runtime = RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    async def update_product_async(
        self,
        request: main_models.UpdateProductRequest,
    ) -> main_models.UpdateProductResponse:
        runtime = RuntimeOptions()
        return await self.update_product_with_options_async(request, runtime)

    def update_product_version_with_options(
        self,
        request: main_models.UpdateProductVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.active):
            body['Active'] = request.active
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.guidance):
            body['Guidance'] = request.guidance
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProductVersion',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProductVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_version_with_options_async(
        self,
        request: main_models.UpdateProductVersionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductVersionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.active):
            body['Active'] = request.active
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.guidance):
            body['Guidance'] = request.guidance
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.product_version_name):
            body['ProductVersionName'] = request.product_version_name
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProductVersion',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProductVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_product_version(
        self,
        request: main_models.UpdateProductVersionRequest,
    ) -> main_models.UpdateProductVersionResponse:
        runtime = RuntimeOptions()
        return self.update_product_version_with_options(request, runtime)

    async def update_product_version_async(
        self,
        request: main_models.UpdateProductVersionRequest,
    ) -> main_models.UpdateProductVersionResponse:
        runtime = RuntimeOptions()
        return await self.update_product_version_with_options_async(request, runtime)

    def update_provisioned_product_with_options(
        self,
        request: main_models.UpdateProvisionedProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProvisionedProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProvisionedProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProvisionedProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_provisioned_product_with_options_async(
        self,
        request: main_models.UpdateProvisionedProductRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProvisionedProductResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.provisioned_product_id):
            body['ProvisionedProductId'] = request.provisioned_product_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProvisionedProduct',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProvisionedProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_provisioned_product(
        self,
        request: main_models.UpdateProvisionedProductRequest,
    ) -> main_models.UpdateProvisionedProductResponse:
        runtime = RuntimeOptions()
        return self.update_provisioned_product_with_options(request, runtime)

    async def update_provisioned_product_async(
        self,
        request: main_models.UpdateProvisionedProductRequest,
    ) -> main_models.UpdateProvisionedProductResponse:
        runtime = RuntimeOptions()
        return await self.update_provisioned_product_with_options_async(request, runtime)

    def update_provisioned_product_plan_with_options(
        self,
        request: main_models.UpdateProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProvisionedProductPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_provisioned_product_plan_with_options_async(
        self,
        request: main_models.UpdateProvisionedProductPlanRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProvisionedProductPlanResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['Description'] = request.description
        if not DaraCore.is_null(request.parameters):
            body['Parameters'] = request.parameters
        if not DaraCore.is_null(request.plan_id):
            body['PlanId'] = request.plan_id
        if not DaraCore.is_null(request.portfolio_id):
            body['PortfolioId'] = request.portfolio_id
        if not DaraCore.is_null(request.product_id):
            body['ProductId'] = request.product_id
        if not DaraCore.is_null(request.product_version_id):
            body['ProductVersionId'] = request.product_version_id
        if not DaraCore.is_null(request.tags):
            body['Tags'] = request.tags
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProvisionedProductPlan',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProvisionedProductPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_provisioned_product_plan(
        self,
        request: main_models.UpdateProvisionedProductPlanRequest,
    ) -> main_models.UpdateProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return self.update_provisioned_product_plan_with_options(request, runtime)

    async def update_provisioned_product_plan_async(
        self,
        request: main_models.UpdateProvisionedProductPlanRequest,
    ) -> main_models.UpdateProvisionedProductPlanResponse:
        runtime = RuntimeOptions()
        return await self.update_provisioned_product_plan_with_options_async(request, runtime)

    def update_tag_option_with_options(
        self,
        request: main_models.UpdateTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTagOptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.active):
            body['Active'] = request.active
        if not DaraCore.is_null(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTagOptionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_tag_option_with_options_async(
        self,
        request: main_models.UpdateTagOptionRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateTagOptionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.active):
            body['Active'] = request.active
        if not DaraCore.is_null(request.tag_option_id):
            body['TagOptionId'] = request.tag_option_id
        if not DaraCore.is_null(request.value):
            body['Value'] = request.value
        req = open_api_util_models.OpenApiRequest(
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateTagOption',
            version = '2021-09-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateTagOptionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_tag_option(
        self,
        request: main_models.UpdateTagOptionRequest,
    ) -> main_models.UpdateTagOptionResponse:
        runtime = RuntimeOptions()
        return self.update_tag_option_with_options(request, runtime)

    async def update_tag_option_async(
        self,
        request: main_models.UpdateTagOptionRequest,
    ) -> main_models.UpdateTagOptionResponse:
        runtime = RuntimeOptions()
        return await self.update_tag_option_with_options_async(request, runtime)
