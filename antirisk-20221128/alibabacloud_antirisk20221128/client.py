# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_antirisk20221128 import models as antirisk_20221128_models
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
        self._endpoint = self.get_endpoint('antirisk', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_real_time_risk_info_with_options(
        self,
        request: antirisk_20221128_models.GetRealTimeRiskInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.GetRealTimeRiskInfoResponse:
        """
        @summary 获取实时反作弊信息
        
        @param request: GetRealTimeRiskInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealTimeRiskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.atoken):
            query['atoken'] = request.atoken
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.extra):
            query['extra'] = request.extra
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealTimeRiskInfo',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/anti/getRealTimeRiskInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.GetRealTimeRiskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_real_time_risk_info_with_options_async(
        self,
        request: antirisk_20221128_models.GetRealTimeRiskInfoRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.GetRealTimeRiskInfoResponse:
        """
        @summary 获取实时反作弊信息
        
        @param request: GetRealTimeRiskInfoRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetRealTimeRiskInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.atoken):
            query['atoken'] = request.atoken
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.extra):
            query['extra'] = request.extra
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealTimeRiskInfo',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/anti/getRealTimeRiskInfo',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.GetRealTimeRiskInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_real_time_risk_info(
        self,
        request: antirisk_20221128_models.GetRealTimeRiskInfoRequest,
    ) -> antirisk_20221128_models.GetRealTimeRiskInfoResponse:
        """
        @summary 获取实时反作弊信息
        
        @param request: GetRealTimeRiskInfoRequest
        @return: GetRealTimeRiskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_real_time_risk_info_with_options(request, headers, runtime)

    async def get_real_time_risk_info_async(
        self,
        request: antirisk_20221128_models.GetRealTimeRiskInfoRequest,
    ) -> antirisk_20221128_models.GetRealTimeRiskInfoResponse:
        """
        @summary 获取实时反作弊信息
        
        @param request: GetRealTimeRiskInfoRequest
        @return: GetRealTimeRiskInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_real_time_risk_info_with_options_async(request, headers, runtime)

    def get_zid_tag_by_atoken_with_options(
        self,
        request: antirisk_20221128_models.GetZidTagByAtokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.GetZidTagByAtokenResponse:
        """
        @summary atoken换zid+tags
        
        @param request: GetZidTagByAtokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetZidTagByAtokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.atoken):
            query['atoken'] = request.atoken
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetZidTagByAtoken',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/anti/getZidTagByAtoken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.GetZidTagByAtokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_zid_tag_by_atoken_with_options_async(
        self,
        request: antirisk_20221128_models.GetZidTagByAtokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.GetZidTagByAtokenResponse:
        """
        @summary atoken换zid+tags
        
        @param request: GetZidTagByAtokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetZidTagByAtokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.atoken):
            query['atoken'] = request.atoken
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetZidTagByAtoken',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/anti/getZidTagByAtoken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.GetZidTagByAtokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_zid_tag_by_atoken(
        self,
        request: antirisk_20221128_models.GetZidTagByAtokenRequest,
    ) -> antirisk_20221128_models.GetZidTagByAtokenResponse:
        """
        @summary atoken换zid+tags
        
        @param request: GetZidTagByAtokenRequest
        @return: GetZidTagByAtokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_zid_tag_by_atoken_with_options(request, headers, runtime)

    async def get_zid_tag_by_atoken_async(
        self,
        request: antirisk_20221128_models.GetZidTagByAtokenRequest,
    ) -> antirisk_20221128_models.GetZidTagByAtokenResponse:
        """
        @summary atoken换zid+tags
        
        @param request: GetZidTagByAtokenRequest
        @return: GetZidTagByAtokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_zid_tag_by_atoken_with_options_async(request, headers, runtime)

    def get_zid_tag_score_by_atoken_with_options(
        self,
        request: antirisk_20221128_models.GetZidTagScoreByAtokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.GetZidTagScoreByAtokenResponse:
        """
        @summary atoken换zid+tags+风险分
        
        @param request: GetZidTagScoreByAtokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetZidTagScoreByAtokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.atoken):
            query['atoken'] = request.atoken
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetZidTagScoreByAtoken',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/anti/getZidTagScoreByAtoken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.GetZidTagScoreByAtokenResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_zid_tag_score_by_atoken_with_options_async(
        self,
        request: antirisk_20221128_models.GetZidTagScoreByAtokenRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.GetZidTagScoreByAtokenResponse:
        """
        @summary atoken换zid+tags+风险分
        
        @param request: GetZidTagScoreByAtokenRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: GetZidTagScoreByAtokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.atoken):
            query['atoken'] = request.atoken
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetZidTagScoreByAtoken',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/anti/getZidTagScoreByAtoken',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.GetZidTagScoreByAtokenResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_zid_tag_score_by_atoken(
        self,
        request: antirisk_20221128_models.GetZidTagScoreByAtokenRequest,
    ) -> antirisk_20221128_models.GetZidTagScoreByAtokenResponse:
        """
        @summary atoken换zid+tags+风险分
        
        @param request: GetZidTagScoreByAtokenRequest
        @return: GetZidTagScoreByAtokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.get_zid_tag_score_by_atoken_with_options(request, headers, runtime)

    async def get_zid_tag_score_by_atoken_async(
        self,
        request: antirisk_20221128_models.GetZidTagScoreByAtokenRequest,
    ) -> antirisk_20221128_models.GetZidTagScoreByAtokenResponse:
        """
        @summary atoken换zid+tags+风险分
        
        @param request: GetZidTagScoreByAtokenRequest
        @return: GetZidTagScoreByAtokenResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.get_zid_tag_score_by_atoken_with_options_async(request, headers, runtime)

    def list_channel_risk_details_with_options(
        self,
        request: antirisk_20221128_models.ListChannelRiskDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.ListChannelRiskDetailsResponse:
        """
        @summary  渠道风险明细
        
        @param request: ListChannelRiskDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChannelRiskDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.is_all_channel):
            query['isAllChannel'] = request.is_all_channel
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChannelRiskDetails',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/anti/listChannelRiskDetails',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.ListChannelRiskDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_channel_risk_details_with_options_async(
        self,
        request: antirisk_20221128_models.ListChannelRiskDetailsRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.ListChannelRiskDetailsResponse:
        """
        @summary  渠道风险明细
        
        @param request: ListChannelRiskDetailsRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListChannelRiskDetailsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['channel'] = request.channel
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end):
            query['end'] = request.end
        if not UtilClient.is_unset(request.is_all_channel):
            query['isAllChannel'] = request.is_all_channel
        if not UtilClient.is_unset(request.start):
            query['start'] = request.start
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChannelRiskDetails',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/anti/listChannelRiskDetails',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.ListChannelRiskDetailsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_channel_risk_details(
        self,
        request: antirisk_20221128_models.ListChannelRiskDetailsRequest,
    ) -> antirisk_20221128_models.ListChannelRiskDetailsResponse:
        """
        @summary  渠道风险明细
        
        @param request: ListChannelRiskDetailsRequest
        @return: ListChannelRiskDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_channel_risk_details_with_options(request, headers, runtime)

    async def list_channel_risk_details_async(
        self,
        request: antirisk_20221128_models.ListChannelRiskDetailsRequest,
    ) -> antirisk_20221128_models.ListChannelRiskDetailsResponse:
        """
        @summary  渠道风险明细
        
        @param request: ListChannelRiskDetailsRequest
        @return: ListChannelRiskDetailsResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_channel_risk_details_with_options_async(request, headers, runtime)

    def list_uninstall_detail_with_options(
        self,
        request: antirisk_20221128_models.ListUninstallDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.ListUninstallDetailResponse:
        """
        @summary 卸载明细列表
        
        @param request: ListUninstallDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUninstallDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_ds):
            query['endDs'] = request.end_ds
        if not UtilClient.is_unset(request.start_ds):
            query['startDs'] = request.start_ds
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUninstallDetail',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/uninstall/listUninstallDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.ListUninstallDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def list_uninstall_detail_with_options_async(
        self,
        request: antirisk_20221128_models.ListUninstallDetailRequest,
        headers: Dict[str, str],
        runtime: util_models.RuntimeOptions,
    ) -> antirisk_20221128_models.ListUninstallDetailResponse:
        """
        @summary 卸载明细列表
        
        @param request: ListUninstallDetailRequest
        @param headers: map
        @param runtime: runtime options for this request RuntimeOptions
        @return: ListUninstallDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['dataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_ds):
            query['endDs'] = request.end_ds
        if not UtilClient.is_unset(request.start_ds):
            query['startDs'] = request.start_ds
        req = open_api_models.OpenApiRequest(
            headers=headers,
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUninstallDetail',
            version='2022-11-28',
            protocol='HTTPS',
            pathname=f'/uninstall/listUninstallDetail',
            method='GET',
            auth_type='AK',
            style='ROA',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            antirisk_20221128_models.ListUninstallDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def list_uninstall_detail(
        self,
        request: antirisk_20221128_models.ListUninstallDetailRequest,
    ) -> antirisk_20221128_models.ListUninstallDetailResponse:
        """
        @summary 卸载明细列表
        
        @param request: ListUninstallDetailRequest
        @return: ListUninstallDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return self.list_uninstall_detail_with_options(request, headers, runtime)

    async def list_uninstall_detail_async(
        self,
        request: antirisk_20221128_models.ListUninstallDetailRequest,
    ) -> antirisk_20221128_models.ListUninstallDetailResponse:
        """
        @summary 卸载明细列表
        
        @param request: ListUninstallDetailRequest
        @return: ListUninstallDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        headers = {}
        return await self.list_uninstall_detail_with_options_async(request, headers, runtime)
