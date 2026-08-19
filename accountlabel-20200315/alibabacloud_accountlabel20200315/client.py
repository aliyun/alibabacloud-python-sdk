# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_accountlabel20200315 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('accountlabel', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def add_customer_label_with_options(
        self,
        request: main_models.AddCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endtime):
            query['Endtime'] = request.endtime
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.label_types):
            query['LabelTypes'] = request.label_types
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomerLabel',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomerLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def add_customer_label_with_options_async(
        self,
        request: main_models.AddCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AddCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.endtime):
            query['Endtime'] = request.endtime
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.label_types):
            query['LabelTypes'] = request.label_types
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.start_time):
            query['StartTime'] = request.start_time
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AddCustomerLabel',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AddCustomerLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def add_customer_label(
        self,
        request: main_models.AddCustomerLabelRequest,
    ) -> main_models.AddCustomerLabelResponse:
        runtime = RuntimeOptions()
        return self.add_customer_label_with_options(request, runtime)

    async def add_customer_label_async(
        self,
        request: main_models.AddCustomerLabelRequest,
    ) -> main_models.AddCustomerLabelResponse:
        runtime = RuntimeOptions()
        return await self.add_customer_label_with_options_async(request, runtime)

    def batch_fetch_account_label_with_options(
        self,
        tmp_req: main_models.BatchFetchAccountLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchFetchAccountLabelResponse:
        tmp_req.validate()
        request = main_models.BatchFetchAccountLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label_series_list):
            request.label_series_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_series_list, 'LabelSeriesList', 'simple')
        query = {}
        if not DaraCore.is_null(request.instant):
            query['Instant'] = request.instant
        if not DaraCore.is_null(request.label_series_list_shrink):
            query['LabelSeriesList'] = request.label_series_list_shrink
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchFetchAccountLabel',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchFetchAccountLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_fetch_account_label_with_options_async(
        self,
        tmp_req: main_models.BatchFetchAccountLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchFetchAccountLabelResponse:
        tmp_req.validate()
        request = main_models.BatchFetchAccountLabelShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.label_series_list):
            request.label_series_list_shrink = Utils.array_to_string_with_specified_style(tmp_req.label_series_list, 'LabelSeriesList', 'simple')
        query = {}
        if not DaraCore.is_null(request.instant):
            query['Instant'] = request.instant
        if not DaraCore.is_null(request.label_series_list_shrink):
            query['LabelSeriesList'] = request.label_series_list_shrink
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['Pk'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchFetchAccountLabel',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchFetchAccountLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_fetch_account_label(
        self,
        request: main_models.BatchFetchAccountLabelRequest,
    ) -> main_models.BatchFetchAccountLabelResponse:
        runtime = RuntimeOptions()
        return self.batch_fetch_account_label_with_options(request, runtime)

    async def batch_fetch_account_label_async(
        self,
        request: main_models.BatchFetchAccountLabelRequest,
    ) -> main_models.BatchFetchAccountLabelResponse:
        runtime = RuntimeOptions()
        return await self.batch_fetch_account_label_with_options_async(request, runtime)

    def delete_customer_label_with_options(
        self,
        request: main_models.DeleteCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.label_types):
            query['LabelTypes'] = request.label_types
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomerLabel',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomerLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_customer_label_with_options_async(
        self,
        request: main_models.DeleteCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.label_types):
            query['LabelTypes'] = request.label_types
        if not DaraCore.is_null(request.organization):
            query['Organization'] = request.organization
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        if not DaraCore.is_null(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteCustomerLabel',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteCustomerLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_customer_label(
        self,
        request: main_models.DeleteCustomerLabelRequest,
    ) -> main_models.DeleteCustomerLabelResponse:
        runtime = RuntimeOptions()
        return self.delete_customer_label_with_options(request, runtime)

    async def delete_customer_label_async(
        self,
        request: main_models.DeleteCustomerLabelRequest,
    ) -> main_models.DeleteCustomerLabelResponse:
        runtime = RuntimeOptions()
        return await self.delete_customer_label_with_options_async(request, runtime)

    def query_customer_label_with_options(
        self,
        request: main_models.QueryCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instant):
            query['Instant'] = request.instant
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomerLabel',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomerLabelResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_customer_label_with_options_async(
        self,
        request: main_models.QueryCustomerLabelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomerLabelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.instant):
            query['Instant'] = request.instant
        if not DaraCore.is_null(request.label_series):
            query['LabelSeries'] = request.label_series
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomerLabel',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomerLabelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_customer_label(
        self,
        request: main_models.QueryCustomerLabelRequest,
    ) -> main_models.QueryCustomerLabelResponse:
        runtime = RuntimeOptions()
        return self.query_customer_label_with_options(request, runtime)

    async def query_customer_label_async(
        self,
        request: main_models.QueryCustomerLabelRequest,
    ) -> main_models.QueryCustomerLabelResponse:
        runtime = RuntimeOptions()
        return await self.query_customer_label_with_options_async(request, runtime)

    def query_customer_label_by_config_group_with_options(
        self,
        request: main_models.QueryCustomerLabelByConfigGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomerLabelByConfigGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomerLabelByConfigGroup',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomerLabelByConfigGroupResponse(),
            self.call_api(params, req, runtime)
        )

    async def query_customer_label_by_config_group_with_options_async(
        self,
        request: main_models.QueryCustomerLabelByConfigGroupRequest,
        runtime: RuntimeOptions,
    ) -> main_models.QueryCustomerLabelByConfigGroupResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.group_type):
            query['GroupType'] = request.group_type
        if not DaraCore.is_null(request.pk):
            query['PK'] = request.pk
        if not DaraCore.is_null(request.token):
            query['Token'] = request.token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'QueryCustomerLabelByConfigGroup',
            version = '2020-03-15',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.QueryCustomerLabelByConfigGroupResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def query_customer_label_by_config_group(
        self,
        request: main_models.QueryCustomerLabelByConfigGroupRequest,
    ) -> main_models.QueryCustomerLabelByConfigGroupResponse:
        runtime = RuntimeOptions()
        return self.query_customer_label_by_config_group_with_options(request, runtime)

    async def query_customer_label_by_config_group_async(
        self,
        request: main_models.QueryCustomerLabelByConfigGroupRequest,
    ) -> main_models.QueryCustomerLabelByConfigGroupResponse:
        runtime = RuntimeOptions()
        return await self.query_customer_label_by_config_group_with_options_async(request, runtime)
