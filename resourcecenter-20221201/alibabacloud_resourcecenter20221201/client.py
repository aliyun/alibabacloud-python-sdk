# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_resourcecenter20221201 import models as main_models
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
        self._endpoint = self.get_endpoint('resourcecenter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def associate_default_filter_with_options(
        self,
        request: main_models.AssociateDefaultFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateDefaultFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateDefaultFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateDefaultFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def associate_default_filter_with_options_async(
        self,
        request: main_models.AssociateDefaultFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AssociateDefaultFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AssociateDefaultFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AssociateDefaultFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def associate_default_filter(
        self,
        request: main_models.AssociateDefaultFilterRequest,
    ) -> main_models.AssociateDefaultFilterResponse:
        runtime = RuntimeOptions()
        return self.associate_default_filter_with_options(request, runtime)

    async def associate_default_filter_async(
        self,
        request: main_models.AssociateDefaultFilterRequest,
    ) -> main_models.AssociateDefaultFilterResponse:
        runtime = RuntimeOptions()
        return await self.associate_default_filter_with_options_async(request, runtime)

    def batch_get_resource_configurations_with_options(
        self,
        request: main_models.BatchGetResourceConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetResourceConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetResourceConfigurations',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetResourceConfigurationsResponse(),
            self.call_api(params, req, runtime)
        )

    async def batch_get_resource_configurations_with_options_async(
        self,
        request: main_models.BatchGetResourceConfigurationsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.BatchGetResourceConfigurationsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resources):
            query['Resources'] = request.resources
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'BatchGetResourceConfigurations',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.BatchGetResourceConfigurationsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def batch_get_resource_configurations(
        self,
        request: main_models.BatchGetResourceConfigurationsRequest,
    ) -> main_models.BatchGetResourceConfigurationsResponse:
        runtime = RuntimeOptions()
        return self.batch_get_resource_configurations_with_options(request, runtime)

    async def batch_get_resource_configurations_async(
        self,
        request: main_models.BatchGetResourceConfigurationsRequest,
    ) -> main_models.BatchGetResourceConfigurationsResponse:
        runtime = RuntimeOptions()
        return await self.batch_get_resource_configurations_with_options_async(request, runtime)

    def create_delivery_channel_with_options(
        self,
        request: main_models.CreateDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_description):
            query['DeliveryChannelDescription'] = request.delivery_channel_description
        if not DaraCore.is_null(request.delivery_channel_filter):
            query['DeliveryChannelFilter'] = request.delivery_channel_filter
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.resource_change_delivery):
            query['ResourceChangeDelivery'] = request.resource_change_delivery
        if not DaraCore.is_null(request.resource_snapshot_delivery):
            query['ResourceSnapshotDelivery'] = request.resource_snapshot_delivery
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_delivery_channel_with_options_async(
        self,
        request: main_models.CreateDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_description):
            query['DeliveryChannelDescription'] = request.delivery_channel_description
        if not DaraCore.is_null(request.delivery_channel_filter):
            query['DeliveryChannelFilter'] = request.delivery_channel_filter
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.resource_change_delivery):
            query['ResourceChangeDelivery'] = request.resource_change_delivery
        if not DaraCore.is_null(request.resource_snapshot_delivery):
            query['ResourceSnapshotDelivery'] = request.resource_snapshot_delivery
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_delivery_channel(
        self,
        request: main_models.CreateDeliveryChannelRequest,
    ) -> main_models.CreateDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.create_delivery_channel_with_options(request, runtime)

    async def create_delivery_channel_async(
        self,
        request: main_models.CreateDeliveryChannelRequest,
    ) -> main_models.CreateDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.create_delivery_channel_with_options_async(request, runtime)

    def create_filter_with_options(
        self,
        request: main_models.CreateFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_configuration):
            query['FilterConfiguration'] = request.filter_configuration
        if not DaraCore.is_null(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_filter_with_options_async(
        self,
        request: main_models.CreateFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_configuration):
            query['FilterConfiguration'] = request.filter_configuration
        if not DaraCore.is_null(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_filter(
        self,
        request: main_models.CreateFilterRequest,
    ) -> main_models.CreateFilterResponse:
        runtime = RuntimeOptions()
        return self.create_filter_with_options(request, runtime)

    async def create_filter_async(
        self,
        request: main_models.CreateFilterRequest,
    ) -> main_models.CreateFilterResponse:
        runtime = RuntimeOptions()
        return await self.create_filter_with_options_async(request, runtime)

    def create_multi_account_delivery_channel_with_options(
        self,
        request: main_models.CreateMultiAccountDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultiAccountDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_description):
            query['DeliveryChannelDescription'] = request.delivery_channel_description
        if not DaraCore.is_null(request.delivery_channel_filter):
            query['DeliveryChannelFilter'] = request.delivery_channel_filter
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.resource_change_delivery):
            query['ResourceChangeDelivery'] = request.resource_change_delivery
        if not DaraCore.is_null(request.resource_snapshot_delivery):
            query['ResourceSnapshotDelivery'] = request.resource_snapshot_delivery
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultiAccountDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultiAccountDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_multi_account_delivery_channel_with_options_async(
        self,
        request: main_models.CreateMultiAccountDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateMultiAccountDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_description):
            query['DeliveryChannelDescription'] = request.delivery_channel_description
        if not DaraCore.is_null(request.delivery_channel_filter):
            query['DeliveryChannelFilter'] = request.delivery_channel_filter
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.resource_change_delivery):
            query['ResourceChangeDelivery'] = request.resource_change_delivery
        if not DaraCore.is_null(request.resource_snapshot_delivery):
            query['ResourceSnapshotDelivery'] = request.resource_snapshot_delivery
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateMultiAccountDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateMultiAccountDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_multi_account_delivery_channel(
        self,
        request: main_models.CreateMultiAccountDeliveryChannelRequest,
    ) -> main_models.CreateMultiAccountDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.create_multi_account_delivery_channel_with_options(request, runtime)

    async def create_multi_account_delivery_channel_async(
        self,
        request: main_models.CreateMultiAccountDeliveryChannelRequest,
    ) -> main_models.CreateMultiAccountDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.create_multi_account_delivery_channel_with_options_async(request, runtime)

    def create_saved_query_with_options(
        self,
        request: main_models.CreateSavedQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSavedQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSavedQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSavedQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_saved_query_with_options_async(
        self,
        request: main_models.CreateSavedQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateSavedQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateSavedQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateSavedQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_saved_query(
        self,
        request: main_models.CreateSavedQueryRequest,
    ) -> main_models.CreateSavedQueryResponse:
        runtime = RuntimeOptions()
        return self.create_saved_query_with_options(request, runtime)

    async def create_saved_query_async(
        self,
        request: main_models.CreateSavedQueryRequest,
    ) -> main_models.CreateSavedQueryResponse:
        runtime = RuntimeOptions()
        return await self.create_saved_query_with_options_async(request, runtime)

    def delete_delivery_channel_with_options(
        self,
        request: main_models.DeleteDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_delivery_channel_with_options_async(
        self,
        request: main_models.DeleteDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_delivery_channel(
        self,
        request: main_models.DeleteDeliveryChannelRequest,
    ) -> main_models.DeleteDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.delete_delivery_channel_with_options(request, runtime)

    async def delete_delivery_channel_async(
        self,
        request: main_models.DeleteDeliveryChannelRequest,
    ) -> main_models.DeleteDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.delete_delivery_channel_with_options_async(request, runtime)

    def delete_filter_with_options(
        self,
        request: main_models.DeleteFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_filter_with_options_async(
        self,
        request: main_models.DeleteFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_filter(
        self,
        request: main_models.DeleteFilterRequest,
    ) -> main_models.DeleteFilterResponse:
        runtime = RuntimeOptions()
        return self.delete_filter_with_options(request, runtime)

    async def delete_filter_async(
        self,
        request: main_models.DeleteFilterRequest,
    ) -> main_models.DeleteFilterResponse:
        runtime = RuntimeOptions()
        return await self.delete_filter_with_options_async(request, runtime)

    def delete_multi_account_delivery_channel_with_options(
        self,
        request: main_models.DeleteMultiAccountDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultiAccountDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultiAccountDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultiAccountDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_multi_account_delivery_channel_with_options_async(
        self,
        request: main_models.DeleteMultiAccountDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteMultiAccountDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteMultiAccountDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteMultiAccountDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_multi_account_delivery_channel(
        self,
        request: main_models.DeleteMultiAccountDeliveryChannelRequest,
    ) -> main_models.DeleteMultiAccountDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.delete_multi_account_delivery_channel_with_options(request, runtime)

    async def delete_multi_account_delivery_channel_async(
        self,
        request: main_models.DeleteMultiAccountDeliveryChannelRequest,
    ) -> main_models.DeleteMultiAccountDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.delete_multi_account_delivery_channel_with_options_async(request, runtime)

    def delete_saved_query_with_options(
        self,
        request: main_models.DeleteSavedQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSavedQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSavedQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSavedQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_saved_query_with_options_async(
        self,
        request: main_models.DeleteSavedQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteSavedQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteSavedQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteSavedQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_saved_query(
        self,
        request: main_models.DeleteSavedQueryRequest,
    ) -> main_models.DeleteSavedQueryResponse:
        runtime = RuntimeOptions()
        return self.delete_saved_query_with_options(request, runtime)

    async def delete_saved_query_async(
        self,
        request: main_models.DeleteSavedQueryRequest,
    ) -> main_models.DeleteSavedQueryResponse:
        runtime = RuntimeOptions()
        return await self.delete_saved_query_with_options_async(request, runtime)

    def disable_multi_account_resource_center_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableMultiAccountResourceCenterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableMultiAccountResourceCenter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableMultiAccountResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_multi_account_resource_center_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableMultiAccountResourceCenterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableMultiAccountResourceCenter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableMultiAccountResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_multi_account_resource_center(self) -> main_models.DisableMultiAccountResourceCenterResponse:
        runtime = RuntimeOptions()
        return self.disable_multi_account_resource_center_with_options(runtime)

    async def disable_multi_account_resource_center_async(self) -> main_models.DisableMultiAccountResourceCenterResponse:
        runtime = RuntimeOptions()
        return await self.disable_multi_account_resource_center_with_options_async(runtime)

    def disable_resource_center_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableResourceCenterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableResourceCenter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def disable_resource_center_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisableResourceCenterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisableResourceCenter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisableResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disable_resource_center(self) -> main_models.DisableResourceCenterResponse:
        runtime = RuntimeOptions()
        return self.disable_resource_center_with_options(runtime)

    async def disable_resource_center_async(self) -> main_models.DisableResourceCenterResponse:
        runtime = RuntimeOptions()
        return await self.disable_resource_center_with_options_async(runtime)

    def disassociate_default_filter_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateDefaultFilterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisassociateDefaultFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateDefaultFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def disassociate_default_filter_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.DisassociateDefaultFilterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'DisassociateDefaultFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DisassociateDefaultFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def disassociate_default_filter(self) -> main_models.DisassociateDefaultFilterResponse:
        runtime = RuntimeOptions()
        return self.disassociate_default_filter_with_options(runtime)

    async def disassociate_default_filter_async(self) -> main_models.DisassociateDefaultFilterResponse:
        runtime = RuntimeOptions()
        return await self.disassociate_default_filter_with_options_async(runtime)

    def enable_multi_account_resource_center_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableMultiAccountResourceCenterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableMultiAccountResourceCenter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMultiAccountResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_multi_account_resource_center_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableMultiAccountResourceCenterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableMultiAccountResourceCenter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableMultiAccountResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_multi_account_resource_center(self) -> main_models.EnableMultiAccountResourceCenterResponse:
        runtime = RuntimeOptions()
        return self.enable_multi_account_resource_center_with_options(runtime)

    async def enable_multi_account_resource_center_async(self) -> main_models.EnableMultiAccountResourceCenterResponse:
        runtime = RuntimeOptions()
        return await self.enable_multi_account_resource_center_with_options_async(runtime)

    def enable_resource_center_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableResourceCenterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableResourceCenter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableResourceCenterResponse(),
            self.call_api(params, req, runtime)
        )

    async def enable_resource_center_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.EnableResourceCenterResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'EnableResourceCenter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.EnableResourceCenterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def enable_resource_center(self) -> main_models.EnableResourceCenterResponse:
        runtime = RuntimeOptions()
        return self.enable_resource_center_with_options(runtime)

    async def enable_resource_center_async(self) -> main_models.EnableResourceCenterResponse:
        runtime = RuntimeOptions()
        return await self.enable_resource_center_with_options_async(runtime)

    def execute_multi_account_sqlquery_with_options(
        self,
        request: main_models.ExecuteMultiAccountSQLQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteMultiAccountSQLQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteMultiAccountSQLQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteMultiAccountSQLQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_multi_account_sqlquery_with_options_async(
        self,
        request: main_models.ExecuteMultiAccountSQLQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteMultiAccountSQLQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteMultiAccountSQLQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteMultiAccountSQLQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_multi_account_sqlquery(
        self,
        request: main_models.ExecuteMultiAccountSQLQueryRequest,
    ) -> main_models.ExecuteMultiAccountSQLQueryResponse:
        runtime = RuntimeOptions()
        return self.execute_multi_account_sqlquery_with_options(request, runtime)

    async def execute_multi_account_sqlquery_async(
        self,
        request: main_models.ExecuteMultiAccountSQLQueryRequest,
    ) -> main_models.ExecuteMultiAccountSQLQueryResponse:
        runtime = RuntimeOptions()
        return await self.execute_multi_account_sqlquery_with_options_async(request, runtime)

    def execute_sqlquery_with_options(
        self,
        request: main_models.ExecuteSQLQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSQLQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteSQLQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSQLQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def execute_sqlquery_with_options_async(
        self,
        request: main_models.ExecuteSQLQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ExecuteSQLQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ExecuteSQLQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ExecuteSQLQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def execute_sqlquery(
        self,
        request: main_models.ExecuteSQLQueryRequest,
    ) -> main_models.ExecuteSQLQueryResponse:
        runtime = RuntimeOptions()
        return self.execute_sqlquery_with_options(request, runtime)

    async def execute_sqlquery_async(
        self,
        request: main_models.ExecuteSQLQueryRequest,
    ) -> main_models.ExecuteSQLQueryResponse:
        runtime = RuntimeOptions()
        return await self.execute_sqlquery_with_options_async(request, runtime)

    def get_delivery_channel_with_options(
        self,
        request: main_models.GetDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_delivery_channel_with_options_async(
        self,
        request: main_models.GetDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_delivery_channel(
        self,
        request: main_models.GetDeliveryChannelRequest,
    ) -> main_models.GetDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.get_delivery_channel_with_options(request, runtime)

    async def get_delivery_channel_async(
        self,
        request: main_models.GetDeliveryChannelRequest,
    ) -> main_models.GetDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.get_delivery_channel_with_options_async(request, runtime)

    def get_delivery_channel_statistics_with_options(
        self,
        request: main_models.GetDeliveryChannelStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeliveryChannelStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeliveryChannelStatistics',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeliveryChannelStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_delivery_channel_statistics_with_options_async(
        self,
        request: main_models.GetDeliveryChannelStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetDeliveryChannelStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetDeliveryChannelStatistics',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetDeliveryChannelStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_delivery_channel_statistics(
        self,
        request: main_models.GetDeliveryChannelStatisticsRequest,
    ) -> main_models.GetDeliveryChannelStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_delivery_channel_statistics_with_options(request, runtime)

    async def get_delivery_channel_statistics_async(
        self,
        request: main_models.GetDeliveryChannelStatisticsRequest,
    ) -> main_models.GetDeliveryChannelStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_delivery_channel_statistics_with_options_async(request, runtime)

    def get_example_query_with_options(
        self,
        request: main_models.GetExampleQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExampleQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExampleQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExampleQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_example_query_with_options_async(
        self,
        request: main_models.GetExampleQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetExampleQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetExampleQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetExampleQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_example_query(
        self,
        request: main_models.GetExampleQueryRequest,
    ) -> main_models.GetExampleQueryResponse:
        runtime = RuntimeOptions()
        return self.get_example_query_with_options(request, runtime)

    async def get_example_query_async(
        self,
        request: main_models.GetExampleQueryRequest,
    ) -> main_models.GetExampleQueryResponse:
        runtime = RuntimeOptions()
        return await self.get_example_query_with_options_async(request, runtime)

    def get_multi_account_delivery_channel_with_options(
        self,
        request: main_models.GetMultiAccountDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiAccountDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_account_delivery_channel_with_options_async(
        self,
        request: main_models.GetMultiAccountDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiAccountDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_account_delivery_channel(
        self,
        request: main_models.GetMultiAccountDeliveryChannelRequest,
    ) -> main_models.GetMultiAccountDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.get_multi_account_delivery_channel_with_options(request, runtime)

    async def get_multi_account_delivery_channel_async(
        self,
        request: main_models.GetMultiAccountDeliveryChannelRequest,
    ) -> main_models.GetMultiAccountDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.get_multi_account_delivery_channel_with_options_async(request, runtime)

    def get_multi_account_delivery_channel_statistics_with_options(
        self,
        request: main_models.GetMultiAccountDeliveryChannelStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountDeliveryChannelStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiAccountDeliveryChannelStatistics',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountDeliveryChannelStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_account_delivery_channel_statistics_with_options_async(
        self,
        request: main_models.GetMultiAccountDeliveryChannelStatisticsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountDeliveryChannelStatisticsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiAccountDeliveryChannelStatistics',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountDeliveryChannelStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_account_delivery_channel_statistics(
        self,
        request: main_models.GetMultiAccountDeliveryChannelStatisticsRequest,
    ) -> main_models.GetMultiAccountDeliveryChannelStatisticsResponse:
        runtime = RuntimeOptions()
        return self.get_multi_account_delivery_channel_statistics_with_options(request, runtime)

    async def get_multi_account_delivery_channel_statistics_async(
        self,
        request: main_models.GetMultiAccountDeliveryChannelStatisticsRequest,
    ) -> main_models.GetMultiAccountDeliveryChannelStatisticsResponse:
        runtime = RuntimeOptions()
        return await self.get_multi_account_delivery_channel_statistics_with_options_async(request, runtime)

    def get_multi_account_resource_center_service_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountResourceCenterServiceStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetMultiAccountResourceCenterServiceStatus',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountResourceCenterServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_account_resource_center_service_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountResourceCenterServiceStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetMultiAccountResourceCenterServiceStatus',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountResourceCenterServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_account_resource_center_service_status(self) -> main_models.GetMultiAccountResourceCenterServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.get_multi_account_resource_center_service_status_with_options(runtime)

    async def get_multi_account_resource_center_service_status_async(self) -> main_models.GetMultiAccountResourceCenterServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_multi_account_resource_center_service_status_with_options_async(runtime)

    def get_multi_account_resource_configuration_with_options(
        self,
        request: main_models.GetMultiAccountResourceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountResourceConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiAccountResourceConfiguration',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountResourceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_account_resource_configuration_with_options_async(
        self,
        request: main_models.GetMultiAccountResourceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountResourceConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiAccountResourceConfiguration',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountResourceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_account_resource_configuration(
        self,
        request: main_models.GetMultiAccountResourceConfigurationRequest,
    ) -> main_models.GetMultiAccountResourceConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_multi_account_resource_configuration_with_options(request, runtime)

    async def get_multi_account_resource_configuration_async(
        self,
        request: main_models.GetMultiAccountResourceConfigurationRequest,
    ) -> main_models.GetMultiAccountResourceConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_multi_account_resource_configuration_with_options_async(request, runtime)

    def get_multi_account_resource_counts_with_options(
        self,
        request: main_models.GetMultiAccountResourceCountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountResourceCountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiAccountResourceCounts',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountResourceCountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_multi_account_resource_counts_with_options_async(
        self,
        request: main_models.GetMultiAccountResourceCountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetMultiAccountResourceCountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetMultiAccountResourceCounts',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetMultiAccountResourceCountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_multi_account_resource_counts(
        self,
        request: main_models.GetMultiAccountResourceCountsRequest,
    ) -> main_models.GetMultiAccountResourceCountsResponse:
        runtime = RuntimeOptions()
        return self.get_multi_account_resource_counts_with_options(request, runtime)

    async def get_multi_account_resource_counts_async(
        self,
        request: main_models.GetMultiAccountResourceCountsRequest,
    ) -> main_models.GetMultiAccountResourceCountsResponse:
        runtime = RuntimeOptions()
        return await self.get_multi_account_resource_counts_with_options_async(request, runtime)

    def get_resource_center_service_status_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceCenterServiceStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceCenterServiceStatus',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceCenterServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_center_service_status_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceCenterServiceStatusResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'GetResourceCenterServiceStatus',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceCenterServiceStatusResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_center_service_status(self) -> main_models.GetResourceCenterServiceStatusResponse:
        runtime = RuntimeOptions()
        return self.get_resource_center_service_status_with_options(runtime)

    async def get_resource_center_service_status_async(self) -> main_models.GetResourceCenterServiceStatusResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_center_service_status_with_options_async(runtime)

    def get_resource_configuration_with_options(
        self,
        request: main_models.GetResourceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceConfiguration',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceConfigurationResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_configuration_with_options_async(
        self,
        request: main_models.GetResourceConfigurationRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceConfigurationResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceConfiguration',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceConfigurationResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_configuration(
        self,
        request: main_models.GetResourceConfigurationRequest,
    ) -> main_models.GetResourceConfigurationResponse:
        runtime = RuntimeOptions()
        return self.get_resource_configuration_with_options(request, runtime)

    async def get_resource_configuration_async(
        self,
        request: main_models.GetResourceConfigurationRequest,
    ) -> main_models.GetResourceConfigurationResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_configuration_with_options_async(request, runtime)

    def get_resource_counts_with_options(
        self,
        request: main_models.GetResourceCountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceCountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        if not DaraCore.is_null(request.include_deleted_resources):
            query['IncludeDeletedResources'] = request.include_deleted_resources
        if not DaraCore.is_null(request.search_expression):
            query['SearchExpression'] = request.search_expression
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceCounts',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceCountsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_resource_counts_with_options_async(
        self,
        request: main_models.GetResourceCountsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetResourceCountsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.group_by_key):
            query['GroupByKey'] = request.group_by_key
        if not DaraCore.is_null(request.include_deleted_resources):
            query['IncludeDeletedResources'] = request.include_deleted_resources
        if not DaraCore.is_null(request.search_expression):
            query['SearchExpression'] = request.search_expression
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetResourceCounts',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetResourceCountsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_resource_counts(
        self,
        request: main_models.GetResourceCountsRequest,
    ) -> main_models.GetResourceCountsResponse:
        runtime = RuntimeOptions()
        return self.get_resource_counts_with_options(request, runtime)

    async def get_resource_counts_async(
        self,
        request: main_models.GetResourceCountsRequest,
    ) -> main_models.GetResourceCountsResponse:
        runtime = RuntimeOptions()
        return await self.get_resource_counts_with_options_async(request, runtime)

    def get_saved_query_with_options(
        self,
        request: main_models.GetSavedQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavedQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSavedQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavedQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_saved_query_with_options_async(
        self,
        request: main_models.GetSavedQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetSavedQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetSavedQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetSavedQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_saved_query(
        self,
        request: main_models.GetSavedQueryRequest,
    ) -> main_models.GetSavedQueryResponse:
        runtime = RuntimeOptions()
        return self.get_saved_query_with_options(request, runtime)

    async def get_saved_query_async(
        self,
        request: main_models.GetSavedQueryRequest,
    ) -> main_models.GetSavedQueryResponse:
        runtime = RuntimeOptions()
        return await self.get_saved_query_with_options_async(request, runtime)

    def list_delivery_channels_with_options(
        self,
        request: main_models.ListDeliveryChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeliveryChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeliveryChannels',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeliveryChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_delivery_channels_with_options_async(
        self,
        request: main_models.ListDeliveryChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListDeliveryChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListDeliveryChannels',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListDeliveryChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_delivery_channels(
        self,
        request: main_models.ListDeliveryChannelsRequest,
    ) -> main_models.ListDeliveryChannelsResponse:
        runtime = RuntimeOptions()
        return self.list_delivery_channels_with_options(request, runtime)

    async def list_delivery_channels_async(
        self,
        request: main_models.ListDeliveryChannelsRequest,
    ) -> main_models.ListDeliveryChannelsResponse:
        runtime = RuntimeOptions()
        return await self.list_delivery_channels_with_options_async(request, runtime)

    def list_example_queries_with_options(
        self,
        request: main_models.ListExampleQueriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExampleQueriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExampleQueries',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExampleQueriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_example_queries_with_options_async(
        self,
        request: main_models.ListExampleQueriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListExampleQueriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListExampleQueries',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListExampleQueriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_example_queries(
        self,
        request: main_models.ListExampleQueriesRequest,
    ) -> main_models.ListExampleQueriesResponse:
        runtime = RuntimeOptions()
        return self.list_example_queries_with_options(request, runtime)

    async def list_example_queries_async(
        self,
        request: main_models.ListExampleQueriesRequest,
    ) -> main_models.ListExampleQueriesResponse:
        runtime = RuntimeOptions()
        return await self.list_example_queries_with_options_async(request, runtime)

    def list_filters_with_options(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListFiltersResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListFilters',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFiltersResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_filters_with_options_async(
        self,
        runtime: RuntimeOptions,
    ) -> main_models.ListFiltersResponse:
        req = open_api_util_models.OpenApiRequest()
        params = open_api_util_models.Params(
            action = 'ListFilters',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListFiltersResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_filters(self) -> main_models.ListFiltersResponse:
        runtime = RuntimeOptions()
        return self.list_filters_with_options(runtime)

    async def list_filters_async(self) -> main_models.ListFiltersResponse:
        runtime = RuntimeOptions()
        return await self.list_filters_with_options_async(runtime)

    def list_multi_account_delivery_channels_with_options(
        self,
        request: main_models.ListMultiAccountDeliveryChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountDeliveryChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountDeliveryChannels',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountDeliveryChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_delivery_channels_with_options_async(
        self,
        request: main_models.ListMultiAccountDeliveryChannelsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountDeliveryChannelsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountDeliveryChannels',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountDeliveryChannelsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_delivery_channels(
        self,
        request: main_models.ListMultiAccountDeliveryChannelsRequest,
    ) -> main_models.ListMultiAccountDeliveryChannelsResponse:
        runtime = RuntimeOptions()
        return self.list_multi_account_delivery_channels_with_options(request, runtime)

    async def list_multi_account_delivery_channels_async(
        self,
        request: main_models.ListMultiAccountDeliveryChannelsRequest,
    ) -> main_models.ListMultiAccountDeliveryChannelsResponse:
        runtime = RuntimeOptions()
        return await self.list_multi_account_delivery_channels_with_options_async(request, runtime)

    def list_multi_account_resource_groups_with_options(
        self,
        request: main_models.ListMultiAccountResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountResourceGroups',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_resource_groups_with_options_async(
        self,
        request: main_models.ListMultiAccountResourceGroupsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountResourceGroupsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.account_id):
            query['AccountId'] = request.account_id
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountResourceGroups',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountResourceGroupsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_resource_groups(
        self,
        request: main_models.ListMultiAccountResourceGroupsRequest,
    ) -> main_models.ListMultiAccountResourceGroupsResponse:
        runtime = RuntimeOptions()
        return self.list_multi_account_resource_groups_with_options(request, runtime)

    async def list_multi_account_resource_groups_async(
        self,
        request: main_models.ListMultiAccountResourceGroupsRequest,
    ) -> main_models.ListMultiAccountResourceGroupsResponse:
        runtime = RuntimeOptions()
        return await self.list_multi_account_resource_groups_with_options_async(request, runtime)

    def list_multi_account_resource_relationships_with_options(
        self,
        request: main_models.ListMultiAccountResourceRelationshipsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountResourceRelationshipsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.related_resource_filter):
            query['RelatedResourceFilter'] = request.related_resource_filter
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountResourceRelationships',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountResourceRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_resource_relationships_with_options_async(
        self,
        request: main_models.ListMultiAccountResourceRelationshipsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountResourceRelationshipsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.related_resource_filter):
            query['RelatedResourceFilter'] = request.related_resource_filter
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountResourceRelationships',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountResourceRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_resource_relationships(
        self,
        request: main_models.ListMultiAccountResourceRelationshipsRequest,
    ) -> main_models.ListMultiAccountResourceRelationshipsResponse:
        runtime = RuntimeOptions()
        return self.list_multi_account_resource_relationships_with_options(request, runtime)

    async def list_multi_account_resource_relationships_async(
        self,
        request: main_models.ListMultiAccountResourceRelationshipsRequest,
    ) -> main_models.ListMultiAccountResourceRelationshipsResponse:
        runtime = RuntimeOptions()
        return await self.list_multi_account_resource_relationships_with_options_async(request, runtime)

    def list_multi_account_tag_keys_with_options(
        self,
        request: main_models.ListMultiAccountTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountTagKeys',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_tag_keys_with_options_async(
        self,
        request: main_models.ListMultiAccountTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountTagKeys',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_tag_keys(
        self,
        request: main_models.ListMultiAccountTagKeysRequest,
    ) -> main_models.ListMultiAccountTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_multi_account_tag_keys_with_options(request, runtime)

    async def list_multi_account_tag_keys_async(
        self,
        request: main_models.ListMultiAccountTagKeysRequest,
    ) -> main_models.ListMultiAccountTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_multi_account_tag_keys_with_options_async(request, runtime)

    def list_multi_account_tag_values_with_options(
        self,
        request: main_models.ListMultiAccountTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountTagValues',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_multi_account_tag_values_with_options_async(
        self,
        request: main_models.ListMultiAccountTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListMultiAccountTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListMultiAccountTagValues',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListMultiAccountTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_multi_account_tag_values(
        self,
        request: main_models.ListMultiAccountTagValuesRequest,
    ) -> main_models.ListMultiAccountTagValuesResponse:
        runtime = RuntimeOptions()
        return self.list_multi_account_tag_values_with_options(request, runtime)

    async def list_multi_account_tag_values_async(
        self,
        request: main_models.ListMultiAccountTagValuesRequest,
    ) -> main_models.ListMultiAccountTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.list_multi_account_tag_values_with_options_async(request, runtime)

    def list_resource_relationships_with_options(
        self,
        request: main_models.ListResourceRelationshipsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceRelationshipsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.related_resource_filter):
            query['RelatedResourceFilter'] = request.related_resource_filter
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceRelationships',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceRelationshipsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_relationships_with_options_async(
        self,
        request: main_models.ListResourceRelationshipsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceRelationshipsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.related_resource_filter):
            query['RelatedResourceFilter'] = request.related_resource_filter
        if not DaraCore.is_null(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceRelationships',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceRelationshipsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_relationships(
        self,
        request: main_models.ListResourceRelationshipsRequest,
    ) -> main_models.ListResourceRelationshipsResponse:
        runtime = RuntimeOptions()
        return self.list_resource_relationships_with_options(request, runtime)

    async def list_resource_relationships_async(
        self,
        request: main_models.ListResourceRelationshipsRequest,
    ) -> main_models.ListResourceRelationshipsResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_relationships_with_options_async(request, runtime)

    def list_resource_types_with_options(
        self,
        request: main_models.ListResourceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypes',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_resource_types_with_options_async(
        self,
        request: main_models.ListResourceTypesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListResourceTypesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not DaraCore.is_null(request.query):
            query['Query'] = request.query
        if not DaraCore.is_null(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListResourceTypes',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListResourceTypesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_resource_types(
        self,
        request: main_models.ListResourceTypesRequest,
    ) -> main_models.ListResourceTypesResponse:
        runtime = RuntimeOptions()
        return self.list_resource_types_with_options(request, runtime)

    async def list_resource_types_async(
        self,
        request: main_models.ListResourceTypesRequest,
    ) -> main_models.ListResourceTypesResponse:
        runtime = RuntimeOptions()
        return await self.list_resource_types_with_options_async(request, runtime)

    def list_saved_queries_with_options(
        self,
        request: main_models.ListSavedQueriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSavedQueriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSavedQueries',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSavedQueriesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_saved_queries_with_options_async(
        self,
        request: main_models.ListSavedQueriesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListSavedQueriesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListSavedQueries',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListSavedQueriesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_saved_queries(
        self,
        request: main_models.ListSavedQueriesRequest,
    ) -> main_models.ListSavedQueriesResponse:
        runtime = RuntimeOptions()
        return self.list_saved_queries_with_options(request, runtime)

    async def list_saved_queries_async(
        self,
        request: main_models.ListSavedQueriesRequest,
    ) -> main_models.ListSavedQueriesResponse:
        runtime = RuntimeOptions()
        return await self.list_saved_queries_with_options_async(request, runtime)

    def list_tag_keys_with_options(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_keys_with_options_async(
        self,
        request: main_models.ListTagKeysRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagKeysResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagKeys',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagKeysResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_keys(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    async def list_tag_keys_async(
        self,
        request: main_models.ListTagKeysRequest,
    ) -> main_models.ListTagKeysResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_keys_with_options_async(request, runtime)

    def list_tag_values_with_options(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_tag_values_with_options_async(
        self,
        request: main_models.ListTagValuesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListTagValuesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.match_type):
            query['MatchType'] = request.match_type
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.tag_key):
            query['TagKey'] = request.tag_key
        if not DaraCore.is_null(request.tag_value):
            query['TagValue'] = request.tag_value
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListTagValues',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListTagValuesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_tag_values(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    async def list_tag_values_async(
        self,
        request: main_models.ListTagValuesRequest,
    ) -> main_models.ListTagValuesResponse:
        runtime = RuntimeOptions()
        return await self.list_tag_values_with_options_async(request, runtime)

    def search_multi_account_resources_with_options(
        self,
        request: main_models.SearchMultiAccountResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchMultiAccountResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchMultiAccountResources',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchMultiAccountResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_multi_account_resources_with_options_async(
        self,
        request: main_models.SearchMultiAccountResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchMultiAccountResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.scope):
            query['Scope'] = request.scope
        if not DaraCore.is_null(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchMultiAccountResources',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchMultiAccountResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_multi_account_resources(
        self,
        request: main_models.SearchMultiAccountResourcesRequest,
    ) -> main_models.SearchMultiAccountResourcesResponse:
        runtime = RuntimeOptions()
        return self.search_multi_account_resources_with_options(request, runtime)

    async def search_multi_account_resources_async(
        self,
        request: main_models.SearchMultiAccountResourcesRequest,
    ) -> main_models.SearchMultiAccountResourcesResponse:
        runtime = RuntimeOptions()
        return await self.search_multi_account_resources_with_options_async(request, runtime)

    def search_resources_with_options(
        self,
        request: main_models.SearchResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.include_deleted_resources):
            query['IncludeDeletedResources'] = request.include_deleted_resources
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.search_expression):
            query['SearchExpression'] = request.search_expression
        if not DaraCore.is_null(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchResources',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    async def search_resources_with_options_async(
        self,
        request: main_models.SearchResourcesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.SearchResourcesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter):
            query['Filter'] = request.filter
        if not DaraCore.is_null(request.include_deleted_resources):
            query['IncludeDeletedResources'] = request.include_deleted_resources
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.search_expression):
            query['SearchExpression'] = request.search_expression
        if not DaraCore.is_null(request.sort_criterion):
            query['SortCriterion'] = request.sort_criterion
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'SearchResources',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.SearchResourcesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def search_resources(
        self,
        request: main_models.SearchResourcesRequest,
    ) -> main_models.SearchResourcesResponse:
        runtime = RuntimeOptions()
        return self.search_resources_with_options(request, runtime)

    async def search_resources_async(
        self,
        request: main_models.SearchResourcesRequest,
    ) -> main_models.SearchResourcesResponse:
        runtime = RuntimeOptions()
        return await self.search_resources_with_options_async(request, runtime)

    def update_delivery_channel_with_options(
        self,
        request: main_models.UpdateDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_description):
            query['DeliveryChannelDescription'] = request.delivery_channel_description
        if not DaraCore.is_null(request.delivery_channel_filter):
            query['DeliveryChannelFilter'] = request.delivery_channel_filter
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.resource_change_delivery):
            query['ResourceChangeDelivery'] = request.resource_change_delivery
        if not DaraCore.is_null(request.resource_snapshot_delivery):
            query['ResourceSnapshotDelivery'] = request.resource_snapshot_delivery
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_delivery_channel_with_options_async(
        self,
        request: main_models.UpdateDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_description):
            query['DeliveryChannelDescription'] = request.delivery_channel_description
        if not DaraCore.is_null(request.delivery_channel_filter):
            query['DeliveryChannelFilter'] = request.delivery_channel_filter
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.resource_change_delivery):
            query['ResourceChangeDelivery'] = request.resource_change_delivery
        if not DaraCore.is_null(request.resource_snapshot_delivery):
            query['ResourceSnapshotDelivery'] = request.resource_snapshot_delivery
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_delivery_channel(
        self,
        request: main_models.UpdateDeliveryChannelRequest,
    ) -> main_models.UpdateDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.update_delivery_channel_with_options(request, runtime)

    async def update_delivery_channel_async(
        self,
        request: main_models.UpdateDeliveryChannelRequest,
    ) -> main_models.UpdateDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.update_delivery_channel_with_options_async(request, runtime)

    def update_filter_with_options(
        self,
        request: main_models.UpdateFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_configuration):
            query['FilterConfiguration'] = request.filter_configuration
        if not DaraCore.is_null(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFilterResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_filter_with_options_async(
        self,
        request: main_models.UpdateFilterRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateFilterResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.filter_configuration):
            query['FilterConfiguration'] = request.filter_configuration
        if not DaraCore.is_null(request.filter_name):
            query['FilterName'] = request.filter_name
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateFilter',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateFilterResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_filter(
        self,
        request: main_models.UpdateFilterRequest,
    ) -> main_models.UpdateFilterResponse:
        runtime = RuntimeOptions()
        return self.update_filter_with_options(request, runtime)

    async def update_filter_async(
        self,
        request: main_models.UpdateFilterRequest,
    ) -> main_models.UpdateFilterResponse:
        runtime = RuntimeOptions()
        return await self.update_filter_with_options_async(request, runtime)

    def update_multi_account_delivery_channel_with_options(
        self,
        request: main_models.UpdateMultiAccountDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMultiAccountDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_description):
            query['DeliveryChannelDescription'] = request.delivery_channel_description
        if not DaraCore.is_null(request.delivery_channel_filter):
            query['DeliveryChannelFilter'] = request.delivery_channel_filter
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.resource_change_delivery):
            query['ResourceChangeDelivery'] = request.resource_change_delivery
        if not DaraCore.is_null(request.resource_snapshot_delivery):
            query['ResourceSnapshotDelivery'] = request.resource_snapshot_delivery
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMultiAccountDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMultiAccountDeliveryChannelResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_multi_account_delivery_channel_with_options_async(
        self,
        request: main_models.UpdateMultiAccountDeliveryChannelRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateMultiAccountDeliveryChannelResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.delivery_channel_description):
            query['DeliveryChannelDescription'] = request.delivery_channel_description
        if not DaraCore.is_null(request.delivery_channel_filter):
            query['DeliveryChannelFilter'] = request.delivery_channel_filter
        if not DaraCore.is_null(request.delivery_channel_id):
            query['DeliveryChannelId'] = request.delivery_channel_id
        if not DaraCore.is_null(request.delivery_channel_name):
            query['DeliveryChannelName'] = request.delivery_channel_name
        if not DaraCore.is_null(request.resource_change_delivery):
            query['ResourceChangeDelivery'] = request.resource_change_delivery
        if not DaraCore.is_null(request.resource_snapshot_delivery):
            query['ResourceSnapshotDelivery'] = request.resource_snapshot_delivery
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateMultiAccountDeliveryChannel',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateMultiAccountDeliveryChannelResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_multi_account_delivery_channel(
        self,
        request: main_models.UpdateMultiAccountDeliveryChannelRequest,
    ) -> main_models.UpdateMultiAccountDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return self.update_multi_account_delivery_channel_with_options(request, runtime)

    async def update_multi_account_delivery_channel_async(
        self,
        request: main_models.UpdateMultiAccountDeliveryChannelRequest,
    ) -> main_models.UpdateMultiAccountDeliveryChannelResponse:
        runtime = RuntimeOptions()
        return await self.update_multi_account_delivery_channel_with_options_async(request, runtime)

    def update_saved_query_with_options(
        self,
        request: main_models.UpdateSavedQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSavedQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSavedQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSavedQueryResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_saved_query_with_options_async(
        self,
        request: main_models.UpdateSavedQueryRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateSavedQueryResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.expression):
            query['Expression'] = request.expression
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.query_id):
            query['QueryId'] = request.query_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateSavedQuery',
            version = '2022-12-01',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateSavedQueryResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_saved_query(
        self,
        request: main_models.UpdateSavedQueryRequest,
    ) -> main_models.UpdateSavedQueryResponse:
        runtime = RuntimeOptions()
        return self.update_saved_query_with_options(request, runtime)

    async def update_saved_query_async(
        self,
        request: main_models.UpdateSavedQueryRequest,
    ) -> main_models.UpdateSavedQueryResponse:
        runtime = RuntimeOptions()
        return await self.update_saved_query_with_options_async(request, runtime)
