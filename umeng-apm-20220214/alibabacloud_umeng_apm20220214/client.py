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
from alibabacloud_openplatform20191219.client import Client as OpenPlatformClient
from alibabacloud_openplatform20191219 import models as open_platform_models
from alibabacloud_oss_sdk import models as oss_models
from alibabacloud_tea_fileform import models as file_form_models
from alibabacloud_oss_util import models as ossutil_models
from alibabacloud_oss_sdk.client import Client as OSSClient


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

    def get_h5page_trend_with_options(
        self,
        request: umeng_apm_20220214_models.GetH5PageTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetH5PageTrendResponse:
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
        if not UtilClient.is_unset(request.time_unit):
            query['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetH5PageTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getH5PageTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetH5PageTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_h5page_trend_with_options_async(
        self,
        request: umeng_apm_20220214_models.GetH5PageTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetH5PageTrendResponse:
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
        if not UtilClient.is_unset(request.time_unit):
            query['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetH5PageTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getH5PageTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetH5PageTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_h5page_trend(
        self,
        request: umeng_apm_20220214_models.GetH5PageTrendRequest,
    ) -> umeng_apm_20220214_models.GetH5PageTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_h5page_trend_with_options(request, headers, runtime)

    async def get_h5page_trend_async(
        self,
        request: umeng_apm_20220214_models.GetH5PageTrendRequest,
    ) -> umeng_apm_20220214_models.GetH5PageTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_h5page_trend_with_options_async(request, headers, runtime)

    def get_launch_trend_with_options(
        self,
        request: umeng_apm_20220214_models.GetLaunchTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetLaunchTrendResponse:
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
        if not UtilClient.is_unset(request.time_unit):
            query['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLaunchTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getLaunchTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetLaunchTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_launch_trend_with_options_async(
        self,
        request: umeng_apm_20220214_models.GetLaunchTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetLaunchTrendResponse:
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
        if not UtilClient.is_unset(request.time_unit):
            query['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLaunchTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getLaunchTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetLaunchTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_launch_trend(
        self,
        request: umeng_apm_20220214_models.GetLaunchTrendRequest,
    ) -> umeng_apm_20220214_models.GetLaunchTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_launch_trend_with_options(request, headers, runtime)

    async def get_launch_trend_async(
        self,
        request: umeng_apm_20220214_models.GetLaunchTrendRequest,
    ) -> umeng_apm_20220214_models.GetLaunchTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_launch_trend_with_options_async(request, headers, runtime)

    def get_native_page_trend_with_options(
        self,
        request: umeng_apm_20220214_models.GetNativePageTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetNativePageTrendResponse:
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
        if not UtilClient.is_unset(request.time_unit):
            query['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNativePageTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getNativePageTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetNativePageTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_native_page_trend_with_options_async(
        self,
        request: umeng_apm_20220214_models.GetNativePageTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetNativePageTrendResponse:
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
        if not UtilClient.is_unset(request.time_unit):
            query['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNativePageTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getNativePageTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetNativePageTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_native_page_trend(
        self,
        request: umeng_apm_20220214_models.GetNativePageTrendRequest,
    ) -> umeng_apm_20220214_models.GetNativePageTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_native_page_trend_with_options(request, headers, runtime)

    async def get_native_page_trend_async(
        self,
        request: umeng_apm_20220214_models.GetNativePageTrendRequest,
    ) -> umeng_apm_20220214_models.GetNativePageTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_native_page_trend_with_options_async(request, headers, runtime)

    def get_network_trend_with_options(
        self,
        request: umeng_apm_20220214_models.GetNetworkTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetNetworkTrendResponse:
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
        if not UtilClient.is_unset(request.time_unit):
            query['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getNetworkTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetNetworkTrendResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_network_trend_with_options_async(
        self,
        request: umeng_apm_20220214_models.GetNetworkTrendRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.GetNetworkTrendResponse:
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
        if not UtilClient.is_unset(request.time_unit):
            query['timeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNetworkTrend',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/stat/getNetworkTrend',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.GetNetworkTrendResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_network_trend(
        self,
        request: umeng_apm_20220214_models.GetNetworkTrendRequest,
    ) -> umeng_apm_20220214_models.GetNetworkTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_network_trend_with_options(request, headers, runtime)

    async def get_network_trend_async(
        self,
        request: umeng_apm_20220214_models.GetNetworkTrendRequest,
    ) -> umeng_apm_20220214_models.GetNetworkTrendResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_network_trend_with_options_async(request, headers, runtime)

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
        if not UtilClient.is_unset(request.flutter_name):
            query['flutterName'] = request.flutter_name
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
        if not UtilClient.is_unset(request.flutter_name):
            query['flutterName'] = request.flutter_name
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

    def update_alert_plan_with_options(
        self,
        request: umeng_apm_20220214_models.UpdateAlertPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.UpdateAlertPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.plan_id):
            query['planId'] = request.plan_id
        if not UtilClient.is_unset(request.versions):
            query['versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertPlan',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/updateAlertPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.UpdateAlertPlanResponse(),
            self.call_api(params, req, runtime)
        )

    async def update_alert_plan_with_options_async(
        self,
        request: umeng_apm_20220214_models.UpdateAlertPlanRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.UpdateAlertPlanResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.plan_id):
            query['planId'] = request.plan_id
        if not UtilClient.is_unset(request.versions):
            query['versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertPlan',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/updateAlertPlan',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.UpdateAlertPlanResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def update_alert_plan(
        self,
        request: umeng_apm_20220214_models.UpdateAlertPlanRequest,
    ) -> umeng_apm_20220214_models.UpdateAlertPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.update_alert_plan_with_options(request, headers, runtime)

    async def update_alert_plan_async(
        self,
        request: umeng_apm_20220214_models.UpdateAlertPlanRequest,
    ) -> umeng_apm_20220214_models.UpdateAlertPlanResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.update_alert_plan_with_options_async(request, headers, runtime)

    def upload_symbol_file_with_options(
        self,
        request: umeng_apm_20220214_models.UploadSymbolFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.UploadSymbolFileResponse:
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
        if not UtilClient.is_unset(request.flutter_name):
            query['flutterName'] = request.flutter_name
        if not UtilClient.is_unset(request.oss_url):
            query['ossUrl'] = request.oss_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadSymbolFile',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/uploadSymbolFile',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.UploadSymbolFileResponse(),
            self.call_api(params, req, runtime)
        )

    async def upload_symbol_file_with_options_async(
        self,
        request: umeng_apm_20220214_models.UploadSymbolFileRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.UploadSymbolFileResponse:
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
        if not UtilClient.is_unset(request.flutter_name):
            query['flutterName'] = request.flutter_name
        if not UtilClient.is_unset(request.oss_url):
            query['ossUrl'] = request.oss_url
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadSymbolFile',
            version='2022-02-14',
            protocol='HTTPS',
            pathname=f'/uploadSymbolFile',
            method='POST',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            umeng_apm_20220214_models.UploadSymbolFileResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def upload_symbol_file(
        self,
        request: umeng_apm_20220214_models.UploadSymbolFileRequest,
    ) -> umeng_apm_20220214_models.UploadSymbolFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.upload_symbol_file_with_options(request, headers, runtime)

    async def upload_symbol_file_async(
        self,
        request: umeng_apm_20220214_models.UploadSymbolFileRequest,
    ) -> umeng_apm_20220214_models.UploadSymbolFileResponse:
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.upload_symbol_file_with_options_async(request, headers, runtime)

    def upload_symbol_file_advance(
        self,
        request: umeng_apm_20220214_models.UploadSymbolFileAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.UploadSymbolFileResponse:
        # Step 0: init client
        access_key_id = self._credential.get_access_key_id()
        access_key_secret = self._credential.get_access_key_secret()
        security_token = self._credential.get_security_token()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='umeng-apm',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        upload_symbol_file_req = umeng_apm_20220214_models.UploadSymbolFileRequest()
        OpenApiUtilClient.convert(request, upload_symbol_file_req)
        if not UtilClient.is_unset(request.oss_url_object):
            auth_response = auth_client.authorize_file_upload_with_options(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.oss_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            oss_client.post_object(upload_request, oss_runtime)
            upload_symbol_file_req.oss_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        upload_symbol_file_resp = self.upload_symbol_file_with_options(upload_symbol_file_req, headers, runtime)
        return upload_symbol_file_resp

    async def upload_symbol_file_advance_async(
        self,
        request: umeng_apm_20220214_models.UploadSymbolFileAdvanceRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> umeng_apm_20220214_models.UploadSymbolFileResponse:
        # Step 0: init client
        access_key_id = await self._credential.get_access_key_id_async()
        access_key_secret = await self._credential.get_access_key_secret_async()
        security_token = await self._credential.get_security_token_async()
        credential_type = self._credential.get_type()
        open_platform_endpoint = self._open_platform_endpoint
        if UtilClient.is_unset(open_platform_endpoint):
            open_platform_endpoint = 'openplatform.aliyuncs.com'
        if UtilClient.is_unset(credential_type):
            credential_type = 'access_key'
        auth_config = open_api_models.Config(
            access_key_id=access_key_id,
            access_key_secret=access_key_secret,
            security_token=security_token,
            type=credential_type,
            endpoint=open_platform_endpoint,
            protocol=self._protocol,
            region_id=self._region_id
        )
        auth_client = OpenPlatformClient(auth_config)
        auth_request = open_platform_models.AuthorizeFileUploadRequest(
            product='umeng-apm',
            region_id=self._region_id
        )
        auth_response = open_platform_models.AuthorizeFileUploadResponse()
        oss_config = oss_models.Config(
            access_key_secret=access_key_secret,
            type='access_key',
            protocol=self._protocol,
            region_id=self._region_id
        )
        oss_client = None
        file_obj = file_form_models.FileField()
        oss_header = oss_models.PostObjectRequestHeader()
        upload_request = oss_models.PostObjectRequest()
        oss_runtime = ossutil_models.RuntimeOptions()
        OpenApiUtilClient.convert(runtime, oss_runtime)
        upload_symbol_file_req = umeng_apm_20220214_models.UploadSymbolFileRequest()
        OpenApiUtilClient.convert(request, upload_symbol_file_req)
        if not UtilClient.is_unset(request.oss_url_object):
            auth_response = await auth_client.authorize_file_upload_with_options_async(auth_request, runtime)
            oss_config.access_key_id = auth_response.body.access_key_id
            oss_config.endpoint = OpenApiUtilClient.get_endpoint(auth_response.body.endpoint, auth_response.body.use_accelerate, self._endpoint_type)
            oss_client = OSSClient(oss_config)
            file_obj = file_form_models.FileField(
                filename=auth_response.body.object_key,
                content=request.oss_url_object,
                content_type=''
            )
            oss_header = oss_models.PostObjectRequestHeader(
                access_key_id=auth_response.body.access_key_id,
                policy=auth_response.body.encoded_policy,
                signature=auth_response.body.signature,
                key=auth_response.body.object_key,
                file=file_obj,
                success_action_status='201'
            )
            upload_request = oss_models.PostObjectRequest(
                bucket_name=auth_response.body.bucket,
                header=oss_header
            )
            await oss_client.post_object_async(upload_request, oss_runtime)
            upload_symbol_file_req.oss_url = f'http://{auth_response.body.bucket}.{auth_response.body.endpoint}/{auth_response.body.object_key}'
        upload_symbol_file_resp = await self.upload_symbol_file_with_options_async(upload_symbol_file_req, headers, runtime)
        return upload_symbol_file_resp
