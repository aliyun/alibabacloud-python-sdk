# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_aiearth_engine20220609 import models as aiearth__engine_20220609_models
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
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('aiearth-engine', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def download_data_with_options(
        self,
        request: aiearth__engine_20220609_models.DownloadDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.DownloadDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.band_no):
            body['BandNo'] = request.band_no
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadData',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.DownloadDataResponse(),
            self.call_api(params, req, runtime)
        )

    async def download_data_with_options_async(
        self,
        request: aiearth__engine_20220609_models.DownloadDataRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.DownloadDataResponse:
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.band_no):
            body['BandNo'] = request.band_no
        if not UtilClient.is_unset(request.data_id):
            body['DataId'] = request.data_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DownloadData',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.DownloadDataResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def download_data(
        self,
        request: aiearth__engine_20220609_models.DownloadDataRequest,
    ) -> aiearth__engine_20220609_models.DownloadDataResponse:
        runtime = util_models.RuntimeOptions()
        return self.download_data_with_options(request, runtime)

    async def download_data_async(
        self,
        request: aiearth__engine_20220609_models.DownloadDataRequest,
    ) -> aiearth__engine_20220609_models.DownloadDataResponse:
        runtime = util_models.RuntimeOptions()
        return await self.download_data_with_options_async(request, runtime)

    def list_datas_with_options(
        self,
        tmp_req: aiearth__engine_20220609_models.ListDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.ListDatasResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.ListDatasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_type_list):
            request.source_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_type_list, 'SourceTypeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.cloudage_max):
            body['CloudageMax'] = request.cloudage_max
        if not UtilClient.is_unset(request.cloudage_min):
            body['CloudageMin'] = request.cloudage_min
        if not UtilClient.is_unset(request.date_end):
            body['DateEnd'] = request.date_end
        if not UtilClient.is_unset(request.date_start):
            body['DateStart'] = request.date_start
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_wkt):
            body['RegionWkt'] = request.region_wkt
        if not UtilClient.is_unset(request.source_type_list_shrink):
            body['SourceTypeList'] = request.source_type_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatas',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.ListDatasResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_datas_with_options_async(
        self,
        tmp_req: aiearth__engine_20220609_models.ListDatasRequest,
        runtime: util_models.RuntimeOptions,
    ) -> aiearth__engine_20220609_models.ListDatasResponse:
        UtilClient.validate_model(tmp_req)
        request = aiearth__engine_20220609_models.ListDatasShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.source_type_list):
            request.source_type_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.source_type_list, 'SourceTypeList', 'json')
        body = {}
        if not UtilClient.is_unset(request.cloudage_max):
            body['CloudageMax'] = request.cloudage_max
        if not UtilClient.is_unset(request.cloudage_min):
            body['CloudageMin'] = request.cloudage_min
        if not UtilClient.is_unset(request.date_end):
            body['DateEnd'] = request.date_end
        if not UtilClient.is_unset(request.date_start):
            body['DateStart'] = request.date_start
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_wkt):
            body['RegionWkt'] = request.region_wkt
        if not UtilClient.is_unset(request.source_type_list_shrink):
            body['SourceTypeList'] = request.source_type_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDatas',
            version='2022-06-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            aiearth__engine_20220609_models.ListDatasResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_datas(
        self,
        request: aiearth__engine_20220609_models.ListDatasRequest,
    ) -> aiearth__engine_20220609_models.ListDatasResponse:
        runtime = util_models.RuntimeOptions()
        return self.list_datas_with_options(request, runtime)

    async def list_datas_async(
        self,
        request: aiearth__engine_20220609_models.ListDatasRequest,
    ) -> aiearth__engine_20220609_models.ListDatasResponse:
        runtime = util_models.RuntimeOptions()
        return await self.list_datas_with_options_async(request, runtime)
