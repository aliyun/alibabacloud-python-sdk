# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_kvcachestore20260617 import models as main_models
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
        self._endpoint_map = {
            'cn-beijing': 'kvcachestore.cn-beijing.aliyuncs.com',
            'cn-shanghai': 'kvcachestore.cn-shanghai.aliyuncs.com',
            'ap-southeast-1': 'kvcachestore.ap-southeast-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('kvcachestore', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def attach_kvcache_store_with_options(
        self,
        request: main_models.AttachKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arns):
            query['Arns'] = request.arns
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachKVCacheStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def attach_kvcache_store_with_options_async(
        self,
        request: main_models.AttachKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.AttachKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.arns):
            query['Arns'] = request.arns
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'AttachKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.AttachKVCacheStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def attach_kvcache_store(
        self,
        request: main_models.AttachKVCacheStoreRequest,
    ) -> main_models.AttachKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return self.attach_kvcache_store_with_options(request, runtime)

    async def attach_kvcache_store_async(
        self,
        request: main_models.AttachKVCacheStoreRequest,
    ) -> main_models.AttachKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return await self.attach_kvcache_store_with_options_async(request, runtime)

    def create_kvcache_store_with_options(
        self,
        request: main_models.CreateKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.hpn_zone):
            query['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKVCacheStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def create_kvcache_store_with_options_async(
        self,
        request: main_models.CreateKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.CreateKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.hpn_zone):
            query['HpnZone'] = request.hpn_zone
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'CreateKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.CreateKVCacheStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def create_kvcache_store(
        self,
        request: main_models.CreateKVCacheStoreRequest,
    ) -> main_models.CreateKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return self.create_kvcache_store_with_options(request, runtime)

    async def create_kvcache_store_async(
        self,
        request: main_models.CreateKVCacheStoreRequest,
    ) -> main_models.CreateKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return await self.create_kvcache_store_with_options_async(request, runtime)

    def delete_kvcache_store_with_options(
        self,
        request: main_models.DeleteKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_id):
            query['KvcsId'] = request.kvcs_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKVCacheStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def delete_kvcache_store_with_options_async(
        self,
        request: main_models.DeleteKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DeleteKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_id):
            query['KvcsId'] = request.kvcs_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DeleteKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DeleteKVCacheStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def delete_kvcache_store(
        self,
        request: main_models.DeleteKVCacheStoreRequest,
    ) -> main_models.DeleteKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return self.delete_kvcache_store_with_options(request, runtime)

    async def delete_kvcache_store_async(
        self,
        request: main_models.DeleteKVCacheStoreRequest,
    ) -> main_models.DeleteKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return await self.delete_kvcache_store_with_options_async(request, runtime)

    def describe_regions_with_options(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_regions_with_options_async(
        self,
        request: main_models.DescribeRegionsRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeRegionsResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeRegions',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeRegionsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_regions(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    async def describe_regions_async(
        self,
        request: main_models.DescribeRegionsRequest,
    ) -> main_models.DescribeRegionsResponse:
        runtime = RuntimeOptions()
        return await self.describe_regions_with_options_async(request, runtime)

    def describe_zones_with_options(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def describe_zones_with_options_async(
        self,
        request: main_models.DescribeZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DescribeZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DescribeZones',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DescribeZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def describe_zones(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    async def describe_zones_async(
        self,
        request: main_models.DescribeZonesRequest,
    ) -> main_models.DescribeZonesResponse:
        runtime = RuntimeOptions()
        return await self.describe_zones_with_options_async(request, runtime)

    def detach_kvcache_store_with_options(
        self,
        request: main_models.DetachKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachKVCacheStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def detach_kvcache_store_with_options_async(
        self,
        request: main_models.DetachKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.DetachKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'DetachKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.DetachKVCacheStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def detach_kvcache_store(
        self,
        request: main_models.DetachKVCacheStoreRequest,
    ) -> main_models.DetachKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return self.detach_kvcache_store_with_options(request, runtime)

    async def detach_kvcache_store_async(
        self,
        request: main_models.DetachKVCacheStoreRequest,
    ) -> main_models.DetachKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return await self.detach_kvcache_store_with_options_async(request, runtime)

    def get_kvcache_store_with_options(
        self,
        request: main_models.GetKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_id):
            query['KvcsId'] = request.kvcs_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKVCacheStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_kvcache_store_with_options_async(
        self,
        request: main_models.GetKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.GetKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_id):
            query['KvcsId'] = request.kvcs_id
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'GetKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.GetKVCacheStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_kvcache_store(
        self,
        request: main_models.GetKVCacheStoreRequest,
    ) -> main_models.GetKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return self.get_kvcache_store_with_options(request, runtime)

    async def get_kvcache_store_async(
        self,
        request: main_models.GetKVCacheStoreRequest,
    ) -> main_models.GetKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return await self.get_kvcache_store_with_options_async(request, runtime)

    def list_kvcache_store_attach_info_with_options(
        self,
        request: main_models.ListKVCacheStoreAttachInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKVCacheStoreAttachInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_ids):
            query['KvcsIds'] = request.kvcs_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKVCacheStoreAttachInfo',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKVCacheStoreAttachInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kvcache_store_attach_info_with_options_async(
        self,
        request: main_models.ListKVCacheStoreAttachInfoRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKVCacheStoreAttachInfoResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_ids):
            query['KvcsIds'] = request.kvcs_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKVCacheStoreAttachInfo',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKVCacheStoreAttachInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kvcache_store_attach_info(
        self,
        request: main_models.ListKVCacheStoreAttachInfoRequest,
    ) -> main_models.ListKVCacheStoreAttachInfoResponse:
        runtime = RuntimeOptions()
        return self.list_kvcache_store_attach_info_with_options(request, runtime)

    async def list_kvcache_store_attach_info_async(
        self,
        request: main_models.ListKVCacheStoreAttachInfoRequest,
    ) -> main_models.ListKVCacheStoreAttachInfoResponse:
        runtime = RuntimeOptions()
        return await self.list_kvcache_store_attach_info_with_options_async(request, runtime)

    def list_kvcache_store_available_hpn_zones_with_options(
        self,
        request: main_models.ListKVCacheStoreAvailableHpnZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKVCacheStoreAvailableHpnZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_ids):
            query['KvcsIds'] = request.kvcs_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKVCacheStoreAvailableHpnZones',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKVCacheStoreAvailableHpnZonesResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kvcache_store_available_hpn_zones_with_options_async(
        self,
        request: main_models.ListKVCacheStoreAvailableHpnZonesRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKVCacheStoreAvailableHpnZonesResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_ids):
            query['KvcsIds'] = request.kvcs_ids
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKVCacheStoreAvailableHpnZones',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKVCacheStoreAvailableHpnZonesResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kvcache_store_available_hpn_zones(
        self,
        request: main_models.ListKVCacheStoreAvailableHpnZonesRequest,
    ) -> main_models.ListKVCacheStoreAvailableHpnZonesResponse:
        runtime = RuntimeOptions()
        return self.list_kvcache_store_available_hpn_zones_with_options(request, runtime)

    async def list_kvcache_store_available_hpn_zones_async(
        self,
        request: main_models.ListKVCacheStoreAvailableHpnZonesRequest,
    ) -> main_models.ListKVCacheStoreAvailableHpnZonesResponse:
        runtime = RuntimeOptions()
        return await self.list_kvcache_store_available_hpn_zones_with_options_async(request, runtime)

    def list_kvcache_stores_with_options(
        self,
        request: main_models.ListKVCacheStoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKVCacheStoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_ids):
            query['KvcsIds'] = request.kvcs_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKVCacheStores',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKVCacheStoresResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_kvcache_stores_with_options_async(
        self,
        request: main_models.ListKVCacheStoresRequest,
        runtime: RuntimeOptions,
    ) -> main_models.ListKVCacheStoresResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.kvcs_ids):
            query['KvcsIds'] = request.kvcs_ids
        if not DaraCore.is_null(request.max_results):
            query['MaxResults'] = request.max_results
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.next_token):
            query['NextToken'] = request.next_token
        if not DaraCore.is_null(request.page_number):
            query['PageNumber'] = request.page_number
        if not DaraCore.is_null(request.page_size):
            query['PageSize'] = request.page_size
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.status):
            query['Status'] = request.status
        if not DaraCore.is_null(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'ListKVCacheStores',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.ListKVCacheStoresResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_kvcache_stores(
        self,
        request: main_models.ListKVCacheStoresRequest,
    ) -> main_models.ListKVCacheStoresResponse:
        runtime = RuntimeOptions()
        return self.list_kvcache_stores_with_options(request, runtime)

    async def list_kvcache_stores_async(
        self,
        request: main_models.ListKVCacheStoresRequest,
    ) -> main_models.ListKVCacheStoresResponse:
        runtime = RuntimeOptions()
        return await self.list_kvcache_stores_with_options_async(request, runtime)

    def update_kvcache_store_with_options(
        self,
        request: main_models.UpdateKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.kvcs_id):
            query['KvcsId'] = request.kvcs_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKVCacheStoreResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_kvcache_store_with_options_async(
        self,
        request: main_models.UpdateKVCacheStoreRequest,
        runtime: RuntimeOptions,
    ) -> main_models.UpdateKVCacheStoreResponse:
        request.validate()
        query = {}
        if not DaraCore.is_null(request.capacity):
            query['Capacity'] = request.capacity
        if not DaraCore.is_null(request.client_token):
            query['ClientToken'] = request.client_token
        if not DaraCore.is_null(request.description):
            query['Description'] = request.description
        if not DaraCore.is_null(request.kvcs_id):
            query['KvcsId'] = request.kvcs_id
        if not DaraCore.is_null(request.name):
            query['Name'] = request.name
        if not DaraCore.is_null(request.region_id):
            query['RegionId'] = request.region_id
        if not DaraCore.is_null(request.tag):
            query['Tag'] = request.tag
        req = open_api_util_models.OpenApiRequest(
            query = Utils.query(query)
        )
        params = open_api_util_models.Params(
            action = 'UpdateKVCacheStore',
            version = '2026-06-17',
            protocol = 'HTTPS',
            pathname = '/',
            method = 'POST',
            auth_type = 'AK',
            style = 'RPC',
            req_body_type = 'formData',
            body_type = 'json'
        )
        return DaraCore.from_map(
            main_models.UpdateKVCacheStoreResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_kvcache_store(
        self,
        request: main_models.UpdateKVCacheStoreRequest,
    ) -> main_models.UpdateKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return self.update_kvcache_store_with_options(request, runtime)

    async def update_kvcache_store_async(
        self,
        request: main_models.UpdateKVCacheStoreRequest,
    ) -> main_models.UpdateKVCacheStoreResponse:
        runtime = RuntimeOptions()
        return await self.update_kvcache_store_with_options_async(request, runtime)
