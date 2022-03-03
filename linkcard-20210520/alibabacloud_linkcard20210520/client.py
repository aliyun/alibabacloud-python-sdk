# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from typing import Dict
from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkcard20210520 import models as linkcard_20210520_models
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
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkcard', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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

    def get_card_detail_with_options(
        self,
        request: linkcard_20210520_models.GetCardDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destroy_card):
            query['DestroyCard'] = request.destroy_card
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.show_psim):
            query['ShowPsim'] = request.show_psim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardDetail',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardDetailResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_detail_with_options_async(
        self,
        request: linkcard_20210520_models.GetCardDetailRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardDetailResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destroy_card):
            query['DestroyCard'] = request.destroy_card
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.show_psim):
            query['ShowPsim'] = request.show_psim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardDetail',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardDetailResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_detail(
        self,
        request: linkcard_20210520_models.GetCardDetailRequest,
    ) -> linkcard_20210520_models.GetCardDetailResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_card_detail_with_options(request, runtime)

    async def get_card_detail_async(
        self,
        request: linkcard_20210520_models.GetCardDetailRequest,
    ) -> linkcard_20210520_models.GetCardDetailResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_card_detail_with_options_async(request, runtime)

    def get_card_flow_info_with_options(
        self,
        request: linkcard_20210520_models.GetCardFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_list):
            query['DateList'] = request.date_list
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardFlowInfo',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardFlowInfoResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_card_flow_info_with_options_async(
        self,
        request: linkcard_20210520_models.GetCardFlowInfoRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCardFlowInfoResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.date_list):
            query['DateList'] = request.date_list
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCardFlowInfo',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCardFlowInfoResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_card_flow_info(
        self,
        request: linkcard_20210520_models.GetCardFlowInfoRequest,
    ) -> linkcard_20210520_models.GetCardFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_card_flow_info_with_options(request, runtime)

    async def get_card_flow_info_async(
        self,
        request: linkcard_20210520_models.GetCardFlowInfoRequest,
    ) -> linkcard_20210520_models.GetCardFlowInfoResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_card_flow_info_with_options_async(request, runtime)

    def get_credential_pool_statistics_with_options(
        self,
        request: linkcard_20210520_models.GetCredentialPoolStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCredentialPoolStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNO'] = request.credential_no
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCredentialPoolStatistics',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCredentialPoolStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    async def get_credential_pool_statistics_with_options_async(
        self,
        request: linkcard_20210520_models.GetCredentialPoolStatisticsRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.GetCredentialPoolStatisticsResponse:
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_no):
            query['CredentialNO'] = request.credential_no
        if not UtilClient.is_unset(request.date):
            query['Date'] = request.date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCredentialPoolStatistics',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.GetCredentialPoolStatisticsResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def get_credential_pool_statistics(
        self,
        request: linkcard_20210520_models.GetCredentialPoolStatisticsRequest,
    ) -> linkcard_20210520_models.GetCredentialPoolStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return self.get_credential_pool_statistics_with_options(request, runtime)

    async def get_credential_pool_statistics_async(
        self,
        request: linkcard_20210520_models.GetCredentialPoolStatisticsRequest,
    ) -> linkcard_20210520_models.GetCredentialPoolStatisticsResponse:
        runtime = util_models.RuntimeOptions()
        return await self.get_credential_pool_statistics_with_options_async(request, runtime)

    def rebind_resume_single_card_with_options(
        self,
        tmp_req: linkcard_20210520_models.RebindResumeSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.RebindResumeSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.RebindResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebindResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.RebindResumeSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def rebind_resume_single_card_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.RebindResumeSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.RebindResumeSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.RebindResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebindResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.RebindResumeSingleCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def rebind_resume_single_card(
        self,
        request: linkcard_20210520_models.RebindResumeSingleCardRequest,
    ) -> linkcard_20210520_models.RebindResumeSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.rebind_resume_single_card_with_options(request, runtime)

    async def rebind_resume_single_card_async(
        self,
        request: linkcard_20210520_models.RebindResumeSingleCardRequest,
    ) -> linkcard_20210520_models.RebindResumeSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.rebind_resume_single_card_with_options_async(request, runtime)

    def resume_single_card_with_options(
        self,
        tmp_req: linkcard_20210520_models.ResumeSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ResumeSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.ResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ResumeSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def resume_single_card_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.ResumeSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.ResumeSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.ResumeSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.ResumeSingleCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def resume_single_card(
        self,
        request: linkcard_20210520_models.ResumeSingleCardRequest,
    ) -> linkcard_20210520_models.ResumeSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.resume_single_card_with_options(request, runtime)

    async def resume_single_card_async(
        self,
        request: linkcard_20210520_models.ResumeSingleCardRequest,
    ) -> linkcard_20210520_models.ResumeSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.resume_single_card_with_options_async(request, runtime)

    def stop_single_card_with_options(
        self,
        tmp_req: linkcard_20210520_models.StopSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.StopSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.StopSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.StopSingleCardResponse(),
            self.call_api(params, req, runtime)
        )

    async def stop_single_card_with_options_async(
        self,
        tmp_req: linkcard_20210520_models.StopSingleCardRequest,
        runtime: util_models.RuntimeOptions,
    ) -> linkcard_20210520_models.StopSingleCardResponse:
        UtilClient.validate_model(tmp_req)
        request = linkcard_20210520_models.StopSingleCardShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.opt_msisdns):
            request.opt_msisdns_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.opt_msisdns, 'OptMsisdns', 'json')
        query = {}
        if not UtilClient.is_unset(request.iccid):
            query['Iccid'] = request.iccid
        if not UtilClient.is_unset(request.opt_msisdns_shrink):
            query['OptMsisdns'] = request.opt_msisdns_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopSingleCard',
            version='2021-05-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkcard_20210520_models.StopSingleCardResponse(),
            await self.call_api_async(params, req, runtime)
        )

    def stop_single_card(
        self,
        request: linkcard_20210520_models.StopSingleCardRequest,
    ) -> linkcard_20210520_models.StopSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return self.stop_single_card_with_options(request, runtime)

    async def stop_single_card_async(
        self,
        request: linkcard_20210520_models.StopSingleCardRequest,
    ) -> linkcard_20210520_models.StopSingleCardResponse:
        runtime = util_models.RuntimeOptions()
        return await self.stop_single_card_with_options_async(request, runtime)
