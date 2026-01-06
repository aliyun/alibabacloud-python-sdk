# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

import json

from typing import Dict, Generator, AsyncGenerator

from alibabacloud_polardbai20251013 import models as main_models
from alibabacloud_tea_openapi import utils_models as open_api_util_models
from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi.utils import Utils
from darabonba.core import DaraCore as DaraCore
from darabonba.core import DaraCore
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
        self._endpoint = self.get_endpoint('polardbai', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def chat_biconfig_create_with_options(
        self,
        request: main_models.ChatBIConfigCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigCreate',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_biconfig_create_with_options_async(
        self,
        request: main_models.ChatBIConfigCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigCreate',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_biconfig_create(
        self,
        request: main_models.ChatBIConfigCreateRequest,
    ) -> main_models.ChatBIConfigCreateResponse:
        runtime = RuntimeOptions()
        return self.chat_biconfig_create_with_options(request, runtime)

    async def chat_biconfig_create_async(
        self,
        request: main_models.ChatBIConfigCreateRequest,
    ) -> main_models.ChatBIConfigCreateResponse:
        runtime = RuntimeOptions()
        return await self.chat_biconfig_create_with_options_async(request, runtime)

    def chat_biconfig_delete_with_options(
        self,
        request: main_models.ChatBIConfigDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigDelete',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_biconfig_delete_with_options_async(
        self,
        request: main_models.ChatBIConfigDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigDelete',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_biconfig_delete(
        self,
        request: main_models.ChatBIConfigDeleteRequest,
    ) -> main_models.ChatBIConfigDeleteResponse:
        runtime = RuntimeOptions()
        return self.chat_biconfig_delete_with_options(request, runtime)

    async def chat_biconfig_delete_async(
        self,
        request: main_models.ChatBIConfigDeleteRequest,
    ) -> main_models.ChatBIConfigDeleteResponse:
        runtime = RuntimeOptions()
        return await self.chat_biconfig_delete_with_options_async(request, runtime)

    def chat_biconfig_delete_entry_with_options(
        self,
        request: main_models.ChatBIConfigDeleteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigDeleteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigDeleteEntry',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigDeleteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_biconfig_delete_entry_with_options_async(
        self,
        request: main_models.ChatBIConfigDeleteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigDeleteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigDeleteEntry',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigDeleteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_biconfig_delete_entry(
        self,
        request: main_models.ChatBIConfigDeleteEntryRequest,
    ) -> main_models.ChatBIConfigDeleteEntryResponse:
        runtime = RuntimeOptions()
        return self.chat_biconfig_delete_entry_with_options(request, runtime)

    async def chat_biconfig_delete_entry_async(
        self,
        request: main_models.ChatBIConfigDeleteEntryRequest,
    ) -> main_models.ChatBIConfigDeleteEntryResponse:
        runtime = RuntimeOptions()
        return await self.chat_biconfig_delete_entry_with_options_async(request, runtime)

    def chat_biconfig_query_entries_with_options(
        self,
        request: main_models.ChatBIConfigQueryEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigQueryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigQueryEntries',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigQueryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_biconfig_query_entries_with_options_async(
        self,
        request: main_models.ChatBIConfigQueryEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigQueryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigQueryEntries',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigQueryEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_biconfig_query_entries(
        self,
        request: main_models.ChatBIConfigQueryEntriesRequest,
    ) -> main_models.ChatBIConfigQueryEntriesResponse:
        runtime = RuntimeOptions()
        return self.chat_biconfig_query_entries_with_options(request, runtime)

    async def chat_biconfig_query_entries_async(
        self,
        request: main_models.ChatBIConfigQueryEntriesRequest,
    ) -> main_models.ChatBIConfigQueryEntriesResponse:
        runtime = RuntimeOptions()
        return await self.chat_biconfig_query_entries_with_options_async(request, runtime)

    def chat_biconfig_query_tables_with_options(
        self,
        request: main_models.ChatBIConfigQueryTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigQueryTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigQueryTables',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigQueryTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_biconfig_query_tables_with_options_async(
        self,
        request: main_models.ChatBIConfigQueryTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigQueryTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigQueryTables',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigQueryTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_biconfig_query_tables(
        self,
        request: main_models.ChatBIConfigQueryTablesRequest,
    ) -> main_models.ChatBIConfigQueryTablesResponse:
        runtime = RuntimeOptions()
        return self.chat_biconfig_query_tables_with_options(request, runtime)

    async def chat_biconfig_query_tables_async(
        self,
        request: main_models.ChatBIConfigQueryTablesRequest,
    ) -> main_models.ChatBIConfigQueryTablesResponse:
        runtime = RuntimeOptions()
        return await self.chat_biconfig_query_tables_with_options_async(request, runtime)

    def chat_biconfig_update_entry_with_options(
        self,
        request: main_models.ChatBIConfigUpdateEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigUpdateEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.formula_function):
            query['FormulaFunction'] = request.formula_function
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_functional):
            query['IsFunctional'] = request.is_functional
        if not DaraCore.is_null(request.query_function):
            query['QueryFunction'] = request.query_function
        if not DaraCore.is_null(request.sql_condition):
            query['SqlCondition'] = request.sql_condition
        if not DaraCore.is_null(request.sql_function):
            query['SqlFunction'] = request.sql_function
        if not DaraCore.is_null(request.text_condition):
            query['TextCondition'] = request.text_condition
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigUpdateEntry',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigUpdateEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_biconfig_update_entry_with_options_async(
        self,
        request: main_models.ChatBIConfigUpdateEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIConfigUpdateEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.formula_function):
            query['FormulaFunction'] = request.formula_function
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.is_functional):
            query['IsFunctional'] = request.is_functional
        if not DaraCore.is_null(request.query_function):
            query['QueryFunction'] = request.query_function
        if not DaraCore.is_null(request.sql_condition):
            query['SqlCondition'] = request.sql_condition
        if not DaraCore.is_null(request.sql_function):
            query['SqlFunction'] = request.sql_function
        if not DaraCore.is_null(request.text_condition):
            query['TextCondition'] = request.text_condition
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIConfigUpdateEntry',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIConfigUpdateEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_biconfig_update_entry(
        self,
        request: main_models.ChatBIConfigUpdateEntryRequest,
    ) -> main_models.ChatBIConfigUpdateEntryResponse:
        runtime = RuntimeOptions()
        return self.chat_biconfig_update_entry_with_options(request, runtime)

    async def chat_biconfig_update_entry_async(
        self,
        request: main_models.ChatBIConfigUpdateEntryRequest,
    ) -> main_models.ChatBIConfigUpdateEntryResponse:
        runtime = RuntimeOptions()
        return await self.chat_biconfig_update_entry_with_options_async(request, runtime)

    def chat_bifile_template_download_with_options(
        self,
        request: main_models.ChatBIFileTemplateDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIFileTemplateDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIFileTemplateDownload',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIFileTemplateDownloadResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bifile_template_download_with_options_async(
        self,
        request: main_models.ChatBIFileTemplateDownloadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIFileTemplateDownloadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIFileTemplateDownload',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIFileTemplateDownloadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bifile_template_download(
        self,
        request: main_models.ChatBIFileTemplateDownloadRequest,
    ) -> main_models.ChatBIFileTemplateDownloadResponse:
        runtime = RuntimeOptions()
        return self.chat_bifile_template_download_with_options(request, runtime)

    async def chat_bifile_template_download_async(
        self,
        request: main_models.ChatBIFileTemplateDownloadRequest,
    ) -> main_models.ChatBIFileTemplateDownloadResponse:
        runtime = RuntimeOptions()
        return await self.chat_bifile_template_download_with_options_async(request, runtime)

    def chat_bifile_upload_with_options(
        self,
        request: main_models.ChatBIFileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIFileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIFileUpload',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIFileUploadResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bifile_upload_with_options_async(
        self,
        request: main_models.ChatBIFileUploadRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIFileUploadResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIFileUpload',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIFileUploadResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bifile_upload(
        self,
        request: main_models.ChatBIFileUploadRequest,
    ) -> main_models.ChatBIFileUploadResponse:
        runtime = RuntimeOptions()
        return self.chat_bifile_upload_with_options(request, runtime)

    async def chat_bifile_upload_async(
        self,
        request: main_models.ChatBIFileUploadRequest,
    ) -> main_models.ChatBIFileUploadResponse:
        runtime = RuntimeOptions()
        return await self.chat_bifile_upload_with_options_async(request, runtime)

    def chat_bifile_upload_callback_with_options(
        self,
        request: main_models.ChatBIFileUploadCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIFileUploadCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.character_set_name):
            query['CharacterSetName'] = request.character_set_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIFileUploadCallback',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIFileUploadCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bifile_upload_callback_with_options_async(
        self,
        request: main_models.ChatBIFileUploadCallbackRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIFileUploadCallbackResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.character_set_name):
            query['CharacterSetName'] = request.character_set_name
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.file_name):
            query['FileName'] = request.file_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIFileUploadCallback',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIFileUploadCallbackResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bifile_upload_callback(
        self,
        request: main_models.ChatBIFileUploadCallbackRequest,
    ) -> main_models.ChatBIFileUploadCallbackResponse:
        runtime = RuntimeOptions()
        return self.chat_bifile_upload_callback_with_options(request, runtime)

    async def chat_bifile_upload_callback_async(
        self,
        request: main_models.ChatBIFileUploadCallbackRequest,
    ) -> main_models.ChatBIFileUploadCallbackResponse:
        runtime = RuntimeOptions()
        return await self.chat_bifile_upload_callback_with_options_async(request, runtime)

    def chat_bipattern_create_with_options(
        self,
        request: main_models.ChatBIPatternCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name_suffix):
            query['TableNameSuffix'] = request.table_name_suffix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternCreate',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipattern_create_with_options_async(
        self,
        request: main_models.ChatBIPatternCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name_suffix):
            query['TableNameSuffix'] = request.table_name_suffix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternCreate',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipattern_create(
        self,
        request: main_models.ChatBIPatternCreateRequest,
    ) -> main_models.ChatBIPatternCreateResponse:
        runtime = RuntimeOptions()
        return self.chat_bipattern_create_with_options(request, runtime)

    async def chat_bipattern_create_async(
        self,
        request: main_models.ChatBIPatternCreateRequest,
    ) -> main_models.ChatBIPatternCreateResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipattern_create_with_options_async(request, runtime)

    def chat_bipattern_delete_with_options(
        self,
        request: main_models.ChatBIPatternDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternDelete',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipattern_delete_with_options_async(
        self,
        request: main_models.ChatBIPatternDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternDelete',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipattern_delete(
        self,
        request: main_models.ChatBIPatternDeleteRequest,
    ) -> main_models.ChatBIPatternDeleteResponse:
        runtime = RuntimeOptions()
        return self.chat_bipattern_delete_with_options(request, runtime)

    async def chat_bipattern_delete_async(
        self,
        request: main_models.ChatBIPatternDeleteRequest,
    ) -> main_models.ChatBIPatternDeleteResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipattern_delete_with_options_async(request, runtime)

    def chat_bipattern_delete_entry_with_options(
        self,
        request: main_models.ChatBIPatternDeleteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternDeleteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternDeleteEntry',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternDeleteEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipattern_delete_entry_with_options_async(
        self,
        request: main_models.ChatBIPatternDeleteEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternDeleteEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternDeleteEntry',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternDeleteEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipattern_delete_entry(
        self,
        request: main_models.ChatBIPatternDeleteEntryRequest,
    ) -> main_models.ChatBIPatternDeleteEntryResponse:
        runtime = RuntimeOptions()
        return self.chat_bipattern_delete_entry_with_options(request, runtime)

    async def chat_bipattern_delete_entry_async(
        self,
        request: main_models.ChatBIPatternDeleteEntryRequest,
    ) -> main_models.ChatBIPatternDeleteEntryResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipattern_delete_entry_with_options_async(request, runtime)

    def chat_bipattern_index_create_with_options(
        self,
        request: main_models.ChatBIPatternIndexCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternIndexCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.pattern_table_name):
            query['PatternTableName'] = request.pattern_table_name
        if not DaraCore.is_null(request.table_name_suffix):
            query['TableNameSuffix'] = request.table_name_suffix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternIndexCreate',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternIndexCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipattern_index_create_with_options_async(
        self,
        request: main_models.ChatBIPatternIndexCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternIndexCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.pattern_table_name):
            query['PatternTableName'] = request.pattern_table_name
        if not DaraCore.is_null(request.table_name_suffix):
            query['TableNameSuffix'] = request.table_name_suffix
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternIndexCreate',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternIndexCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipattern_index_create(
        self,
        request: main_models.ChatBIPatternIndexCreateRequest,
    ) -> main_models.ChatBIPatternIndexCreateResponse:
        runtime = RuntimeOptions()
        return self.chat_bipattern_index_create_with_options(request, runtime)

    async def chat_bipattern_index_create_async(
        self,
        request: main_models.ChatBIPatternIndexCreateRequest,
    ) -> main_models.ChatBIPatternIndexCreateResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipattern_index_create_with_options_async(request, runtime)

    def chat_bipattern_index_delete_with_options(
        self,
        request: main_models.ChatBIPatternIndexDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternIndexDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternIndexDelete',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternIndexDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipattern_index_delete_with_options_async(
        self,
        request: main_models.ChatBIPatternIndexDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternIndexDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternIndexDelete',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternIndexDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipattern_index_delete(
        self,
        request: main_models.ChatBIPatternIndexDeleteRequest,
    ) -> main_models.ChatBIPatternIndexDeleteResponse:
        runtime = RuntimeOptions()
        return self.chat_bipattern_index_delete_with_options(request, runtime)

    async def chat_bipattern_index_delete_async(
        self,
        request: main_models.ChatBIPatternIndexDeleteRequest,
    ) -> main_models.ChatBIPatternIndexDeleteResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipattern_index_delete_with_options_async(request, runtime)

    def chat_bipattern_index_query_tables_with_options(
        self,
        request: main_models.ChatBIPatternIndexQueryTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternIndexQueryTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternIndexQueryTables',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternIndexQueryTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipattern_index_query_tables_with_options_async(
        self,
        request: main_models.ChatBIPatternIndexQueryTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternIndexQueryTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternIndexQueryTables',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternIndexQueryTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipattern_index_query_tables(
        self,
        request: main_models.ChatBIPatternIndexQueryTablesRequest,
    ) -> main_models.ChatBIPatternIndexQueryTablesResponse:
        runtime = RuntimeOptions()
        return self.chat_bipattern_index_query_tables_with_options(request, runtime)

    async def chat_bipattern_index_query_tables_async(
        self,
        request: main_models.ChatBIPatternIndexQueryTablesRequest,
    ) -> main_models.ChatBIPatternIndexQueryTablesResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipattern_index_query_tables_with_options_async(request, runtime)

    def chat_bipattern_query_entries_with_options(
        self,
        request: main_models.ChatBIPatternQueryEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternQueryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternQueryEntries',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternQueryEntriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipattern_query_entries_with_options_async(
        self,
        request: main_models.ChatBIPatternQueryEntriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternQueryEntriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternQueryEntries',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternQueryEntriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipattern_query_entries(
        self,
        request: main_models.ChatBIPatternQueryEntriesRequest,
    ) -> main_models.ChatBIPatternQueryEntriesResponse:
        runtime = RuntimeOptions()
        return self.chat_bipattern_query_entries_with_options(request, runtime)

    async def chat_bipattern_query_entries_async(
        self,
        request: main_models.ChatBIPatternQueryEntriesRequest,
    ) -> main_models.ChatBIPatternQueryEntriesResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipattern_query_entries_with_options_async(request, runtime)

    def chat_bipattern_query_tables_with_options(
        self,
        request: main_models.ChatBIPatternQueryTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternQueryTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternQueryTables',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternQueryTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipattern_query_tables_with_options_async(
        self,
        request: main_models.ChatBIPatternQueryTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternQueryTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternQueryTables',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternQueryTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipattern_query_tables(
        self,
        request: main_models.ChatBIPatternQueryTablesRequest,
    ) -> main_models.ChatBIPatternQueryTablesResponse:
        runtime = RuntimeOptions()
        return self.chat_bipattern_query_tables_with_options(request, runtime)

    async def chat_bipattern_query_tables_async(
        self,
        request: main_models.ChatBIPatternQueryTablesRequest,
    ) -> main_models.ChatBIPatternQueryTablesResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipattern_query_tables_with_options_async(request, runtime)

    def chat_bipattern_update_entry_with_options(
        self,
        request: main_models.ChatBIPatternUpdateEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternUpdateEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.pattern_description):
            query['PatternDescription'] = request.pattern_description
        if not DaraCore.is_null(request.pattern_params):
            query['PatternParams'] = request.pattern_params
        if not DaraCore.is_null(request.pattern_question):
            query['PatternQuestion'] = request.pattern_question
        if not DaraCore.is_null(request.pattern_sql):
            query['PatternSql'] = request.pattern_sql
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternUpdateEntry',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternUpdateEntryResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipattern_update_entry_with_options_async(
        self,
        request: main_models.ChatBIPatternUpdateEntryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPatternUpdateEntryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.id):
            query['Id'] = request.id
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.pattern_description):
            query['PatternDescription'] = request.pattern_description
        if not DaraCore.is_null(request.pattern_params):
            query['PatternParams'] = request.pattern_params
        if not DaraCore.is_null(request.pattern_question):
            query['PatternQuestion'] = request.pattern_question
        if not DaraCore.is_null(request.pattern_sql):
            query['PatternSql'] = request.pattern_sql
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPatternUpdateEntry',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPatternUpdateEntryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipattern_update_entry(
        self,
        request: main_models.ChatBIPatternUpdateEntryRequest,
    ) -> main_models.ChatBIPatternUpdateEntryResponse:
        runtime = RuntimeOptions()
        return self.chat_bipattern_update_entry_with_options(request, runtime)

    async def chat_bipattern_update_entry_async(
        self,
        request: main_models.ChatBIPatternUpdateEntryRequest,
    ) -> main_models.ChatBIPatternUpdateEntryResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipattern_update_entry_with_options_async(request, runtime)

    def chat_bipredict_sse_with_sse(
        self,
        tmp_req: main_models.ChatBIPredictSseRequest,
        runtime: RuntimeOptions,
    ) -> Generator[main_models.ChatBIPredictSseResponse, None, None]:
        tmp_req.validate()
        request = main_models.ChatBIPredictSseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.generate_chart):
            query['GenerateChart'] = request.generate_chart
        if not DaraCore.is_null(request.generate_summary):
            query['GenerateSummary'] = request.generate_summary
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.pattern_index_table_name):
            query['PatternIndexTableName'] = request.pattern_index_table_name
        if not DaraCore.is_null(request.question):
            query['Question'] = request.question
        if not DaraCore.is_null(request.schema_index_table_name):
            query['SchemaIndexTableName'] = request.schema_index_table_name
        if not DaraCore.is_null(request.select_data):
            query['SelectData'] = request.select_data
        if not DaraCore.is_null(request.thinking_mode):
            query['ThinkingMode'] = request.thinking_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPredictSse',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi(params, req, runtime)
        for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.ChatBIPredictSseResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    async def chat_bipredict_sse_with_sse_async(
        self,
        tmp_req: main_models.ChatBIPredictSseRequest,
        runtime: RuntimeOptions,
    ) -> AsyncGenerator[main_models.ChatBIPredictSseResponse, None, None]:
        tmp_req.validate()
        request = main_models.ChatBIPredictSseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.generate_chart):
            query['GenerateChart'] = request.generate_chart
        if not DaraCore.is_null(request.generate_summary):
            query['GenerateSummary'] = request.generate_summary
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.pattern_index_table_name):
            query['PatternIndexTableName'] = request.pattern_index_table_name
        if not DaraCore.is_null(request.question):
            query['Question'] = request.question
        if not DaraCore.is_null(request.schema_index_table_name):
            query['SchemaIndexTableName'] = request.schema_index_table_name
        if not DaraCore.is_null(request.select_data):
            query['SelectData'] = request.select_data
        if not DaraCore.is_null(request.thinking_mode):
            query['ThinkingMode'] = request.thinking_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPredictSse',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        sse_resp = self.call_sseapi_async(params, req, runtime)
        async for resp in sse_resp:
            data = json.loads(resp.event.data)
            yield  DaraCore.from_map(
                main_models.ChatBIPredictSseResponse(),
                {
                'statusCode': resp.status_code,
                'headers': resp.headers,
                'body': DaraCore.merge({
                    'RequestId': resp.event.id,
                    'Message': resp.event.event
                }, data)
            })

    def chat_bipredict_sse_with_options(
        self,
        tmp_req: main_models.ChatBIPredictSseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPredictSseResponse:
        tmp_req.validate()
        request = main_models.ChatBIPredictSseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.generate_chart):
            query['GenerateChart'] = request.generate_chart
        if not DaraCore.is_null(request.generate_summary):
            query['GenerateSummary'] = request.generate_summary
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.pattern_index_table_name):
            query['PatternIndexTableName'] = request.pattern_index_table_name
        if not DaraCore.is_null(request.question):
            query['Question'] = request.question
        if not DaraCore.is_null(request.schema_index_table_name):
            query['SchemaIndexTableName'] = request.schema_index_table_name
        if not DaraCore.is_null(request.select_data):
            query['SelectData'] = request.select_data
        if not DaraCore.is_null(request.thinking_mode):
            query['ThinkingMode'] = request.thinking_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPredictSse',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPredictSseResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bipredict_sse_with_options_async(
        self,
        tmp_req: main_models.ChatBIPredictSseRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIPredictSseResponse:
        tmp_req.validate()
        request = main_models.ChatBIPredictSseShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.parameters):
            request.parameters_shrink = Utils.array_to_string_with_specified_style(tmp_req.parameters, 'Parameters', 'json')
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.generate_chart):
            query['GenerateChart'] = request.generate_chart
        if not DaraCore.is_null(request.generate_summary):
            query['GenerateSummary'] = request.generate_summary
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.parameters_shrink):
            query['Parameters'] = request.parameters_shrink
        if not DaraCore.is_null(request.pattern_index_table_name):
            query['PatternIndexTableName'] = request.pattern_index_table_name
        if not DaraCore.is_null(request.question):
            query['Question'] = request.question
        if not DaraCore.is_null(request.schema_index_table_name):
            query['SchemaIndexTableName'] = request.schema_index_table_name
        if not DaraCore.is_null(request.select_data):
            query['SelectData'] = request.select_data
        if not DaraCore.is_null(request.thinking_mode):
            query['ThinkingMode'] = request.thinking_mode
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIPredictSse',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIPredictSseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bipredict_sse(
        self,
        request: main_models.ChatBIPredictSseRequest,
    ) -> main_models.ChatBIPredictSseResponse:
        runtime = RuntimeOptions()
        return self.chat_bipredict_sse_with_options(request, runtime)

    async def chat_bipredict_sse_async(
        self,
        request: main_models.ChatBIPredictSseRequest,
    ) -> main_models.ChatBIPredictSseResponse:
        runtime = RuntimeOptions()
        return await self.chat_bipredict_sse_with_options_async(request, runtime)

    def chat_bischema_index_create_with_options(
        self,
        request: main_models.ChatBISchemaIndexCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBISchemaIndexCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.columns_excluded):
            query['ColumnsExcluded'] = request.columns_excluded
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name_suffix):
            query['TableNameSuffix'] = request.table_name_suffix
        if not DaraCore.is_null(request.tables_included):
            query['TablesIncluded'] = request.tables_included
        if not DaraCore.is_null(request.to_sample):
            query['ToSample'] = request.to_sample
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBISchemaIndexCreate',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBISchemaIndexCreateResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bischema_index_create_with_options_async(
        self,
        request: main_models.ChatBISchemaIndexCreateRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBISchemaIndexCreateResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.columns_excluded):
            query['ColumnsExcluded'] = request.columns_excluded
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name_suffix):
            query['TableNameSuffix'] = request.table_name_suffix
        if not DaraCore.is_null(request.tables_included):
            query['TablesIncluded'] = request.tables_included
        if not DaraCore.is_null(request.to_sample):
            query['ToSample'] = request.to_sample
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBISchemaIndexCreate',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBISchemaIndexCreateResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bischema_index_create(
        self,
        request: main_models.ChatBISchemaIndexCreateRequest,
    ) -> main_models.ChatBISchemaIndexCreateResponse:
        runtime = RuntimeOptions()
        return self.chat_bischema_index_create_with_options(request, runtime)

    async def chat_bischema_index_create_async(
        self,
        request: main_models.ChatBISchemaIndexCreateRequest,
    ) -> main_models.ChatBISchemaIndexCreateResponse:
        runtime = RuntimeOptions()
        return await self.chat_bischema_index_create_with_options_async(request, runtime)

    def chat_bischema_index_delete_with_options(
        self,
        request: main_models.ChatBISchemaIndexDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBISchemaIndexDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBISchemaIndexDelete',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBISchemaIndexDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bischema_index_delete_with_options_async(
        self,
        request: main_models.ChatBISchemaIndexDeleteRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBISchemaIndexDeleteResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBISchemaIndexDelete',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBISchemaIndexDeleteResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bischema_index_delete(
        self,
        request: main_models.ChatBISchemaIndexDeleteRequest,
    ) -> main_models.ChatBISchemaIndexDeleteResponse:
        runtime = RuntimeOptions()
        return self.chat_bischema_index_delete_with_options(request, runtime)

    async def chat_bischema_index_delete_async(
        self,
        request: main_models.ChatBISchemaIndexDeleteRequest,
    ) -> main_models.ChatBISchemaIndexDeleteResponse:
        runtime = RuntimeOptions()
        return await self.chat_bischema_index_delete_with_options_async(request, runtime)

    def chat_bischema_index_query_tables_with_options(
        self,
        request: main_models.ChatBISchemaIndexQueryTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBISchemaIndexQueryTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBISchemaIndexQueryTables',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBISchemaIndexQueryTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_bischema_index_query_tables_with_options_async(
        self,
        request: main_models.ChatBISchemaIndexQueryTablesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBISchemaIndexQueryTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBISchemaIndexQueryTables',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBISchemaIndexQueryTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_bischema_index_query_tables(
        self,
        request: main_models.ChatBISchemaIndexQueryTablesRequest,
    ) -> main_models.ChatBISchemaIndexQueryTablesResponse:
        runtime = RuntimeOptions()
        return self.chat_bischema_index_query_tables_with_options(request, runtime)

    async def chat_bischema_index_query_tables_async(
        self,
        request: main_models.ChatBISchemaIndexQueryTablesRequest,
    ) -> main_models.ChatBISchemaIndexQueryTablesResponse:
        runtime = RuntimeOptions()
        return await self.chat_bischema_index_query_tables_with_options_async(request, runtime)

    def chat_biupdate_table_validation_columns_with_options(
        self,
        request: main_models.ChatBIUpdateTableValidationColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIUpdateTableValidationColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIUpdateTableValidationColumns',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIUpdateTableValidationColumnsResponse(),
            self.call_api(params, req, runtime)
        )

    async def chat_biupdate_table_validation_columns_with_options_async(
        self,
        request: main_models.ChatBIUpdateTableValidationColumnsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ChatBIUpdateTableValidationColumnsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.db_name):
            query['DbName'] = request.db_name
        if not DaraCore.is_null(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not DaraCore.is_null(request.table_name):
            query['TableName'] = request.table_name
        if not DaraCore.is_null(request.table_type):
            query['TableType'] = request.table_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ChatBIUpdateTableValidationColumns',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ChatBIUpdateTableValidationColumnsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def chat_biupdate_table_validation_columns(
        self,
        request: main_models.ChatBIUpdateTableValidationColumnsRequest,
    ) -> main_models.ChatBIUpdateTableValidationColumnsResponse:
        runtime = RuntimeOptions()
        return self.chat_biupdate_table_validation_columns_with_options(request, runtime)

    async def chat_biupdate_table_validation_columns_async(
        self,
        request: main_models.ChatBIUpdateTableValidationColumnsRequest,
    ) -> main_models.ChatBIUpdateTableValidationColumnsResponse:
        runtime = RuntimeOptions()
        return await self.chat_biupdate_table_validation_columns_with_options_async(request, runtime)

    def create_multimodal_dataset_with_options(
        self,
        request: main_models.CreateMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_description):
            query['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultimodalDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_multimodal_dataset_with_options_async(
        self,
        request: main_models.CreateMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_description):
            query['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultimodalDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_multimodal_dataset(
        self,
        request: main_models.CreateMultimodalDatasetRequest,
    ) -> main_models.CreateMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return self.create_multimodal_dataset_with_options(request, runtime)

    async def create_multimodal_dataset_async(
        self,
        request: main_models.CreateMultimodalDatasetRequest,
    ) -> main_models.CreateMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return await self.create_multimodal_dataset_with_options_async(request, runtime)

    def create_multimodal_dataset_embedding_with_options(
        self,
        request: main_models.CreateMultimodalDatasetEmbeddingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultimodalDatasetEmbeddingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultimodalDatasetEmbedding',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultimodalDatasetEmbeddingResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_multimodal_dataset_embedding_with_options_async(
        self,
        request: main_models.CreateMultimodalDatasetEmbeddingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultimodalDatasetEmbeddingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.model):
            query['Model'] = request.model
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultimodalDatasetEmbedding',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultimodalDatasetEmbeddingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_multimodal_dataset_embedding(
        self,
        request: main_models.CreateMultimodalDatasetEmbeddingRequest,
    ) -> main_models.CreateMultimodalDatasetEmbeddingResponse:
        runtime = RuntimeOptions()
        return self.create_multimodal_dataset_embedding_with_options(request, runtime)

    async def create_multimodal_dataset_embedding_async(
        self,
        request: main_models.CreateMultimodalDatasetEmbeddingRequest,
    ) -> main_models.CreateMultimodalDatasetEmbeddingResponse:
        runtime = RuntimeOptions()
        return await self.create_multimodal_dataset_embedding_with_options_async(request, runtime)

    def create_multimodal_search_task_with_options(
        self,
        tmp_req: main_models.CreateMultimodalSearchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultimodalSearchTaskResponse:
        tmp_req.validate()
        request = main_models.CreateMultimodalSearchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_ids):
            request.dataset_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_ids, 'DatasetIds', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_ids_shrink):
            query['DatasetIds'] = request.dataset_ids_shrink
        if not DaraCore.is_null(request.embedding_model):
            query['EmbeddingModel'] = request.embedding_model
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.search_model):
            query['SearchModel'] = request.search_model
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultimodalSearchTask',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultimodalSearchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_multimodal_search_task_with_options_async(
        self,
        tmp_req: main_models.CreateMultimodalSearchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultimodalSearchTaskResponse:
        tmp_req.validate()
        request = main_models.CreateMultimodalSearchTaskShrinkRequest()
        Utils.convert(tmp_req, request)
        if not DaraCore.is_null(tmp_req.dataset_ids):
            request.dataset_ids_shrink = Utils.array_to_string_with_specified_style(tmp_req.dataset_ids, 'DatasetIds', 'json')
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_ids_shrink):
            query['DatasetIds'] = request.dataset_ids_shrink
        if not DaraCore.is_null(request.embedding_model):
            query['EmbeddingModel'] = request.embedding_model
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.search_model):
            query['SearchModel'] = request.search_model
        if not DaraCore.is_null(request.top_k):
            query['TopK'] = request.top_k
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultimodalSearchTask',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultimodalSearchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_multimodal_search_task(
        self,
        request: main_models.CreateMultimodalSearchTaskRequest,
    ) -> main_models.CreateMultimodalSearchTaskResponse:
        runtime = RuntimeOptions()
        return self.create_multimodal_search_task_with_options(request, runtime)

    async def create_multimodal_search_task_async(
        self,
        request: main_models.CreateMultimodalSearchTaskRequest,
    ) -> main_models.CreateMultimodalSearchTaskResponse:
        runtime = RuntimeOptions()
        return await self.create_multimodal_search_task_with_options_async(request, runtime)

    def delete_multimodal_dataset_with_options(
        self,
        request: main_models.DeleteMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultimodalDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_multimodal_dataset_with_options_async(
        self,
        request: main_models.DeleteMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultimodalDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_multimodal_dataset(
        self,
        request: main_models.DeleteMultimodalDatasetRequest,
    ) -> main_models.DeleteMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return self.delete_multimodal_dataset_with_options(request, runtime)

    async def delete_multimodal_dataset_async(
        self,
        request: main_models.DeleteMultimodalDatasetRequest,
    ) -> main_models.DeleteMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return await self.delete_multimodal_dataset_with_options_async(request, runtime)

    def delete_multimodal_embedding_with_options(
        self,
        request: main_models.DeleteMultimodalEmbeddingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultimodalEmbeddingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.embedding):
            query['Embedding'] = request.embedding
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultimodalEmbedding',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultimodalEmbeddingResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_multimodal_embedding_with_options_async(
        self,
        request: main_models.DeleteMultimodalEmbeddingRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultimodalEmbeddingResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.embedding):
            query['Embedding'] = request.embedding
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultimodalEmbedding',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultimodalEmbeddingResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_multimodal_embedding(
        self,
        request: main_models.DeleteMultimodalEmbeddingRequest,
    ) -> main_models.DeleteMultimodalEmbeddingResponse:
        runtime = RuntimeOptions()
        return self.delete_multimodal_embedding_with_options(request, runtime)

    async def delete_multimodal_embedding_async(
        self,
        request: main_models.DeleteMultimodalEmbeddingRequest,
    ) -> main_models.DeleteMultimodalEmbeddingResponse:
        runtime = RuntimeOptions()
        return await self.delete_multimodal_embedding_with_options_async(request, runtime)

    def download_multimodal_search_task_result_metadata_with_options(
        self,
        request: main_models.DownloadMultimodalSearchTaskResultMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadMultimodalSearchTaskResultMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadMultimodalSearchTaskResultMetadata',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadMultimodalSearchTaskResultMetadataResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_multimodal_search_task_result_metadata_with_options_async(
        self,
        request: main_models.DownloadMultimodalSearchTaskResultMetadataRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DownloadMultimodalSearchTaskResultMetadataResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DownloadMultimodalSearchTaskResultMetadata',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DownloadMultimodalSearchTaskResultMetadataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_multimodal_search_task_result_metadata(
        self,
        request: main_models.DownloadMultimodalSearchTaskResultMetadataRequest,
    ) -> main_models.DownloadMultimodalSearchTaskResultMetadataResponse:
        runtime = RuntimeOptions()
        return self.download_multimodal_search_task_result_metadata_with_options(request, runtime)

    async def download_multimodal_search_task_result_metadata_async(
        self,
        request: main_models.DownloadMultimodalSearchTaskResultMetadataRequest,
    ) -> main_models.DownloadMultimodalSearchTaskResultMetadataResponse:
        runtime = RuntimeOptions()
        return await self.download_multimodal_search_task_result_metadata_with_options_async(request, runtime)

    def get_user_token_with_options(
        self,
        request: main_models.GetUserTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserToken',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_token_with_options_async(
        self,
        request: main_models.GetUserTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetUserTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.password):
            query['Password'] = request.password
        if not DaraCore.is_null(request.username):
            query['Username'] = request.username
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUserToken',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user_token(
        self,
        request: main_models.GetUserTokenRequest,
    ) -> main_models.GetUserTokenResponse:
        runtime = RuntimeOptions()
        return self.get_user_token_with_options(request, runtime)

    async def get_user_token_async(
        self,
        request: main_models.GetUserTokenRequest,
    ) -> main_models.GetUserTokenResponse:
        runtime = RuntimeOptions()
        return await self.get_user_token_with_options_async(request, runtime)

    def list_multimodal_dataset_with_options(
        self,
        request: main_models.ListMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultimodalDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multimodal_dataset_with_options_async(
        self,
        request: main_models.ListMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.input_field):
            query['InputField'] = request.input_field
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultimodalDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multimodal_dataset(
        self,
        request: main_models.ListMultimodalDatasetRequest,
    ) -> main_models.ListMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return self.list_multimodal_dataset_with_options(request, runtime)

    async def list_multimodal_dataset_async(
        self,
        request: main_models.ListMultimodalDatasetRequest,
    ) -> main_models.ListMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return await self.list_multimodal_dataset_with_options_async(request, runtime)

    def list_multimodal_embedding_model_with_options(
        self,
        request: main_models.ListMultimodalEmbeddingModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultimodalEmbeddingModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultimodalEmbeddingModel',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultimodalEmbeddingModelResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multimodal_embedding_model_with_options_async(
        self,
        request: main_models.ListMultimodalEmbeddingModelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultimodalEmbeddingModelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultimodalEmbeddingModel',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultimodalEmbeddingModelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multimodal_embedding_model(
        self,
        request: main_models.ListMultimodalEmbeddingModelRequest,
    ) -> main_models.ListMultimodalEmbeddingModelResponse:
        runtime = RuntimeOptions()
        return self.list_multimodal_embedding_model_with_options(request, runtime)

    async def list_multimodal_embedding_model_async(
        self,
        request: main_models.ListMultimodalEmbeddingModelRequest,
    ) -> main_models.ListMultimodalEmbeddingModelResponse:
        runtime = RuntimeOptions()
        return await self.list_multimodal_embedding_model_with_options_async(request, runtime)

    def list_multimodal_search_task_with_options(
        self,
        request: main_models.ListMultimodalSearchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultimodalSearchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultimodalSearchTask',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultimodalSearchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multimodal_search_task_with_options_async(
        self,
        request: main_models.ListMultimodalSearchTaskRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultimodalSearchTaskResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultimodalSearchTask',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultimodalSearchTaskResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multimodal_search_task(
        self,
        request: main_models.ListMultimodalSearchTaskRequest,
    ) -> main_models.ListMultimodalSearchTaskResponse:
        runtime = RuntimeOptions()
        return self.list_multimodal_search_task_with_options(request, runtime)

    async def list_multimodal_search_task_async(
        self,
        request: main_models.ListMultimodalSearchTaskRequest,
    ) -> main_models.ListMultimodalSearchTaskResponse:
        runtime = RuntimeOptions()
        return await self.list_multimodal_search_task_with_options_async(request, runtime)

    def list_multimodal_search_task_result_with_options(
        self,
        request: main_models.ListMultimodalSearchTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultimodalSearchTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultimodalSearchTaskResult',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultimodalSearchTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multimodal_search_task_result_with_options_async(
        self,
        request: main_models.ListMultimodalSearchTaskResultRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultimodalSearchTaskResultResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultimodalSearchTaskResult',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultimodalSearchTaskResultResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multimodal_search_task_result(
        self,
        request: main_models.ListMultimodalSearchTaskResultRequest,
    ) -> main_models.ListMultimodalSearchTaskResultResponse:
        runtime = RuntimeOptions()
        return self.list_multimodal_search_task_result_with_options(request, runtime)

    async def list_multimodal_search_task_result_async(
        self,
        request: main_models.ListMultimodalSearchTaskResultRequest,
    ) -> main_models.ListMultimodalSearchTaskResultResponse:
        runtime = RuntimeOptions()
        return await self.list_multimodal_search_task_result_with_options_async(request, runtime)

    def update_multimodal_dataset_with_options(
        self,
        request: main_models.UpdateMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_description):
            query['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMultimodalDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_multimodal_dataset_with_options_async(
        self,
        request: main_models.UpdateMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_description):
            query['DatasetDescription'] = request.dataset_description
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.dataset_name):
            query['DatasetName'] = request.dataset_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMultimodalDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_multimodal_dataset(
        self,
        request: main_models.UpdateMultimodalDatasetRequest,
    ) -> main_models.UpdateMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return self.update_multimodal_dataset_with_options(request, runtime)

    async def update_multimodal_dataset_async(
        self,
        request: main_models.UpdateMultimodalDatasetRequest,
    ) -> main_models.UpdateMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return await self.update_multimodal_dataset_with_options_async(request, runtime)

    def upload_ossmultimodal_dataset_with_options(
        self,
        request: main_models.UploadOSSMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadOSSMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.oss_url):
            query['OssUrl'] = request.oss_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadOSSMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadOSSMultimodalDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_ossmultimodal_dataset_with_options_async(
        self,
        request: main_models.UploadOSSMultimodalDatasetRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UploadOSSMultimodalDatasetResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not DaraCore.is_null(request.oss_url):
            query['OssUrl'] = request.oss_url
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UploadOSSMultimodalDataset',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UploadOSSMultimodalDatasetResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_ossmultimodal_dataset(
        self,
        request: main_models.UploadOSSMultimodalDatasetRequest,
    ) -> main_models.UploadOSSMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return self.upload_ossmultimodal_dataset_with_options(request, runtime)

    async def upload_ossmultimodal_dataset_async(
        self,
        request: main_models.UploadOSSMultimodalDatasetRequest,
    ) -> main_models.UploadOSSMultimodalDatasetResponse:
        runtime = RuntimeOptions()
        return await self.upload_ossmultimodal_dataset_with_options_async(request, runtime)

    def validate_database_user_token_with_options(
        self,
        request: main_models.ValidateDatabaseUserTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateDatabaseUserTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateDatabaseUserToken',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateDatabaseUserTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_database_user_token_with_options_async(
        self,
        request: main_models.ValidateDatabaseUserTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateDatabaseUserTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        if not DaraCore.is_null(request.dbname):
            query['DBName'] = request.dbname
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateDatabaseUserToken',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateDatabaseUserTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_database_user_token(
        self,
        request: main_models.ValidateDatabaseUserTokenRequest,
    ) -> main_models.ValidateDatabaseUserTokenResponse:
        runtime = RuntimeOptions()
        return self.validate_database_user_token_with_options(request, runtime)

    async def validate_database_user_token_async(
        self,
        request: main_models.ValidateDatabaseUserTokenRequest,
    ) -> main_models.ValidateDatabaseUserTokenResponse:
        runtime = RuntimeOptions()
        return await self.validate_database_user_token_with_options_async(request, runtime)

    def validate_user_token_with_options(
        self,
        request: main_models.ValidateUserTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateUserTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateUserToken',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateUserTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def validate_user_token_with_options_async(
        self,
        request: main_models.ValidateUserTokenRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ValidateUserTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.auth_message):
            query['AuthMessage'] = request.auth_message
        if not DaraCore.is_null(request.auth_type):
            query['AuthType'] = request.auth_type
        if not DaraCore.is_null(request.dbcluster_id):
            query['DBClusterId'] = request.dbcluster_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ValidateUserToken',
            version = '2025-10-13',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ValidateUserTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def validate_user_token(
        self,
        request: main_models.ValidateUserTokenRequest,
    ) -> main_models.ValidateUserTokenResponse:
        runtime = RuntimeOptions()
        return self.validate_user_token_with_options(request, runtime)

    async def validate_user_token_async(
        self,
        request: main_models.ValidateUserTokenRequest,
    ) -> main_models.ValidateUserTokenResponse:
        runtime = RuntimeOptions()
        return await self.validate_user_token_with_options_async(request, runtime)
