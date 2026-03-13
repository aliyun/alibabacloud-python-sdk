# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_governance20210120 import models as main_models
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
        self._endpoint = self.get_endpoint('governance', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def batch_enroll_accounts_with_options(
        self,
        request: main_models.BatchEnrollAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchEnrollAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accounts):
            query['Accounts'] = request.accounts
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchEnrollAccounts',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchEnrollAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_enroll_accounts_with_options_async(
        self,
        request: main_models.BatchEnrollAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchEnrollAccountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accounts):
            query['Accounts'] = request.accounts
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchEnrollAccounts',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchEnrollAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_enroll_accounts(
        self,
        request: main_models.BatchEnrollAccountsRequest,
    ) -> main_models.BatchEnrollAccountsResponse:
        runtime = RuntimeOptions()
        return self.batch_enroll_accounts_with_options(request, runtime)

    async def batch_enroll_accounts_async(
        self,
        request: main_models.BatchEnrollAccountsRequest,
    ) -> main_models.BatchEnrollAccountsResponse:
        runtime = RuntimeOptions()
        return await self.batch_enroll_accounts_with_options_async(request, runtime)

    def create_account_factory_baseline_with_options(
        self,
        request: main_models.CreateAccountFactoryBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountFactoryBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not DaraCore.is_null(request.baseline_name):
            query['BaselineName'] = request.baseline_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccountFactoryBaseline',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountFactoryBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_account_factory_baseline_with_options_async(
        self,
        request: main_models.CreateAccountFactoryBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateAccountFactoryBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not DaraCore.is_null(request.baseline_name):
            query['BaselineName'] = request.baseline_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateAccountFactoryBaseline',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateAccountFactoryBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_account_factory_baseline(
        self,
        request: main_models.CreateAccountFactoryBaselineRequest,
    ) -> main_models.CreateAccountFactoryBaselineResponse:
        runtime = RuntimeOptions()
        return self.create_account_factory_baseline_with_options(request, runtime)

    async def create_account_factory_baseline_async(
        self,
        request: main_models.CreateAccountFactoryBaselineRequest,
    ) -> main_models.CreateAccountFactoryBaselineResponse:
        runtime = RuntimeOptions()
        return await self.create_account_factory_baseline_with_options_async(request, runtime)

    def delete_account_factory_baseline_with_options(
        self,
        request: main_models.DeleteAccountFactoryBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountFactoryBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccountFactoryBaseline',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountFactoryBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_account_factory_baseline_with_options_async(
        self,
        request: main_models.DeleteAccountFactoryBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteAccountFactoryBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteAccountFactoryBaseline',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteAccountFactoryBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_account_factory_baseline(
        self,
        request: main_models.DeleteAccountFactoryBaselineRequest,
    ) -> main_models.DeleteAccountFactoryBaselineResponse:
        runtime = RuntimeOptions()
        return self.delete_account_factory_baseline_with_options(request, runtime)

    async def delete_account_factory_baseline_async(
        self,
        request: main_models.DeleteAccountFactoryBaselineRequest,
    ) -> main_models.DeleteAccountFactoryBaselineResponse:
        runtime = RuntimeOptions()
        return await self.delete_account_factory_baseline_with_options_async(request, runtime)

    def enroll_account_with_options(
        self,
        tmp_req: main_models.EnrollAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnrollAccountResponse:
        tmp_req.validate()
        request = main_models.EnrollAccountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not DaraCore.is_null(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.payer_account_uid):
            query['PayerAccountUid'] = request.payer_account_uid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnrollAccount',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnrollAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def enroll_account_with_options_async(
        self,
        tmp_req: main_models.EnrollAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.EnrollAccountResponse:
        tmp_req.validate()
        request = main_models.EnrollAccountShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.tag):
            request.tag_shrink = Utils.array_to_string_with_specified_style(tmp_req.tag, 'Tag', 'json')
        query = {}
        if not DaraCore.is_null(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not DaraCore.is_null(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not DaraCore.is_null(request.display_name):
            query['DisplayName'] = request.display_name
        if not DaraCore.is_null(request.folder_id):
            query['FolderId'] = request.folder_id
        if not DaraCore.is_null(request.payer_account_uid):
            query['PayerAccountUid'] = request.payer_account_uid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not DaraCore.is_null(request.tag_shrink):
            query['Tag'] = request.tag_shrink
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'EnrollAccount',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnrollAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enroll_account(
        self,
        request: main_models.EnrollAccountRequest,
    ) -> main_models.EnrollAccountResponse:
        runtime = RuntimeOptions()
        return self.enroll_account_with_options(request, runtime)

    async def enroll_account_async(
        self,
        request: main_models.EnrollAccountRequest,
    ) -> main_models.EnrollAccountResponse:
        runtime = RuntimeOptions()
        return await self.enroll_account_with_options_async(request, runtime)

    def generate_evaluation_report_with_options(
        self,
        tmp_req: main_models.GenerateEvaluationReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateEvaluationReportResponse:
        tmp_req.validate()
        request = main_models.GenerateEvaluationReportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateEvaluationReport',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateEvaluationReportResponse(),
            self.call_api(params, req, runtime)
        )

    async def generate_evaluation_report_with_options_async(
        self,
        tmp_req: main_models.GenerateEvaluationReportRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GenerateEvaluationReportResponse:
        tmp_req.validate()
        request = main_models.GenerateEvaluationReportShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.account_ids):
            request.account_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.account_ids, 'AccountIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.account_ids_shrink):
            query['AccountIds'] = request.account_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.report_type):
            query['ReportType'] = request.report_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GenerateEvaluationReport',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GenerateEvaluationReportResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def generate_evaluation_report(
        self,
        request: main_models.GenerateEvaluationReportRequest,
    ) -> main_models.GenerateEvaluationReportResponse:
        runtime = RuntimeOptions()
        return self.generate_evaluation_report_with_options(request, runtime)

    async def generate_evaluation_report_async(
        self,
        request: main_models.GenerateEvaluationReportRequest,
    ) -> main_models.GenerateEvaluationReportResponse:
        runtime = RuntimeOptions()
        return await self.generate_evaluation_report_with_options_async(request, runtime)

    def get_account_factory_baseline_with_options(
        self,
        request: main_models.GetAccountFactoryBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountFactoryBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountFactoryBaseline',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountFactoryBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_account_factory_baseline_with_options_async(
        self,
        request: main_models.GetAccountFactoryBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetAccountFactoryBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetAccountFactoryBaseline',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetAccountFactoryBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_account_factory_baseline(
        self,
        request: main_models.GetAccountFactoryBaselineRequest,
    ) -> main_models.GetAccountFactoryBaselineResponse:
        runtime = RuntimeOptions()
        return self.get_account_factory_baseline_with_options(request, runtime)

    async def get_account_factory_baseline_async(
        self,
        request: main_models.GetAccountFactoryBaselineRequest,
    ) -> main_models.GetAccountFactoryBaselineResponse:
        runtime = RuntimeOptions()
        return await self.get_account_factory_baseline_with_options_async(request, runtime)

    def get_enrolled_account_with_options(
        self,
        request: main_models.GetEnrolledAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEnrolledAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEnrolledAccount',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnrolledAccountResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_enrolled_account_with_options_async(
        self,
        request: main_models.GetEnrolledAccountRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetEnrolledAccountResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_uid):
            query['AccountUid'] = request.account_uid
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetEnrolledAccount',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetEnrolledAccountResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_enrolled_account(
        self,
        request: main_models.GetEnrolledAccountRequest,
    ) -> main_models.GetEnrolledAccountResponse:
        runtime = RuntimeOptions()
        return self.get_enrolled_account_with_options(request, runtime)

    async def get_enrolled_account_async(
        self,
        request: main_models.GetEnrolledAccountRequest,
    ) -> main_models.GetEnrolledAccountResponse:
        runtime = RuntimeOptions()
        return await self.get_enrolled_account_with_options_async(request, runtime)

    def list_account_factory_baseline_items_with_options(
        self,
        request: main_models.ListAccountFactoryBaselineItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountFactoryBaselineItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.versions):
            query['Versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccountFactoryBaselineItems',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountFactoryBaselineItemsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_account_factory_baseline_items_with_options_async(
        self,
        request: main_models.ListAccountFactoryBaselineItemsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountFactoryBaselineItemsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.names):
            query['Names'] = request.names
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.type):
            query['Type'] = request.type
        if not DaraCore.is_null(request.versions):
            query['Versions'] = request.versions
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListAccountFactoryBaselineItems',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountFactoryBaselineItemsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_account_factory_baseline_items(
        self,
        request: main_models.ListAccountFactoryBaselineItemsRequest,
    ) -> main_models.ListAccountFactoryBaselineItemsResponse:
        runtime = RuntimeOptions()
        return self.list_account_factory_baseline_items_with_options(request, runtime)

    async def list_account_factory_baseline_items_async(
        self,
        request: main_models.ListAccountFactoryBaselineItemsRequest,
    ) -> main_models.ListAccountFactoryBaselineItemsResponse:
        runtime = RuntimeOptions()
        return await self.list_account_factory_baseline_items_with_options_async(request, runtime)

    def list_account_factory_baselines_with_options(
        self,
        request: main_models.ListAccountFactoryBaselinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountFactoryBaselinesResponse:
        request.validate()
        query = {}
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
            action = 'ListAccountFactoryBaselines',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountFactoryBaselinesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_account_factory_baselines_with_options_async(
        self,
        request: main_models.ListAccountFactoryBaselinesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListAccountFactoryBaselinesResponse:
        request.validate()
        query = {}
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
            action = 'ListAccountFactoryBaselines',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListAccountFactoryBaselinesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_account_factory_baselines(
        self,
        request: main_models.ListAccountFactoryBaselinesRequest,
    ) -> main_models.ListAccountFactoryBaselinesResponse:
        runtime = RuntimeOptions()
        return self.list_account_factory_baselines_with_options(request, runtime)

    async def list_account_factory_baselines_async(
        self,
        request: main_models.ListAccountFactoryBaselinesRequest,
    ) -> main_models.ListAccountFactoryBaselinesResponse:
        runtime = RuntimeOptions()
        return await self.list_account_factory_baselines_with_options_async(request, runtime)

    def list_enrolled_accounts_with_options(
        self,
        request: main_models.ListEnrolledAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnrolledAccountsResponse:
        request.validate()
        query = {}
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
            action = 'ListEnrolledAccounts',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnrolledAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_enrolled_accounts_with_options_async(
        self,
        request: main_models.ListEnrolledAccountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEnrolledAccountsResponse:
        request.validate()
        query = {}
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
            action = 'ListEnrolledAccounts',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEnrolledAccountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_enrolled_accounts(
        self,
        request: main_models.ListEnrolledAccountsRequest,
    ) -> main_models.ListEnrolledAccountsResponse:
        runtime = RuntimeOptions()
        return self.list_enrolled_accounts_with_options(request, runtime)

    async def list_enrolled_accounts_async(
        self,
        request: main_models.ListEnrolledAccountsRequest,
    ) -> main_models.ListEnrolledAccountsResponse:
        runtime = RuntimeOptions()
        return await self.list_enrolled_accounts_with_options_async(request, runtime)

    def list_evaluation_metadata_with_options(
        self,
        request: main_models.ListEvaluationMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.lens_code):
            query['LensCode'] = request.lens_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic_code):
            query['TopicCode'] = request.topic_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationMetadata',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_metadata_with_options_async(
        self,
        request: main_models.ListEvaluationMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.language):
            query['Language'] = request.language
        if not DaraCore.is_null(request.lens_code):
            query['LensCode'] = request.lens_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.topic_code):
            query['TopicCode'] = request.topic_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationMetadata',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_metadata(
        self,
        request: main_models.ListEvaluationMetadataRequest,
    ) -> main_models.ListEvaluationMetadataResponse:
        runtime = RuntimeOptions()
        return self.list_evaluation_metadata_with_options(request, runtime)

    async def list_evaluation_metadata_async(
        self,
        request: main_models.ListEvaluationMetadataRequest,
    ) -> main_models.ListEvaluationMetadataResponse:
        runtime = RuntimeOptions()
        return await self.list_evaluation_metadata_with_options_async(request, runtime)

    def list_evaluation_metric_details_with_options(
        self,
        request: main_models.ListEvaluationMetricDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationMetricDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationMetricDetails',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationMetricDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_metric_details_with_options_async(
        self,
        request: main_models.ListEvaluationMetricDetailsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationMetricDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.date):
            query['Date'] = request.date
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationMetricDetails',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationMetricDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_metric_details(
        self,
        request: main_models.ListEvaluationMetricDetailsRequest,
    ) -> main_models.ListEvaluationMetricDetailsResponse:
        runtime = RuntimeOptions()
        return self.list_evaluation_metric_details_with_options(request, runtime)

    async def list_evaluation_metric_details_async(
        self,
        request: main_models.ListEvaluationMetricDetailsRequest,
    ) -> main_models.ListEvaluationMetricDetailsResponse:
        runtime = RuntimeOptions()
        return await self.list_evaluation_metric_details_with_options_async(request, runtime)

    def list_evaluation_results_with_options(
        self,
        request: main_models.ListEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.lens_code):
            query['LensCode'] = request.lens_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.topic_code):
            query['TopicCode'] = request.topic_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationResults',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationResultsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_results_with_options_async(
        self,
        request: main_models.ListEvaluationResultsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationResultsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.filters):
            query['Filters'] = request.filters
        if not DaraCore.is_null(request.lens_code):
            query['LensCode'] = request.lens_code
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not DaraCore.is_null(request.topic_code):
            query['TopicCode'] = request.topic_code
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationResults',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationResultsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_results(
        self,
        request: main_models.ListEvaluationResultsRequest,
    ) -> main_models.ListEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return self.list_evaluation_results_with_options(request, runtime)

    async def list_evaluation_results_async(
        self,
        request: main_models.ListEvaluationResultsRequest,
    ) -> main_models.ListEvaluationResultsResponse:
        runtime = RuntimeOptions()
        return await self.list_evaluation_results_with_options_async(request, runtime)

    def list_evaluation_score_history_with_options(
        self,
        request: main_models.ListEvaluationScoreHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationScoreHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationScoreHistory',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationScoreHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_evaluation_score_history_with_options_async(
        self,
        request: main_models.ListEvaluationScoreHistoryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListEvaluationScoreHistoryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.end_date):
            query['EndDate'] = request.end_date
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListEvaluationScoreHistory',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListEvaluationScoreHistoryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_evaluation_score_history(
        self,
        request: main_models.ListEvaluationScoreHistoryRequest,
    ) -> main_models.ListEvaluationScoreHistoryResponse:
        runtime = RuntimeOptions()
        return self.list_evaluation_score_history_with_options(request, runtime)

    async def list_evaluation_score_history_async(
        self,
        request: main_models.ListEvaluationScoreHistoryRequest,
    ) -> main_models.ListEvaluationScoreHistoryResponse:
        runtime = RuntimeOptions()
        return await self.list_evaluation_score_history_with_options_async(request, runtime)

    def run_evaluation_with_options(
        self,
        tmp_req: main_models.RunEvaluationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunEvaluationResponse:
        tmp_req.validate()
        request = main_models.RunEvaluationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metric_ids):
            request.metric_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_ids, 'MetricIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.metric_ids_shrink):
            query['MetricIds'] = request.metric_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunEvaluation',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunEvaluationResponse(),
            self.call_api(params, req, runtime)
        )

    async def run_evaluation_with_options_async(
        self,
        tmp_req: main_models.RunEvaluationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.RunEvaluationResponse:
        tmp_req.validate()
        request = main_models.RunEvaluationShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.metric_ids):
            request.metric_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.metric_ids, 'MetricIds', 'json')
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.metric_ids_shrink):
            query['MetricIds'] = request.metric_ids_shrink
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'RunEvaluation',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.RunEvaluationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def run_evaluation(
        self,
        request: main_models.RunEvaluationRequest,
    ) -> main_models.RunEvaluationResponse:
        runtime = RuntimeOptions()
        return self.run_evaluation_with_options(request, runtime)

    async def run_evaluation_async(
        self,
        request: main_models.RunEvaluationRequest,
    ) -> main_models.RunEvaluationResponse:
        runtime = RuntimeOptions()
        return await self.run_evaluation_with_options_async(request, runtime)

    def update_account_factory_baseline_with_options(
        self,
        request: main_models.UpdateAccountFactoryBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountFactoryBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not DaraCore.is_null(request.baseline_name):
            query['BaselineName'] = request.baseline_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountFactoryBaseline',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountFactoryBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_account_factory_baseline_with_options_async(
        self,
        request: main_models.UpdateAccountFactoryBaselineRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateAccountFactoryBaselineResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.baseline_id):
            query['BaselineId'] = request.baseline_id
        if not DaraCore.is_null(request.baseline_items):
            query['BaselineItems'] = request.baseline_items
        if not DaraCore.is_null(request.baseline_name):
            query['BaselineName'] = request.baseline_name
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateAccountFactoryBaseline',
            version = '2021-01-20',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateAccountFactoryBaselineResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_account_factory_baseline(
        self,
        request: main_models.UpdateAccountFactoryBaselineRequest,
    ) -> main_models.UpdateAccountFactoryBaselineResponse:
        runtime = RuntimeOptions()
        return self.update_account_factory_baseline_with_options(request, runtime)

    async def update_account_factory_baseline_async(
        self,
        request: main_models.UpdateAccountFactoryBaselineRequest,
    ) -> main_models.UpdateAccountFactoryBaselineResponse:
        runtime = RuntimeOptions()
        return await self.update_account_factory_baseline_with_options_async(request, runtime)
