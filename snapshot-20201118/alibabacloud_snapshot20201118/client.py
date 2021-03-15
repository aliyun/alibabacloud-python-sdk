# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_snapshot20201118 import models as snapshot_20201118_models
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
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('snapshot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_snapshot_block(
        self,
        request: snapshot_20201118_models.GetSnapshotBlockRequest,
    ) -> snapshot_20201118_models.GetSnapshotBlockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_snapshot_block_with_options(request, headers, runtime)

    async def get_snapshot_block_async(
        self,
        request: snapshot_20201118_models.GetSnapshotBlockRequest,
    ) -> snapshot_20201118_models.GetSnapshotBlockResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_snapshot_block_with_options_async(request, headers, runtime)

    def get_snapshot_block_with_options(
        self,
        request: snapshot_20201118_models.GetSnapshotBlockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> snapshot_20201118_models.GetSnapshotBlockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.block_index):
            query['BlockIndex'] = request.block_index
        if not UtilClient.is_unset(request.block_token):
            query['BlockToken'] = request.block_token
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        res = snapshot_20201118_models.GetSnapshotBlockResponse()
        tmp = UtilClient.assert_as_map(self.do_roarequest('GetSnapshotBlock', '2020-11-18', 'HTTPS', 'GET', 'AK', f'/snapshots/block', 'binary', req, runtime))
        if not UtilClient.is_unset(tmp.get('body')):
            resp_body = UtilClient.assert_as_readable(tmp.get('body'))
            res.body = resp_body
        if not UtilClient.is_unset(tmp.get('headers')):
            resp_headers = UtilClient.assert_as_map(tmp.get('headers'))
            res.headers = UtilClient.stringify_map_value(resp_headers)
        return res

    async def get_snapshot_block_with_options_async(
        self,
        request: snapshot_20201118_models.GetSnapshotBlockRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> snapshot_20201118_models.GetSnapshotBlockResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.block_index):
            query['BlockIndex'] = request.block_index
        if not UtilClient.is_unset(request.block_token):
            query['BlockToken'] = request.block_token
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        res = snapshot_20201118_models.GetSnapshotBlockResponse()
        tmp = UtilClient.assert_as_map(await self.do_roarequest_async('GetSnapshotBlock', '2020-11-18', 'HTTPS', 'GET', 'AK', f'/snapshots/block', 'binary', req, runtime))
        if not UtilClient.is_unset(tmp.get('body')):
            resp_body = UtilClient.assert_as_readable(tmp.get('body'))
            res.body = resp_body
        if not UtilClient.is_unset(tmp.get('headers')):
            resp_headers = UtilClient.assert_as_map(tmp.get('headers'))
            res.headers = UtilClient.stringify_map_value(resp_headers)
        return res

    def get_snapshot_info(
        self,
        request: snapshot_20201118_models.GetSnapshotInfoRequest,
    ) -> snapshot_20201118_models.GetSnapshotInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_snapshot_info_with_options(request, headers, runtime)

    async def get_snapshot_info_async(
        self,
        request: snapshot_20201118_models.GetSnapshotInfoRequest,
    ) -> snapshot_20201118_models.GetSnapshotInfoResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_snapshot_info_with_options_async(request, headers, runtime)

    def get_snapshot_info_with_options(
        self,
        request: snapshot_20201118_models.GetSnapshotInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> snapshot_20201118_models.GetSnapshotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return snapshot_20201118_models.GetSnapshotInfoResponse().from_map(
            self.do_roarequest('GetSnapshotInfo', '2020-11-18', 'HTTPS', 'GET', 'AK', f'/snapshots/info', 'json', req, runtime)
        )

    async def get_snapshot_info_with_options_async(
        self,
        request: snapshot_20201118_models.GetSnapshotInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> snapshot_20201118_models.GetSnapshotInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.show_detail):
            query['ShowDetail'] = request.show_detail
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return snapshot_20201118_models.GetSnapshotInfoResponse().from_map(
            await self.do_roarequest_async('GetSnapshotInfo', '2020-11-18', 'HTTPS', 'GET', 'AK', f'/snapshots/info', 'json', req, runtime)
        )

    def list_changed_blocks(
        self,
        request: snapshot_20201118_models.ListChangedBlocksRequest,
    ) -> snapshot_20201118_models.ListChangedBlocksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_changed_blocks_with_options(request, headers, runtime)

    async def list_changed_blocks_async(
        self,
        request: snapshot_20201118_models.ListChangedBlocksRequest,
    ) -> snapshot_20201118_models.ListChangedBlocksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_changed_blocks_with_options_async(request, headers, runtime)

    def list_changed_blocks_with_options(
        self,
        request: snapshot_20201118_models.ListChangedBlocksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> snapshot_20201118_models.ListChangedBlocksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.first_snapshot_id):
            query['FirstSnapshotId'] = request.first_snapshot_id
        if not UtilClient.is_unset(request.second_snapshot_id):
            query['SecondSnapshotId'] = request.second_snapshot_id
        if not UtilClient.is_unset(request.starting_block_index):
            query['StartingBlockIndex'] = request.starting_block_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return snapshot_20201118_models.ListChangedBlocksResponse().from_map(
            self.do_roarequest('ListChangedBlocks', '2020-11-18', 'HTTPS', 'GET', 'AK', f'/snapshots/changedblocks', 'json', req, runtime)
        )

    async def list_changed_blocks_with_options_async(
        self,
        request: snapshot_20201118_models.ListChangedBlocksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> snapshot_20201118_models.ListChangedBlocksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.first_snapshot_id):
            query['FirstSnapshotId'] = request.first_snapshot_id
        if not UtilClient.is_unset(request.second_snapshot_id):
            query['SecondSnapshotId'] = request.second_snapshot_id
        if not UtilClient.is_unset(request.starting_block_index):
            query['StartingBlockIndex'] = request.starting_block_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return snapshot_20201118_models.ListChangedBlocksResponse().from_map(
            await self.do_roarequest_async('ListChangedBlocks', '2020-11-18', 'HTTPS', 'GET', 'AK', f'/snapshots/changedblocks', 'json', req, runtime)
        )

    def list_snapshot_blocks(
        self,
        request: snapshot_20201118_models.ListSnapshotBlocksRequest,
    ) -> snapshot_20201118_models.ListSnapshotBlocksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_snapshot_blocks_with_options(request, headers, runtime)

    async def list_snapshot_blocks_async(
        self,
        request: snapshot_20201118_models.ListSnapshotBlocksRequest,
    ) -> snapshot_20201118_models.ListSnapshotBlocksResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_snapshot_blocks_with_options_async(request, headers, runtime)

    def list_snapshot_blocks_with_options(
        self,
        request: snapshot_20201118_models.ListSnapshotBlocksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> snapshot_20201118_models.ListSnapshotBlocksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.starting_block_index):
            query['StartingBlockIndex'] = request.starting_block_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return snapshot_20201118_models.ListSnapshotBlocksResponse().from_map(
            self.do_roarequest('ListSnapshotBlocks', '2020-11-18', 'HTTPS', 'GET', 'AK', f'/snapshots/listblocks', 'json', req, runtime)
        )

    async def list_snapshot_blocks_with_options_async(
        self,
        request: snapshot_20201118_models.ListSnapshotBlocksRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> snapshot_20201118_models.ListSnapshotBlocksResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.snapshot_id):
            query['SnapshotId'] = request.snapshot_id
        if not UtilClient.is_unset(request.starting_block_index):
            query['StartingBlockIndex'] = request.starting_block_index
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        return snapshot_20201118_models.ListSnapshotBlocksResponse().from_map(
            await self.do_roarequest_async('ListSnapshotBlocks', '2020-11-18', 'HTTPS', 'GET', 'AK', f'/snapshots/listblocks', 'json', req, runtime)
        )
