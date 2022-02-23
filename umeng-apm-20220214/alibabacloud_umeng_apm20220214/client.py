# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_umeng_apm20220214 import models as umeng_apm_20220214_models
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
        self._endpoint = self.get_endpoint('umeng-apm', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_stat_trend(
        self,
        request: umeng_apm_20220214_models.GetStatTrendRequest,
    ) -> umeng_apm_20220214_models.GetStatTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_stat_trend_with_options(request, headers, runtime)

    async def get_stat_trend_async(
        self,
        request: umeng_apm_20220214_models.GetStatTrendRequest,
    ) -> umeng_apm_20220214_models.GetStatTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_stat_trend_with_options_async(request, headers, runtime)

    def get_stat_trend_with_options(
        self,
        request: umeng_apm_20220214_models.GetStatTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetStatTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['appVersion'] = request.app_version
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStatTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getStatTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetStatTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_stat_trend_with_options_async(
        self,
        request: umeng_apm_20220214_models.GetStatTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetStatTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['appVersion'] = request.app_version
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_date):
            query['endDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['startDate'] = request.start_date
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStatTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getStatTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetStatTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_sym_upload_param(
        self,
        request: umeng_apm_20220214_models.GetSymUploadParamRequest,
    ) -> umeng_apm_20220214_models.GetSymUploadParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_sym_upload_param_with_options(request, headers, runtime)

    async def get_sym_upload_param_async(
        self,
        request: umeng_apm_20220214_models.GetSymUploadParamRequest,
    ) -> umeng_apm_20220214_models.GetSymUploadParamResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_sym_upload_param_with_options_async(request, headers, runtime)

    def get_sym_upload_param_with_options(
        self,
        request: umeng_apm_20220214_models.GetSymUploadParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetSymUploadParamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['appVersion'] = request.app_version
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['fileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSymUploadParam',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/getSymUploadParam',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetSymUploadParamResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_sym_upload_param_with_options_async(
        self,
        request: umeng_apm_20220214_models.GetSymUploadParamRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetSymUploadParamResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['appVersion'] = request.app_version
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.file_name):
            query['fileName'] = request.file_name
        if not UtilClient.is_unset(request.file_type):
            query['fileType'] = request.file_type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSymUploadParam',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/getSymUploadParam',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetSymUploadParamResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_today_stat_trend(
        self,
        request: umeng_apm_20220214_models.GetTodayStatTrendRequest,
    ) -> umeng_apm_20220214_models.GetTodayStatTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_today_stat_trend_with_options(request, headers, runtime)

    async def get_today_stat_trend_async(
        self,
        request: umeng_apm_20220214_models.GetTodayStatTrendRequest,
    ) -> umeng_apm_20220214_models.GetTodayStatTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_today_stat_trend_with_options_async(request, headers, runtime)

    def get_today_stat_trend_with_options(
        self,
        request: umeng_apm_20220214_models.GetTodayStatTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetTodayStatTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['appVersion'] = request.app_version
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTodayStatTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getTodayStatTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetTodayStatTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_today_stat_trend_with_options_async(
        self,
        request: umeng_apm_20220214_models.GetTodayStatTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetTodayStatTrendResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_version):
            query['appVersion'] = request.app_version
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.type):
            query['type'] = request.type
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTodayStatTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getTodayStatTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetTodayStatTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )
