# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_neuron20211115 import models as main_models
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
        self._endpoint_map = {
            'ap-northeast-1': 'neuron.aliyuncs.com',
            'ap-northeast-2-pop': 'neuron.aliyuncs.com',
            'ap-south-1': 'neuron.aliyuncs.com',
            'ap-southeast-1': 'neuron.aliyuncs.com',
            'ap-southeast-2': 'neuron.aliyuncs.com',
            'ap-southeast-3': 'neuron.aliyuncs.com',
            'ap-southeast-5': 'neuron.aliyuncs.com',
            'cn-beijing': 'neuron.aliyuncs.com',
            'cn-beijing-finance-1': 'neuron.aliyuncs.com',
            'cn-beijing-finance-pop': 'neuron.aliyuncs.com',
            'cn-beijing-gov-1': 'neuron.aliyuncs.com',
            'cn-beijing-nu16-b01': 'neuron.aliyuncs.com',
            'cn-chengdu': 'neuron.aliyuncs.com',
            'cn-edge-1': 'neuron.aliyuncs.com',
            'cn-fujian': 'neuron.aliyuncs.com',
            'cn-haidian-cm12-c01': 'neuron.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'neuron.aliyuncs.com',
            'cn-hangzhou-finance': 'neuron.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'neuron.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'neuron.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'neuron.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'neuron.aliyuncs.com',
            'cn-hangzhou-test-306': 'neuron.aliyuncs.com',
            'cn-hongkong': 'neuron.aliyuncs.com',
            'cn-hongkong-finance-pop': 'neuron.aliyuncs.com',
            'cn-huhehaote': 'neuron.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'neuron.aliyuncs.com',
            'cn-north-2-gov-1': 'neuron.aliyuncs.com',
            'cn-qingdao': 'neuron.aliyuncs.com',
            'cn-qingdao-nebula': 'neuron.aliyuncs.com',
            'cn-shanghai': 'neuron.aliyuncs.com',
            'cn-shanghai-et15-b01': 'neuron.aliyuncs.com',
            'cn-shanghai-et2-b01': 'neuron.aliyuncs.com',
            'cn-shanghai-finance-1': 'neuron.aliyuncs.com',
            'cn-shanghai-inner': 'neuron.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'neuron.aliyuncs.com',
            'cn-shenzhen': 'neuron.aliyuncs.com',
            'cn-shenzhen-finance-1': 'neuron.aliyuncs.com',
            'cn-shenzhen-inner': 'neuron.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'neuron.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'neuron.aliyuncs.com',
            'cn-wuhan': 'neuron.aliyuncs.com',
            'cn-wulanchabu': 'neuron.aliyuncs.com',
            'cn-yushanfang': 'neuron.aliyuncs.com',
            'cn-zhangbei': 'neuron.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'neuron.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'neuron.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'neuron.aliyuncs.com',
            'eu-central-1': 'neuron.aliyuncs.com',
            'eu-west-1': 'neuron.aliyuncs.com',
            'eu-west-1-oxs': 'neuron.aliyuncs.com',
            'me-east-1': 'neuron.aliyuncs.com',
            'rus-west-1-pop': 'neuron.aliyuncs.com',
            'us-east-1': 'neuron.aliyuncs.com',
            'us-west-1': 'neuron.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('neuron', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_or_quit_pdp_lane_for_service_group_with_options(
        self,
        request: main_models.AddOrQuitPdpLaneForServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddOrQuitPdpLaneForServiceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrQuitPdpLaneForServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/add-quit-lane',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrQuitPdpLaneForServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_or_quit_pdp_lane_for_service_group_with_options_async(
        self,
        request: main_models.AddOrQuitPdpLaneForServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AddOrQuitPdpLaneForServiceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'AddOrQuitPdpLaneForServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/add-quit-lane',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddOrQuitPdpLaneForServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_or_quit_pdp_lane_for_service_group(
        self,
        request: main_models.AddOrQuitPdpLaneForServiceGroupRequest,
    ) -> main_models.AddOrQuitPdpLaneForServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.add_or_quit_pdp_lane_for_service_group_with_options(request, headers, runtime)

    async def add_or_quit_pdp_lane_for_service_group_async(
        self,
        request: main_models.AddOrQuitPdpLaneForServiceGroupRequest,
    ) -> main_models.AddOrQuitPdpLaneForServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.add_or_quit_pdp_lane_for_service_group_with_options_async(request, headers, runtime)

    def audit_fork_review_with_options(
        self,
        review_id: str,
        request: main_models.AuditForkReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuditForkReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'AuditForkReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/fork-reviews/{DaraURL.percent_encode(review_id)}/commands/audit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditForkReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def audit_fork_review_with_options_async(
        self,
        review_id: str,
        request: main_models.AuditForkReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuditForkReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'AuditForkReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/fork-reviews/{DaraURL.percent_encode(review_id)}/commands/audit',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditForkReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def audit_fork_review(
        self,
        review_id: str,
        request: main_models.AuditForkReviewRequest,
    ) -> main_models.AuditForkReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.audit_fork_review_with_options(review_id, request, headers, runtime)

    async def audit_fork_review_async(
        self,
        review_id: str,
        request: main_models.AuditForkReviewRequest,
    ) -> main_models.AuditForkReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.audit_fork_review_with_options_async(review_id, request, headers, runtime)

    def audit_pbc_invoke_review_with_options(
        self,
        review_id: str,
        request: main_models.AuditPbcInvokeReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuditPbcInvokeReviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approve):
            body['approve'] = request.approve
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuditPbcInvokeReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invoke-reviews/{DaraURL.percent_encode(review_id)}/commands/audit',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditPbcInvokeReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def audit_pbc_invoke_review_with_options_async(
        self,
        review_id: str,
        request: main_models.AuditPbcInvokeReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuditPbcInvokeReviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approve):
            body['approve'] = request.approve
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AuditPbcInvokeReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invoke-reviews/{DaraURL.percent_encode(review_id)}/commands/audit',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuditPbcInvokeReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def audit_pbc_invoke_review(
        self,
        review_id: str,
        request: main_models.AuditPbcInvokeReviewRequest,
    ) -> main_models.AuditPbcInvokeReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.audit_pbc_invoke_review_with_options(review_id, request, headers, runtime)

    async def audit_pbc_invoke_review_async(
        self,
        review_id: str,
        request: main_models.AuditPbcInvokeReviewRequest,
    ) -> main_models.AuditPbcInvokeReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.audit_pbc_invoke_review_with_options_async(review_id, request, headers, runtime)

    def authorize_products_with_options(
        self,
        request: main_models.AuthorizeProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeProductsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeProducts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products/commands/authorize',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def authorize_products_with_options_async(
        self,
        request: main_models.AuthorizeProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AuthorizeProductsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'AuthorizeProducts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products/commands/authorize',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AuthorizeProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def authorize_products(
        self,
        request: main_models.AuthorizeProductsRequest,
    ) -> main_models.AuthorizeProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.authorize_products_with_options(request, headers, runtime)

    async def authorize_products_async(
        self,
        request: main_models.AuthorizeProductsRequest,
    ) -> main_models.AuthorizeProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.authorize_products_with_options_async(request, headers, runtime)

    def batch_grant_roles_to_developer_with_options(
        self,
        request: main_models.BatchGrantRolesToDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGrantRolesToDeveloperResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'BatchGrantRolesToDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/commands/batch-grant-roles',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.BatchGrantRolesToDeveloperResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_grant_roles_to_developer_with_options_async(
        self,
        request: main_models.BatchGrantRolesToDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGrantRolesToDeveloperResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'BatchGrantRolesToDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/commands/batch-grant-roles',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.BatchGrantRolesToDeveloperResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_grant_roles_to_developer(
        self,
        request: main_models.BatchGrantRolesToDeveloperRequest,
    ) -> main_models.BatchGrantRolesToDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_grant_roles_to_developer_with_options(request, headers, runtime)

    async def batch_grant_roles_to_developer_async(
        self,
        request: main_models.BatchGrantRolesToDeveloperRequest,
    ) -> main_models.BatchGrantRolesToDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_grant_roles_to_developer_with_options_async(request, headers, runtime)

    def check_developer_role_with_options(
        self,
        request: main_models.CheckDeveloperRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckDeveloperRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['accountId'] = request.account_id
        if not DaraCore.is_null(request.company_id):
            body['companyId'] = request.company_id
        if not DaraCore.is_null(request.platform):
            body['platform'] = request.platform
        if not DaraCore.is_null(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckDeveloperRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/commands/check-role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDeveloperRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def check_developer_role_with_options_async(
        self,
        request: main_models.CheckDeveloperRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CheckDeveloperRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['accountId'] = request.account_id
        if not DaraCore.is_null(request.company_id):
            body['companyId'] = request.company_id
        if not DaraCore.is_null(request.platform):
            body['platform'] = request.platform
        if not DaraCore.is_null(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CheckDeveloperRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/commands/check-role',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CheckDeveloperRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def check_developer_role(
        self,
        request: main_models.CheckDeveloperRoleRequest,
    ) -> main_models.CheckDeveloperRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.check_developer_role_with_options(request, headers, runtime)

    async def check_developer_role_async(
        self,
        request: main_models.CheckDeveloperRoleRequest,
    ) -> main_models.CheckDeveloperRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.check_developer_role_with_options_async(request, headers, runtime)

    def complete_register_library_with_options(
        self,
        id: str,
        request: main_models.CompleteRegisterLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompleteRegisterLibraryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.depend_integral):
            body['dependIntegral'] = request.depend_integral
        if not DaraCore.is_null(request.market_id):
            body['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompleteRegisterLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}/commands/complete-register',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteRegisterLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_register_library_with_options_async(
        self,
        id: str,
        request: main_models.CompleteRegisterLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompleteRegisterLibraryResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.depend_integral):
            body['dependIntegral'] = request.depend_integral
        if not DaraCore.is_null(request.market_id):
            body['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CompleteRegisterLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}/commands/complete-register',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteRegisterLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_register_library(
        self,
        id: str,
        request: main_models.CompleteRegisterLibraryRequest,
    ) -> main_models.CompleteRegisterLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.complete_register_library_with_options(id, request, headers, runtime)

    async def complete_register_library_async(
        self,
        id: str,
        request: main_models.CompleteRegisterLibraryRequest,
    ) -> main_models.CompleteRegisterLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.complete_register_library_with_options_async(id, request, headers, runtime)

    def complete_registration_pbc_version_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompleteRegistrationPbcVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CompleteRegistrationPbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}/commands/complete-register',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteRegistrationPbcVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def complete_registration_pbc_version_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CompleteRegistrationPbcVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'CompleteRegistrationPbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}/commands/complete-register',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CompleteRegistrationPbcVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def complete_registration_pbc_version(
        self,
        id: str,
    ) -> main_models.CompleteRegistrationPbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.complete_registration_pbc_version_with_options(id, headers, runtime)

    async def complete_registration_pbc_version_async(
        self,
        id: str,
    ) -> main_models.CompleteRegistrationPbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.complete_registration_pbc_version_with_options_async(id, headers, runtime)

    def continue_deployment_with_options(
        self,
        request: main_models.ContinueDeploymentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ContinueDeploymentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ContinueDeployment',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/commands/continue',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def continue_deployment_with_options_async(
        self,
        request: main_models.ContinueDeploymentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ContinueDeploymentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ContinueDeployment',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/commands/continue',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ContinueDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def continue_deployment(
        self,
        request: main_models.ContinueDeploymentRequest,
    ) -> main_models.ContinueDeploymentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.continue_deployment_with_options(request, headers, runtime)

    async def continue_deployment_async(
        self,
        request: main_models.ContinueDeploymentRequest,
    ) -> main_models.ContinueDeploymentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.continue_deployment_with_options_async(request, headers, runtime)

    def create_asset_watch_with_options(
        self,
        request: main_models.CreateAssetWatchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAssetWatchResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAssetWatch',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/asset-watchs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAssetWatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_asset_watch_with_options_async(
        self,
        request: main_models.CreateAssetWatchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateAssetWatchResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateAssetWatch',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/asset-watchs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAssetWatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_asset_watch(
        self,
        request: main_models.CreateAssetWatchRequest,
    ) -> main_models.CreateAssetWatchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_asset_watch_with_options(request, headers, runtime)

    async def create_asset_watch_async(
        self,
        request: main_models.CreateAssetWatchRequest,
    ) -> main_models.CreateAssetWatchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_asset_watch_with_options_async(request, headers, runtime)

    def create_component_with_options(
        self,
        request: main_models.CreateComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponent',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_component_with_options_async(
        self,
        request: main_models.CreateComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponent',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_component(
        self,
        request: main_models.CreateComponentRequest,
    ) -> main_models.CreateComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_component_with_options(request, headers, runtime)

    async def create_component_async(
        self,
        request: main_models.CreateComponentRequest,
    ) -> main_models.CreateComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_component_with_options_async(request, headers, runtime)

    def create_component_template_with_options(
        self,
        request: main_models.CreateComponentTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponentTemplate',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_component_template_with_options_async(
        self,
        request: main_models.CreateComponentTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateComponentTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateComponentTemplate',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateComponentTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_component_template(
        self,
        request: main_models.CreateComponentTemplateRequest,
    ) -> main_models.CreateComponentTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_component_template_with_options(request, headers, runtime)

    async def create_component_template_async(
        self,
        request: main_models.CreateComponentTemplateRequest,
    ) -> main_models.CreateComponentTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_component_template_with_options_async(request, headers, runtime)

    def create_developer_with_options(
        self,
        request: main_models.CreateDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeveloperResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeveloperResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_developer_with_options_async(
        self,
        request: main_models.CreateDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeveloperResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeveloperResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_developer(
        self,
        request: main_models.CreateDeveloperRequest,
    ) -> main_models.CreateDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_developer_with_options(request, headers, runtime)

    async def create_developer_async(
        self,
        request: main_models.CreateDeveloperRequest,
    ) -> main_models.CreateDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_developer_with_options_async(request, headers, runtime)

    def create_enterprise_with_options(
        self,
        request: main_models.CreateEnterpriseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_enterprise_with_options_async(
        self,
        request: main_models.CreateEnterpriseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateEnterpriseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_enterprise(
        self,
        request: main_models.CreateEnterpriseRequest,
    ) -> main_models.CreateEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_enterprise_with_options(request, headers, runtime)

    async def create_enterprise_async(
        self,
        request: main_models.CreateEnterpriseRequest,
    ) -> main_models.CreateEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_enterprise_with_options_async(request, headers, runtime)

    def create_fork_review_with_options(
        self,
        request: main_models.CreateForkReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateForkReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateForkReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/fork-reviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateForkReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_fork_review_with_options_async(
        self,
        request: main_models.CreateForkReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateForkReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateForkReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/fork-reviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateForkReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_fork_review(
        self,
        request: main_models.CreateForkReviewRequest,
    ) -> main_models.CreateForkReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_fork_review_with_options(request, headers, runtime)

    async def create_fork_review_async(
        self,
        request: main_models.CreateForkReviewRequest,
    ) -> main_models.CreateForkReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_fork_review_with_options_async(request, headers, runtime)

    def create_grey_pdp_service_group_with_options(
        self,
        request: main_models.CreateGreyPdpServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGreyPdpServiceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGreyPdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups/grey',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGreyPdpServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_grey_pdp_service_group_with_options_async(
        self,
        request: main_models.CreateGreyPdpServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateGreyPdpServiceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateGreyPdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups/grey',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateGreyPdpServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_grey_pdp_service_group(
        self,
        request: main_models.CreateGreyPdpServiceGroupRequest,
    ) -> main_models.CreateGreyPdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_grey_pdp_service_group_with_options(request, headers, runtime)

    async def create_grey_pdp_service_group_async(
        self,
        request: main_models.CreateGreyPdpServiceGroupRequest,
    ) -> main_models.CreateGreyPdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_grey_pdp_service_group_with_options_async(request, headers, runtime)

    def create_library_with_options(
        self,
        request: main_models.CreateLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibraryResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_library_with_options_async(
        self,
        request: main_models.CreateLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibraryResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_library(
        self,
        request: main_models.CreateLibraryRequest,
    ) -> main_models.CreateLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_library_with_options(request, headers, runtime)

    async def create_library_async(
        self,
        request: main_models.CreateLibraryRequest,
    ) -> main_models.CreateLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_library_with_options_async(request, headers, runtime)

    def create_library_instruction_with_options(
        self,
        library_id: str,
        request: main_models.CreateLibraryInstructionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibraryInstructionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.company_id):
            body['companyId'] = request.company_id
        if not DaraCore.is_null(request.document):
            body['document'] = request.document
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.market_id):
            body['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibraryInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/instructions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibraryInstructionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_library_instruction_with_options_async(
        self,
        library_id: str,
        request: main_models.CreateLibraryInstructionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibraryInstructionResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.company_id):
            body['companyId'] = request.company_id
        if not DaraCore.is_null(request.document):
            body['document'] = request.document
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        if not DaraCore.is_null(request.library_id):
            body['libraryId'] = request.library_id
        if not DaraCore.is_null(request.market_id):
            body['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibraryInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/instructions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibraryInstructionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_library_instruction(
        self,
        library_id: str,
        request: main_models.CreateLibraryInstructionRequest,
    ) -> main_models.CreateLibraryInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_library_instruction_with_options(library_id, request, headers, runtime)

    async def create_library_instruction_async(
        self,
        library_id: str,
        request: main_models.CreateLibraryInstructionRequest,
    ) -> main_models.CreateLibraryInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_library_instruction_with_options_async(library_id, request, headers, runtime)

    def create_library_review_with_options(
        self,
        request: main_models.CreateLibraryReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibraryReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibraryReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibraryReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_library_review_with_options_async(
        self,
        request: main_models.CreateLibraryReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibraryReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibraryReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibraryReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_library_review(
        self,
        request: main_models.CreateLibraryReviewRequest,
    ) -> main_models.CreateLibraryReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_library_review_with_options(request, headers, runtime)

    async def create_library_review_async(
        self,
        request: main_models.CreateLibraryReviewRequest,
    ) -> main_models.CreateLibraryReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_library_review_with_options_async(request, headers, runtime)

    def create_library_schema_with_options(
        self,
        request: main_models.CreateLibrarySchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibrarySchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibrarySchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/schemas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibrarySchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_library_schema_with_options_async(
        self,
        request: main_models.CreateLibrarySchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateLibrarySchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateLibrarySchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/schemas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateLibrarySchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_library_schema(
        self,
        request: main_models.CreateLibrarySchemaRequest,
    ) -> main_models.CreateLibrarySchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_library_schema_with_options(request, headers, runtime)

    async def create_library_schema_async(
        self,
        request: main_models.CreateLibrarySchemaRequest,
    ) -> main_models.CreateLibrarySchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_library_schema_with_options_async(request, headers, runtime)

    def create_monitor_arms_alert_with_options(
        self,
        request: main_models.CreateMonitorArmsAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorArmsAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorArmsAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorArmsAlert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorArmsAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_arms_alert_with_options_async(
        self,
        request: main_models.CreateMonitorArmsAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorArmsAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorArmsAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorArmsAlert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorArmsAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_arms_alert(
        self,
        request: main_models.CreateMonitorArmsAlertRequest,
    ) -> main_models.CreateMonitorArmsAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_arms_alert_with_options(request, headers, runtime)

    async def create_monitor_arms_alert_async(
        self,
        request: main_models.CreateMonitorArmsAlertRequest,
    ) -> main_models.CreateMonitorArmsAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_arms_alert_with_options_async(request, headers, runtime)

    def create_monitor_arms_alerts_with_options(
        self,
        request: main_models.CreateMonitorArmsAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorArmsAlertsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorArmsAlerts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorArmsAlerts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorArmsAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_arms_alerts_with_options_async(
        self,
        request: main_models.CreateMonitorArmsAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorArmsAlertsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorArmsAlerts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorArmsAlerts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorArmsAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_arms_alerts(
        self,
        request: main_models.CreateMonitorArmsAlertsRequest,
    ) -> main_models.CreateMonitorArmsAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_arms_alerts_with_options(request, headers, runtime)

    async def create_monitor_arms_alerts_async(
        self,
        request: main_models.CreateMonitorArmsAlertsRequest,
    ) -> main_models.CreateMonitorArmsAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_arms_alerts_with_options_async(request, headers, runtime)

    def create_monitor_contact_with_options(
        self,
        request: main_models.CreateMonitorContactRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorContactResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorContact',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_contact_with_options_async(
        self,
        request: main_models.CreateMonitorContactRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorContactResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorContact',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_contact(
        self,
        request: main_models.CreateMonitorContactRequest,
    ) -> main_models.CreateMonitorContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_contact_with_options(request, headers, runtime)

    async def create_monitor_contact_async(
        self,
        request: main_models.CreateMonitorContactRequest,
    ) -> main_models.CreateMonitorContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_contact_with_options_async(request, headers, runtime)

    def create_monitor_contact_group_with_options(
        self,
        request: main_models.CreateMonitorContactGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorContactGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorContactGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_contact_group_with_options_async(
        self,
        request: main_models.CreateMonitorContactGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorContactGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorContactGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_contact_group(
        self,
        request: main_models.CreateMonitorContactGroupRequest,
    ) -> main_models.CreateMonitorContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_contact_group_with_options(request, headers, runtime)

    async def create_monitor_contact_group_async(
        self,
        request: main_models.CreateMonitorContactGroupRequest,
    ) -> main_models.CreateMonitorContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_contact_group_with_options_async(request, headers, runtime)

    def create_monitor_group_member_with_options(
        self,
        group_id: str,
        request: main_models.CreateMonitorGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupMemberResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroupMember',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group/{DaraURL.percent_encode(group_id)}/commands/create-member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_group_member_with_options_async(
        self,
        group_id: str,
        request: main_models.CreateMonitorGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorGroupMemberResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorGroupMember',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group/{DaraURL.percent_encode(group_id)}/commands/create-member',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_group_member(
        self,
        group_id: str,
        request: main_models.CreateMonitorGroupMemberRequest,
    ) -> main_models.CreateMonitorGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_group_member_with_options(group_id, request, headers, runtime)

    async def create_monitor_group_member_async(
        self,
        group_id: str,
        request: main_models.CreateMonitorGroupMemberRequest,
    ) -> main_models.CreateMonitorGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_group_member_with_options_async(group_id, request, headers, runtime)

    def create_monitor_mq_alert_with_options(
        self,
        request: main_models.CreateMonitorMqAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorMqAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorMqAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorMqAlert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorMqAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_mq_alert_with_options_async(
        self,
        request: main_models.CreateMonitorMqAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorMqAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorMqAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorMqAlert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorMqAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_mq_alert(
        self,
        request: main_models.CreateMonitorMqAlertRequest,
    ) -> main_models.CreateMonitorMqAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_mq_alert_with_options(request, headers, runtime)

    async def create_monitor_mq_alert_async(
        self,
        request: main_models.CreateMonitorMqAlertRequest,
    ) -> main_models.CreateMonitorMqAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_mq_alert_with_options_async(request, headers, runtime)

    def create_monitor_mq_alerts_with_options(
        self,
        request: main_models.CreateMonitorMqAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorMqAlertsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorMqAlerts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorMqAlerts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorMqAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_mq_alerts_with_options_async(
        self,
        request: main_models.CreateMonitorMqAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorMqAlertsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorMqAlerts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorMqAlerts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorMqAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_mq_alerts(
        self,
        request: main_models.CreateMonitorMqAlertsRequest,
    ) -> main_models.CreateMonitorMqAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_mq_alerts_with_options(request, headers, runtime)

    async def create_monitor_mq_alerts_async(
        self,
        request: main_models.CreateMonitorMqAlertsRequest,
    ) -> main_models.CreateMonitorMqAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_mq_alerts_with_options_async(request, headers, runtime)

    def create_monitor_sls_alert_with_options(
        self,
        request: main_models.CreateMonitorSlsAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorSlsAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorSlsAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorSlsAlert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorSlsAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_sls_alert_with_options_async(
        self,
        request: main_models.CreateMonitorSlsAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorSlsAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorSlsAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorSlsAlert',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorSlsAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_sls_alert(
        self,
        request: main_models.CreateMonitorSlsAlertRequest,
    ) -> main_models.CreateMonitorSlsAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_sls_alert_with_options(request, headers, runtime)

    async def create_monitor_sls_alert_async(
        self,
        request: main_models.CreateMonitorSlsAlertRequest,
    ) -> main_models.CreateMonitorSlsAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_sls_alert_with_options_async(request, headers, runtime)

    def create_monitor_sls_alerts_with_options(
        self,
        request: main_models.CreateMonitorSlsAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorSlsAlertsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorSlsAlerts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorSlsAlerts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorSlsAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_sls_alerts_with_options_async(
        self,
        request: main_models.CreateMonitorSlsAlertsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorSlsAlertsResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorSlsAlerts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/createMonitorSlsAlerts',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorSlsAlertsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_sls_alerts(
        self,
        request: main_models.CreateMonitorSlsAlertsRequest,
    ) -> main_models.CreateMonitorSlsAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_sls_alerts_with_options(request, headers, runtime)

    async def create_monitor_sls_alerts_async(
        self,
        request: main_models.CreateMonitorSlsAlertsRequest,
    ) -> main_models.CreateMonitorSlsAlertsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_sls_alerts_with_options_async(request, headers, runtime)

    def create_monitor_webhook_with_options(
        self,
        request: main_models.CreateMonitorWebhookRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorWebhookResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorWebhook',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_monitor_webhook_with_options_async(
        self,
        request: main_models.CreateMonitorWebhookRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMonitorWebhookResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMonitorWebhook',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMonitorWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_monitor_webhook(
        self,
        request: main_models.CreateMonitorWebhookRequest,
    ) -> main_models.CreateMonitorWebhookResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_monitor_webhook_with_options(request, headers, runtime)

    async def create_monitor_webhook_async(
        self,
        request: main_models.CreateMonitorWebhookRequest,
    ) -> main_models.CreateMonitorWebhookResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_monitor_webhook_with_options_async(request, headers, runtime)

    def create_mq_group_with_options(
        self,
        request: main_models.CreateMqGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMqGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMqGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMqGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mq_group_with_options_async(
        self,
        request: main_models.CreateMqGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMqGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMqGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/group',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMqGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mq_group(
        self,
        request: main_models.CreateMqGroupRequest,
    ) -> main_models.CreateMqGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_mq_group_with_options(request, headers, runtime)

    async def create_mq_group_async(
        self,
        request: main_models.CreateMqGroupRequest,
    ) -> main_models.CreateMqGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_mq_group_with_options_async(request, headers, runtime)

    def create_mq_topic_with_options(
        self,
        request: main_models.CreateMqTopicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMqTopicResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMqTopic',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMqTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_mq_topic_with_options_async(
        self,
        request: main_models.CreateMqTopicRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateMqTopicResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateMqTopic',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMqTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_mq_topic(
        self,
        request: main_models.CreateMqTopicRequest,
    ) -> main_models.CreateMqTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_mq_topic_with_options(request, headers, runtime)

    async def create_mq_topic_async(
        self,
        request: main_models.CreateMqTopicRequest,
    ) -> main_models.CreateMqTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_mq_topic_with_options_async(request, headers, runtime)

    def create_pbc_with_options(
        self,
        request: main_models.CreatePbcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pbc_with_options_async(
        self,
        request: main_models.CreatePbcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pbc(
        self,
        request: main_models.CreatePbcRequest,
    ) -> main_models.CreatePbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pbc_with_options(request, headers, runtime)

    async def create_pbc_async(
        self,
        request: main_models.CreatePbcRequest,
    ) -> main_models.CreatePbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pbc_with_options_async(request, headers, runtime)

    def create_pbc_api_schema_with_options(
        self,
        request: main_models.CreatePbcApiSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcApiSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcApiSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/api-schemas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcApiSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pbc_api_schema_with_options_async(
        self,
        request: main_models.CreatePbcApiSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcApiSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcApiSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/api-schemas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcApiSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pbc_api_schema(
        self,
        request: main_models.CreatePbcApiSchemaRequest,
    ) -> main_models.CreatePbcApiSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pbc_api_schema_with_options(request, headers, runtime)

    async def create_pbc_api_schema_async(
        self,
        request: main_models.CreatePbcApiSchemaRequest,
    ) -> main_models.CreatePbcApiSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pbc_api_schema_with_options_async(request, headers, runtime)

    def create_pbc_instruction_with_options(
        self,
        request: main_models.CreatePbcInstructionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcInstructionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/instructions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcInstructionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pbc_instruction_with_options_async(
        self,
        request: main_models.CreatePbcInstructionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcInstructionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/instructions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcInstructionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pbc_instruction(
        self,
        request: main_models.CreatePbcInstructionRequest,
    ) -> main_models.CreatePbcInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pbc_instruction_with_options(request, headers, runtime)

    async def create_pbc_instruction_async(
        self,
        request: main_models.CreatePbcInstructionRequest,
    ) -> main_models.CreatePbcInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pbc_instruction_with_options_async(request, headers, runtime)

    def create_pbc_invoke_with_options(
        self,
        request: main_models.CreatePbcInvokeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcInvokeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcInvoke',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invokes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pbc_invoke_with_options_async(
        self,
        request: main_models.CreatePbcInvokeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcInvokeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcInvoke',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invokes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pbc_invoke(
        self,
        request: main_models.CreatePbcInvokeRequest,
    ) -> main_models.CreatePbcInvokeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pbc_invoke_with_options(request, headers, runtime)

    async def create_pbc_invoke_async(
        self,
        request: main_models.CreatePbcInvokeRequest,
    ) -> main_models.CreatePbcInvokeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pbc_invoke_with_options_async(request, headers, runtime)

    def create_pbc_invoke_review_with_options(
        self,
        request: main_models.CreatePbcInvokeReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcInvokeReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcInvokeReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invoke-reviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcInvokeReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pbc_invoke_review_with_options_async(
        self,
        request: main_models.CreatePbcInvokeReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcInvokeReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcInvokeReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invoke-reviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcInvokeReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pbc_invoke_review(
        self,
        request: main_models.CreatePbcInvokeReviewRequest,
    ) -> main_models.CreatePbcInvokeReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pbc_invoke_review_with_options(request, headers, runtime)

    async def create_pbc_invoke_review_async(
        self,
        request: main_models.CreatePbcInvokeReviewRequest,
    ) -> main_models.CreatePbcInvokeReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pbc_invoke_review_with_options_async(request, headers, runtime)

    def create_pbc_review_with_options(
        self,
        request: main_models.CreatePbcReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pbc_review_with_options_async(
        self,
        request: main_models.CreatePbcReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pbc_review(
        self,
        request: main_models.CreatePbcReviewRequest,
    ) -> main_models.CreatePbcReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pbc_review_with_options(request, headers, runtime)

    async def create_pbc_review_async(
        self,
        request: main_models.CreatePbcReviewRequest,
    ) -> main_models.CreatePbcReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pbc_review_with_options_async(request, headers, runtime)

    def create_pbc_schema_with_options(
        self,
        request: main_models.CreatePbcSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/schemas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pbc_schema_with_options_async(
        self,
        request: main_models.CreatePbcSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/schemas',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pbc_schema(
        self,
        request: main_models.CreatePbcSchemaRequest,
    ) -> main_models.CreatePbcSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pbc_schema_with_options(request, headers, runtime)

    async def create_pbc_schema_async(
        self,
        request: main_models.CreatePbcSchemaRequest,
    ) -> main_models.CreatePbcSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pbc_schema_with_options_async(request, headers, runtime)

    def create_pbc_version_with_options(
        self,
        request: main_models.CreatePbcVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pbc_version_with_options_async(
        self,
        request: main_models.CreatePbcVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePbcVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePbcVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pbc_version(
        self,
        request: main_models.CreatePbcVersionRequest,
    ) -> main_models.CreatePbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pbc_version_with_options(request, headers, runtime)

    async def create_pbc_version_async(
        self,
        request: main_models.CreatePbcVersionRequest,
    ) -> main_models.CreatePbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pbc_version_with_options_async(request, headers, runtime)

    def create_pdp_config_with_options(
        self,
        request: main_models.CreatePdpConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdp_config_with_options_async(
        self,
        request: main_models.CreatePdpConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdp_config(
        self,
        request: main_models.CreatePdpConfigRequest,
    ) -> main_models.CreatePdpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pdp_config_with_options(request, headers, runtime)

    async def create_pdp_config_async(
        self,
        request: main_models.CreatePdpConfigRequest,
    ) -> main_models.CreatePdpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pdp_config_with_options_async(request, headers, runtime)

    def create_pdp_lane_with_options(
        self,
        request: main_models.CreatePdpLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpLaneResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpLane',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdp_lane_with_options_async(
        self,
        request: main_models.CreatePdpLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpLaneResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpLane',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdp_lane(
        self,
        request: main_models.CreatePdpLaneRequest,
    ) -> main_models.CreatePdpLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pdp_lane_with_options(request, headers, runtime)

    async def create_pdp_lane_async(
        self,
        request: main_models.CreatePdpLaneRequest,
    ) -> main_models.CreatePdpLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pdp_lane_with_options_async(request, headers, runtime)

    def create_pdp_pbc_with_options(
        self,
        request: main_models.CreatePdpPbcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpPbcResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpPbcResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdp_pbc_with_options_async(
        self,
        request: main_models.CreatePdpPbcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpPbcResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpPbcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdp_pbc(
        self,
        request: main_models.CreatePdpPbcRequest,
    ) -> main_models.CreatePdpPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pdp_pbc_with_options(request, headers, runtime)

    async def create_pdp_pbc_async(
        self,
        request: main_models.CreatePdpPbcRequest,
    ) -> main_models.CreatePdpPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pdp_pbc_with_options_async(request, headers, runtime)

    def create_pdp_service_with_options(
        self,
        request: main_models.CreatePdpServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdp_service_with_options_async(
        self,
        request: main_models.CreatePdpServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdp_service(
        self,
        request: main_models.CreatePdpServiceRequest,
    ) -> main_models.CreatePdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pdp_service_with_options(request, headers, runtime)

    async def create_pdp_service_async(
        self,
        request: main_models.CreatePdpServiceRequest,
    ) -> main_models.CreatePdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pdp_service_with_options_async(request, headers, runtime)

    def create_pdp_service_group_with_options(
        self,
        request: main_models.CreatePdpServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpServiceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_pdp_service_group_with_options_async(
        self,
        request: main_models.CreatePdpServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePdpServiceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePdpServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_pdp_service_group(
        self,
        request: main_models.CreatePdpServiceGroupRequest,
    ) -> main_models.CreatePdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_pdp_service_group_with_options(request, headers, runtime)

    async def create_pdp_service_group_async(
        self,
        request: main_models.CreatePdpServiceGroupRequest,
    ) -> main_models.CreatePdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_pdp_service_group_with_options_async(request, headers, runtime)

    def create_privilege_with_options(
        self,
        role_id: str,
        request: main_models.CreatePrivilegeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivilegeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivilege',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/privileges',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_privilege_with_options_async(
        self,
        role_id: str,
        request: main_models.CreatePrivilegeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivilegeResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivilege',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/privileges',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_privilege(
        self,
        role_id: str,
        request: main_models.CreatePrivilegeRequest,
    ) -> main_models.CreatePrivilegeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_privilege_with_options(role_id, request, headers, runtime)

    async def create_privilege_async(
        self,
        role_id: str,
        request: main_models.CreatePrivilegeRequest,
    ) -> main_models.CreatePrivilegeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_privilege_with_options_async(role_id, request, headers, runtime)

    def create_privilege_pop_with_options(
        self,
        role_id: str,
        request: main_models.CreatePrivilegePopRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivilegePopResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivilegePop',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/privileges/pop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivilegePopResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_privilege_pop_with_options_async(
        self,
        role_id: str,
        request: main_models.CreatePrivilegePopRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreatePrivilegePopResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreatePrivilegePop',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/privileges/pop',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreatePrivilegePopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_privilege_pop(
        self,
        role_id: str,
        request: main_models.CreatePrivilegePopRequest,
    ) -> main_models.CreatePrivilegePopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_privilege_pop_with_options(role_id, request, headers, runtime)

    async def create_privilege_pop_async(
        self,
        role_id: str,
        request: main_models.CreatePrivilegePopRequest,
    ) -> main_models.CreatePrivilegePopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_privilege_pop_with_options_async(role_id, request, headers, runtime)

    def create_product_with_options(
        self,
        request: main_models.CreateProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduct',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_product_with_options_async(
        self,
        request: main_models.CreateProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateProductResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateProduct',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.create_product_with_options(request, headers, runtime)

    async def create_product_async(
        self,
        request: main_models.CreateProductRequest,
    ) -> main_models.CreateProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_product_with_options_async(request, headers, runtime)

    def create_repo_fork_with_options(
        self,
        request: main_models.CreateRepoForkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoForkResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoFork',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/repo-forks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoForkResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_repo_fork_with_options_async(
        self,
        request: main_models.CreateRepoForkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRepoForkResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRepoFork',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/repo-forks',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRepoForkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_repo_fork(
        self,
        request: main_models.CreateRepoForkRequest,
    ) -> main_models.CreateRepoForkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_repo_fork_with_options(request, headers, runtime)

    async def create_repo_fork_async(
        self,
        request: main_models.CreateRepoForkRequest,
    ) -> main_models.CreateRepoForkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_repo_fork_with_options_async(request, headers, runtime)

    def create_resource_with_options(
        self,
        request: main_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_resource_with_options_async(
        self,
        request: main_models.CreateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateResourceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_resource(
        self,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_resource_with_options(request, headers, runtime)

    async def create_resource_async(
        self,
        request: main_models.CreateResourceRequest,
    ) -> main_models.CreateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_resource_with_options_async(request, headers, runtime)

    def create_role_with_options(
        self,
        request: main_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_role_with_options_async(
        self,
        request: main_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_role(
        self,
        request: main_models.CreateRoleRequest,
    ) -> main_models.CreateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_role_with_options(request, headers, runtime)

    async def create_role_async(
        self,
        request: main_models.CreateRoleRequest,
    ) -> main_models.CreateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_role_with_options_async(request, headers, runtime)

    def create_settled_with_options(
        self,
        request: main_models.CreateSettledRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSettledResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSettled',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/settleds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSettledResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_settled_with_options_async(
        self,
        request: main_models.CreateSettledRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateSettledResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'CreateSettled',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/settleds',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSettledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_settled(
        self,
        request: main_models.CreateSettledRequest,
    ) -> main_models.CreateSettledResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_settled_with_options(request, headers, runtime)

    async def create_settled_async(
        self,
        request: main_models.CreateSettledRequest,
    ) -> main_models.CreateSettledResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_settled_with_options_async(request, headers, runtime)

    def delete_component_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponent',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_component_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponent',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_component(
        self,
        id: str,
    ) -> main_models.DeleteComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_component_with_options(id, headers, runtime)

    async def delete_component_async(
        self,
        id: str,
    ) -> main_models.DeleteComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_component_with_options_async(id, headers, runtime)

    def delete_component_template_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponentTemplate',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_component_template_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteComponentTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteComponentTemplate',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteComponentTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_component_template(
        self,
        id: str,
    ) -> main_models.DeleteComponentTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_component_template_with_options(id, headers, runtime)

    async def delete_component_template_async(
        self,
        id: str,
    ) -> main_models.DeleteComponentTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_component_template_with_options_async(id, headers, runtime)

    def delete_developer_with_options(
        self,
        account_id: str,
        request: main_models.DeleteDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeveloperResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteDeveloperResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_developer_with_options_async(
        self,
        account_id: str,
        request: main_models.DeleteDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeveloperResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteDeveloperResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_developer(
        self,
        account_id: str,
        request: main_models.DeleteDeveloperRequest,
    ) -> main_models.DeleteDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_developer_with_options(account_id, request, headers, runtime)

    async def delete_developer_async(
        self,
        account_id: str,
        request: main_models.DeleteDeveloperRequest,
    ) -> main_models.DeleteDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_developer_with_options_async(account_id, request, headers, runtime)

    def delete_enterprise_with_options(
        self,
        enterprise_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_enterprise_with_options_async(
        self,
        enterprise_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteEnterpriseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_enterprise(
        self,
        enterprise_id: str,
    ) -> main_models.DeleteEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_enterprise_with_options(enterprise_id, headers, runtime)

    async def delete_enterprise_async(
        self,
        enterprise_id: str,
    ) -> main_models.DeleteEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_enterprise_with_options_async(enterprise_id, headers, runtime)

    def delete_library_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLibraryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_library_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLibraryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_library(
        self,
        id: str,
    ) -> main_models.DeleteLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_library_with_options(id, headers, runtime)

    async def delete_library_async(
        self,
        id: str,
    ) -> main_models.DeleteLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_library_with_options_async(id, headers, runtime)

    def delete_library_instruction_with_options(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLibraryInstructionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLibraryInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/instructions',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLibraryInstructionResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_library_instruction_with_options_async(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLibraryInstructionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLibraryInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/instructions',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLibraryInstructionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_library_instruction(
        self,
        library_id: str,
    ) -> main_models.DeleteLibraryInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_library_instruction_with_options(library_id, headers, runtime)

    async def delete_library_instruction_async(
        self,
        library_id: str,
    ) -> main_models.DeleteLibraryInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_library_instruction_with_options_async(library_id, headers, runtime)

    def delete_library_schema_with_options(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLibrarySchemaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLibrarySchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/schemas',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLibrarySchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_library_schema_with_options_async(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteLibrarySchemaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteLibrarySchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/schemas',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteLibrarySchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_library_schema(
        self,
        library_id: str,
    ) -> main_models.DeleteLibrarySchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_library_schema_with_options(library_id, headers, runtime)

    async def delete_library_schema_async(
        self,
        library_id: str,
    ) -> main_models.DeleteLibrarySchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_library_schema_with_options_async(library_id, headers, runtime)

    def delete_monitor_alert_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorAlertResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_alert_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorAlertResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_alert(
        self,
        id: str,
    ) -> main_models.DeleteMonitorAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_monitor_alert_with_options(id, headers, runtime)

    async def delete_monitor_alert_async(
        self,
        id: str,
    ) -> main_models.DeleteMonitorAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_monitor_alert_with_options_async(id, headers, runtime)

    def delete_monitor_contact_with_options(
        self,
        contact_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorContactResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorContact',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact/{DaraURL.percent_encode(contact_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_contact_with_options_async(
        self,
        contact_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorContactResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorContact',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact/{DaraURL.percent_encode(contact_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_contact(
        self,
        contact_id: str,
    ) -> main_models.DeleteMonitorContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_monitor_contact_with_options(contact_id, headers, runtime)

    async def delete_monitor_contact_async(
        self,
        contact_id: str,
    ) -> main_models.DeleteMonitorContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_monitor_contact_with_options_async(contact_id, headers, runtime)

    def delete_monitor_contact_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorContactGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorContactGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_contact_group_with_options_async(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorContactGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorContactGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_contact_group(
        self,
        group_id: str,
    ) -> main_models.DeleteMonitorContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_monitor_contact_group_with_options(group_id, headers, runtime)

    async def delete_monitor_contact_group_async(
        self,
        group_id: str,
    ) -> main_models.DeleteMonitorContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_monitor_contact_group_with_options_async(group_id, headers, runtime)

    def delete_monitor_group_member_with_options(
        self,
        group_id: str,
        request: main_models.DeleteMonitorGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_ids):
            query['contactIds'] = request.contact_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroupMember',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group/{DaraURL.percent_encode(group_id)}/commands/delete-member',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupMemberResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_group_member_with_options_async(
        self,
        group_id: str,
        request: main_models.DeleteMonitorGroupMemberRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorGroupMemberResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.contact_ids):
            query['contactIds'] = request.contact_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorGroupMember',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group/{DaraURL.percent_encode(group_id)}/commands/delete-member',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorGroupMemberResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_group_member(
        self,
        group_id: str,
        request: main_models.DeleteMonitorGroupMemberRequest,
    ) -> main_models.DeleteMonitorGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_monitor_group_member_with_options(group_id, request, headers, runtime)

    async def delete_monitor_group_member_async(
        self,
        group_id: str,
        request: main_models.DeleteMonitorGroupMemberRequest,
    ) -> main_models.DeleteMonitorGroupMemberResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_monitor_group_member_with_options_async(group_id, request, headers, runtime)

    def delete_monitor_webhook_with_options(
        self,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorWebhookResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorWebhook',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook/{DaraURL.percent_encode(webhook_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_monitor_webhook_with_options_async(
        self,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMonitorWebhookResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMonitorWebhook',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook/{DaraURL.percent_encode(webhook_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMonitorWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_monitor_webhook(
        self,
        webhook_id: str,
    ) -> main_models.DeleteMonitorWebhookResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_monitor_webhook_with_options(webhook_id, headers, runtime)

    async def delete_monitor_webhook_async(
        self,
        webhook_id: str,
    ) -> main_models.DeleteMonitorWebhookResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_monitor_webhook_with_options_async(webhook_id, headers, runtime)

    def delete_mq_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMqGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMqGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/group/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMqGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mq_group_with_options_async(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMqGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMqGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/group/{DaraURL.percent_encode(group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMqGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mq_group(
        self,
        group_id: str,
    ) -> main_models.DeleteMqGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mq_group_with_options(group_id, headers, runtime)

    async def delete_mq_group_async(
        self,
        group_id: str,
    ) -> main_models.DeleteMqGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mq_group_with_options_async(group_id, headers, runtime)

    def delete_mq_topic_with_options(
        self,
        topic_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMqTopicResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMqTopic',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/{DaraURL.percent_encode(topic_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMqTopicResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_mq_topic_with_options_async(
        self,
        topic_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMqTopicResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteMqTopic',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/{DaraURL.percent_encode(topic_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteMqTopicResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_mq_topic(
        self,
        topic_id: str,
    ) -> main_models.DeleteMqTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_mq_topic_with_options(topic_id, headers, runtime)

    async def delete_mq_topic_async(
        self,
        topic_id: str,
    ) -> main_models.DeleteMqTopicResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_mq_topic_with_options_async(topic_id, headers, runtime)

    def delete_pbc_invoke_with_options(
        self,
        request: main_models.DeletePbcInvokeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePbcInvokeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePbcInvoke',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invokes',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePbcInvokeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pbc_invoke_with_options_async(
        self,
        request: main_models.DeletePbcInvokeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePbcInvokeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeletePbcInvoke',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invokes',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePbcInvokeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pbc_invoke(
        self,
        request: main_models.DeletePbcInvokeRequest,
    ) -> main_models.DeletePbcInvokeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pbc_invoke_with_options(request, headers, runtime)

    async def delete_pbc_invoke_async(
        self,
        request: main_models.DeletePbcInvokeRequest,
    ) -> main_models.DeletePbcInvokeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pbc_invoke_with_options_async(request, headers, runtime)

    def delete_pdp_config_with_options(
        self,
        config_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs/{DaraURL.percent_encode(config_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pdp_config_with_options_async(
        self,
        config_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs/{DaraURL.percent_encode(config_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pdp_config(
        self,
        config_id: str,
    ) -> main_models.DeletePdpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pdp_config_with_options(config_id, headers, runtime)

    async def delete_pdp_config_async(
        self,
        config_id: str,
    ) -> main_models.DeletePdpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pdp_config_with_options_async(config_id, headers, runtime)

    def delete_pdp_lane_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpLaneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpLane',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pdp_lane_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpLaneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpLane',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pdp_lane(
        self,
        id: str,
    ) -> main_models.DeletePdpLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pdp_lane_with_options(id, headers, runtime)

    async def delete_pdp_lane_async(
        self,
        id: str,
    ) -> main_models.DeletePdpLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pdp_lane_with_options_async(id, headers, runtime)

    def delete_pdp_lane_inlet_service_with_options(
        self,
        lane_id: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpLaneInletServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpLaneInletService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/{DaraURL.percent_encode(lane_id)}/commands/deleted-inlet-service/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpLaneInletServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pdp_lane_inlet_service_with_options_async(
        self,
        lane_id: str,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpLaneInletServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpLaneInletService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/{DaraURL.percent_encode(lane_id)}/commands/deleted-inlet-service/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpLaneInletServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pdp_lane_inlet_service(
        self,
        lane_id: str,
        service_id: str,
    ) -> main_models.DeletePdpLaneInletServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pdp_lane_inlet_service_with_options(lane_id, service_id, headers, runtime)

    async def delete_pdp_lane_inlet_service_async(
        self,
        lane_id: str,
        service_id: str,
    ) -> main_models.DeletePdpLaneInletServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pdp_lane_inlet_service_with_options_async(lane_id, service_id, headers, runtime)

    def delete_pdp_lane_service_group_with_options(
        self,
        service_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpLaneServiceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpLaneServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/deleted-service-group/{DaraURL.percent_encode(service_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpLaneServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pdp_lane_service_group_with_options_async(
        self,
        service_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpLaneServiceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpLaneServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/deleted-service-group/{DaraURL.percent_encode(service_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpLaneServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pdp_lane_service_group(
        self,
        service_group_id: str,
    ) -> main_models.DeletePdpLaneServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pdp_lane_service_group_with_options(service_group_id, headers, runtime)

    async def delete_pdp_lane_service_group_async(
        self,
        service_group_id: str,
    ) -> main_models.DeletePdpLaneServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pdp_lane_service_group_with_options_async(service_group_id, headers, runtime)

    def delete_pdp_pbc_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpPbcResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pdp_pbc_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpPbcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pdp_pbc(
        self,
        id: str,
    ) -> main_models.DeletePdpPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pdp_pbc_with_options(id, headers, runtime)

    async def delete_pdp_pbc_async(
        self,
        id: str,
    ) -> main_models.DeletePdpPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pdp_pbc_with_options_async(id, headers, runtime)

    def delete_pdp_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pdp_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeletePdpServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pdp_service(
        self,
        service_id: str,
    ) -> main_models.DeletePdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pdp_service_with_options(service_id, headers, runtime)

    async def delete_pdp_service_async(
        self,
        service_id: str,
    ) -> main_models.DeletePdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pdp_service_with_options_async(service_id, headers, runtime)

    def delete_pdp_service_group_with_options(
        self,
        service_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpServiceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups/{DaraURL.percent_encode(service_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeletePdpServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_pdp_service_group_with_options_async(
        self,
        service_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePdpServiceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups/{DaraURL.percent_encode(service_group_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeletePdpServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_pdp_service_group(
        self,
        service_group_id: str,
    ) -> main_models.DeletePdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_pdp_service_group_with_options(service_group_id, headers, runtime)

    async def delete_pdp_service_group_async(
        self,
        service_group_id: str,
    ) -> main_models.DeletePdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_pdp_service_group_with_options_async(service_group_id, headers, runtime)

    def delete_privilege_with_options(
        self,
        privilege_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivilegeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivilege',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/privileges/{DaraURL.percent_encode(privilege_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeletePrivilegeResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_privilege_with_options_async(
        self,
        privilege_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeletePrivilegeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeletePrivilege',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/privileges/{DaraURL.percent_encode(privilege_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeletePrivilegeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_privilege(
        self,
        privilege_id: str,
    ) -> main_models.DeletePrivilegeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_privilege_with_options(privilege_id, headers, runtime)

    async def delete_privilege_async(
        self,
        privilege_id: str,
    ) -> main_models.DeletePrivilegeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_privilege_with_options_async(privilege_id, headers, runtime)

    def delete_product_with_options(
        self,
        id: str,
        request: main_models.DeleteProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProduct',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_product_with_options_async(
        self,
        id: str,
        request: main_models.DeleteProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteProductResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteProduct',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_product(
        self,
        id: str,
        request: main_models.DeleteProductRequest,
    ) -> main_models.DeleteProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_product_with_options(id, request, headers, runtime)

    async def delete_product_async(
        self,
        id: str,
        request: main_models.DeleteProductRequest,
    ) -> main_models.DeleteProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_product_with_options_async(id, request, headers, runtime)

    def delete_resource_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_resource_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_resource(
        self,
        id: str,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_resource_with_options(id, headers, runtime)

    async def delete_resource_async(
        self,
        id: str,
    ) -> main_models.DeleteResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_resource_with_options_async(id, headers, runtime)

    def delete_role_with_options(
        self,
        role_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        role_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        role_id: str,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_role_with_options(role_id, headers, runtime)

    async def delete_role_async(
        self,
        role_id: str,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_role_with_options_async(role_id, headers, runtime)

    def delete_settled_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSettledResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSettled',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/settleds/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSettledResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_settled_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSettledResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DeleteSettled',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/settleds/{DaraURL.percent_encode(id)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSettledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_settled(
        self,
        id: str,
    ) -> main_models.DeleteSettledResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_settled_with_options(id, headers, runtime)

    async def delete_settled_async(
        self,
        id: str,
    ) -> main_models.DeleteSettledResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_settled_with_options_async(id, headers, runtime)

    def depend_library_with_options(
        self,
        id: str,
        request: main_models.DependLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DependLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DependLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}/commands/dependency',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DependLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def depend_library_with_options_async(
        self,
        id: str,
        request: main_models.DependLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DependLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DependLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}/commands/dependency',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DependLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def depend_library(
        self,
        id: str,
        request: main_models.DependLibraryRequest,
    ) -> main_models.DependLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.depend_library_with_options(id, request, headers, runtime)

    async def depend_library_async(
        self,
        id: str,
        request: main_models.DependLibraryRequest,
    ) -> main_models.DependLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.depend_library_with_options_async(id, request, headers, runtime)

    def feedback_library_review_with_options(
        self,
        review_id: str,
        request: main_models.FeedbackLibraryReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FeedbackLibraryReviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approve):
            body['approve'] = request.approve
        if not DaraCore.is_null(request.feedback):
            body['feedback'] = request.feedback
        if not DaraCore.is_null(request.review_id):
            body['reviewId'] = request.review_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FeedbackLibraryReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews/{DaraURL.percent_encode(review_id)}/commands/feedback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FeedbackLibraryReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_library_review_with_options_async(
        self,
        review_id: str,
        request: main_models.FeedbackLibraryReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FeedbackLibraryReviewResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.approve):
            body['approve'] = request.approve
        if not DaraCore.is_null(request.feedback):
            body['feedback'] = request.feedback
        if not DaraCore.is_null(request.review_id):
            body['reviewId'] = request.review_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'FeedbackLibraryReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews/{DaraURL.percent_encode(review_id)}/commands/feedback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FeedbackLibraryReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback_library_review(
        self,
        review_id: str,
        request: main_models.FeedbackLibraryReviewRequest,
    ) -> main_models.FeedbackLibraryReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.feedback_library_review_with_options(review_id, request, headers, runtime)

    async def feedback_library_review_async(
        self,
        review_id: str,
        request: main_models.FeedbackLibraryReviewRequest,
    ) -> main_models.FeedbackLibraryReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.feedback_library_review_with_options_async(review_id, request, headers, runtime)

    def feedback_pbc_review_with_options(
        self,
        review_id: str,
        request: main_models.FeedbackPbcReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FeedbackPbcReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'FeedbackPbcReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews/{DaraURL.percent_encode(review_id)}/commands/feedback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FeedbackPbcReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def feedback_pbc_review_with_options_async(
        self,
        review_id: str,
        request: main_models.FeedbackPbcReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.FeedbackPbcReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'FeedbackPbcReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews/{DaraURL.percent_encode(review_id)}/commands/feedback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.FeedbackPbcReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def feedback_pbc_review(
        self,
        review_id: str,
        request: main_models.FeedbackPbcReviewRequest,
    ) -> main_models.FeedbackPbcReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.feedback_pbc_review_with_options(review_id, request, headers, runtime)

    async def feedback_pbc_review_async(
        self,
        review_id: str,
        request: main_models.FeedbackPbcReviewRequest,
    ) -> main_models.FeedbackPbcReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.feedback_pbc_review_with_options_async(review_id, request, headers, runtime)

    def get_buc_enterprise_with_options(
        self,
        enterprise_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBucEnterpriseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBucEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/bucs/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBucEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_buc_enterprise_with_options_async(
        self,
        enterprise_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetBucEnterpriseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetBucEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/bucs/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetBucEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_buc_enterprise(
        self,
        enterprise_id: str,
    ) -> main_models.GetBucEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_buc_enterprise_with_options(enterprise_id, headers, runtime)

    async def get_buc_enterprise_async(
        self,
        enterprise_id: str,
    ) -> main_models.GetBucEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_buc_enterprise_with_options_async(enterprise_id, headers, runtime)

    def get_component_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComponentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetComponent',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_component_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComponentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetComponent',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_component(
        self,
        id: str,
    ) -> main_models.GetComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_component_with_options(id, headers, runtime)

    async def get_component_async(
        self,
        id: str,
    ) -> main_models.GetComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_component_with_options_async(id, headers, runtime)

    def get_component_template_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComponentTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetComponentTemplate',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComponentTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_component_template_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetComponentTemplateResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetComponentTemplate',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetComponentTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_component_template(
        self,
        id: str,
    ) -> main_models.GetComponentTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_component_template_with_options(id, headers, runtime)

    async def get_component_template_async(
        self,
        id: str,
    ) -> main_models.GetComponentTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_component_template_with_options_async(id, headers, runtime)

    def get_deployment_with_options(
        self,
        deployment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeployment',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/instance/{DaraURL.percent_encode(deployment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_deployment_with_options_async(
        self,
        deployment_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeploymentResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeployment',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/instance/{DaraURL.percent_encode(deployment_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_deployment(
        self,
        deployment_id: str,
    ) -> main_models.GetDeploymentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_deployment_with_options(deployment_id, headers, runtime)

    async def get_deployment_async(
        self,
        deployment_id: str,
    ) -> main_models.GetDeploymentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_deployment_with_options_async(deployment_id, headers, runtime)

    def get_developer_with_options(
        self,
        account_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeveloperResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeveloperResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_developer_with_options_async(
        self,
        account_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeveloperResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeveloperResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_developer(
        self,
        account_id: str,
    ) -> main_models.GetDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_developer_with_options(account_id, headers, runtime)

    async def get_developer_async(
        self,
        account_id: str,
    ) -> main_models.GetDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_developer_with_options_async(account_id, headers, runtime)

    def get_developer_enterprise_with_options(
        self,
        account_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeveloperEnterpriseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeveloperEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/developers/{DaraURL.percent_encode(account_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeveloperEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_developer_enterprise_with_options_async(
        self,
        account_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDeveloperEnterpriseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDeveloperEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/developers/{DaraURL.percent_encode(account_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeveloperEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_developer_enterprise(
        self,
        account_id: str,
    ) -> main_models.GetDeveloperEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_developer_enterprise_with_options(account_id, headers, runtime)

    async def get_developer_enterprise_async(
        self,
        account_id: str,
    ) -> main_models.GetDeveloperEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_developer_enterprise_with_options_async(account_id, headers, runtime)

    def get_enterprise_with_options(
        self,
        enterprise_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_with_options_async(
        self,
        enterprise_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise(
        self,
        enterprise_id: str,
    ) -> main_models.GetEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_enterprise_with_options(enterprise_id, headers, runtime)

    async def get_enterprise_async(
        self,
        enterprise_id: str,
    ) -> main_models.GetEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_enterprise_with_options_async(enterprise_id, headers, runtime)

    def get_enterprise_developer_with_options(
        self,
        account_id: str,
        enterprise_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseDeveloperResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEnterpriseDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseDeveloperResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enterprise_developer_with_options_async(
        self,
        account_id: str,
        enterprise_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetEnterpriseDeveloperResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetEnterpriseDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnterpriseDeveloperResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enterprise_developer(
        self,
        account_id: str,
        enterprise_id: str,
    ) -> main_models.GetEnterpriseDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_enterprise_developer_with_options(account_id, enterprise_id, headers, runtime)

    async def get_enterprise_developer_async(
        self,
        account_id: str,
        enterprise_id: str,
    ) -> main_models.GetEnterpriseDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_enterprise_developer_with_options_async(account_id, enterprise_id, headers, runtime)

    def get_fork_review_with_options(
        self,
        review_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetForkReviewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetForkReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/fork-reviews/{DaraURL.percent_encode(review_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetForkReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_fork_review_with_options_async(
        self,
        review_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetForkReviewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetForkReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/fork-reviews/{DaraURL.percent_encode(review_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetForkReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_fork_review(
        self,
        review_id: str,
    ) -> main_models.GetForkReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_fork_review_with_options(review_id, headers, runtime)

    async def get_fork_review_async(
        self,
        review_id: str,
    ) -> main_models.GetForkReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_fork_review_with_options_async(review_id, headers, runtime)

    def get_history_developer_with_options(
        self,
        account_id: str,
        request: main_models.GetHistoryDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoryDeveloperResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoryDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}/commonds/history',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoryDeveloperResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_history_developer_with_options_async(
        self,
        account_id: str,
        request: main_models.GetHistoryDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetHistoryDeveloperResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['nextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetHistoryDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}/commonds/history',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetHistoryDeveloperResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_history_developer(
        self,
        account_id: str,
        request: main_models.GetHistoryDeveloperRequest,
    ) -> main_models.GetHistoryDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_history_developer_with_options(account_id, request, headers, runtime)

    async def get_history_developer_async(
        self,
        account_id: str,
        request: main_models.GetHistoryDeveloperRequest,
    ) -> main_models.GetHistoryDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_history_developer_with_options_async(account_id, request, headers, runtime)

    def get_last_deployment_config_with_options(
        self,
        request: main_models.GetLastDeploymentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLastDeploymentConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLastDeploymentConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/last-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLastDeploymentConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_last_deployment_config_with_options_async(
        self,
        request: main_models.GetLastDeploymentConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLastDeploymentConfigResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLastDeploymentConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/last-config',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLastDeploymentConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_last_deployment_config(
        self,
        request: main_models.GetLastDeploymentConfigRequest,
    ) -> main_models.GetLastDeploymentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_last_deployment_config_with_options(request, headers, runtime)

    async def get_last_deployment_config_async(
        self,
        request: main_models.GetLastDeploymentConfigRequest,
    ) -> main_models.GetLastDeploymentConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_last_deployment_config_with_options_async(request, headers, runtime)

    def get_library_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library(
        self,
        id: str,
    ) -> main_models.GetLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_library_with_options(id, headers, runtime)

    async def get_library_async(
        self,
        id: str,
    ) -> main_models.GetLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_library_with_options_async(id, headers, runtime)

    def get_library_developer_repo_metrics_with_options(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryDeveloperRepoMetricsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryDeveloperRepoMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/Librarys/{DaraURL.percent_encode(library_id)}/code/commands/get-developer-repo-metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryDeveloperRepoMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_developer_repo_metrics_with_options_async(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryDeveloperRepoMetricsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryDeveloperRepoMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/Librarys/{DaraURL.percent_encode(library_id)}/code/commands/get-developer-repo-metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryDeveloperRepoMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library_developer_repo_metrics(
        self,
        library_id: str,
    ) -> main_models.GetLibraryDeveloperRepoMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_library_developer_repo_metrics_with_options(library_id, headers, runtime)

    async def get_library_developer_repo_metrics_async(
        self,
        library_id: str,
    ) -> main_models.GetLibraryDeveloperRepoMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_library_developer_repo_metrics_with_options_async(library_id, headers, runtime)

    def get_library_instruction_with_options(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryInstructionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/instructions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryInstructionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_instruction_with_options_async(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryInstructionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/instructions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryInstructionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library_instruction(
        self,
        library_id: str,
    ) -> main_models.GetLibraryInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_library_instruction_with_options(library_id, headers, runtime)

    async def get_library_instruction_async(
        self,
        library_id: str,
    ) -> main_models.GetLibraryInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_library_instruction_with_options_async(library_id, headers, runtime)

    def get_library_repo_metrics_with_options(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryRepoMetricsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryRepoMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/Librarys/{DaraURL.percent_encode(library_id)}/code/commands/get-repo-metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryRepoMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_repo_metrics_with_options_async(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryRepoMetricsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryRepoMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/Librarys/{DaraURL.percent_encode(library_id)}/code/commands/get-repo-metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryRepoMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library_repo_metrics(
        self,
        library_id: str,
    ) -> main_models.GetLibraryRepoMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_library_repo_metrics_with_options(library_id, headers, runtime)

    async def get_library_repo_metrics_async(
        self,
        library_id: str,
    ) -> main_models.GetLibraryRepoMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_library_repo_metrics_with_options_async(library_id, headers, runtime)

    def get_library_review_with_options(
        self,
        review_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryReviewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews/{DaraURL.percent_encode(review_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_review_with_options_async(
        self,
        review_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibraryReviewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibraryReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews/{DaraURL.percent_encode(review_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibraryReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library_review(
        self,
        review_id: str,
    ) -> main_models.GetLibraryReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_library_review_with_options(review_id, headers, runtime)

    async def get_library_review_async(
        self,
        review_id: str,
    ) -> main_models.GetLibraryReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_library_review_with_options_async(review_id, headers, runtime)

    def get_library_schema_with_options(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibrarySchemaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibrarySchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/schemas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibrarySchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_library_schema_with_options_async(
        self,
        library_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLibrarySchemaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLibrarySchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/schemas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLibrarySchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_library_schema(
        self,
        library_id: str,
    ) -> main_models.GetLibrarySchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_library_schema_with_options(library_id, headers, runtime)

    async def get_library_schema_async(
        self,
        library_id: str,
    ) -> main_models.GetLibrarySchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_library_schema_with_options_async(library_id, headers, runtime)

    def get_log_url_with_options(
        self,
        request: main_models.GetLogUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogUrl',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/pdp-log/url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogUrlResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_log_url_with_options_async(
        self,
        request: main_models.GetLogUrlRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLogUrlResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetLogUrl',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/pdp-log/url',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLogUrlResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_log_url(
        self,
        request: main_models.GetLogUrlRequest,
    ) -> main_models.GetLogUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_log_url_with_options(request, headers, runtime)

    async def get_log_url_async(
        self,
        request: main_models.GetLogUrlRequest,
    ) -> main_models.GetLogUrlResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_log_url_with_options_async(request, headers, runtime)

    def get_login_user_info_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginUserInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLoginUserInfo',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/bucs/logins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_login_user_info_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetLoginUserInfoResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetLoginUserInfo',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/bucs/logins',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetLoginUserInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_login_user_info(self) -> main_models.GetLoginUserInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_login_user_info_with_options(headers, runtime)

    async def get_login_user_info_async(self) -> main_models.GetLoginUserInfoResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_login_user_info_with_options_async(headers, runtime)

    def get_monitor_alert_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorAlertResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monitor_alert_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorAlertResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monitor_alert(
        self,
        id: str,
    ) -> main_models.GetMonitorAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_monitor_alert_with_options(id, headers, runtime)

    async def get_monitor_alert_async(
        self,
        id: str,
    ) -> main_models.GetMonitorAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_monitor_alert_with_options_async(id, headers, runtime)

    def get_monitor_alert_history_with_options(
        self,
        request: main_models.GetMonitorAlertHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorAlertHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_rule_name):
            query['alertRuleName'] = request.alert_rule_name
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorAlertHistory',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/getMonitorAlertHistory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorAlertHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monitor_alert_history_with_options_async(
        self,
        request: main_models.GetMonitorAlertHistoryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorAlertHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_rule_name):
            query['alertRuleName'] = request.alert_rule_name
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorAlertHistory',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/getMonitorAlertHistory',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorAlertHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monitor_alert_history(
        self,
        request: main_models.GetMonitorAlertHistoryRequest,
    ) -> main_models.GetMonitorAlertHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_monitor_alert_history_with_options(request, headers, runtime)

    async def get_monitor_alert_history_async(
        self,
        request: main_models.GetMonitorAlertHistoryRequest,
    ) -> main_models.GetMonitorAlertHistoryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_monitor_alert_history_with_options_async(request, headers, runtime)

    def get_monitor_contact_with_options(
        self,
        contact_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorContactResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorContact',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact/{DaraURL.percent_encode(contact_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monitor_contact_with_options_async(
        self,
        contact_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorContactResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorContact',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact/{DaraURL.percent_encode(contact_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monitor_contact(
        self,
        contact_id: str,
    ) -> main_models.GetMonitorContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_monitor_contact_with_options(contact_id, headers, runtime)

    async def get_monitor_contact_async(
        self,
        contact_id: str,
    ) -> main_models.GetMonitorContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_monitor_contact_with_options_async(contact_id, headers, runtime)

    def get_monitor_contact_group_with_options(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorContactGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorContactGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monitor_contact_group_with_options_async(
        self,
        group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorContactGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorContactGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group/{DaraURL.percent_encode(group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monitor_contact_group(
        self,
        group_id: str,
    ) -> main_models.GetMonitorContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_monitor_contact_group_with_options(group_id, headers, runtime)

    async def get_monitor_contact_group_async(
        self,
        group_id: str,
    ) -> main_models.GetMonitorContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_monitor_contact_group_with_options_async(group_id, headers, runtime)

    def get_monitor_webhook_with_options(
        self,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorWebhookResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorWebhook',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook/{DaraURL.percent_encode(webhook_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_monitor_webhook_with_options_async(
        self,
        webhook_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetMonitorWebhookResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetMonitorWebhook',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook/{DaraURL.percent_encode(webhook_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMonitorWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_monitor_webhook(
        self,
        webhook_id: str,
    ) -> main_models.GetMonitorWebhookResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_monitor_webhook_with_options(webhook_id, headers, runtime)

    async def get_monitor_webhook_async(
        self,
        webhook_id: str,
    ) -> main_models.GetMonitorWebhookResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_monitor_webhook_with_options_async(webhook_id, headers, runtime)

    def get_pbc_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pbc_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pbc(
        self,
        id: str,
    ) -> main_models.GetPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pbc_with_options(id, headers, runtime)

    async def get_pbc_async(
        self,
        id: str,
    ) -> main_models.GetPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pbc_with_options_async(id, headers, runtime)

    def get_pbc_api_schema_with_options(
        self,
        pbc_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcApiSchemaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcApiSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/api-schemas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcApiSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pbc_api_schema_with_options_async(
        self,
        pbc_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcApiSchemaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcApiSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/api-schemas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcApiSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pbc_api_schema(
        self,
        pbc_version_id: str,
    ) -> main_models.GetPbcApiSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pbc_api_schema_with_options(pbc_version_id, headers, runtime)

    async def get_pbc_api_schema_async(
        self,
        pbc_version_id: str,
    ) -> main_models.GetPbcApiSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pbc_api_schema_with_options_async(pbc_version_id, headers, runtime)

    def get_pbc_developer_repo_metrics_with_options(
        self,
        pbc_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcDeveloperRepoMetricsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcDeveloperRepoMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(pbc_id)}/code/commands/get-developer-repo-metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcDeveloperRepoMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pbc_developer_repo_metrics_with_options_async(
        self,
        pbc_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcDeveloperRepoMetricsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcDeveloperRepoMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(pbc_id)}/code/commands/get-developer-repo-metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcDeveloperRepoMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pbc_developer_repo_metrics(
        self,
        pbc_id: str,
    ) -> main_models.GetPbcDeveloperRepoMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pbc_developer_repo_metrics_with_options(pbc_id, headers, runtime)

    async def get_pbc_developer_repo_metrics_async(
        self,
        pbc_id: str,
    ) -> main_models.GetPbcDeveloperRepoMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pbc_developer_repo_metrics_with_options_async(pbc_id, headers, runtime)

    def get_pbc_instruction_with_options(
        self,
        pbc_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcInstructionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/instructions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcInstructionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pbc_instruction_with_options_async(
        self,
        pbc_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcInstructionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/instructions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcInstructionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pbc_instruction(
        self,
        pbc_version_id: str,
    ) -> main_models.GetPbcInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pbc_instruction_with_options(pbc_version_id, headers, runtime)

    async def get_pbc_instruction_async(
        self,
        pbc_version_id: str,
    ) -> main_models.GetPbcInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pbc_instruction_with_options_async(pbc_version_id, headers, runtime)

    def get_pbc_invoke_review_with_options(
        self,
        review_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcInvokeReviewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcInvokeReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invoke-reviews/{DaraURL.percent_encode(review_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcInvokeReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pbc_invoke_review_with_options_async(
        self,
        review_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcInvokeReviewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcInvokeReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invoke-reviews/{DaraURL.percent_encode(review_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcInvokeReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pbc_invoke_review(
        self,
        review_id: str,
    ) -> main_models.GetPbcInvokeReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pbc_invoke_review_with_options(review_id, headers, runtime)

    async def get_pbc_invoke_review_async(
        self,
        review_id: str,
    ) -> main_models.GetPbcInvokeReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pbc_invoke_review_with_options_async(review_id, headers, runtime)

    def get_pbc_repo_metrics_with_options(
        self,
        pbc_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcRepoMetricsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcRepoMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(pbc_id)}/code/commands/get-repo-metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcRepoMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pbc_repo_metrics_with_options_async(
        self,
        pbc_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcRepoMetricsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcRepoMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(pbc_id)}/code/commands/get-repo-metrics',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcRepoMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pbc_repo_metrics(
        self,
        pbc_id: str,
    ) -> main_models.GetPbcRepoMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pbc_repo_metrics_with_options(pbc_id, headers, runtime)

    async def get_pbc_repo_metrics_async(
        self,
        pbc_id: str,
    ) -> main_models.GetPbcRepoMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pbc_repo_metrics_with_options_async(pbc_id, headers, runtime)

    def get_pbc_review_with_options(
        self,
        review_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcReviewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews/{DaraURL.percent_encode(review_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pbc_review_with_options_async(
        self,
        review_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcReviewResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews/{DaraURL.percent_encode(review_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pbc_review(
        self,
        review_id: str,
    ) -> main_models.GetPbcReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pbc_review_with_options(review_id, headers, runtime)

    async def get_pbc_review_async(
        self,
        review_id: str,
    ) -> main_models.GetPbcReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pbc_review_with_options_async(review_id, headers, runtime)

    def get_pbc_schema_with_options(
        self,
        pbc_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcSchemaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/schemas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pbc_schema_with_options_async(
        self,
        pbc_version_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcSchemaResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/schemas',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pbc_schema(
        self,
        pbc_version_id: str,
    ) -> main_models.GetPbcSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pbc_schema_with_options(pbc_version_id, headers, runtime)

    async def get_pbc_schema_async(
        self,
        pbc_version_id: str,
    ) -> main_models.GetPbcSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pbc_schema_with_options_async(pbc_version_id, headers, runtime)

    def get_pbc_version_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pbc_version_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPbcVersionResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPbcVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pbc_version(
        self,
        id: str,
    ) -> main_models.GetPbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pbc_version_with_options(id, headers, runtime)

    async def get_pbc_version_async(
        self,
        id: str,
    ) -> main_models.GetPbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pbc_version_with_options_async(id, headers, runtime)

    def get_pdp_config_with_options(
        self,
        config_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs/last/{DaraURL.percent_encode(config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pdp_config_with_options_async(
        self,
        config_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs/last/{DaraURL.percent_encode(config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pdp_config(
        self,
        config_id: str,
    ) -> main_models.GetPdpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pdp_config_with_options(config_id, headers, runtime)

    async def get_pdp_config_async(
        self,
        config_id: str,
    ) -> main_models.GetPdpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pdp_config_with_options_async(config_id, headers, runtime)

    def get_pdp_history_config_with_options(
        self,
        history_config_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpHistoryConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpHistoryConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs/history/{DaraURL.percent_encode(history_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpHistoryConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pdp_history_config_with_options_async(
        self,
        history_config_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpHistoryConfigResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpHistoryConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs/history/{DaraURL.percent_encode(history_config_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpHistoryConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pdp_history_config(
        self,
        history_config_id: str,
    ) -> main_models.GetPdpHistoryConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pdp_history_config_with_options(history_config_id, headers, runtime)

    async def get_pdp_history_config_async(
        self,
        history_config_id: str,
    ) -> main_models.GetPdpHistoryConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pdp_history_config_with_options_async(history_config_id, headers, runtime)

    def get_pdp_lane_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpLaneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpLane',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pdp_lane_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpLaneResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpLane',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pdp_lane(
        self,
        id: str,
    ) -> main_models.GetPdpLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pdp_lane_with_options(id, headers, runtime)

    async def get_pdp_lane_async(
        self,
        id: str,
    ) -> main_models.GetPdpLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pdp_lane_with_options_async(id, headers, runtime)

    def get_pdp_pbc_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpPbcResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pdp_pbc_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpPbcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pdp_pbc(
        self,
        id: str,
    ) -> main_models.GetPdpPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pdp_pbc_with_options(id, headers, runtime)

    async def get_pdp_pbc_async(
        self,
        id: str,
    ) -> main_models.GetPdpPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pdp_pbc_with_options_async(id, headers, runtime)

    def get_pdp_service_with_options(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pdp_service_with_options_async(
        self,
        service_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpServiceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/{DaraURL.percent_encode(service_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pdp_service(
        self,
        service_id: str,
    ) -> main_models.GetPdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pdp_service_with_options(service_id, headers, runtime)

    async def get_pdp_service_async(
        self,
        service_id: str,
    ) -> main_models.GetPdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pdp_service_with_options_async(service_id, headers, runtime)

    def get_pdp_service_group_with_options(
        self,
        service_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpServiceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups/{DaraURL.percent_encode(service_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_pdp_service_group_with_options_async(
        self,
        service_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetPdpServiceGroupResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetPdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups/{DaraURL.percent_encode(service_group_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetPdpServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_pdp_service_group(
        self,
        service_group_id: str,
    ) -> main_models.GetPdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_pdp_service_group_with_options(service_group_id, headers, runtime)

    async def get_pdp_service_group_async(
        self,
        service_group_id: str,
    ) -> main_models.GetPdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_pdp_service_group_with_options_async(service_group_id, headers, runtime)

    def get_product_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProductResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProduct',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_product_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetProductResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetProduct',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetProductResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_product(
        self,
        id: str,
    ) -> main_models.GetProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_product_with_options(id, headers, runtime)

    async def get_product_async(
        self,
        id: str,
    ) -> main_models.GetProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_product_with_options_async(id, headers, runtime)

    def get_resource_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource(
        self,
        id: str,
    ) -> main_models.GetResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_resource_with_options(id, headers, runtime)

    async def get_resource_async(
        self,
        id: str,
    ) -> main_models.GetResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_resource_with_options_async(id, headers, runtime)

    def get_role_with_options(
        self,
        role_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/role-id/{DaraURL.percent_encode(role_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_role_with_options_async(
        self,
        role_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/role-id/{DaraURL.percent_encode(role_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_role(
        self,
        role_id: str,
    ) -> main_models.GetRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_role_with_options(role_id, headers, runtime)

    async def get_role_async(
        self,
        role_id: str,
    ) -> main_models.GetRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_role_with_options_async(role_id, headers, runtime)

    def get_stack_detail_with_options(
        self,
        trace_id: str,
        request: main_models.GetStackDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStackDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.rpc_id):
            query['rpcId'] = request.rpc_id
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackDetail',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/traces/{DaraURL.percent_encode(trace_id)}/commonds/stack',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stack_detail_with_options_async(
        self,
        trace_id: str,
        request: main_models.GetStackDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetStackDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.rpc_id):
            query['rpcId'] = request.rpc_id
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetStackDetail',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/traces/{DaraURL.percent_encode(trace_id)}/commonds/stack',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetStackDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_stack_detail(
        self,
        trace_id: str,
        request: main_models.GetStackDetailRequest,
    ) -> main_models.GetStackDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_stack_detail_with_options(trace_id, request, headers, runtime)

    async def get_stack_detail_async(
        self,
        trace_id: str,
        request: main_models.GetStackDetailRequest,
    ) -> main_models.GetStackDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_stack_detail_with_options_async(trace_id, request, headers, runtime)

    def get_token_with_options(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['accountId'] = request.account_id
        if not DaraCore.is_null(request.pbc_id):
            body['pbcId'] = request.pbc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs/token',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_token_with_options_async(
        self,
        request: main_models.GetTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTokenResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.account_id):
            body['accountId'] = request.account_id
        if not DaraCore.is_null(request.pbc_id):
            body['pbcId'] = request.pbc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GetToken',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs/token',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_token(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_token_with_options(request, headers, runtime)

    async def get_token_async(
        self,
        request: main_models.GetTokenRequest,
    ) -> main_models.GetTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_token_with_options_async(request, headers, runtime)

    def get_trace_detail_with_options(
        self,
        trace_id: str,
        request: main_models.GetTraceDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceDetail',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/traces/{DaraURL.percent_encode(trace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_trace_detail_with_options_async(
        self,
        trace_id: str,
        request: main_models.GetTraceDetailRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTraceDetailResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTraceDetail',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/traces/{DaraURL.percent_encode(trace_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTraceDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_trace_detail(
        self,
        trace_id: str,
        request: main_models.GetTraceDetailRequest,
    ) -> main_models.GetTraceDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_trace_detail_with_options(trace_id, request, headers, runtime)

    async def get_trace_detail_async(
        self,
        trace_id: str,
        request: main_models.GetTraceDetailRequest,
    ) -> main_models.GetTraceDetailResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_trace_detail_with_options_async(trace_id, request, headers, runtime)

    def grant_role_with_options(
        self,
        role_id: str,
        request: main_models.GrantRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GrantRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/commands/grant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.GrantRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_role_with_options_async(
        self,
        role_id: str,
        request: main_models.GrantRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'GrantRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/commands/grant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.GrantRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_role(
        self,
        role_id: str,
        request: main_models.GrantRoleRequest,
    ) -> main_models.GrantRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.grant_role_with_options(role_id, request, headers, runtime)

    async def grant_role_async(
        self,
        role_id: str,
        request: main_models.GrantRoleRequest,
    ) -> main_models.GrantRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.grant_role_with_options_async(role_id, request, headers, runtime)

    def list_authorize_products_with_options(
        self,
        request: main_models.ListAuthorizeProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizeProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizeProducts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products/commands/list-authorize',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizeProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_authorize_products_with_options_async(
        self,
        request: main_models.ListAuthorizeProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListAuthorizeProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAuthorizeProducts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products/commands/list-authorize',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAuthorizeProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_authorize_products(
        self,
        request: main_models.ListAuthorizeProductsRequest,
    ) -> main_models.ListAuthorizeProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_authorize_products_with_options(request, headers, runtime)

    async def list_authorize_products_async(
        self,
        request: main_models.ListAuthorizeProductsRequest,
    ) -> main_models.ListAuthorizeProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_authorize_products_with_options_async(request, headers, runtime)

    def list_buc_user_enterprise_with_options(
        self,
        request: main_models.ListBucUserEnterpriseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBucUserEnterpriseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.emp_id):
            query['empId'] = request.emp_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBucUserEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/bucs/enterprises',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBucUserEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_buc_user_enterprise_with_options_async(
        self,
        request: main_models.ListBucUserEnterpriseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListBucUserEnterpriseResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.emp_id):
            query['empId'] = request.emp_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListBucUserEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/bucs/enterprises',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListBucUserEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_buc_user_enterprise(
        self,
        request: main_models.ListBucUserEnterpriseRequest,
    ) -> main_models.ListBucUserEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_buc_user_enterprise_with_options(request, headers, runtime)

    async def list_buc_user_enterprise_async(
        self,
        request: main_models.ListBucUserEnterpriseRequest,
    ) -> main_models.ListBucUserEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_buc_user_enterprise_with_options_async(request, headers, runtime)

    def list_component_templates_with_options(
        self,
        request: main_models.ListComponentTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponentTemplates',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_component_templates_with_options_async(
        self,
        request: main_models.ListComponentTemplatesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentTemplatesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponentTemplates',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentTemplatesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_component_templates(
        self,
        request: main_models.ListComponentTemplatesRequest,
    ) -> main_models.ListComponentTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_component_templates_with_options(request, headers, runtime)

    async def list_component_templates_async(
        self,
        request: main_models.ListComponentTemplatesRequest,
    ) -> main_models.ListComponentTemplatesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_component_templates_with_options_async(request, headers, runtime)

    def list_components_with_options(
        self,
        request: main_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_components_with_options_async(
        self,
        request: main_models.ListComponentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListComponentsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.template_id):
            query['templateId'] = request.template_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListComponents',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListComponentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_components(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_components_with_options(request, headers, runtime)

    async def list_components_async(
        self,
        request: main_models.ListComponentsRequest,
    ) -> main_models.ListComponentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_components_with_options_async(request, headers, runtime)

    def list_depend_librarys_with_options(
        self,
        request: main_models.ListDependLibrarysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDependLibrarysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDependLibrarys',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/commands/list-dependency',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDependLibrarysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_depend_librarys_with_options_async(
        self,
        request: main_models.ListDependLibrarysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDependLibrarysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDependLibrarys',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/commands/list-dependency',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDependLibrarysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_depend_librarys(
        self,
        request: main_models.ListDependLibrarysRequest,
    ) -> main_models.ListDependLibrarysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_depend_librarys_with_options(request, headers, runtime)

    async def list_depend_librarys_async(
        self,
        request: main_models.ListDependLibrarysRequest,
    ) -> main_models.ListDependLibrarysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_depend_librarys_with_options_async(request, headers, runtime)

    def list_deployments_with_options(
        self,
        tmp_req: main_models.ListDeploymentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentsResponse:
        tmp_req.validate()
        request = main_models.ListDeploymentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_status):
            request.exclude_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_status, 'excludeStatus', 'json')
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not DaraCore.is_null(request.exclude_status_shrink):
            query['excludeStatus'] = request.exclude_status_shrink
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.status_shrink):
            query['status'] = request.status_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeployments',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_deployments_with_options_async(
        self,
        tmp_req: main_models.ListDeploymentsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeploymentsResponse:
        tmp_req.validate()
        request = main_models.ListDeploymentsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.exclude_status):
            request.exclude_status_shrink = Utils.array_to_string_with_specified_style(tmp_req.exclude_status, 'excludeStatus', 'json')
        if not DaraCore.is_null(tmp_req.status):
            request.status_shrink = Utils.array_to_string_with_specified_style(tmp_req.status, 'status', 'json')
        query = {}
        if not DaraCore.is_null(request.exclude_status_shrink):
            query['excludeStatus'] = request.exclude_status_shrink
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.status_shrink):
            query['status'] = request.status_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeployments',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeploymentsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_deployments(
        self,
        request: main_models.ListDeploymentsRequest,
    ) -> main_models.ListDeploymentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_deployments_with_options(request, headers, runtime)

    async def list_deployments_async(
        self,
        request: main_models.ListDeploymentsRequest,
    ) -> main_models.ListDeploymentsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_deployments_with_options_async(request, headers, runtime)

    def list_developer_enterprises_with_options(
        self,
        account_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeveloperEnterprisesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDeveloperEnterprises',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/developers/{DaraURL.percent_encode(account_id)}/commands/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeveloperEnterprisesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_developer_enterprises_with_options_async(
        self,
        account_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeveloperEnterprisesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDeveloperEnterprises',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/developers/{DaraURL.percent_encode(account_id)}/commands/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeveloperEnterprisesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_developer_enterprises(
        self,
        account_id: str,
    ) -> main_models.ListDeveloperEnterprisesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_developer_enterprises_with_options(account_id, headers, runtime)

    async def list_developer_enterprises_async(
        self,
        account_id: str,
    ) -> main_models.ListDeveloperEnterprisesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_developer_enterprises_with_options_async(account_id, headers, runtime)

    def list_developer_pbcs_with_options(
        self,
        request: main_models.ListDeveloperPbcsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeveloperPbcsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeveloperPbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/commands/allow-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeveloperPbcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_developer_pbcs_with_options_async(
        self,
        request: main_models.ListDeveloperPbcsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDeveloperPbcsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeveloperPbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/commands/allow-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeveloperPbcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_developer_pbcs(
        self,
        request: main_models.ListDeveloperPbcsRequest,
    ) -> main_models.ListDeveloperPbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_developer_pbcs_with_options(request, headers, runtime)

    async def list_developer_pbcs_async(
        self,
        request: main_models.ListDeveloperPbcsRequest,
    ) -> main_models.ListDeveloperPbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_developer_pbcs_with_options_async(request, headers, runtime)

    def list_developers_with_options(
        self,
        tmp_req: main_models.ListDevelopersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDevelopersResponse:
        tmp_req.validate()
        request = main_models.ListDevelopersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'accountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['accountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.role_id):
            query['roleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDevelopers',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDevelopersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_developers_with_options_async(
        self,
        tmp_req: main_models.ListDevelopersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDevelopersResponse:
        tmp_req.validate()
        request = main_models.ListDevelopersShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'accountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_ids_shrink):
            query['accountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.role_id):
            query['roleId'] = request.role_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDevelopers',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDevelopersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_developers(
        self,
        request: main_models.ListDevelopersRequest,
    ) -> main_models.ListDevelopersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_developers_with_options(request, headers, runtime)

    async def list_developers_async(
        self,
        request: main_models.ListDevelopersRequest,
    ) -> main_models.ListDevelopersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_developers_with_options_async(request, headers, runtime)

    def list_downstream_pbc_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDownstreamPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDownstreamPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}/commands/list-downstream',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownstreamPbcResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_downstream_pbc_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDownstreamPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListDownstreamPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}/commands/list-downstream',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDownstreamPbcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_downstream_pbc(
        self,
        id: str,
    ) -> main_models.ListDownstreamPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_downstream_pbc_with_options(id, headers, runtime)

    async def list_downstream_pbc_async(
        self,
        id: str,
    ) -> main_models.ListDownstreamPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_downstream_pbc_with_options_async(id, headers, runtime)

    def list_enterprises_with_options(
        self,
        request: main_models.ListEnterprisesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterprisesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterprises',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterprisesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enterprises_with_options_async(
        self,
        request: main_models.ListEnterprisesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnterprisesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnterprises',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnterprisesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enterprises(
        self,
        request: main_models.ListEnterprisesRequest,
    ) -> main_models.ListEnterprisesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_enterprises_with_options(request, headers, runtime)

    async def list_enterprises_async(
        self,
        request: main_models.ListEnterprisesRequest,
    ) -> main_models.ListEnterprisesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_enterprises_with_options_async(request, headers, runtime)

    def list_env_infos_with_options(
        self,
        request: main_models.ListEnvInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvInfos',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/env/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_env_infos_with_options_async(
        self,
        request: main_models.ListEnvInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListEnvInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEnvInfos',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/env/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnvInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_env_infos(
        self,
        request: main_models.ListEnvInfosRequest,
    ) -> main_models.ListEnvInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_env_infos_with_options(request, headers, runtime)

    async def list_env_infos_async(
        self,
        request: main_models.ListEnvInfosRequest,
    ) -> main_models.ListEnvInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_env_infos_with_options_async(request, headers, runtime)

    def list_fork_reviews_with_options(
        self,
        request: main_models.ListForkReviewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListForkReviewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reviewer):
            query['reviewer'] = request.reviewer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListForkReviews',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/fork-reviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListForkReviewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_fork_reviews_with_options_async(
        self,
        request: main_models.ListForkReviewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListForkReviewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reviewer):
            query['reviewer'] = request.reviewer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListForkReviews',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/fork-reviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListForkReviewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_fork_reviews(
        self,
        request: main_models.ListForkReviewsRequest,
    ) -> main_models.ListForkReviewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_fork_reviews_with_options(request, headers, runtime)

    async def list_fork_reviews_async(
        self,
        request: main_models.ListForkReviewsRequest,
    ) -> main_models.ListForkReviewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_fork_reviews_with_options_async(request, headers, runtime)

    def list_granted_roles_with_options(
        self,
        request: main_models.ListGrantedRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGrantedRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorizer_id):
            query['authorizerId'] = request.authorizer_id
        if not DaraCore.is_null(request.authorizer_type):
            query['authorizerType'] = request.authorizer_type
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGrantedRoles',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/commands/list-granted-roles',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGrantedRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_granted_roles_with_options_async(
        self,
        request: main_models.ListGrantedRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListGrantedRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.authorizer_id):
            query['authorizerId'] = request.authorizer_id
        if not DaraCore.is_null(request.authorizer_type):
            query['authorizerType'] = request.authorizer_type
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListGrantedRoles',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/commands/list-granted-roles',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListGrantedRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_granted_roles(
        self,
        request: main_models.ListGrantedRolesRequest,
    ) -> main_models.ListGrantedRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_granted_roles_with_options(request, headers, runtime)

    async def list_granted_roles_async(
        self,
        request: main_models.ListGrantedRolesRequest,
    ) -> main_models.ListGrantedRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_granted_roles_with_options_async(request, headers, runtime)

    def list_invoke_pbcs_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInvokePbcsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListInvokePbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(id)}/commands/invoke-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInvokePbcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_invoke_pbcs_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListInvokePbcsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListInvokePbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(id)}/commands/invoke-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListInvokePbcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_invoke_pbcs(
        self,
        id: str,
    ) -> main_models.ListInvokePbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_invoke_pbcs_with_options(id, headers, runtime)

    async def list_invoke_pbcs_async(
        self,
        id: str,
    ) -> main_models.ListInvokePbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_invoke_pbcs_with_options_async(id, headers, runtime)

    def list_library_reviews_with_options(
        self,
        request: main_models.ListLibraryReviewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLibraryReviewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reviewer):
            query['reviewer'] = request.reviewer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLibraryReviews',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLibraryReviewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_library_reviews_with_options_async(
        self,
        request: main_models.ListLibraryReviewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLibraryReviewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reviewer):
            query['reviewer'] = request.reviewer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLibraryReviews',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLibraryReviewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_library_reviews(
        self,
        request: main_models.ListLibraryReviewsRequest,
    ) -> main_models.ListLibraryReviewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_library_reviews_with_options(request, headers, runtime)

    async def list_library_reviews_async(
        self,
        request: main_models.ListLibraryReviewsRequest,
    ) -> main_models.ListLibraryReviewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_library_reviews_with_options_async(request, headers, runtime)

    def list_librarys_with_options(
        self,
        request: main_models.ListLibrarysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLibrarysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLibrarys',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLibrarysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_librarys_with_options_async(
        self,
        request: main_models.ListLibrarysRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListLibrarysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.provider):
            query['provider'] = request.provider
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListLibrarys',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListLibrarysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_librarys(
        self,
        request: main_models.ListLibrarysRequest,
    ) -> main_models.ListLibrarysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_librarys_with_options(request, headers, runtime)

    async def list_librarys_async(
        self,
        request: main_models.ListLibrarysRequest,
    ) -> main_models.ListLibrarysResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_librarys_with_options_async(request, headers, runtime)

    def list_markets_with_options(
        self,
        request: main_models.ListMarketsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMarketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMarkets',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/markets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMarketsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_markets_with_options_async(
        self,
        request: main_models.ListMarketsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMarketsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMarkets',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/markets',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMarketsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_markets(
        self,
        request: main_models.ListMarketsRequest,
    ) -> main_models.ListMarketsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_markets_with_options(request, headers, runtime)

    async def list_markets_async(
        self,
        request: main_models.ListMarketsRequest,
    ) -> main_models.ListMarketsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_markets_with_options_async(request, headers, runtime)

    def list_metadata_infos_with_options(
        self,
        request: main_models.ListMetadataInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMetadataInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.namespace_id):
            query['namespace_id'] = request.namespace_id
        if not DaraCore.is_null(request.namespace_name):
            query['namespace_name'] = request.namespace_name
        if not DaraCore.is_null(request.order_by):
            query['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbc_id'] = request.pbc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMetadataInfos',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/metadata',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetadataInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_metadata_infos_with_options_async(
        self,
        request: main_models.ListMetadataInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMetadataInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.namespace_id):
            query['namespace_id'] = request.namespace_id
        if not DaraCore.is_null(request.namespace_name):
            query['namespace_name'] = request.namespace_name
        if not DaraCore.is_null(request.order_by):
            query['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.org_id):
            query['org_id'] = request.org_id
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbc_id'] = request.pbc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMetadataInfos',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/metadata',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMetadataInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_metadata_infos(
        self,
        request: main_models.ListMetadataInfosRequest,
    ) -> main_models.ListMetadataInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_metadata_infos_with_options(request, headers, runtime)

    async def list_metadata_infos_async(
        self,
        request: main_models.ListMetadataInfosRequest,
    ) -> main_models.ListMetadataInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_metadata_infos_with_options_async(request, headers, runtime)

    def list_micro_service_with_options(
        self,
        env: str,
        request: main_models.ListMicroServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMicroServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.service_ids):
            query['serviceIds'] = request.service_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMicroService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/group/env/{DaraURL.percent_encode(env)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMicroServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_micro_service_with_options_async(
        self,
        env: str,
        request: main_models.ListMicroServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMicroServiceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.service_ids):
            query['serviceIds'] = request.service_ids
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMicroService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/group/env/{DaraURL.percent_encode(env)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMicroServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_micro_service(
        self,
        env: str,
        request: main_models.ListMicroServiceRequest,
    ) -> main_models.ListMicroServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_micro_service_with_options(env, request, headers, runtime)

    async def list_micro_service_async(
        self,
        env: str,
        request: main_models.ListMicroServiceRequest,
    ) -> main_models.ListMicroServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_micro_service_with_options_async(env, request, headers, runtime)

    def list_monitor_contact_groups_with_options(
        self,
        request: main_models.ListMonitorContactGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorContactGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorContactGroups',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorContactGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_monitor_contact_groups_with_options_async(
        self,
        request: main_models.ListMonitorContactGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorContactGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorContactGroups',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorContactGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_monitor_contact_groups(
        self,
        request: main_models.ListMonitorContactGroupsRequest,
    ) -> main_models.ListMonitorContactGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_monitor_contact_groups_with_options(request, headers, runtime)

    async def list_monitor_contact_groups_async(
        self,
        request: main_models.ListMonitorContactGroupsRequest,
    ) -> main_models.ListMonitorContactGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_monitor_contact_groups_with_options_async(request, headers, runtime)

    def list_monitor_contacts_with_options(
        self,
        request: main_models.ListMonitorContactsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorContacts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorContactsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_monitor_contacts_with_options_async(
        self,
        request: main_models.ListMonitorContactsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorContactsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorContacts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorContactsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_monitor_contacts(
        self,
        request: main_models.ListMonitorContactsRequest,
    ) -> main_models.ListMonitorContactsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_monitor_contacts_with_options(request, headers, runtime)

    async def list_monitor_contacts_async(
        self,
        request: main_models.ListMonitorContactsRequest,
    ) -> main_models.ListMonitorContactsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_monitor_contacts_with_options_async(request, headers, runtime)

    def list_monitor_notify_objects_with_options(
        self,
        request: main_models.ListMonitorNotifyObjectsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorNotifyObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.webhook_type):
            query['webhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorNotifyObjects',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/listMonitorNotifyObjects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorNotifyObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_monitor_notify_objects_with_options_async(
        self,
        request: main_models.ListMonitorNotifyObjectsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorNotifyObjectsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.webhook_type):
            query['webhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorNotifyObjects',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/listMonitorNotifyObjects',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorNotifyObjectsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_monitor_notify_objects(
        self,
        request: main_models.ListMonitorNotifyObjectsRequest,
    ) -> main_models.ListMonitorNotifyObjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_monitor_notify_objects_with_options(request, headers, runtime)

    async def list_monitor_notify_objects_async(
        self,
        request: main_models.ListMonitorNotifyObjectsRequest,
    ) -> main_models.ListMonitorNotifyObjectsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_monitor_notify_objects_with_options_async(request, headers, runtime)

    def list_monitor_tasks_with_options(
        self,
        request: main_models.ListMonitorTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_name):
            query['alertName'] = request.alert_name
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorTasks',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/listMonitorTasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorTasksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_monitor_tasks_with_options_async(
        self,
        request: main_models.ListMonitorTasksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorTasksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.alert_name):
            query['alertName'] = request.alert_name
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorTasks',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/listMonitorTasks',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorTasksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_monitor_tasks(
        self,
        request: main_models.ListMonitorTasksRequest,
    ) -> main_models.ListMonitorTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_monitor_tasks_with_options(request, headers, runtime)

    async def list_monitor_tasks_async(
        self,
        request: main_models.ListMonitorTasksRequest,
    ) -> main_models.ListMonitorTasksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_monitor_tasks_with_options_async(request, headers, runtime)

    def list_monitor_webhooks_with_options(
        self,
        request: main_models.ListMonitorWebhooksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorWebhooksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.webhook_type):
            query['webhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorWebhooks',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorWebhooksResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_monitor_webhooks_with_options_async(
        self,
        request: main_models.ListMonitorWebhooksRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMonitorWebhooksResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.webhook_type):
            query['webhookType'] = request.webhook_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMonitorWebhooks',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMonitorWebhooksResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_monitor_webhooks(
        self,
        request: main_models.ListMonitorWebhooksRequest,
    ) -> main_models.ListMonitorWebhooksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_monitor_webhooks_with_options(request, headers, runtime)

    async def list_monitor_webhooks_async(
        self,
        request: main_models.ListMonitorWebhooksRequest,
    ) -> main_models.ListMonitorWebhooksResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_monitor_webhooks_with_options_async(request, headers, runtime)

    def list_mq_group_msgs_with_options(
        self,
        group_id: str,
        request: main_models.ListMqGroupMsgsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMqGroupMsgsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.msg_id):
            query['msgId'] = request.msg_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMqGroupMsgs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/group/{DaraURL.percent_encode(group_id)}/commands/msgs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMqGroupMsgsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mq_group_msgs_with_options_async(
        self,
        group_id: str,
        request: main_models.ListMqGroupMsgsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMqGroupMsgsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.msg_id):
            query['msgId'] = request.msg_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMqGroupMsgs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/group/{DaraURL.percent_encode(group_id)}/commands/msgs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMqGroupMsgsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mq_group_msgs(
        self,
        group_id: str,
        request: main_models.ListMqGroupMsgsRequest,
    ) -> main_models.ListMqGroupMsgsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mq_group_msgs_with_options(group_id, request, headers, runtime)

    async def list_mq_group_msgs_async(
        self,
        group_id: str,
        request: main_models.ListMqGroupMsgsRequest,
    ) -> main_models.ListMqGroupMsgsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mq_group_msgs_with_options_async(group_id, request, headers, runtime)

    def list_mq_topic_msgs_with_options(
        self,
        topic_id: str,
        request: main_models.ListMqTopicMsgsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMqTopicMsgsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.msg_id):
            query['msgId'] = request.msg_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMqTopicMsgs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/{DaraURL.percent_encode(topic_id)}/commands/msgs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMqTopicMsgsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mq_topic_msgs_with_options_async(
        self,
        topic_id: str,
        request: main_models.ListMqTopicMsgsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMqTopicMsgsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.msg_id):
            query['msgId'] = request.msg_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMqTopicMsgs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/{DaraURL.percent_encode(topic_id)}/commands/msgs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMqTopicMsgsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mq_topic_msgs(
        self,
        topic_id: str,
        request: main_models.ListMqTopicMsgsRequest,
    ) -> main_models.ListMqTopicMsgsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mq_topic_msgs_with_options(topic_id, request, headers, runtime)

    async def list_mq_topic_msgs_async(
        self,
        topic_id: str,
        request: main_models.ListMqTopicMsgsRequest,
    ) -> main_models.ListMqTopicMsgsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mq_topic_msgs_with_options_async(topic_id, request, headers, runtime)

    def list_mq_topic_subs_with_options(
        self,
        topic_id: str,
        request: main_models.ListMqTopicSubsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMqTopicSubsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMqTopicSubs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/{DaraURL.percent_encode(topic_id)}/commands/subs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMqTopicSubsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mq_topic_subs_with_options_async(
        self,
        topic_id: str,
        request: main_models.ListMqTopicSubsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMqTopicSubsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMqTopicSubs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/{DaraURL.percent_encode(topic_id)}/commands/subs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMqTopicSubsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mq_topic_subs(
        self,
        topic_id: str,
        request: main_models.ListMqTopicSubsRequest,
    ) -> main_models.ListMqTopicSubsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mq_topic_subs_with_options(topic_id, request, headers, runtime)

    async def list_mq_topic_subs_async(
        self,
        topic_id: str,
        request: main_models.ListMqTopicSubsRequest,
    ) -> main_models.ListMqTopicSubsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mq_topic_subs_with_options_async(topic_id, request, headers, runtime)

    def list_mq_topics_with_options(
        self,
        env: str,
        pbc_id: str,
        request: main_models.ListMqTopicsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMqTopicsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMqTopics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/env/{DaraURL.percent_encode(env)}/pbcId/{DaraURL.percent_encode(pbc_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMqTopicsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_mq_topics_with_options_async(
        self,
        env: str,
        pbc_id: str,
        request: main_models.ListMqTopicsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListMqTopicsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.topic_name):
            query['topicName'] = request.topic_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMqTopics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/env/{DaraURL.percent_encode(env)}/pbcId/{DaraURL.percent_encode(pbc_id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMqTopicsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_mq_topics(
        self,
        env: str,
        pbc_id: str,
        request: main_models.ListMqTopicsRequest,
    ) -> main_models.ListMqTopicsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_mq_topics_with_options(env, pbc_id, request, headers, runtime)

    async def list_mq_topics_async(
        self,
        env: str,
        pbc_id: str,
        request: main_models.ListMqTopicsRequest,
    ) -> main_models.ListMqTopicsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_mq_topics_with_options_async(env, pbc_id, request, headers, runtime)

    def list_pbc_invoke_reviews_with_options(
        self,
        request: main_models.ListPbcInvokeReviewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcInvokeReviewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.orderby):
            query['orderby'] = request.orderby
        if not DaraCore.is_null(request.reviewer):
            query['reviewer'] = request.reviewer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcInvokeReviews',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invoke-reviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcInvokeReviewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pbc_invoke_reviews_with_options_async(
        self,
        request: main_models.ListPbcInvokeReviewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcInvokeReviewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.orderby):
            query['orderby'] = request.orderby
        if not DaraCore.is_null(request.reviewer):
            query['reviewer'] = request.reviewer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcInvokeReviews',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invoke-reviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcInvokeReviewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pbc_invoke_reviews(
        self,
        request: main_models.ListPbcInvokeReviewsRequest,
    ) -> main_models.ListPbcInvokeReviewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pbc_invoke_reviews_with_options(request, headers, runtime)

    async def list_pbc_invoke_reviews_async(
        self,
        request: main_models.ListPbcInvokeReviewsRequest,
    ) -> main_models.ListPbcInvokeReviewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pbc_invoke_reviews_with_options_async(request, headers, runtime)

    def list_pbc_invokes_with_options(
        self,
        request: main_models.ListPbcInvokesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcInvokesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcInvokes',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invokes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcInvokesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pbc_invokes_with_options_async(
        self,
        request: main_models.ListPbcInvokesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcInvokesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcInvokes',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-invokes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcInvokesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pbc_invokes(
        self,
        request: main_models.ListPbcInvokesRequest,
    ) -> main_models.ListPbcInvokesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pbc_invokes_with_options(request, headers, runtime)

    async def list_pbc_invokes_async(
        self,
        request: main_models.ListPbcInvokesRequest,
    ) -> main_models.ListPbcInvokesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pbc_invokes_with_options_async(request, headers, runtime)

    def list_pbc_reviews_with_options(
        self,
        request: main_models.ListPbcReviewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcReviewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reviewer):
            query['reviewer'] = request.reviewer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcReviews',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcReviewsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pbc_reviews_with_options_async(
        self,
        request: main_models.ListPbcReviewsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcReviewsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.reviewer):
            query['reviewer'] = request.reviewer
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcReviews',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcReviewsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pbc_reviews(
        self,
        request: main_models.ListPbcReviewsRequest,
    ) -> main_models.ListPbcReviewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pbc_reviews_with_options(request, headers, runtime)

    async def list_pbc_reviews_async(
        self,
        request: main_models.ListPbcReviewsRequest,
    ) -> main_models.ListPbcReviewsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pbc_reviews_with_options_async(request, headers, runtime)

    def list_pbc_subscribe_with_options(
        self,
        request: main_models.ListPbcSubscribeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcSubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcSubscribe',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/commands/list-subscribe',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pbc_subscribe_with_options_async(
        self,
        request: main_models.ListPbcSubscribeRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcSubscribeResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcSubscribe',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/commands/list-subscribe',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcSubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pbc_subscribe(
        self,
        request: main_models.ListPbcSubscribeRequest,
    ) -> main_models.ListPbcSubscribeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pbc_subscribe_with_options(request, headers, runtime)

    async def list_pbc_subscribe_async(
        self,
        request: main_models.ListPbcSubscribeRequest,
    ) -> main_models.ListPbcSubscribeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pbc_subscribe_with_options_async(request, headers, runtime)

    def list_pbc_version_build_with_options(
        self,
        request: main_models.ListPbcVersionBuildRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcVersionBuildResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['accountId'] = request.account_id
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcVersionBuild',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/commands/list-build',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcVersionBuildResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pbc_version_build_with_options_async(
        self,
        request: main_models.ListPbcVersionBuildRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcVersionBuildResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['accountId'] = request.account_id
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcVersionBuild',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/commands/list-build',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcVersionBuildResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pbc_version_build(
        self,
        request: main_models.ListPbcVersionBuildRequest,
    ) -> main_models.ListPbcVersionBuildResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pbc_version_build_with_options(request, headers, runtime)

    async def list_pbc_version_build_async(
        self,
        request: main_models.ListPbcVersionBuildRequest,
    ) -> main_models.ListPbcVersionBuildResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pbc_version_build_with_options_async(request, headers, runtime)

    def list_pbc_version_numbers_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcVersionNumbersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPbcVersionNumbers',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(id)}/commands/listPbcVersionNumbers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcVersionNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pbc_version_numbers_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcVersionNumbersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListPbcVersionNumbers',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(id)}/commands/listPbcVersionNumbers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcVersionNumbersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pbc_version_numbers(
        self,
        id: str,
    ) -> main_models.ListPbcVersionNumbersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pbc_version_numbers_with_options(id, headers, runtime)

    async def list_pbc_version_numbers_async(
        self,
        id: str,
    ) -> main_models.ListPbcVersionNumbersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pbc_version_numbers_with_options_async(id, headers, runtime)

    def list_pbcs_with_options(
        self,
        request: main_models.ListPbcsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.developer_id):
            query['developerId'] = request.developer_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pbcs_with_options_async(
        self,
        request: main_models.ListPbcsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPbcsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.developer_id):
            query['developerId'] = request.developer_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPbcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pbcs(
        self,
        request: main_models.ListPbcsRequest,
    ) -> main_models.ListPbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pbcs_with_options(request, headers, runtime)

    async def list_pbcs_async(
        self,
        request: main_models.ListPbcsRequest,
    ) -> main_models.ListPbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pbcs_with_options_async(request, headers, runtime)

    def list_pdp_configs_with_options(
        self,
        request: main_models.ListPdpConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpConfigs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pdp_configs_with_options_async(
        self,
        request: main_models.ListPdpConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpConfigs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pdp_configs(
        self,
        request: main_models.ListPdpConfigsRequest,
    ) -> main_models.ListPdpConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pdp_configs_with_options(request, headers, runtime)

    async def list_pdp_configs_async(
        self,
        request: main_models.ListPdpConfigsRequest,
    ) -> main_models.ListPdpConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pdp_configs_with_options_async(request, headers, runtime)

    def list_pdp_history_configs_with_options(
        self,
        request: main_models.ListPdpHistoryConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpHistoryConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['configId'] = request.config_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpHistoryConfigs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs/history',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpHistoryConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pdp_history_configs_with_options_async(
        self,
        request: main_models.ListPdpHistoryConfigsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpHistoryConfigsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.config_id):
            query['configId'] = request.config_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpHistoryConfigs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs/history',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpHistoryConfigsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pdp_history_configs(
        self,
        request: main_models.ListPdpHistoryConfigsRequest,
    ) -> main_models.ListPdpHistoryConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pdp_history_configs_with_options(request, headers, runtime)

    async def list_pdp_history_configs_async(
        self,
        request: main_models.ListPdpHistoryConfigsRequest,
    ) -> main_models.ListPdpHistoryConfigsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pdp_history_configs_with_options_async(request, headers, runtime)

    def list_pdp_image_with_options(
        self,
        request: main_models.ListPdpImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpImage',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/instance/images',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpImageResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pdp_image_with_options_async(
        self,
        request: main_models.ListPdpImageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpImageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpImage',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/instance/images',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpImageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pdp_image(
        self,
        request: main_models.ListPdpImageRequest,
    ) -> main_models.ListPdpImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pdp_image_with_options(request, headers, runtime)

    async def list_pdp_image_async(
        self,
        request: main_models.ListPdpImageRequest,
    ) -> main_models.ListPdpImageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pdp_image_with_options_async(request, headers, runtime)

    def list_pdp_lanes_with_options(
        self,
        request: main_models.ListPdpLanesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpLanesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.inlet_service_id):
            query['inletServiceId'] = request.inlet_service_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpLanes',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpLanesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pdp_lanes_with_options_async(
        self,
        request: main_models.ListPdpLanesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpLanesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.inlet_service_id):
            query['inletServiceId'] = request.inlet_service_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpLanes',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpLanesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pdp_lanes(
        self,
        request: main_models.ListPdpLanesRequest,
    ) -> main_models.ListPdpLanesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pdp_lanes_with_options(request, headers, runtime)

    async def list_pdp_lanes_async(
        self,
        request: main_models.ListPdpLanesRequest,
    ) -> main_models.ListPdpLanesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pdp_lanes_with_options_async(request, headers, runtime)

    def list_pdp_lanes_for_service_group_with_options(
        self,
        tmp_req: main_models.ListPdpLanesForServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpLanesForServiceGroupResponse:
        tmp_req.validate()
        request = main_models.ListPdpLanesForServiceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lane_ids):
            request.lane_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.lane_ids, 'laneIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.lane_ids_shrink):
            query['laneIds'] = request.lane_ids_shrink
        if not DaraCore.is_null(request.operator):
            query['operator'] = request.operator
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpLanesForServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/list-service-group-lane',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpLanesForServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pdp_lanes_for_service_group_with_options_async(
        self,
        tmp_req: main_models.ListPdpLanesForServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpLanesForServiceGroupResponse:
        tmp_req.validate()
        request = main_models.ListPdpLanesForServiceGroupShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.lane_ids):
            request.lane_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.lane_ids, 'laneIds', 'simple')
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.lane_ids_shrink):
            query['laneIds'] = request.lane_ids_shrink
        if not DaraCore.is_null(request.operator):
            query['operator'] = request.operator
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpLanesForServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/list-service-group-lane',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpLanesForServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pdp_lanes_for_service_group(
        self,
        request: main_models.ListPdpLanesForServiceGroupRequest,
    ) -> main_models.ListPdpLanesForServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pdp_lanes_for_service_group_with_options(request, headers, runtime)

    async def list_pdp_lanes_for_service_group_async(
        self,
        request: main_models.ListPdpLanesForServiceGroupRequest,
    ) -> main_models.ListPdpLanesForServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pdp_lanes_for_service_group_with_options_async(request, headers, runtime)

    def list_pdp_logs_with_options(
        self,
        request: main_models.ListPdpLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpLogs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/pdp-log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpLogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pdp_logs_with_options_async(
        self,
        request: main_models.ListPdpLogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpLogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.from_):
            query['from'] = request.from_
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.query):
            query['query'] = request.query
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.source_type):
            query['sourceType'] = request.source_type
        if not DaraCore.is_null(request.to):
            query['to'] = request.to
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpLogs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/pdp-log',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpLogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pdp_logs(
        self,
        request: main_models.ListPdpLogsRequest,
    ) -> main_models.ListPdpLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pdp_logs_with_options(request, headers, runtime)

    async def list_pdp_logs_async(
        self,
        request: main_models.ListPdpLogsRequest,
    ) -> main_models.ListPdpLogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pdp_logs_with_options_async(request, headers, runtime)

    def list_pdp_pbcs_with_options(
        self,
        tmp_req: main_models.ListPdpPbcsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpPbcsResponse:
        tmp_req.validate()
        request = main_models.ListPdpPbcsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pbc_ids):
            request.pbc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.pbc_ids, 'pbcIds', 'json')
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.developer_id):
            query['developerId'] = request.developer_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_ids_shrink):
            query['pbcIds'] = request.pbc_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpPbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpPbcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pdp_pbcs_with_options_async(
        self,
        tmp_req: main_models.ListPdpPbcsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpPbcsResponse:
        tmp_req.validate()
        request = main_models.ListPdpPbcsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pbc_ids):
            request.pbc_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.pbc_ids, 'pbcIds', 'json')
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.developer_id):
            query['developerId'] = request.developer_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_ids_shrink):
            query['pbcIds'] = request.pbc_ids_shrink
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpPbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpPbcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pdp_pbcs(
        self,
        request: main_models.ListPdpPbcsRequest,
    ) -> main_models.ListPdpPbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pdp_pbcs_with_options(request, headers, runtime)

    async def list_pdp_pbcs_async(
        self,
        request: main_models.ListPdpPbcsRequest,
    ) -> main_models.ListPdpPbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pdp_pbcs_with_options_async(request, headers, runtime)

    def list_pdp_service_groups_with_options(
        self,
        tmp_req: main_models.ListPdpServiceGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpServiceGroupsResponse:
        tmp_req.validate()
        request = main_models.ListPdpServiceGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'ids', 'json')
        query = {}
        if not DaraCore.is_null(request.alias):
            query['alias'] = request.alias
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.env_type):
            query['envType'] = request.env_type
        if not DaraCore.is_null(request.group_type):
            query['groupType'] = request.group_type
        if not DaraCore.is_null(request.ids_shrink):
            query['ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.org_type):
            query['orgType'] = request.org_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.repo_id):
            query['repoId'] = request.repo_id
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpServiceGroups',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpServiceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pdp_service_groups_with_options_async(
        self,
        tmp_req: main_models.ListPdpServiceGroupsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpServiceGroupsResponse:
        tmp_req.validate()
        request = main_models.ListPdpServiceGroupsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.ids):
            request.ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.ids, 'ids', 'json')
        query = {}
        if not DaraCore.is_null(request.alias):
            query['alias'] = request.alias
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.env_type):
            query['envType'] = request.env_type
        if not DaraCore.is_null(request.group_type):
            query['groupType'] = request.group_type
        if not DaraCore.is_null(request.ids_shrink):
            query['ids'] = request.ids_shrink
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.org_type):
            query['orgType'] = request.org_type
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.region):
            query['region'] = request.region
        if not DaraCore.is_null(request.repo_id):
            query['repoId'] = request.repo_id
        if not DaraCore.is_null(request.service_id):
            query['serviceId'] = request.service_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpServiceGroups',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpServiceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pdp_service_groups(
        self,
        request: main_models.ListPdpServiceGroupsRequest,
    ) -> main_models.ListPdpServiceGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pdp_service_groups_with_options(request, headers, runtime)

    async def list_pdp_service_groups_async(
        self,
        request: main_models.ListPdpServiceGroupsRequest,
    ) -> main_models.ListPdpServiceGroupsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pdp_service_groups_with_options_async(request, headers, runtime)

    def list_pdp_services_with_options(
        self,
        tmp_req: main_models.ListPdpServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpServicesResponse:
        tmp_req.validate()
        request = main_models.ListPdpServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pdp_service_ids):
            request.pdp_service_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.pdp_service_ids, 'pdpServiceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.alias):
            query['alias'] = request.alias
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.pdp_service_ids_shrink):
            query['pdpServiceIds'] = request.pdp_service_ids_shrink
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpServices',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpServicesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_pdp_services_with_options_async(
        self,
        tmp_req: main_models.ListPdpServicesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPdpServicesResponse:
        tmp_req.validate()
        request = main_models.ListPdpServicesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.pdp_service_ids):
            request.pdp_service_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.pdp_service_ids, 'pdpServiceIds', 'json')
        query = {}
        if not DaraCore.is_null(request.alias):
            query['alias'] = request.alias
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.pdp_service_ids_shrink):
            query['pdpServiceIds'] = request.pdp_service_ids_shrink
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPdpServices',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPdpServicesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_pdp_services(
        self,
        request: main_models.ListPdpServicesRequest,
    ) -> main_models.ListPdpServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_pdp_services_with_options(request, headers, runtime)

    async def list_pdp_services_async(
        self,
        request: main_models.ListPdpServicesRequest,
    ) -> main_models.ListPdpServicesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_pdp_services_with_options_async(request, headers, runtime)

    def list_permission_resource_with_options(
        self,
        request: main_models.ListPermissionResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.operator_id):
            query['operatorId'] = request.operator_id
        if not DaraCore.is_null(request.operator_type):
            query['operatorType'] = request.operator_type
        if not DaraCore.is_null(request.resource_prefix):
            query['resourcePrefix'] = request.resource_prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/permissions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permission_resource_with_options_async(
        self,
        request: main_models.ListPermissionResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionResourceResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.operator_id):
            query['operatorId'] = request.operator_id
        if not DaraCore.is_null(request.operator_type):
            query['operatorType'] = request.operator_type
        if not DaraCore.is_null(request.resource_prefix):
            query['resourcePrefix'] = request.resource_prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/permissions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permission_resource(
        self,
        request: main_models.ListPermissionResourceRequest,
    ) -> main_models.ListPermissionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_permission_resource_with_options(request, headers, runtime)

    async def list_permission_resource_async(
        self,
        request: main_models.ListPermissionResourceRequest,
    ) -> main_models.ListPermissionResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_permission_resource_with_options_async(request, headers, runtime)

    def list_permission_resource_for_front_with_options(
        self,
        request: main_models.ListPermissionResourceForFrontRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionResourceForFrontResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.operator_id):
            query['operatorId'] = request.operator_id
        if not DaraCore.is_null(request.operator_type):
            query['operatorType'] = request.operator_type
        if not DaraCore.is_null(request.query_type):
            query['queryType'] = request.query_type
        if not DaraCore.is_null(request.resource_prefix):
            query['resourcePrefix'] = request.resource_prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionResourceForFront',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/permissions/command/front-permission',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionResourceForFrontResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permission_resource_for_front_with_options_async(
        self,
        request: main_models.ListPermissionResourceForFrontRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionResourceForFrontResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.operator_id):
            query['operatorId'] = request.operator_id
        if not DaraCore.is_null(request.operator_type):
            query['operatorType'] = request.operator_type
        if not DaraCore.is_null(request.query_type):
            query['queryType'] = request.query_type
        if not DaraCore.is_null(request.resource_prefix):
            query['resourcePrefix'] = request.resource_prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionResourceForFront',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/permissions/command/front-permission',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionResourceForFrontResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permission_resource_for_front(
        self,
        request: main_models.ListPermissionResourceForFrontRequest,
    ) -> main_models.ListPermissionResourceForFrontResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_permission_resource_for_front_with_options(request, headers, runtime)

    async def list_permission_resource_for_front_async(
        self,
        request: main_models.ListPermissionResourceForFrontRequest,
    ) -> main_models.ListPermissionResourceForFrontResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_permission_resource_for_front_with_options_async(request, headers, runtime)

    def list_permission_resource_pop_with_options(
        self,
        request: main_models.ListPermissionResourcePopRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionResourcePopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        if not DaraCore.is_null(request.operator_id):
            query['operatorId'] = request.operator_id
        if not DaraCore.is_null(request.operator_type):
            query['operatorType'] = request.operator_type
        if not DaraCore.is_null(request.resource_prefix):
            query['resourcePrefix'] = request.resource_prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionResourcePop',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/permissions/pop',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionResourcePopResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permission_resource_pop_with_options_async(
        self,
        request: main_models.ListPermissionResourcePopRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionResourcePopResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.action):
            query['action'] = request.action
        if not DaraCore.is_null(request.operator_id):
            query['operatorId'] = request.operator_id
        if not DaraCore.is_null(request.operator_type):
            query['operatorType'] = request.operator_type
        if not DaraCore.is_null(request.resource_prefix):
            query['resourcePrefix'] = request.resource_prefix
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissionResourcePop',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/permissions/pop',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionResourcePopResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permission_resource_pop(
        self,
        request: main_models.ListPermissionResourcePopRequest,
    ) -> main_models.ListPermissionResourcePopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_permission_resource_pop_with_options(request, headers, runtime)

    async def list_permission_resource_pop_async(
        self,
        request: main_models.ListPermissionResourcePopRequest,
    ) -> main_models.ListPermissionResourcePopResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_permission_resource_pop_with_options_async(request, headers, runtime)

    def list_privilege_by_role_with_options(
        self,
        role_id: str,
        request: main_models.ListPrivilegeByRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivilegeByRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['accountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivilegeByRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/privileges',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivilegeByRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_privilege_by_role_with_options_async(
        self,
        role_id: str,
        request: main_models.ListPrivilegeByRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPrivilegeByRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['accountId'] = request.account_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPrivilegeByRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/privileges',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPrivilegeByRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_privilege_by_role(
        self,
        role_id: str,
        request: main_models.ListPrivilegeByRoleRequest,
    ) -> main_models.ListPrivilegeByRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_privilege_by_role_with_options(role_id, request, headers, runtime)

    async def list_privilege_by_role_async(
        self,
        role_id: str,
        request: main_models.ListPrivilegeByRoleRequest,
    ) -> main_models.ListPrivilegeByRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_privilege_by_role_with_options_async(role_id, request, headers, runtime)

    def list_product_env_infos_with_options(
        self,
        request: main_models.ListProductEnvInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductEnvInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductEnvInfos',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/list-product-env',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductEnvInfosResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_env_infos_with_options_async(
        self,
        request: main_models.ListProductEnvInfosRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductEnvInfosResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductEnvInfos',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/list-product-env',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductEnvInfosResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_env_infos(
        self,
        request: main_models.ListProductEnvInfosRequest,
    ) -> main_models.ListProductEnvInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_product_env_infos_with_options(request, headers, runtime)

    async def list_product_env_infos_async(
        self,
        request: main_models.ListProductEnvInfosRequest,
    ) -> main_models.ListProductEnvInfosResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_product_env_infos_with_options_async(request, headers, runtime)

    def list_product_envs_with_options(
        self,
        request: main_models.ListProductEnvsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductEnvsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductEnvs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources/commands/list-product-env',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductEnvsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_product_envs_with_options_async(
        self,
        request: main_models.ListProductEnvsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductEnvsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProductEnvs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources/commands/list-product-env',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductEnvsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_product_envs(
        self,
        request: main_models.ListProductEnvsRequest,
    ) -> main_models.ListProductEnvsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_product_envs_with_options(request, headers, runtime)

    async def list_product_envs_async(
        self,
        request: main_models.ListProductEnvsRequest,
    ) -> main_models.ListProductEnvsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_product_envs_with_options_async(request, headers, runtime)

    def list_products_with_options(
        self,
        request: main_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_products_with_options_async(
        self,
        request: main_models.ListProductsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProductsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProducts',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProductsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_products(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_products_with_options(request, headers, runtime)

    async def list_products_async(
        self,
        request: main_models.ListProductsRequest,
    ) -> main_models.ListProductsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_products_with_options_async(request, headers, runtime)

    def list_resources_with_options(
        self,
        request: main_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resources_with_options_async(
        self,
        request: main_models.ListResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.product_id):
            query['productId'] = request.product_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResources',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resources(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_resources_with_options(request, headers, runtime)

    async def list_resources_async(
        self,
        request: main_models.ListResourcesRequest,
    ) -> main_models.ListResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_resources_with_options_async(request, headers, runtime)

    def list_reviewers_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReviewersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListReviewers',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews/commands/listReviewers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReviewersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_reviewers_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReviewersResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListReviewers',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews/commands/listReviewers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReviewersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_reviewers(self) -> main_models.ListReviewersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_reviewers_with_options(headers, runtime)

    async def list_reviewers_async(self) -> main_models.ListReviewersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_reviewers_with_options_async(headers, runtime)

    def list_roles_with_options(
        self,
        tmp_req: main_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        tmp_req.validate()
        request = main_models.ListRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_ids):
            request.role_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_ids, 'roleIds', 'json')
        query = {}
        if not DaraCore.is_null(request.authorizer_id):
            query['authorizerId'] = request.authorizer_id
        if not DaraCore.is_null(request.authorizer_type):
            query['authorizerType'] = request.authorizer_type
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.platform):
            query['platform'] = request.platform
        if not DaraCore.is_null(request.role_ids_shrink):
            query['roleIds'] = request.role_ids_shrink
        if not DaraCore.is_null(request.role_type):
            query['roleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_roles_with_options_async(
        self,
        tmp_req: main_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        tmp_req.validate()
        request = main_models.ListRolesShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.role_ids):
            request.role_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.role_ids, 'roleIds', 'json')
        query = {}
        if not DaraCore.is_null(request.authorizer_id):
            query['authorizerId'] = request.authorizer_id
        if not DaraCore.is_null(request.authorizer_type):
            query['authorizerType'] = request.authorizer_type
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.name):
            query['name'] = request.name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.platform):
            query['platform'] = request.platform
        if not DaraCore.is_null(request.role_ids_shrink):
            query['roleIds'] = request.role_ids_shrink
        if not DaraCore.is_null(request.role_type):
            query['roleType'] = request.role_type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_roles(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_roles_with_options(request, headers, runtime)

    async def list_roles_async(
        self,
        request: main_models.ListRolesRequest,
    ) -> main_models.ListRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_roles_with_options_async(request, headers, runtime)

    def list_runtime_tokens_with_options(
        self,
        request: main_models.ListRuntimeTokensRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRuntimeTokensResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRuntimeTokens',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/env/tokens',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRuntimeTokensResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_runtime_tokens_with_options_async(
        self,
        request: main_models.ListRuntimeTokensRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRuntimeTokensResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.enterprise_id):
            query['enterpriseId'] = request.enterprise_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.pbc_id):
            query['pbcId'] = request.pbc_id
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRuntimeTokens',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services/env/tokens',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRuntimeTokensResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_runtime_tokens(
        self,
        request: main_models.ListRuntimeTokensRequest,
    ) -> main_models.ListRuntimeTokensResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_runtime_tokens_with_options(request, headers, runtime)

    async def list_runtime_tokens_async(
        self,
        request: main_models.ListRuntimeTokensRequest,
    ) -> main_models.ListRuntimeTokensResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_runtime_tokens_with_options_async(request, headers, runtime)

    def list_server_instances_with_options(
        self,
        env: str,
        service_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServerInstancesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListServerInstances',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/services/{DaraURL.percent_encode(service_group_id)}/env/{DaraURL.percent_encode(env)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_server_instances_with_options_async(
        self,
        env: str,
        service_group_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServerInstancesResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListServerInstances',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/services/{DaraURL.percent_encode(service_group_id)}/env/{DaraURL.percent_encode(env)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServerInstancesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_server_instances(
        self,
        env: str,
        service_group_id: str,
    ) -> main_models.ListServerInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_server_instances_with_options(env, service_group_id, headers, runtime)

    async def list_server_instances_async(
        self,
        env: str,
        service_group_id: str,
    ) -> main_models.ListServerInstancesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_server_instances_with_options_async(env, service_group_id, headers, runtime)

    def list_service_metrics_with_options(
        self,
        request: main_models.ListServiceMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.interval_in_sec):
            query['intervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.measures):
            query['measures'] = request.measures
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.topic_id):
            query['topicId'] = request.topic_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_service_metrics_with_options_async(
        self,
        request: main_models.ListServiceMetricsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListServiceMetricsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.group_id):
            query['groupId'] = request.group_id
        if not DaraCore.is_null(request.interval_in_sec):
            query['intervalInSec'] = request.interval_in_sec
        if not DaraCore.is_null(request.ip):
            query['ip'] = request.ip
        if not DaraCore.is_null(request.measures):
            query['measures'] = request.measures
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        if not DaraCore.is_null(request.topic_id):
            query['topicId'] = request.topic_id
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListServiceMetrics',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/services',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListServiceMetricsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_service_metrics(
        self,
        request: main_models.ListServiceMetricsRequest,
    ) -> main_models.ListServiceMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_service_metrics_with_options(request, headers, runtime)

    async def list_service_metrics_async(
        self,
        request: main_models.ListServiceMetricsRequest,
    ) -> main_models.ListServiceMetricsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_service_metrics_with_options_async(request, headers, runtime)

    def list_settleds_with_options(
        self,
        request: main_models.ListSettledsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSettledsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['accountId'] = request.account_id
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.enterprise_name):
            query['enterpriseName'] = request.enterprise_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSettleds',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/settleds',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSettledsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_settleds_with_options_async(
        self,
        request: main_models.ListSettledsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSettledsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['accountId'] = request.account_id
        if not DaraCore.is_null(request.applicant):
            query['applicant'] = request.applicant
        if not DaraCore.is_null(request.enterprise_name):
            query['enterpriseName'] = request.enterprise_name
        if not DaraCore.is_null(request.status):
            query['status'] = request.status
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSettleds',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/settleds',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSettledsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_settleds(
        self,
        request: main_models.ListSettledsRequest,
    ) -> main_models.ListSettledsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_settleds_with_options(request, headers, runtime)

    async def list_settleds_async(
        self,
        request: main_models.ListSettledsRequest,
    ) -> main_models.ListSettledsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_settleds_with_options_async(request, headers, runtime)

    def list_subscribe_pbcs_with_options(
        self,
        pbc_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscribePbcsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSubscribePbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(pbc_name)}/commands/subscribe-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscribePbcsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_subscribe_pbcs_with_options_async(
        self,
        pbc_name: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSubscribePbcsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListSubscribePbcs',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(pbc_name)}/commands/subscribe-list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSubscribePbcsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_subscribe_pbcs(
        self,
        pbc_name: str,
    ) -> main_models.ListSubscribePbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_subscribe_pbcs_with_options(pbc_name, headers, runtime)

    async def list_subscribe_pbcs_async(
        self,
        pbc_name: str,
    ) -> main_models.ListSubscribePbcsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_subscribe_pbcs_with_options_async(pbc_name, headers, runtime)

    def list_upstream_pbc_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUpstreamPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListUpstreamPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-/versions/{DaraURL.percent_encode(id)}/commands/list-upstream',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUpstreamPbcResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_upstream_pbc_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUpstreamPbcResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'ListUpstreamPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-/versions/{DaraURL.percent_encode(id)}/commands/list-upstream',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUpstreamPbcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_upstream_pbc(
        self,
        id: str,
    ) -> main_models.ListUpstreamPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_upstream_pbc_with_options(id, headers, runtime)

    async def list_upstream_pbc_async(
        self,
        id: str,
    ) -> main_models.ListUpstreamPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_upstream_pbc_with_options_async(id, headers, runtime)

    def list_watch_assets_with_options(
        self,
        request: main_models.ListWatchAssetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWatchAssetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['accountId'] = request.account_id
        if not DaraCore.is_null(request.asset_type):
            query['assetType'] = request.asset_type
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.upshelf_asset_id):
            query['upshelfAssetId'] = request.upshelf_asset_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWatchAssets',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/asset-watchs/commands/list-watch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWatchAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_watch_assets_with_options_async(
        self,
        request: main_models.ListWatchAssetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListWatchAssetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['accountId'] = request.account_id
        if not DaraCore.is_null(request.asset_type):
            query['assetType'] = request.asset_type
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.upshelf_asset_id):
            query['upshelfAssetId'] = request.upshelf_asset_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListWatchAssets',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/asset-watchs/commands/list-watch',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListWatchAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_watch_assets(
        self,
        request: main_models.ListWatchAssetsRequest,
    ) -> main_models.ListWatchAssetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_watch_assets_with_options(request, headers, runtime)

    async def list_watch_assets_async(
        self,
        request: main_models.ListWatchAssetsRequest,
    ) -> main_models.ListWatchAssetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_watch_assets_with_options_async(request, headers, runtime)

    def obtain_mq_console_link_with_options(
        self,
        request: main_models.ObtainMqConsoleLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ObtainMqConsoleLinkResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ObtainMqConsoleLink',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/commonds/obtainMqConsoleLink',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainMqConsoleLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def obtain_mq_console_link_with_options_async(
        self,
        request: main_models.ObtainMqConsoleLinkRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ObtainMqConsoleLinkResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'ObtainMqConsoleLink',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/mq/topic/commonds/obtainMqConsoleLink',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ObtainMqConsoleLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def obtain_mq_console_link(
        self,
        request: main_models.ObtainMqConsoleLinkRequest,
    ) -> main_models.ObtainMqConsoleLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.obtain_mq_console_link_with_options(request, headers, runtime)

    async def obtain_mq_console_link_async(
        self,
        request: main_models.ObtainMqConsoleLinkRequest,
    ) -> main_models.ObtainMqConsoleLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.obtain_mq_console_link_with_options_async(request, headers, runtime)

    def open_service_group_for_service_with_options(
        self,
        request: main_models.OpenServiceGroupForServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenServiceGroupForServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'OpenServiceGroupForService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/open-group',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenServiceGroupForServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def open_service_group_for_service_with_options_async(
        self,
        request: main_models.OpenServiceGroupForServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.OpenServiceGroupForServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'OpenServiceGroupForService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/commands/open-group',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.OpenServiceGroupForServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def open_service_group_for_service(
        self,
        request: main_models.OpenServiceGroupForServiceRequest,
    ) -> main_models.OpenServiceGroupForServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.open_service_group_for_service_with_options(request, headers, runtime)

    async def open_service_group_for_service_async(
        self,
        request: main_models.OpenServiceGroupForServiceRequest,
    ) -> main_models.OpenServiceGroupForServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.open_service_group_for_service_with_options_async(request, headers, runtime)

    def preview_component_crd_schema_with_options(
        self,
        request: main_models.PreviewComponentCrdSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PreviewComponentCrdSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewComponentCrdSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/commonds/preview-component-schema',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewComponentCrdSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def preview_component_crd_schema_with_options_async(
        self,
        request: main_models.PreviewComponentCrdSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.PreviewComponentCrdSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'PreviewComponentCrdSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/commonds/preview-component-schema',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.PreviewComponentCrdSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def preview_component_crd_schema(
        self,
        request: main_models.PreviewComponentCrdSchemaRequest,
    ) -> main_models.PreviewComponentCrdSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.preview_component_crd_schema_with_options(request, headers, runtime)

    async def preview_component_crd_schema_async(
        self,
        request: main_models.PreviewComponentCrdSchemaRequest,
    ) -> main_models.PreviewComponentCrdSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.preview_component_crd_schema_with_options_async(request, headers, runtime)

    def register_buc_user_with_options(
        self,
        request: main_models.RegisterBucUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RegisterBucUserResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RegisterBucUser',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/bucs/logins/register',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterBucUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def register_buc_user_with_options_async(
        self,
        request: main_models.RegisterBucUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RegisterBucUserResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RegisterBucUser',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/bucs/logins/register',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RegisterBucUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def register_buc_user(
        self,
        request: main_models.RegisterBucUserRequest,
    ) -> main_models.RegisterBucUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.register_buc_user_with_options(request, headers, runtime)

    async def register_buc_user_async(
        self,
        request: main_models.RegisterBucUserRequest,
    ) -> main_models.RegisterBucUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.register_buc_user_with_options_async(request, headers, runtime)

    def remove_asset_watch_with_options(
        self,
        asset_id: str,
        request: main_models.RemoveAssetWatchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAssetWatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_type):
            query['assetType'] = request.asset_type
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAssetWatch',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/asset-watchs/{DaraURL.percent_encode(asset_id)}/commands/remove-watch',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAssetWatchResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_asset_watch_with_options_async(
        self,
        asset_id: str,
        request: main_models.RemoveAssetWatchRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveAssetWatchResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.asset_type):
            query['assetType'] = request.asset_type
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveAssetWatch',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/asset-watchs/{DaraURL.percent_encode(asset_id)}/commands/remove-watch',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveAssetWatchResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_asset_watch(
        self,
        asset_id: str,
        request: main_models.RemoveAssetWatchRequest,
    ) -> main_models.RemoveAssetWatchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_asset_watch_with_options(asset_id, request, headers, runtime)

    async def remove_asset_watch_async(
        self,
        asset_id: str,
        request: main_models.RemoveAssetWatchRequest,
    ) -> main_models.RemoveAssetWatchResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_asset_watch_with_options_async(asset_id, request, headers, runtime)

    def remove_depend_library_with_options(
        self,
        id: str,
        request: main_models.RemoveDependLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDependLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDependLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}/commands/remove-dependency',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDependLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def remove_depend_library_with_options_async(
        self,
        id: str,
        request: main_models.RemoveDependLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RemoveDependLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RemoveDependLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}/commands/remove-dependency',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RemoveDependLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def remove_depend_library(
        self,
        id: str,
        request: main_models.RemoveDependLibraryRequest,
    ) -> main_models.RemoveDependLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.remove_depend_library_with_options(id, request, headers, runtime)

    async def remove_depend_library_async(
        self,
        id: str,
        request: main_models.RemoveDependLibraryRequest,
    ) -> main_models.RemoveDependLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.remove_depend_library_with_options_async(id, request, headers, runtime)

    def revert_pdp_service_with_options(
        self,
        request: main_models.RevertPdpServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevertPdpServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RevertPdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/commands/revert',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertPdpServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def revert_pdp_service_with_options_async(
        self,
        request: main_models.RevertPdpServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevertPdpServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RevertPdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/commands/revert',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevertPdpServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revert_pdp_service(
        self,
        request: main_models.RevertPdpServiceRequest,
    ) -> main_models.RevertPdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revert_pdp_service_with_options(request, headers, runtime)

    async def revert_pdp_service_async(
        self,
        request: main_models.RevertPdpServiceRequest,
    ) -> main_models.RevertPdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revert_pdp_service_with_options_async(request, headers, runtime)

    def revoke_library_review_with_options(
        self,
        request: main_models.RevokeLibraryReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeLibraryReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeLibraryReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews/commands/revoke-review',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeLibraryReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_library_review_with_options_async(
        self,
        request: main_models.RevokeLibraryReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeLibraryReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeLibraryReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/library-reviews/commands/revoke-review',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokeLibraryReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_library_review(
        self,
        request: main_models.RevokeLibraryReviewRequest,
    ) -> main_models.RevokeLibraryReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_library_review_with_options(request, headers, runtime)

    async def revoke_library_review_async(
        self,
        request: main_models.RevokeLibraryReviewRequest,
    ) -> main_models.RevokeLibraryReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_library_review_with_options_async(request, headers, runtime)

    def revoke_pbc_review_with_options(
        self,
        request: main_models.RevokePbcReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokePbcReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RevokePbcReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews/commands/revoke-review',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokePbcReviewResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_pbc_review_with_options_async(
        self,
        request: main_models.RevokePbcReviewRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokePbcReviewResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RevokePbcReview',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-reviews/commands/revoke-review',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RevokePbcReviewResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_pbc_review(
        self,
        request: main_models.RevokePbcReviewRequest,
    ) -> main_models.RevokePbcReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_pbc_review_with_options(request, headers, runtime)

    async def revoke_pbc_review_async(
        self,
        request: main_models.RevokePbcReviewRequest,
    ) -> main_models.RevokePbcReviewResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_pbc_review_with_options_async(request, headers, runtime)

    def revoke_role_with_options(
        self,
        role_id: str,
        request: main_models.RevokeRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/commands/revoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RevokeRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_role_with_options_async(
        self,
        role_id: str,
        request: main_models.RevokeRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/{DaraURL.percent_encode(role_id)}/commands/revoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RevokeRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_role(
        self,
        role_id: str,
        request: main_models.RevokeRoleRequest,
    ) -> main_models.RevokeRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_role_with_options(role_id, request, headers, runtime)

    async def revoke_role_async(
        self,
        role_id: str,
        request: main_models.RevokeRoleRequest,
    ) -> main_models.RevokeRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_role_with_options_async(role_id, request, headers, runtime)

    def rollback_pdp_service_with_options(
        self,
        request: main_models.RollbackPdpServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackPdpServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RollbackPdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/commands/rollback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackPdpServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_pdp_service_with_options_async(
        self,
        request: main_models.RollbackPdpServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackPdpServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'RollbackPdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments/commands/rollback',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RollbackPdpServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_pdp_service(
        self,
        request: main_models.RollbackPdpServiceRequest,
    ) -> main_models.RollbackPdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rollback_pdp_service_with_options(request, headers, runtime)

    async def rollback_pdp_service_async(
        self,
        request: main_models.RollbackPdpServiceRequest,
    ) -> main_models.RollbackPdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rollback_pdp_service_with_options_async(request, headers, runtime)

    def search_assets_with_options(
        self,
        tmp_req: main_models.SearchAssetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchAssetsResponse:
        tmp_req.validate()
        request = main_models.SearchAssetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_industrys):
            request.asset_industrys_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_industrys, 'assetIndustrys', 'json')
        if not DaraCore.is_null(tmp_req.asset_types):
            request.asset_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_types, 'assetTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.asset_industrys_shrink):
            query['assetIndustrys'] = request.asset_industrys_shrink
        if not DaraCore.is_null(request.asset_name):
            query['assetName'] = request.asset_name
        if not DaraCore.is_null(request.asset_types_shrink):
            query['assetTypes'] = request.asset_types_shrink
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAssets',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/markets/commands/search-asset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_assets_with_options_async(
        self,
        tmp_req: main_models.SearchAssetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchAssetsResponse:
        tmp_req.validate()
        request = main_models.SearchAssetsShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.asset_industrys):
            request.asset_industrys_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_industrys, 'assetIndustrys', 'json')
        if not DaraCore.is_null(tmp_req.asset_types):
            request.asset_types_shrink = Utils.array_to_string_with_specified_style(tmp_req.asset_types, 'assetTypes', 'json')
        query = {}
        if not DaraCore.is_null(request.asset_industrys_shrink):
            query['assetIndustrys'] = request.asset_industrys_shrink
        if not DaraCore.is_null(request.asset_name):
            query['assetName'] = request.asset_name
        if not DaraCore.is_null(request.asset_types_shrink):
            query['assetTypes'] = request.asset_types_shrink
        if not DaraCore.is_null(request.company_id):
            query['companyId'] = request.company_id
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchAssets',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/markets/commands/search-asset',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_assets(
        self,
        request: main_models.SearchAssetsRequest,
    ) -> main_models.SearchAssetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_assets_with_options(request, headers, runtime)

    async def search_assets_async(
        self,
        request: main_models.SearchAssetsRequest,
    ) -> main_models.SearchAssetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_assets_with_options_async(request, headers, runtime)

    def search_pbc_assets_with_options(
        self,
        request: main_models.SearchPbcAssetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchPbcAssetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.order_by):
            query['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchPbcAssets',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/markets/commands/search',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchPbcAssetsResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_pbc_assets_with_options_async(
        self,
        request: main_models.SearchPbcAssetsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchPbcAssetsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.industry):
            query['industry'] = request.industry
        if not DaraCore.is_null(request.keyword):
            query['keyword'] = request.keyword
        if not DaraCore.is_null(request.order_by):
            query['order_by'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['order_direction'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['page_number'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['page_size'] = request.page_size
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchPbcAssets',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/markets/commands/search',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchPbcAssetsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_pbc_assets(
        self,
        request: main_models.SearchPbcAssetsRequest,
    ) -> main_models.SearchPbcAssetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_pbc_assets_with_options(request, headers, runtime)

    async def search_pbc_assets_async(
        self,
        request: main_models.SearchPbcAssetsRequest,
    ) -> main_models.SearchPbcAssetsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_pbc_assets_with_options_async(request, headers, runtime)

    def search_traces_by_page_with_options(
        self,
        request: main_models.SearchTracesByPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchTracesByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.min_duration):
            query['minDuration'] = request.min_duration
        if not DaraCore.is_null(request.operation_name):
            query['operationName'] = request.operation_name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTracesByPage',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/traces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTracesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_traces_by_page_with_options_async(
        self,
        request: main_models.SearchTracesByPageRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SearchTracesByPageResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_time):
            query['endTime'] = request.end_time
        if not DaraCore.is_null(request.env):
            query['env'] = request.env
        if not DaraCore.is_null(request.min_duration):
            query['minDuration'] = request.min_duration
        if not DaraCore.is_null(request.operation_name):
            query['operationName'] = request.operation_name
        if not DaraCore.is_null(request.order_by):
            query['orderBy'] = request.order_by
        if not DaraCore.is_null(request.order_direction):
            query['orderDirection'] = request.order_direction
        if not DaraCore.is_null(request.page_number):
            query['pageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['pageSize'] = request.page_size
        if not DaraCore.is_null(request.service_group_id):
            query['serviceGroupId'] = request.service_group_id
        if not DaraCore.is_null(request.service_name):
            query['serviceName'] = request.service_name
        if not DaraCore.is_null(request.start_time):
            query['startTime'] = request.start_time
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchTracesByPage',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/traces',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchTracesByPageResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_traces_by_page(
        self,
        request: main_models.SearchTracesByPageRequest,
    ) -> main_models.SearchTracesByPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.search_traces_by_page_with_options(request, headers, runtime)

    async def search_traces_by_page_async(
        self,
        request: main_models.SearchTracesByPageRequest,
    ) -> main_models.SearchTracesByPageResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.search_traces_by_page_with_options_async(request, headers, runtime)

    def send_ttsverify_link_with_options(
        self,
        contact_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendTTSVerifyLinkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'SendTTSVerifyLink',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact/commands/phoneVerify/{DaraURL.percent_encode(contact_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTTSVerifyLinkResponse(),
            self.call_api(params, req, runtime)
        )

    async def send_ttsverify_link_with_options_async(
        self,
        contact_id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SendTTSVerifyLinkResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'SendTTSVerifyLink',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact/commands/phoneVerify/{DaraURL.percent_encode(contact_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SendTTSVerifyLinkResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def send_ttsverify_link(
        self,
        contact_id: str,
    ) -> main_models.SendTTSVerifyLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.send_ttsverify_link_with_options(contact_id, headers, runtime)

    async def send_ttsverify_link_async(
        self,
        contact_id: str,
    ) -> main_models.SendTTSVerifyLinkResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.send_ttsverify_link_with_options_async(contact_id, headers, runtime)

    def subscribe_pbc_with_options(
        self,
        pbc_name: str,
        request: main_models.SubscribePbcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubscribePbcResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'SubscribePbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(pbc_name)}/commands/subscribe',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubscribePbcResponse(),
            self.call_api(params, req, runtime)
        )

    async def subscribe_pbc_with_options_async(
        self,
        pbc_name: str,
        request: main_models.SubscribePbcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubscribePbcResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'SubscribePbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbcs/{DaraURL.percent_encode(pbc_name)}/commands/subscribe',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SubscribePbcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def subscribe_pbc(
        self,
        pbc_name: str,
        request: main_models.SubscribePbcRequest,
    ) -> main_models.SubscribePbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.subscribe_pbc_with_options(pbc_name, request, headers, runtime)

    async def subscribe_pbc_async(
        self,
        pbc_name: str,
        request: main_models.SubscribePbcRequest,
    ) -> main_models.SubscribePbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.subscribe_pbc_with_options_async(pbc_name, request, headers, runtime)

    def sync_component_template_config_with_options(
        self,
        request: main_models.SyncComponentTemplateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncComponentTemplateConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncComponentTemplateConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/commonds/sync-template-config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncComponentTemplateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def sync_component_template_config_with_options_async(
        self,
        request: main_models.SyncComponentTemplateConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SyncComponentTemplateConfigResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.id):
            body['id'] = request.id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'SyncComponentTemplateConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/commonds/sync-template-config',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SyncComponentTemplateConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def sync_component_template_config(
        self,
        request: main_models.SyncComponentTemplateConfigRequest,
    ) -> main_models.SyncComponentTemplateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.sync_component_template_config_with_options(request, headers, runtime)

    async def sync_component_template_config_async(
        self,
        request: main_models.SyncComponentTemplateConfigRequest,
    ) -> main_models.SyncComponentTemplateConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.sync_component_template_config_with_options_async(request, headers, runtime)

    def transfer_enterprise_with_options(
        self,
        enterprise_id: str,
        request: main_models.TransferEnterpriseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TransferEnterpriseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'TransferEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/{DaraURL.percent_encode(enterprise_id)}/commands/transfer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def transfer_enterprise_with_options_async(
        self,
        enterprise_id: str,
        request: main_models.TransferEnterpriseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TransferEnterpriseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'TransferEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/{DaraURL.percent_encode(enterprise_id)}/commands/transfer',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TransferEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def transfer_enterprise(
        self,
        enterprise_id: str,
        request: main_models.TransferEnterpriseRequest,
    ) -> main_models.TransferEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.transfer_enterprise_with_options(enterprise_id, request, headers, runtime)

    async def transfer_enterprise_async(
        self,
        enterprise_id: str,
        request: main_models.TransferEnterpriseRequest,
    ) -> main_models.TransferEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.transfer_enterprise_with_options_async(enterprise_id, request, headers, runtime)

    def trigger_deployment_with_options(
        self,
        request: main_models.TriggerDeploymentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TriggerDeploymentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerDeployment',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    async def trigger_deployment_with_options_async(
        self,
        request: main_models.TriggerDeploymentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.TriggerDeploymentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'TriggerDeployment',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/deployments',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.TriggerDeploymentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def trigger_deployment(
        self,
        request: main_models.TriggerDeploymentRequest,
    ) -> main_models.TriggerDeploymentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.trigger_deployment_with_options(request, headers, runtime)

    async def trigger_deployment_async(
        self,
        request: main_models.TriggerDeploymentRequest,
    ) -> main_models.TriggerDeploymentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.trigger_deployment_with_options_async(request, headers, runtime)

    def up_shelf_library_with_options(
        self,
        id: str,
        request: main_models.UpShelfLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpShelfLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpShelfLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}/commands/up-shelf-library',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpShelfLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def up_shelf_library_with_options_async(
        self,
        id: str,
        request: main_models.UpShelfLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpShelfLibraryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpShelfLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(id)}/commands/up-shelf-library',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpShelfLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def up_shelf_library(
        self,
        id: str,
        request: main_models.UpShelfLibraryRequest,
    ) -> main_models.UpShelfLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.up_shelf_library_with_options(id, request, headers, runtime)

    async def up_shelf_library_async(
        self,
        id: str,
        request: main_models.UpShelfLibraryRequest,
    ) -> main_models.UpShelfLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.up_shelf_library_with_options_async(id, request, headers, runtime)

    def up_shelf_pbc_version_with_options(
        self,
        id: str,
        request: main_models.UpShelfPbcVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpShelfPbcVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpShelfPbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}/commands/upShelf',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpShelfPbcVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def up_shelf_pbc_version_with_options_async(
        self,
        id: str,
        request: main_models.UpShelfPbcVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpShelfPbcVersionResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.market_id):
            query['marketId'] = request.market_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpShelfPbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}/commands/upShelf',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpShelfPbcVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def up_shelf_pbc_version(
        self,
        id: str,
        request: main_models.UpShelfPbcVersionRequest,
    ) -> main_models.UpShelfPbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.up_shelf_pbc_version_with_options(id, request, headers, runtime)

    async def up_shelf_pbc_version_async(
        self,
        id: str,
        request: main_models.UpShelfPbcVersionRequest,
    ) -> main_models.UpShelfPbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.up_shelf_pbc_version_with_options_async(id, request, headers, runtime)

    def update_component_with_options(
        self,
        id: str,
        request: main_models.UpdateComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponent',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_component_with_options_async(
        self,
        id: str,
        request: main_models.UpdateComponentRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponent',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/components/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_component(
        self,
        id: str,
        request: main_models.UpdateComponentRequest,
    ) -> main_models.UpdateComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_component_with_options(id, request, headers, runtime)

    async def update_component_async(
        self,
        id: str,
        request: main_models.UpdateComponentRequest,
    ) -> main_models.UpdateComponentResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_component_with_options_async(id, request, headers, runtime)

    def update_component_template_with_options(
        self,
        id: str,
        request: main_models.UpdateComponentTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponentTemplate',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_component_template_with_options_async(
        self,
        id: str,
        request: main_models.UpdateComponentTemplateRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateComponentTemplateResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateComponentTemplate',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/component-templates/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateComponentTemplateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_component_template(
        self,
        id: str,
        request: main_models.UpdateComponentTemplateRequest,
    ) -> main_models.UpdateComponentTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_component_template_with_options(id, request, headers, runtime)

    async def update_component_template_async(
        self,
        id: str,
        request: main_models.UpdateComponentTemplateRequest,
    ) -> main_models.UpdateComponentTemplateResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_component_template_with_options_async(id, request, headers, runtime)

    def update_developer_with_options(
        self,
        account_id: str,
        request: main_models.UpdateDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeveloperResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeveloperResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_developer_with_options_async(
        self,
        account_id: str,
        request: main_models.UpdateDeveloperRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeveloperResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeveloper',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/developers/{DaraURL.percent_encode(account_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeveloperResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_developer(
        self,
        account_id: str,
        request: main_models.UpdateDeveloperRequest,
    ) -> main_models.UpdateDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_developer_with_options(account_id, request, headers, runtime)

    async def update_developer_async(
        self,
        account_id: str,
        request: main_models.UpdateDeveloperRequest,
    ) -> main_models.UpdateDeveloperResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_developer_with_options_async(account_id, request, headers, runtime)

    def update_enterprise_with_options(
        self,
        enterprise_id: str,
        request: main_models.UpdateEnterpriseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnterpriseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnterpriseResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_enterprise_with_options_async(
        self,
        enterprise_id: str,
        request: main_models.UpdateEnterpriseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateEnterpriseResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateEnterprise',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/enterprises/{DaraURL.percent_encode(enterprise_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateEnterpriseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_enterprise(
        self,
        enterprise_id: str,
        request: main_models.UpdateEnterpriseRequest,
    ) -> main_models.UpdateEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_enterprise_with_options(enterprise_id, request, headers, runtime)

    async def update_enterprise_async(
        self,
        enterprise_id: str,
        request: main_models.UpdateEnterpriseRequest,
    ) -> main_models.UpdateEnterpriseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_enterprise_with_options_async(enterprise_id, request, headers, runtime)

    def update_library_with_options(
        self,
        request: main_models.UpdateLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLibraryResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLibraryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_library_with_options_async(
        self,
        request: main_models.UpdateLibraryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLibraryResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLibrary',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLibraryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_library(
        self,
        request: main_models.UpdateLibraryRequest,
    ) -> main_models.UpdateLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_library_with_options(request, headers, runtime)

    async def update_library_async(
        self,
        request: main_models.UpdateLibraryRequest,
    ) -> main_models.UpdateLibraryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_library_with_options_async(request, headers, runtime)

    def update_library_instruction_with_options(
        self,
        library_id: str,
        request: main_models.UpdateLibraryInstructionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLibraryInstructionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLibraryInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/instructions',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLibraryInstructionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_library_instruction_with_options_async(
        self,
        library_id: str,
        request: main_models.UpdateLibraryInstructionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLibraryInstructionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLibraryInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/instructions',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLibraryInstructionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_library_instruction(
        self,
        library_id: str,
        request: main_models.UpdateLibraryInstructionRequest,
    ) -> main_models.UpdateLibraryInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_library_instruction_with_options(library_id, request, headers, runtime)

    async def update_library_instruction_async(
        self,
        library_id: str,
        request: main_models.UpdateLibraryInstructionRequest,
    ) -> main_models.UpdateLibraryInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_library_instruction_with_options_async(library_id, request, headers, runtime)

    def update_library_schema_with_options(
        self,
        library_id: str,
        request: main_models.UpdateLibrarySchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLibrarySchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLibrarySchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/schemas',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLibrarySchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_library_schema_with_options_async(
        self,
        library_id: str,
        request: main_models.UpdateLibrarySchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateLibrarySchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateLibrarySchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/librarys/{DaraURL.percent_encode(library_id)}/schemas',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateLibrarySchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_library_schema(
        self,
        library_id: str,
        request: main_models.UpdateLibrarySchemaRequest,
    ) -> main_models.UpdateLibrarySchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_library_schema_with_options(library_id, request, headers, runtime)

    async def update_library_schema_async(
        self,
        library_id: str,
        request: main_models.UpdateLibrarySchemaRequest,
    ) -> main_models.UpdateLibrarySchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_library_schema_with_options_async(library_id, request, headers, runtime)

    def update_monitor_arms_alert_with_options(
        self,
        request: main_models.UpdateMonitorArmsAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorArmsAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorArmsAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/updateMonitorArmsAlert',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorArmsAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_monitor_arms_alert_with_options_async(
        self,
        request: main_models.UpdateMonitorArmsAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorArmsAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorArmsAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/updateMonitorArmsAlert',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorArmsAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_monitor_arms_alert(
        self,
        request: main_models.UpdateMonitorArmsAlertRequest,
    ) -> main_models.UpdateMonitorArmsAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_monitor_arms_alert_with_options(request, headers, runtime)

    async def update_monitor_arms_alert_async(
        self,
        request: main_models.UpdateMonitorArmsAlertRequest,
    ) -> main_models.UpdateMonitorArmsAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_monitor_arms_alert_with_options_async(request, headers, runtime)

    def update_monitor_contact_with_options(
        self,
        request: main_models.UpdateMonitorContactRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorContactResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorContact',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorContactResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_monitor_contact_with_options_async(
        self,
        request: main_models.UpdateMonitorContactRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorContactResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorContact',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/contact',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorContactResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_monitor_contact(
        self,
        request: main_models.UpdateMonitorContactRequest,
    ) -> main_models.UpdateMonitorContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_monitor_contact_with_options(request, headers, runtime)

    async def update_monitor_contact_async(
        self,
        request: main_models.UpdateMonitorContactRequest,
    ) -> main_models.UpdateMonitorContactResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_monitor_contact_with_options_async(request, headers, runtime)

    def update_monitor_contact_group_with_options(
        self,
        request: main_models.UpdateMonitorContactGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorContactGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorContactGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_monitor_contact_group_with_options_async(
        self,
        request: main_models.UpdateMonitorContactGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorContactGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorContactGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/group',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorContactGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_monitor_contact_group(
        self,
        request: main_models.UpdateMonitorContactGroupRequest,
    ) -> main_models.UpdateMonitorContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_monitor_contact_group_with_options(request, headers, runtime)

    async def update_monitor_contact_group_async(
        self,
        request: main_models.UpdateMonitorContactGroupRequest,
    ) -> main_models.UpdateMonitorContactGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_monitor_contact_group_with_options_async(request, headers, runtime)

    def update_monitor_mq_alert_with_options(
        self,
        request: main_models.UpdateMonitorMqAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorMqAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorMqAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/updateMonitorMqAlert',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorMqAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_monitor_mq_alert_with_options_async(
        self,
        request: main_models.UpdateMonitorMqAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorMqAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorMqAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/updateMonitorMqAlert',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorMqAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_monitor_mq_alert(
        self,
        request: main_models.UpdateMonitorMqAlertRequest,
    ) -> main_models.UpdateMonitorMqAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_monitor_mq_alert_with_options(request, headers, runtime)

    async def update_monitor_mq_alert_async(
        self,
        request: main_models.UpdateMonitorMqAlertRequest,
    ) -> main_models.UpdateMonitorMqAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_monitor_mq_alert_with_options_async(request, headers, runtime)

    def update_monitor_sls_alert_with_options(
        self,
        request: main_models.UpdateMonitorSlsAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorSlsAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorSlsAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/updateMonitorSlsAlert',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorSlsAlertResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_monitor_sls_alert_with_options_async(
        self,
        request: main_models.UpdateMonitorSlsAlertRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorSlsAlertResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorSlsAlert',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/alert/commands/updateMonitorSlsAlert',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorSlsAlertResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_monitor_sls_alert(
        self,
        request: main_models.UpdateMonitorSlsAlertRequest,
    ) -> main_models.UpdateMonitorSlsAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_monitor_sls_alert_with_options(request, headers, runtime)

    async def update_monitor_sls_alert_async(
        self,
        request: main_models.UpdateMonitorSlsAlertRequest,
    ) -> main_models.UpdateMonitorSlsAlertResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_monitor_sls_alert_with_options_async(request, headers, runtime)

    def update_monitor_webhook_with_options(
        self,
        request: main_models.UpdateMonitorWebhookRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorWebhookResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorWebhook',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_monitor_webhook_with_options_async(
        self,
        request: main_models.UpdateMonitorWebhookRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMonitorWebhookResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMonitorWebhook',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-monitor/v1/monitor/webhook',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMonitorWebhookResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_monitor_webhook(
        self,
        request: main_models.UpdateMonitorWebhookRequest,
    ) -> main_models.UpdateMonitorWebhookResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_monitor_webhook_with_options(request, headers, runtime)

    async def update_monitor_webhook_async(
        self,
        request: main_models.UpdateMonitorWebhookRequest,
    ) -> main_models.UpdateMonitorWebhookResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_monitor_webhook_with_options_async(request, headers, runtime)

    def update_pbc_api_schema_with_options(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcApiSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePbcApiSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePbcApiSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/api-schemas',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePbcApiSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pbc_api_schema_with_options_async(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcApiSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePbcApiSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePbcApiSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/api-schemas',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePbcApiSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pbc_api_schema(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcApiSchemaRequest,
    ) -> main_models.UpdatePbcApiSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pbc_api_schema_with_options(pbc_version_id, request, headers, runtime)

    async def update_pbc_api_schema_async(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcApiSchemaRequest,
    ) -> main_models.UpdatePbcApiSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pbc_api_schema_with_options_async(pbc_version_id, request, headers, runtime)

    def update_pbc_instruction_with_options(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcInstructionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePbcInstructionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePbcInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/instructions',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePbcInstructionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pbc_instruction_with_options_async(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcInstructionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePbcInstructionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePbcInstruction',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/instructions',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePbcInstructionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pbc_instruction(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcInstructionRequest,
    ) -> main_models.UpdatePbcInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pbc_instruction_with_options(pbc_version_id, request, headers, runtime)

    async def update_pbc_instruction_async(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcInstructionRequest,
    ) -> main_models.UpdatePbcInstructionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pbc_instruction_with_options_async(pbc_version_id, request, headers, runtime)

    def update_pbc_schema_with_options(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePbcSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePbcSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/schemas',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePbcSchemaResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pbc_schema_with_options_async(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcSchemaRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePbcSchemaResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePbcSchema',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(pbc_version_id)}/schemas',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePbcSchemaResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pbc_schema(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcSchemaRequest,
    ) -> main_models.UpdatePbcSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pbc_schema_with_options(pbc_version_id, request, headers, runtime)

    async def update_pbc_schema_async(
        self,
        pbc_version_id: str,
        request: main_models.UpdatePbcSchemaRequest,
    ) -> main_models.UpdatePbcSchemaResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pbc_schema_with_options_async(pbc_version_id, request, headers, runtime)

    def update_pbc_version_with_options(
        self,
        id: str,
        request: main_models.UpdatePbcVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePbcVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePbcVersionResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pbc_version_with_options_async(
        self,
        id: str,
        request: main_models.UpdatePbcVersionRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePbcVersionResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePbcVersion',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/catalog/v1/pbc-versions/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePbcVersionResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pbc_version(
        self,
        id: str,
        request: main_models.UpdatePbcVersionRequest,
    ) -> main_models.UpdatePbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pbc_version_with_options(id, request, headers, runtime)

    async def update_pbc_version_async(
        self,
        id: str,
        request: main_models.UpdatePbcVersionRequest,
    ) -> main_models.UpdatePbcVersionResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pbc_version_with_options_async(id, request, headers, runtime)

    def update_pdp_config_with_options(
        self,
        request: main_models.UpdatePdpConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpConfigResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pdp_config_with_options_async(
        self,
        request: main_models.UpdatePdpConfigRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpConfigResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpConfig',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/configs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpConfigResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pdp_config(
        self,
        request: main_models.UpdatePdpConfigRequest,
    ) -> main_models.UpdatePdpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pdp_config_with_options(request, headers, runtime)

    async def update_pdp_config_async(
        self,
        request: main_models.UpdatePdpConfigRequest,
    ) -> main_models.UpdatePdpConfigResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pdp_config_with_options_async(request, headers, runtime)

    def update_pdp_lane_with_options(
        self,
        id: str,
        request: main_models.UpdatePdpLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpLaneResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpLane',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpLaneResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pdp_lane_with_options_async(
        self,
        id: str,
        request: main_models.UpdatePdpLaneRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpLaneResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpLane',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/lanes/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpLaneResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pdp_lane(
        self,
        id: str,
        request: main_models.UpdatePdpLaneRequest,
    ) -> main_models.UpdatePdpLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pdp_lane_with_options(id, request, headers, runtime)

    async def update_pdp_lane_async(
        self,
        id: str,
        request: main_models.UpdatePdpLaneRequest,
    ) -> main_models.UpdatePdpLaneResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pdp_lane_with_options_async(id, request, headers, runtime)

    def update_pdp_pbc_with_options(
        self,
        request: main_models.UpdatePdpPbcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpPbcResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpPbcResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pdp_pbc_with_options_async(
        self,
        request: main_models.UpdatePdpPbcRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpPbcResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpPbc',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/pbcs',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpPbcResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pdp_pbc(
        self,
        request: main_models.UpdatePdpPbcRequest,
    ) -> main_models.UpdatePdpPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pdp_pbc_with_options(request, headers, runtime)

    async def update_pdp_pbc_async(
        self,
        request: main_models.UpdatePdpPbcRequest,
    ) -> main_models.UpdatePdpPbcResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pdp_pbc_with_options_async(request, headers, runtime)

    def update_pdp_service_with_options(
        self,
        request: main_models.UpdatePdpServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpServiceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pdp_service_with_options_async(
        self,
        request: main_models.UpdatePdpServiceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpServiceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpService',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/services',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpServiceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pdp_service(
        self,
        request: main_models.UpdatePdpServiceRequest,
    ) -> main_models.UpdatePdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pdp_service_with_options(request, headers, runtime)

    async def update_pdp_service_async(
        self,
        request: main_models.UpdatePdpServiceRequest,
    ) -> main_models.UpdatePdpServiceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pdp_service_with_options_async(request, headers, runtime)

    def update_pdp_service_group_with_options(
        self,
        request: main_models.UpdatePdpServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpServiceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpServiceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_pdp_service_group_with_options_async(
        self,
        request: main_models.UpdatePdpServiceGroupRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdatePdpServiceGroupResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdatePdpServiceGroup',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-service/v1/groups',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdatePdpServiceGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_pdp_service_group(
        self,
        request: main_models.UpdatePdpServiceGroupRequest,
    ) -> main_models.UpdatePdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_pdp_service_group_with_options(request, headers, runtime)

    async def update_pdp_service_group_async(
        self,
        request: main_models.UpdatePdpServiceGroupRequest,
    ) -> main_models.UpdatePdpServiceGroupResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_pdp_service_group_with_options_async(request, headers, runtime)

    def update_product_with_options(
        self,
        request: main_models.UpdateProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProduct',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_product_with_options_async(
        self,
        request: main_models.UpdateProductRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateProductResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateProduct',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-pbc/v1/products',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
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
        headers = {}
        return self.update_product_with_options(request, headers, runtime)

    async def update_product_async(
        self,
        request: main_models.UpdateProductRequest,
    ) -> main_models.UpdateProductResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_product_with_options_async(request, headers, runtime)

    def update_resource_with_options(
        self,
        id: str,
        request: main_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_resource_with_options_async(
        self,
        id: str,
        request: main_models.UpdateResourceRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateResourceResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateResource',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/pdp-resource/v1/resources/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateResourceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_resource(
        self,
        id: str,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_resource_with_options(id, request, headers, runtime)

    async def update_resource_async(
        self,
        id: str,
        request: main_models.UpdateResourceRequest,
    ) -> main_models.UpdateResourceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_resource_with_options_async(id, request, headers, runtime)

    def update_role_with_options(
        self,
        role_id: str,
        request: main_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/role-id/{DaraURL.percent_encode(role_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        role_id: str,
        request: main_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/roles/role-id/{DaraURL.percent_encode(role_id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        role_id: str,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_role_with_options(role_id, request, headers, runtime)

    async def update_role_async(
        self,
        role_id: str,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_role_with_options_async(role_id, request, headers, runtime)

    def update_settled_with_options(
        self,
        id: str,
        request: main_models.UpdateSettledRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSettledResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSettled',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/settleds/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSettledResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_settled_with_options_async(
        self,
        id: str,
        request: main_models.UpdateSettledRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSettledResponse:
        request.validate()
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(request.body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSettled',
            version = '2021-11-15',
            protocol = 'HTTPS',
            pathname = f'/manager/v1/settleds/{DaraURL.percent_encode(id)}',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSettledResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_settled(
        self,
        id: str,
        request: main_models.UpdateSettledRequest,
    ) -> main_models.UpdateSettledResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_settled_with_options(id, request, headers, runtime)

    async def update_settled_async(
        self,
        id: str,
        request: main_models.UpdateSettledRequest,
    ) -> main_models.UpdateSettledResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_settled_with_options_async(id, request, headers, runtime)
