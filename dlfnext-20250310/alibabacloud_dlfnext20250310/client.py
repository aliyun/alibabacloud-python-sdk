# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_dlfnext20250310 import models as main_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('dlfnext', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def alter_catalog_with_options(
        self,
        catalog: str,
        request: main_models.AlterCatalogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterCatalogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.removals):
            body['removals'] = request.removals
        if not DaraCore.is_null(request.updates):
            body['updates'] = request.updates
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterCatalog',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/{DaraURL.percent_encode(catalog)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AlterCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_catalog_with_options_async(
        self,
        catalog: str,
        request: main_models.AlterCatalogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterCatalogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.removals):
            body['removals'] = request.removals
        if not DaraCore.is_null(request.updates):
            body['updates'] = request.updates
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterCatalog',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/{DaraURL.percent_encode(catalog)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AlterCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_catalog(
        self,
        catalog: str,
        request: main_models.AlterCatalogRequest,
    ) -> main_models.AlterCatalogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.alter_catalog_with_options(catalog, request, headers, runtime)

    async def alter_catalog_async(
        self,
        catalog: str,
        request: main_models.AlterCatalogRequest,
    ) -> main_models.AlterCatalogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.alter_catalog_with_options_async(catalog, request, headers, runtime)

    def alter_database_with_options(
        self,
        catalog_id: str,
        database: str,
        request: main_models.AlterDatabaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterDatabaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.removals):
            body['removals'] = request.removals
        if not DaraCore.is_null(request.updates):
            body['updates'] = request.updates
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterDatabase',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AlterDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_database_with_options_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.AlterDatabaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterDatabaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.removals):
            body['removals'] = request.removals
        if not DaraCore.is_null(request.updates):
            body['updates'] = request.updates
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterDatabase',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AlterDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_database(
        self,
        catalog_id: str,
        database: str,
        request: main_models.AlterDatabaseRequest,
    ) -> main_models.AlterDatabaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.alter_database_with_options(catalog_id, database, request, headers, runtime)

    async def alter_database_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.AlterDatabaseRequest,
    ) -> main_models.AlterDatabaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.alter_database_with_options_async(catalog_id, database, request, headers, runtime)

    def alter_receiver_with_options(
        self,
        receiver: str,
        request: main_models.AlterReceiverRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterReceiverResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.receiver_name):
            body['receiverName'] = request.receiver_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterReceiver',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers/{DaraURL.percent_encode(receiver)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_receiver_with_options_async(
        self,
        receiver: str,
        request: main_models.AlterReceiverRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterReceiverResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.receiver_name):
            body['receiverName'] = request.receiver_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterReceiver',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers/{DaraURL.percent_encode(receiver)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterReceiverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_receiver(
        self,
        receiver: str,
        request: main_models.AlterReceiverRequest,
    ) -> main_models.AlterReceiverResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.alter_receiver_with_options(receiver, request, headers, runtime)

    async def alter_receiver_async(
        self,
        receiver: str,
        request: main_models.AlterReceiverRequest,
    ) -> main_models.AlterReceiverResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.alter_receiver_with_options_async(receiver, request, headers, runtime)

    def alter_share_with_options(
        self,
        share: str,
        request: main_models.AlterShareRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterShareResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.enable_write):
            body['enableWrite'] = request.enable_write
        if not DaraCore.is_null(request.share_name):
            body['shareName'] = request.share_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterShare',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_share_with_options_async(
        self,
        share: str,
        request: main_models.AlterShareRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterShareResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.enable_write):
            body['enableWrite'] = request.enable_write
        if not DaraCore.is_null(request.share_name):
            body['shareName'] = request.share_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterShare',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_share(
        self,
        share: str,
        request: main_models.AlterShareRequest,
    ) -> main_models.AlterShareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.alter_share_with_options(share, request, headers, runtime)

    async def alter_share_async(
        self,
        share: str,
        request: main_models.AlterShareRequest,
    ) -> main_models.AlterShareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.alter_share_with_options_async(share, request, headers, runtime)

    def alter_share_receivers_with_options(
        self,
        share: str,
        request: main_models.AlterShareReceiversRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterShareReceiversResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.added_receivers):
            body['addedReceivers'] = request.added_receivers
        if not DaraCore.is_null(request.removed_receivers):
            body['removedReceivers'] = request.removed_receivers
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterShareReceivers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}/receivers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterShareReceiversResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_share_receivers_with_options_async(
        self,
        share: str,
        request: main_models.AlterShareReceiversRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterShareReceiversResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.added_receivers):
            body['addedReceivers'] = request.added_receivers
        if not DaraCore.is_null(request.removed_receivers):
            body['removedReceivers'] = request.removed_receivers
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterShareReceivers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}/receivers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterShareReceiversResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_share_receivers(
        self,
        share: str,
        request: main_models.AlterShareReceiversRequest,
    ) -> main_models.AlterShareReceiversResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.alter_share_receivers_with_options(share, request, headers, runtime)

    async def alter_share_receivers_async(
        self,
        share: str,
        request: main_models.AlterShareReceiversRequest,
    ) -> main_models.AlterShareReceiversResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.alter_share_receivers_with_options_async(share, request, headers, runtime)

    def alter_share_resources_with_options(
        self,
        share: str,
        request: main_models.AlterShareResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterShareResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.catalog_id):
            body['catalogId'] = request.catalog_id
        if not DaraCore.is_null(request.share_resource_list):
            body['shareResourceList'] = request.share_resource_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterShareResources',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterShareResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_share_resources_with_options_async(
        self,
        share: str,
        request: main_models.AlterShareResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterShareResourcesResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.catalog_id):
            body['catalogId'] = request.catalog_id
        if not DaraCore.is_null(request.share_resource_list):
            body['shareResourceList'] = request.share_resource_list
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterShareResources',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}/resources',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterShareResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_share_resources(
        self,
        share: str,
        request: main_models.AlterShareResourcesRequest,
    ) -> main_models.AlterShareResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.alter_share_resources_with_options(share, request, headers, runtime)

    async def alter_share_resources_async(
        self,
        share: str,
        request: main_models.AlterShareResourcesRequest,
    ) -> main_models.AlterShareResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.alter_share_resources_with_options_async(share, request, headers, runtime)

    def alter_table_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.AlterTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.changes):
            body['changes'] = request.changes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def alter_table_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.AlterTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.AlterTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.changes):
            body['changes'] = request.changes
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'AlterTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.AlterTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def alter_table(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.AlterTableRequest,
    ) -> main_models.AlterTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.alter_table_with_options(catalog_id, database, table, request, headers, runtime)

    async def alter_table_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.AlterTableRequest,
    ) -> main_models.AlterTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.alter_table_with_options_async(catalog_id, database, table, request, headers, runtime)

    def batch_grant_permissions_with_options(
        self,
        catalog_id: str,
        request: main_models.BatchGrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGrantPermissionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchGrantPermissions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/permissions/{DaraURL.percent_encode(catalog_id)}/batchgrant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGrantPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_grant_permissions_with_options_async(
        self,
        catalog_id: str,
        request: main_models.BatchGrantPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchGrantPermissionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchGrantPermissions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/permissions/{DaraURL.percent_encode(catalog_id)}/batchgrant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGrantPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_grant_permissions(
        self,
        catalog_id: str,
        request: main_models.BatchGrantPermissionsRequest,
    ) -> main_models.BatchGrantPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_grant_permissions_with_options(catalog_id, request, headers, runtime)

    async def batch_grant_permissions_async(
        self,
        catalog_id: str,
        request: main_models.BatchGrantPermissionsRequest,
    ) -> main_models.BatchGrantPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_grant_permissions_with_options_async(catalog_id, request, headers, runtime)

    def batch_revoke_permissions_with_options(
        self,
        catalog_id: str,
        request: main_models.BatchRevokePermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchRevokePermissionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchRevokePermissions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/permissions/{DaraURL.percent_encode(catalog_id)}/batchrevoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRevokePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_revoke_permissions_with_options_async(
        self,
        catalog_id: str,
        request: main_models.BatchRevokePermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.BatchRevokePermissionsResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.permissions):
            body['permissions'] = request.permissions
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'BatchRevokePermissions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/permissions/{DaraURL.percent_encode(catalog_id)}/batchrevoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchRevokePermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_revoke_permissions(
        self,
        catalog_id: str,
        request: main_models.BatchRevokePermissionsRequest,
    ) -> main_models.BatchRevokePermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.batch_revoke_permissions_with_options(catalog_id, request, headers, runtime)

    async def batch_revoke_permissions_async(
        self,
        catalog_id: str,
        request: main_models.BatchRevokePermissionsRequest,
    ) -> main_models.BatchRevokePermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.batch_revoke_permissions_with_options_async(catalog_id, request, headers, runtime)

    def create_catalog_with_options(
        self,
        request: main_models.CreateCatalogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCatalogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_shared):
            body['isShared'] = request.is_shared
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.share_id):
            body['shareId'] = request.share_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCatalog',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_catalog_with_options_async(
        self,
        request: main_models.CreateCatalogRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateCatalogResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.is_shared):
            body['isShared'] = request.is_shared
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        if not DaraCore.is_null(request.share_id):
            body['shareId'] = request.share_id
        if not DaraCore.is_null(request.type):
            body['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateCatalog',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_catalog(
        self,
        request: main_models.CreateCatalogRequest,
    ) -> main_models.CreateCatalogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_catalog_with_options(request, headers, runtime)

    async def create_catalog_async(
        self,
        request: main_models.CreateCatalogRequest,
    ) -> main_models.CreateCatalogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_catalog_with_options_async(request, headers, runtime)

    def create_database_with_options(
        self,
        catalog_id: str,
        request: main_models.CreateDatabaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatabaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatabase',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_database_with_options_async(
        self,
        catalog_id: str,
        request: main_models.CreateDatabaseRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateDatabaseResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.name):
            body['name'] = request.name
        if not DaraCore.is_null(request.options):
            body['options'] = request.options
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateDatabase',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_database(
        self,
        catalog_id: str,
        request: main_models.CreateDatabaseRequest,
    ) -> main_models.CreateDatabaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_database_with_options(catalog_id, request, headers, runtime)

    async def create_database_async(
        self,
        catalog_id: str,
        request: main_models.CreateDatabaseRequest,
    ) -> main_models.CreateDatabaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_database_with_options_async(catalog_id, request, headers, runtime)

    def create_receiver_with_options(
        self,
        request: main_models.CreateReceiverRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateReceiverResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.receiver_name):
            body['receiverName'] = request.receiver_name
        if not DaraCore.is_null(request.receiver_tenant_id):
            body['receiverTenantId'] = request.receiver_tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateReceiver',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_receiver_with_options_async(
        self,
        request: main_models.CreateReceiverRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateReceiverResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.receiver_name):
            body['receiverName'] = request.receiver_name
        if not DaraCore.is_null(request.receiver_tenant_id):
            body['receiverTenantId'] = request.receiver_tenant_id
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateReceiver',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateReceiverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_receiver(
        self,
        request: main_models.CreateReceiverRequest,
    ) -> main_models.CreateReceiverResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_receiver_with_options(request, headers, runtime)

    async def create_receiver_async(
        self,
        request: main_models.CreateReceiverRequest,
    ) -> main_models.CreateReceiverResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_receiver_with_options_async(request, headers, runtime)

    def create_role_with_options(
        self,
        request: main_models.CreateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
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
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.role_name):
            body['roleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateRole',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
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

    def create_share_with_options(
        self,
        request: main_models.CreateShareRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateShareResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.enable_write):
            body['enableWrite'] = request.enable_write
        if not DaraCore.is_null(request.share_name):
            body['shareName'] = request.share_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateShare',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_share_with_options_async(
        self,
        request: main_models.CreateShareRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateShareResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.comment):
            body['comment'] = request.comment
        if not DaraCore.is_null(request.enable_write):
            body['enableWrite'] = request.enable_write
        if not DaraCore.is_null(request.share_name):
            body['shareName'] = request.share_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateShare',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_share(
        self,
        request: main_models.CreateShareRequest,
    ) -> main_models.CreateShareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_share_with_options(request, headers, runtime)

    async def create_share_async(
        self,
        request: main_models.CreateShareRequest,
    ) -> main_models.CreateShareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_share_with_options_async(request, headers, runtime)

    def create_table_with_options(
        self,
        catalog_id: str,
        database: str,
        request: main_models.CreateTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identifier):
            body['identifier'] = request.identifier
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_table_with_options_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.CreateTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.CreateTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.identifier):
            body['identifier'] = request.identifier
        if not DaraCore.is_null(request.schema):
            body['schema'] = request.schema
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'CreateTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.CreateTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_table(
        self,
        catalog_id: str,
        database: str,
        request: main_models.CreateTableRequest,
    ) -> main_models.CreateTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.create_table_with_options(catalog_id, database, request, headers, runtime)

    async def create_table_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.CreateTableRequest,
    ) -> main_models.CreateTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.create_table_with_options_async(catalog_id, database, request, headers, runtime)

    def delete_role_with_options(
        self,
        request: main_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_role_with_options_async(
        self,
        request: main_models.DeleteRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DeleteRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteRole',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DeleteRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_role(
        self,
        request: main_models.DeleteRoleRequest,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.delete_role_with_options(request, headers, runtime)

    async def delete_role_async(
        self,
        request: main_models.DeleteRoleRequest,
    ) -> main_models.DeleteRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.delete_role_with_options_async(request, headers, runtime)

    def describe_regions_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/service/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/service/regions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.describe_regions_with_options(headers, runtime)

    async def describe_regions_async(self) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.describe_regions_with_options_async(headers, runtime)

    def drop_catalog_with_options(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropCatalogResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropCatalog',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/{DaraURL.percent_encode(catalog)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_catalog_with_options_async(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropCatalogResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropCatalog',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/{DaraURL.percent_encode(catalog)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_catalog(
        self,
        catalog: str,
    ) -> main_models.DropCatalogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.drop_catalog_with_options(catalog, headers, runtime)

    async def drop_catalog_async(
        self,
        catalog: str,
    ) -> main_models.DropCatalogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.drop_catalog_with_options_async(catalog, headers, runtime)

    def drop_database_with_options(
        self,
        catalog_id: str,
        database: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropDatabaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropDatabase',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_database_with_options_async(
        self,
        catalog_id: str,
        database: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropDatabaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropDatabase',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_database(
        self,
        catalog_id: str,
        database: str,
    ) -> main_models.DropDatabaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.drop_database_with_options(catalog_id, database, headers, runtime)

    async def drop_database_async(
        self,
        catalog_id: str,
        database: str,
    ) -> main_models.DropDatabaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.drop_database_with_options_async(catalog_id, database, headers, runtime)

    def drop_receiver_with_options(
        self,
        receiver: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropReceiverResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropReceiver',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers/{DaraURL.percent_encode(receiver)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_receiver_with_options_async(
        self,
        receiver: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropReceiverResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropReceiver',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers/{DaraURL.percent_encode(receiver)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropReceiverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_receiver(
        self,
        receiver: str,
    ) -> main_models.DropReceiverResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.drop_receiver_with_options(receiver, headers, runtime)

    async def drop_receiver_async(
        self,
        receiver: str,
    ) -> main_models.DropReceiverResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.drop_receiver_with_options_async(receiver, headers, runtime)

    def drop_share_with_options(
        self,
        share: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropShareResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropShare',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_share_with_options_async(
        self,
        share: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropShareResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropShare',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_share(
        self,
        share: str,
    ) -> main_models.DropShareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.drop_share_with_options(share, headers, runtime)

    async def drop_share_async(
        self,
        share: str,
    ) -> main_models.DropShareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.drop_share_with_options_async(share, headers, runtime)

    def drop_table_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def drop_table_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.DropTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'DropTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}',
            method = 'DELETE',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.DropTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def drop_table(
        self,
        catalog_id: str,
        database: str,
        table: str,
    ) -> main_models.DropTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.drop_table_with_options(catalog_id, database, table, headers, runtime)

    async def drop_table_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
    ) -> main_models.DropTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.drop_table_with_options_async(catalog_id, database, table, headers, runtime)

    def get_catalog_with_options(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCatalog',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/{DaraURL.percent_encode(catalog)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_with_options_async(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCatalog',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/{DaraURL.percent_encode(catalog)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog(
        self,
        catalog: str,
    ) -> main_models.GetCatalogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_catalog_with_options(catalog, headers, runtime)

    async def get_catalog_async(
        self,
        catalog: str,
    ) -> main_models.GetCatalogResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_catalog_with_options_async(catalog, headers, runtime)

    def get_catalog_by_id_with_options(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogByIdResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogById',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/id/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogByIdResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_by_id_with_options_async(
        self,
        id: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogByIdResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogById',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/id/{DaraURL.percent_encode(id)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogByIdResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog_by_id(
        self,
        id: str,
    ) -> main_models.GetCatalogByIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_catalog_by_id_with_options(id, headers, runtime)

    async def get_catalog_by_id_async(
        self,
        id: str,
    ) -> main_models.GetCatalogByIdResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_catalog_by_id_with_options_async(id, headers, runtime)

    def get_catalog_summary_with_options(
        self,
        catalog_id: str,
        request: main_models.GetCatalogSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogSummary',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/storage-summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_summary_with_options_async(
        self,
        catalog_id: str,
        request: main_models.GetCatalogSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogSummary',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/storage-summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog_summary(
        self,
        catalog_id: str,
        request: main_models.GetCatalogSummaryRequest,
    ) -> main_models.GetCatalogSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_catalog_summary_with_options(catalog_id, request, headers, runtime)

    async def get_catalog_summary_async(
        self,
        catalog_id: str,
        request: main_models.GetCatalogSummaryRequest,
    ) -> main_models.GetCatalogSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_catalog_summary_with_options_async(catalog_id, request, headers, runtime)

    def get_catalog_summary_trend_with_options(
        self,
        catalog_id: str,
        request: main_models.GetCatalogSummaryTrendRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogSummaryTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogSummaryTrend',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/storage-summary/trend',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogSummaryTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_summary_trend_with_options_async(
        self,
        catalog_id: str,
        request: main_models.GetCatalogSummaryTrendRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogSummaryTrendResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.end_date):
            query['endDate'] = request.end_date
        if not DaraCore.is_null(request.start_date):
            query['startDate'] = request.start_date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogSummaryTrend',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/storage-summary/trend',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogSummaryTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog_summary_trend(
        self,
        catalog_id: str,
        request: main_models.GetCatalogSummaryTrendRequest,
    ) -> main_models.GetCatalogSummaryTrendResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_catalog_summary_trend_with_options(catalog_id, request, headers, runtime)

    async def get_catalog_summary_trend_async(
        self,
        catalog_id: str,
        request: main_models.GetCatalogSummaryTrendRequest,
    ) -> main_models.GetCatalogSummaryTrendResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_catalog_summary_trend_with_options_async(catalog_id, request, headers, runtime)

    def get_catalog_token_with_options(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogTokenResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogToken',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/{DaraURL.percent_encode(catalog)}/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_catalog_token_with_options_async(
        self,
        catalog: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetCatalogTokenResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetCatalogToken',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs/{DaraURL.percent_encode(catalog)}/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetCatalogTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_catalog_token(
        self,
        catalog: str,
    ) -> main_models.GetCatalogTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_catalog_token_with_options(catalog, headers, runtime)

    async def get_catalog_token_async(
        self,
        catalog: str,
    ) -> main_models.GetCatalogTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_catalog_token_with_options_async(catalog, headers, runtime)

    def get_database_with_options(
        self,
        catalog_id: str,
        database: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDatabase',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_with_options_async(
        self,
        catalog_id: str,
        database: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetDatabase',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database(
        self,
        catalog_id: str,
        database: str,
    ) -> main_models.GetDatabaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_database_with_options(catalog_id, database, headers, runtime)

    async def get_database_async(
        self,
        catalog_id: str,
        database: str,
    ) -> main_models.GetDatabaseResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_database_with_options_async(catalog_id, database, headers, runtime)

    def get_database_summary_with_options(
        self,
        catalog_id: str,
        database: str,
        request: main_models.GetDatabaseSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabaseSummary',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/storage-summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_database_summary_with_options_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.GetDatabaseSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetDatabaseSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDatabaseSummary',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/storage-summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDatabaseSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_database_summary(
        self,
        catalog_id: str,
        database: str,
        request: main_models.GetDatabaseSummaryRequest,
    ) -> main_models.GetDatabaseSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_database_summary_with_options(catalog_id, database, request, headers, runtime)

    async def get_database_summary_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.GetDatabaseSummaryRequest,
    ) -> main_models.GetDatabaseSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_database_summary_with_options_async(catalog_id, database, request, headers, runtime)

    def get_iceberg_namespace_with_options(
        self,
        catalog_id: str,
        namespace: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIcebergNamespaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIcebergNamespace',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespaces/{DaraURL.percent_encode(namespace)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIcebergNamespaceResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_iceberg_namespace_with_options_async(
        self,
        catalog_id: str,
        namespace: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIcebergNamespaceResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIcebergNamespace',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespaces/{DaraURL.percent_encode(namespace)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIcebergNamespaceResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_iceberg_namespace(
        self,
        catalog_id: str,
        namespace: str,
    ) -> main_models.GetIcebergNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_iceberg_namespace_with_options(catalog_id, namespace, headers, runtime)

    async def get_iceberg_namespace_async(
        self,
        catalog_id: str,
        namespace: str,
    ) -> main_models.GetIcebergNamespaceResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_iceberg_namespace_with_options_async(catalog_id, namespace, headers, runtime)

    def get_iceberg_table_with_options(
        self,
        catalog_id: str,
        namespace: str,
        table: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIcebergTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIcebergTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespaces/{DaraURL.percent_encode(namespace)}/tables/{DaraURL.percent_encode(table)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIcebergTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_iceberg_table_with_options_async(
        self,
        catalog_id: str,
        namespace: str,
        table: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetIcebergTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetIcebergTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespaces/{DaraURL.percent_encode(namespace)}/tables/{DaraURL.percent_encode(table)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetIcebergTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_iceberg_table(
        self,
        catalog_id: str,
        namespace: str,
        table: str,
    ) -> main_models.GetIcebergTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_iceberg_table_with_options(catalog_id, namespace, table, headers, runtime)

    async def get_iceberg_table_async(
        self,
        catalog_id: str,
        namespace: str,
        table: str,
    ) -> main_models.GetIcebergTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_iceberg_table_with_options_async(catalog_id, namespace, table, headers, runtime)

    def get_receiver_with_options(
        self,
        receiver: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetReceiverResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetReceiver',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers/{DaraURL.percent_encode(receiver)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReceiverResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_receiver_with_options_async(
        self,
        receiver: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetReceiverResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetReceiver',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers/{DaraURL.percent_encode(receiver)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetReceiverResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_receiver(
        self,
        receiver: str,
    ) -> main_models.GetReceiverResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_receiver_with_options(receiver, headers, runtime)

    async def get_receiver_async(
        self,
        receiver: str,
    ) -> main_models.GetReceiverResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_receiver_with_options_async(receiver, headers, runtime)

    def get_region_status_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegionStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegionStatus',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/service/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_region_status_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRegionStatusResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetRegionStatus',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/service/status',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetRegionStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_region_status(self) -> main_models.GetRegionStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_region_status_with_options(headers, runtime)

    async def get_region_status_async(self) -> main_models.GetRegionStatusResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_region_status_with_options_async(headers, runtime)

    def get_role_with_options(
        self,
        request: main_models.GetRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles',
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
        request: main_models.GetRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetRoleResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetRole',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles',
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
        request: main_models.GetRoleRequest,
    ) -> main_models.GetRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_role_with_options(request, headers, runtime)

    async def get_role_async(
        self,
        request: main_models.GetRoleRequest,
    ) -> main_models.GetRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_role_with_options_async(request, headers, runtime)

    def get_share_with_options(
        self,
        share: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetShareResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetShare',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShareResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_share_with_options_async(
        self,
        share: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetShareResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetShare',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetShareResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_share(
        self,
        share: str,
    ) -> main_models.GetShareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_share_with_options(share, headers, runtime)

    async def get_share_async(
        self,
        share: str,
    ) -> main_models.GetShareResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_share_with_options_async(share, headers, runtime)

    def get_table_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table(
        self,
        catalog_id: str,
        database: str,
        table: str,
    ) -> main_models.GetTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_table_with_options(catalog_id, database, table, headers, runtime)

    async def get_table_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
    ) -> main_models.GetTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_table_with_options_async(catalog_id, database, table, headers, runtime)

    def get_table_snapshot_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableSnapshotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTableSnapshot',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/snapshot',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_snapshot_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableSnapshotResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'GetTableSnapshot',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/snapshot',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableSnapshotResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_snapshot(
        self,
        catalog_id: str,
        database: str,
        table: str,
    ) -> main_models.GetTableSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_table_snapshot_with_options(catalog_id, database, table, headers, runtime)

    async def get_table_snapshot_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
    ) -> main_models.GetTableSnapshotResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_table_snapshot_with_options_async(catalog_id, database, table, headers, runtime)

    def get_table_summary_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.GetTableSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableSummary',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/storage-summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_summary_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.GetTableSummaryRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableSummaryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.date):
            query['date'] = request.date
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableSummary',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/storage-summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableSummaryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_summary(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.GetTableSummaryRequest,
    ) -> main_models.GetTableSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_table_summary_with_options(catalog_id, database, table, request, headers, runtime)

    async def get_table_summary_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.GetTableSummaryRequest,
    ) -> main_models.GetTableSummaryResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_table_summary_with_options_async(catalog_id, database, table, request, headers, runtime)

    def get_table_token_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.GetTableTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_internal):
            query['isInternal'] = request.is_internal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableToken',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableTokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_table_token_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.GetTableTokenRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetTableTokenResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.is_internal):
            query['isInternal'] = request.is_internal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetTableToken',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/token',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetTableTokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_table_token(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.GetTableTokenRequest,
    ) -> main_models.GetTableTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_table_token_with_options(catalog_id, database, table, request, headers, runtime)

    async def get_table_token_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.GetTableTokenRequest,
    ) -> main_models.GetTableTokenResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_table_token_with_options_async(catalog_id, database, table, request, headers, runtime)

    def get_user_with_options(
        self,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal):
            query['userPrincipal'] = request.user_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_user_with_options_async(
        self,
        request: main_models.GetUserRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GetUserResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.user_principal):
            query['userPrincipal'] = request.user_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetUser',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/users',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetUserResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_user(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.get_user_with_options(request, headers, runtime)

    async def get_user_async(
        self,
        request: main_models.GetUserRequest,
    ) -> main_models.GetUserResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.get_user_with_options_async(request, headers, runtime)

    def grant_role_to_users_with_options(
        self,
        request: main_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantRoleToUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not DaraCore.is_null(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantRoleToUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/grant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.GrantRoleToUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def grant_role_to_users_with_options_async(
        self,
        request: main_models.GrantRoleToUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.GrantRoleToUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not DaraCore.is_null(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'GrantRoleToUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/grant',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.GrantRoleToUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def grant_role_to_users(
        self,
        request: main_models.GrantRoleToUsersRequest,
    ) -> main_models.GrantRoleToUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.grant_role_to_users_with_options(request, headers, runtime)

    async def grant_role_to_users_async(
        self,
        request: main_models.GrantRoleToUsersRequest,
    ) -> main_models.GrantRoleToUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.grant_role_to_users_with_options_async(request, headers, runtime)

    def list_catalogs_with_options(
        self,
        request: main_models.ListCatalogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name_pattern):
            query['catalogNamePattern'] = request.catalog_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCatalogs',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_catalogs_with_options_async(
        self,
        request: main_models.ListCatalogsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListCatalogsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.catalog_name_pattern):
            query['catalogNamePattern'] = request.catalog_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListCatalogs',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/catalogs',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListCatalogsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_catalogs(
        self,
        request: main_models.ListCatalogsRequest,
    ) -> main_models.ListCatalogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_catalogs_with_options(request, headers, runtime)

    async def list_catalogs_async(
        self,
        request: main_models.ListCatalogsRequest,
    ) -> main_models.ListCatalogsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_catalogs_with_options_async(request, headers, runtime)

    def list_database_details_with_options(
        self,
        catalog_id: str,
        request: main_models.ListDatabaseDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_name_pattern):
            query['databaseNamePattern'] = request.database_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseDetails',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/database-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_database_details_with_options_async(
        self,
        catalog_id: str,
        request: main_models.ListDatabaseDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabaseDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_name_pattern):
            query['databaseNamePattern'] = request.database_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabaseDetails',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/database-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabaseDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_database_details(
        self,
        catalog_id: str,
        request: main_models.ListDatabaseDetailsRequest,
    ) -> main_models.ListDatabaseDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_database_details_with_options(catalog_id, request, headers, runtime)

    async def list_database_details_async(
        self,
        catalog_id: str,
        request: main_models.ListDatabaseDetailsRequest,
    ) -> main_models.ListDatabaseDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_database_details_with_options_async(catalog_id, request, headers, runtime)

    def list_databases_with_options(
        self,
        catalog_id: str,
        request: main_models.ListDatabasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_name_pattern):
            query['databaseNamePattern'] = request.database_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_databases_with_options_async(
        self,
        catalog_id: str,
        request: main_models.ListDatabasesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListDatabasesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database_name_pattern):
            query['databaseNamePattern'] = request.database_name_pattern
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDatabases',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDatabasesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_databases(
        self,
        catalog_id: str,
        request: main_models.ListDatabasesRequest,
    ) -> main_models.ListDatabasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_databases_with_options(catalog_id, request, headers, runtime)

    async def list_databases_async(
        self,
        catalog_id: str,
        request: main_models.ListDatabasesRequest,
    ) -> main_models.ListDatabasesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_databases_with_options_async(catalog_id, request, headers, runtime)

    def list_iceberg_namespace_details_with_options(
        self,
        catalog_id: str,
        request: main_models.ListIcebergNamespaceDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIcebergNamespaceDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.namespace_name_pattern):
            query['namespaceNamePattern'] = request.namespace_name_pattern
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIcebergNamespaceDetails',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespace-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIcebergNamespaceDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_iceberg_namespace_details_with_options_async(
        self,
        catalog_id: str,
        request: main_models.ListIcebergNamespaceDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIcebergNamespaceDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.namespace_name_pattern):
            query['namespaceNamePattern'] = request.namespace_name_pattern
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIcebergNamespaceDetails',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespace-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIcebergNamespaceDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_iceberg_namespace_details(
        self,
        catalog_id: str,
        request: main_models.ListIcebergNamespaceDetailsRequest,
    ) -> main_models.ListIcebergNamespaceDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_iceberg_namespace_details_with_options(catalog_id, request, headers, runtime)

    async def list_iceberg_namespace_details_async(
        self,
        catalog_id: str,
        request: main_models.ListIcebergNamespaceDetailsRequest,
    ) -> main_models.ListIcebergNamespaceDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_iceberg_namespace_details_with_options_async(catalog_id, request, headers, runtime)

    def list_iceberg_snapshots_with_options(
        self,
        catalog_id: str,
        namespace: str,
        table: str,
        request: main_models.ListIcebergSnapshotsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIcebergSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIcebergSnapshots',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespaces/{DaraURL.percent_encode(namespace)}/tables/{DaraURL.percent_encode(table)}/snapshots',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIcebergSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_iceberg_snapshots_with_options_async(
        self,
        catalog_id: str,
        namespace: str,
        table: str,
        request: main_models.ListIcebergSnapshotsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIcebergSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIcebergSnapshots',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespaces/{DaraURL.percent_encode(namespace)}/tables/{DaraURL.percent_encode(table)}/snapshots',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIcebergSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_iceberg_snapshots(
        self,
        catalog_id: str,
        namespace: str,
        table: str,
        request: main_models.ListIcebergSnapshotsRequest,
    ) -> main_models.ListIcebergSnapshotsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_iceberg_snapshots_with_options(catalog_id, namespace, table, request, headers, runtime)

    async def list_iceberg_snapshots_async(
        self,
        catalog_id: str,
        namespace: str,
        table: str,
        request: main_models.ListIcebergSnapshotsRequest,
    ) -> main_models.ListIcebergSnapshotsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_iceberg_snapshots_with_options_async(catalog_id, namespace, table, request, headers, runtime)

    def list_iceberg_table_details_with_options(
        self,
        catalog_id: str,
        namespace: str,
        request: main_models.ListIcebergTableDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIcebergTableDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['tableNamePattern'] = request.table_name_pattern
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIcebergTableDetails',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespaces/{DaraURL.percent_encode(namespace)}/table-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIcebergTableDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_iceberg_table_details_with_options_async(
        self,
        catalog_id: str,
        namespace: str,
        request: main_models.ListIcebergTableDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListIcebergTableDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['tableNamePattern'] = request.table_name_pattern
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListIcebergTableDetails',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/iceberg/dlf/v1/{DaraURL.percent_encode(catalog_id)}/namespaces/{DaraURL.percent_encode(namespace)}/table-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListIcebergTableDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_iceberg_table_details(
        self,
        catalog_id: str,
        namespace: str,
        request: main_models.ListIcebergTableDetailsRequest,
    ) -> main_models.ListIcebergTableDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_iceberg_table_details_with_options(catalog_id, namespace, request, headers, runtime)

    async def list_iceberg_table_details_async(
        self,
        catalog_id: str,
        namespace: str,
        request: main_models.ListIcebergTableDetailsRequest,
    ) -> main_models.ListIcebergTableDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_iceberg_table_details_with_options_async(catalog_id, namespace, request, headers, runtime)

    def list_partition_summaries_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListPartitionSummariesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPartitionSummariesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.partition_name_pattern):
            query['partitionNamePattern'] = request.partition_name_pattern
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPartitionSummaries',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/partitions/storage-summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPartitionSummariesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_partition_summaries_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListPartitionSummariesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPartitionSummariesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.partition_name_pattern):
            query['partitionNamePattern'] = request.partition_name_pattern
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPartitionSummaries',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/partitions/storage-summary',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPartitionSummariesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_partition_summaries(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListPartitionSummariesRequest,
    ) -> main_models.ListPartitionSummariesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_partition_summaries_with_options(catalog_id, database, table, request, headers, runtime)

    async def list_partition_summaries_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListPartitionSummariesRequest,
    ) -> main_models.ListPartitionSummariesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_partition_summaries_with_options_async(catalog_id, database, table, request, headers, runtime)

    def list_partitions_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListPartitionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPartitionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.partition_name_pattern):
            query['partitionNamePattern'] = request.partition_name_pattern
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPartitions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/partitions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPartitionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_partitions_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListPartitionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPartitionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.partition_name_pattern):
            query['partitionNamePattern'] = request.partition_name_pattern
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPartitions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/partitions',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPartitionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_partitions(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListPartitionsRequest,
    ) -> main_models.ListPartitionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_partitions_with_options(catalog_id, database, table, request, headers, runtime)

    async def list_partitions_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListPartitionsRequest,
    ) -> main_models.ListPartitionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_partitions_with_options_async(catalog_id, database, table, request, headers, runtime)

    def list_permissions_with_options(
        self,
        catalog_id: str,
        request: main_models.ListPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database):
            query['database'] = request.database
        if not DaraCore.is_null(request.function):
            query['function'] = request.function
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.principal):
            query['principal'] = request.principal
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.table):
            query['table'] = request.table
        if not DaraCore.is_null(request.view):
            query['view'] = request.view
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/permissions/{DaraURL.percent_encode(catalog_id)}/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_permissions_with_options_async(
        self,
        catalog_id: str,
        request: main_models.ListPermissionsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListPermissionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.database):
            query['database'] = request.database
        if not DaraCore.is_null(request.function):
            query['function'] = request.function
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.principal):
            query['principal'] = request.principal
        if not DaraCore.is_null(request.resource_type):
            query['resourceType'] = request.resource_type
        if not DaraCore.is_null(request.table):
            query['table'] = request.table
        if not DaraCore.is_null(request.view):
            query['view'] = request.view
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListPermissions',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/permissions/{DaraURL.percent_encode(catalog_id)}/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListPermissionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_permissions(
        self,
        catalog_id: str,
        request: main_models.ListPermissionsRequest,
    ) -> main_models.ListPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_permissions_with_options(catalog_id, request, headers, runtime)

    async def list_permissions_async(
        self,
        catalog_id: str,
        request: main_models.ListPermissionsRequest,
    ) -> main_models.ListPermissionsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_permissions_with_options_async(catalog_id, request, headers, runtime)

    def list_provided_shares_with_options(
        self,
        request: main_models.ListProvidedSharesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProvidedSharesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvidedShares',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/list/provided',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvidedSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_provided_shares_with_options_async(
        self,
        request: main_models.ListProvidedSharesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListProvidedSharesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListProvidedShares',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/list/provided',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListProvidedSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_provided_shares(
        self,
        request: main_models.ListProvidedSharesRequest,
    ) -> main_models.ListProvidedSharesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_provided_shares_with_options(request, headers, runtime)

    async def list_provided_shares_async(
        self,
        request: main_models.ListProvidedSharesRequest,
    ) -> main_models.ListProvidedSharesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_provided_shares_with_options_async(request, headers, runtime)

    def list_received_shares_with_options(
        self,
        request: main_models.ListReceivedSharesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReceivedSharesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReceivedShares',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/list/received',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReceivedSharesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_received_shares_with_options_async(
        self,
        request: main_models.ListReceivedSharesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReceivedSharesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReceivedShares',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/list/received',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReceivedSharesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_received_shares(
        self,
        request: main_models.ListReceivedSharesRequest,
    ) -> main_models.ListReceivedSharesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_received_shares_with_options(request, headers, runtime)

    async def list_received_shares_async(
        self,
        request: main_models.ListReceivedSharesRequest,
    ) -> main_models.ListReceivedSharesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_received_shares_with_options_async(request, headers, runtime)

    def list_receivers_with_options(
        self,
        request: main_models.ListReceiversRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReceiversResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.receiver_name):
            query['receiverName'] = request.receiver_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReceivers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReceiversResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_receivers_with_options_async(
        self,
        request: main_models.ListReceiversRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListReceiversResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.receiver_name):
            query['receiverName'] = request.receiver_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListReceivers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/receivers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListReceiversResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_receivers(
        self,
        request: main_models.ListReceiversRequest,
    ) -> main_models.ListReceiversResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_receivers_with_options(request, headers, runtime)

    async def list_receivers_async(
        self,
        request: main_models.ListReceiversRequest,
    ) -> main_models.ListReceiversResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_receivers_with_options_async(request, headers, runtime)

    def list_role_users_with_options(
        self,
        request: main_models.ListRoleUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRoleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoleUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/users/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_role_users_with_options_async(
        self,
        request: main_models.ListRoleUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRoleUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.role_principal):
            query['rolePrincipal'] = request.role_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoleUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/users/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_role_users(
        self,
        request: main_models.ListRoleUsersRequest,
    ) -> main_models.ListRoleUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_role_users_with_options(request, headers, runtime)

    async def list_role_users_async(
        self,
        request: main_models.ListRoleUsersRequest,
    ) -> main_models.ListRoleUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_role_users_with_options_async(request, headers, runtime)

    def list_roles_with_options(
        self,
        request: main_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.role_name):
            query['roleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/list',
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
        request: main_models.ListRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.role_name):
            query['roleName'] = request.role_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListRoles',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/list',
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

    def list_share_receivers_with_options(
        self,
        share: str,
        request: main_models.ListShareReceiversRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShareReceiversResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListShareReceivers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}/receivers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListShareReceiversResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_share_receivers_with_options_async(
        self,
        share: str,
        request: main_models.ListShareReceiversRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShareReceiversResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListShareReceivers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}/receivers',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListShareReceiversResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_share_receivers(
        self,
        share: str,
        request: main_models.ListShareReceiversRequest,
    ) -> main_models.ListShareReceiversResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_share_receivers_with_options(share, request, headers, runtime)

    async def list_share_receivers_async(
        self,
        share: str,
        request: main_models.ListShareReceiversRequest,
    ) -> main_models.ListShareReceiversResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_share_receivers_with_options_async(share, request, headers, runtime)

    def list_share_resources_with_options(
        self,
        share: str,
        request: main_models.ListShareResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShareResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListShareResources',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListShareResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_share_resources_with_options_async(
        self,
        share: str,
        request: main_models.ListShareResourcesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListShareResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListShareResources',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/share/shares/{DaraURL.percent_encode(share)}/resources',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListShareResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_share_resources(
        self,
        share: str,
        request: main_models.ListShareResourcesRequest,
    ) -> main_models.ListShareResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_share_resources_with_options(share, request, headers, runtime)

    async def list_share_resources_async(
        self,
        share: str,
        request: main_models.ListShareResourcesRequest,
    ) -> main_models.ListShareResourcesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_share_resources_with_options_async(share, request, headers, runtime)

    def list_snapshots_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListSnapshotsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSnapshots',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/snapshots',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSnapshotsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_snapshots_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListSnapshotsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListSnapshotsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSnapshots',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/snapshots',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSnapshotsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_snapshots(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListSnapshotsRequest,
    ) -> main_models.ListSnapshotsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_snapshots_with_options(catalog_id, database, table, request, headers, runtime)

    async def list_snapshots_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.ListSnapshotsRequest,
    ) -> main_models.ListSnapshotsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_snapshots_with_options_async(catalog_id, database, table, request, headers, runtime)

    def list_table_details_with_options(
        self,
        catalog_id: str,
        database: str,
        request: main_models.ListTableDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTableDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['tableNamePattern'] = request.table_name_pattern
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTableDetails',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/table-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTableDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_table_details_with_options_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.ListTableDetailsRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTableDetailsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['tableNamePattern'] = request.table_name_pattern
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTableDetails',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/table-details',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTableDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_table_details(
        self,
        catalog_id: str,
        database: str,
        request: main_models.ListTableDetailsRequest,
    ) -> main_models.ListTableDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_table_details_with_options(catalog_id, database, request, headers, runtime)

    async def list_table_details_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.ListTableDetailsRequest,
    ) -> main_models.ListTableDetailsResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_table_details_with_options_async(catalog_id, database, request, headers, runtime)

    def list_tables_with_options(
        self,
        catalog_id: str,
        database: str,
        request: main_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['tableNamePattern'] = request.table_name_pattern
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tables_with_options_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.ListTablesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListTablesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.table_name_pattern):
            query['tableNamePattern'] = request.table_name_pattern
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTables',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTablesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tables(
        self,
        catalog_id: str,
        database: str,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_tables_with_options(catalog_id, database, request, headers, runtime)

    async def list_tables_async(
        self,
        catalog_id: str,
        database: str,
        request: main_models.ListTablesRequest,
    ) -> main_models.ListTablesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_tables_with_options_async(catalog_id, database, request, headers, runtime)

    def list_user_roles_with_options(
        self,
        request: main_models.ListUserRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.user_principal):
            query['userPrincipal'] = request.user_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserRoles',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/users/roles/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserRolesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_user_roles_with_options_async(
        self,
        request: main_models.ListUserRolesRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUserRolesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.user_principal):
            query['userPrincipal'] = request.user_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUserRoles',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/users/roles/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUserRolesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_user_roles(
        self,
        request: main_models.ListUserRolesRequest,
    ) -> main_models.ListUserRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_user_roles_with_options(request, headers, runtime)

    async def list_user_roles_async(
        self,
        request: main_models.ListUserRolesRequest,
    ) -> main_models.ListUserRolesResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_user_roles_with_options_async(request, headers, runtime)

    def list_users_with_options(
        self,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.user_name):
            query['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/users/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_users_with_options_async(
        self,
        request: main_models.ListUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.ListUsersResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['maxResults'] = request.max_results
        if not DaraCore.is_null(request.page_token):
            query['pageToken'] = request.page_token
        if not DaraCore.is_null(request.type):
            query['type'] = request.type
        if not DaraCore.is_null(request.user_name):
            query['userName'] = request.user_name
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/users/list',
            method = 'GET',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_users(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.list_users_with_options(request, headers, runtime)

    async def list_users_async(
        self,
        request: main_models.ListUsersRequest,
    ) -> main_models.ListUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.list_users_with_options_async(request, headers, runtime)

    def refresh_user_sync_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RefreshUserSyncResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RefreshUserSync',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/usersync',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RefreshUserSyncResponse(),
            self.call_api(params, req, runtime)
        )

    async def refresh_user_sync_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RefreshUserSyncResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'RefreshUserSync',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/usersync',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RefreshUserSyncResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def refresh_user_sync(self) -> main_models.RefreshUserSyncResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.refresh_user_sync_with_options(headers, runtime)

    async def refresh_user_sync_async(self) -> main_models.RefreshUserSyncResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.refresh_user_sync_with_options_async(headers, runtime)

    def revoke_role_from_users_with_options(
        self,
        request: main_models.RevokeRoleFromUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeRoleFromUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not DaraCore.is_null(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeRoleFromUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/revoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RevokeRoleFromUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def revoke_role_from_users_with_options_async(
        self,
        request: main_models.RevokeRoleFromUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RevokeRoleFromUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not DaraCore.is_null(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RevokeRoleFromUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/revoke',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RevokeRoleFromUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def revoke_role_from_users(
        self,
        request: main_models.RevokeRoleFromUsersRequest,
    ) -> main_models.RevokeRoleFromUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.revoke_role_from_users_with_options(request, headers, runtime)

    async def revoke_role_from_users_async(
        self,
        request: main_models.RevokeRoleFromUsersRequest,
    ) -> main_models.RevokeRoleFromUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.revoke_role_from_users_with_options_async(request, headers, runtime)

    def rollback_table_with_options(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.RollbackTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instant):
            body['instant'] = request.instant
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RollbackTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/rollback',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RollbackTableResponse(),
            self.call_api(params, req, runtime)
        )

    async def rollback_table_with_options_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.RollbackTableRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.RollbackTableResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.instant):
            body['instant'] = request.instant
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'RollbackTable',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/{DaraURL.percent_encode(catalog_id)}/databases/{DaraURL.percent_encode(database)}/tables/{DaraURL.percent_encode(table)}/rollback',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.RollbackTableResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rollback_table(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.RollbackTableRequest,
    ) -> main_models.RollbackTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.rollback_table_with_options(catalog_id, database, table, request, headers, runtime)

    async def rollback_table_async(
        self,
        catalog_id: str,
        database: str,
        table: str,
        request: main_models.RollbackTableRequest,
    ) -> main_models.RollbackTableResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.rollback_table_with_options_async(catalog_id, database, table, request, headers, runtime)

    def subscribe_with_options(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubscribeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'Subscribe',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/service/subscribe',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.SubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    async def subscribe_with_options_async(
        self,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.SubscribeResponse:
        req = open_api_util_models.OpenApiRequest(
            headers = headers
        )
        params = open_api_util_models.Params(
            action = 'Subscribe',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/service/subscribe',
            method = 'POST',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.SubscribeResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def subscribe(self) -> main_models.SubscribeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.subscribe_with_options(headers, runtime)

    async def subscribe_async(self) -> main_models.SubscribeResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.subscribe_with_options_async(headers, runtime)

    def update_role_with_options(
        self,
        request: main_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_with_options_async(
        self,
        request: main_models.UpdateRoleRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.description):
            body['description'] = request.description
        if not DaraCore.is_null(request.display_name):
            body['displayName'] = request.display_name
        if not DaraCore.is_null(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRole',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role(
        self,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_role_with_options(request, headers, runtime)

    async def update_role_async(
        self,
        request: main_models.UpdateRoleRequest,
    ) -> main_models.UpdateRoleResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_role_with_options_async(request, headers, runtime)

    def update_role_users_with_options(
        self,
        request: main_models.UpdateRoleUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not DaraCore.is_null(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRoleUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/users',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleUsersResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_role_users_with_options_async(
        self,
        request: main_models.UpdateRoleUsersRequest,
        headers: Dict[str, str],
        runtime: RuntimeOptions,
    ) -> main_models.UpdateRoleUsersResponse:
        request.validate()
        body = {}
        if not DaraCore.is_null(request.role_principal):
            body['rolePrincipal'] = request.role_principal
        if not DaraCore.is_null(request.user_principals):
            body['userPrincipals'] = request.user_principals
        req = open_api_util_models.OpenApiRequest(
            headers = headers,
            body = Utils.parse_to_map(body)
        )
        params = open_api_util_models.Params(
            action = 'UpdateRoleUsers',
            version = '2025-03-10',
            protocol = 'HTTPS',
            pathname = f'/dlf/v1/auth/roles/users',
            method = 'PUT',
            auth_type = 'AK',
            style = 'ROA',
            req_body_type = 'json',
            body_type = 'none'
        )
        return DaraCore.from_map(
            main_models.UpdateRoleUsersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_role_users(
        self,
        request: main_models.UpdateRoleUsersRequest,
    ) -> main_models.UpdateRoleUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return self.update_role_users_with_options(request, headers, runtime)

    async def update_role_users_async(
        self,
        request: main_models.UpdateRoleUsersRequest,
    ) -> main_models.UpdateRoleUsersResponse:
        runtime = RuntimeOptions()
        headers = {}
        return await self.update_role_users_with_options_async(request, headers, runtime)
